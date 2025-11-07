
# df_rd_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\df_rd_3.pkl' )

# %%

# df_rd_3['treatment'] = (
#                         df_rd_3['treatment']
#                         .replace({'DBD-Ecosol': 'DBD-Omnisol'})
# )

# df_rd_4 = df_rd_3.copy()

# %%

# df_rd_4.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\df_rd_4.pkl' )

df_rd_4 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\df_rd_4.pkl' )


# %%'

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Omnisol": "blue", 
                    "NMP": "red" 
}


# %%'

# this can not be called as sns.FacetGrid opens its own new window !!
# fig = plt.figure( figsize=(16,12) , constrained_layout=True)

# %%' grid

# Create a FacetGrid where each facet corresponds to a specific metric
# importat note : the default values of share-x-y are : True
    # this is not logical.
    # this should only be an option.
    # setting : share-x = True : would cancel specific x-ticks determination for individual subplots !!
g = sns.FacetGrid( 
                    df_rd_4 , 
                    col="metric",  # columns : subplots.
                    col_wrap=2, 
                    sharex=False , 
                    sharey=False , 
                    height=7, 
                    aspect=1.4
)

# %%' pointplot

# g
# pointplot
g.map_dataframe( 
                    sns.pointplot ,    
                    x='time' , 
                    y='value' ,  # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                    hue="treatment",
                    palette=custom_palette ,
                    # col="metric",  # columns : subplots.
                    marker="o" ,  
                    estimator='mean' ,    
                    # capsize=0.2,
                    errorbar='se' ,
                    dodge=0.2
) 

# %%'
# %% Legend

# also adding a legend for the overlapping gray normal range area, under the conventional legend.

# import matplotlib.patches as mpatches

# Get handles/labels from one of the axes
ax0 = g.axes.flatten()[0]
handles , labels = ax0.get_legend_handles_labels()

# gray patch
# Add the proxy patch
# for the normal ranges.
normal_patch = mpatches.Patch(color='lightgray', alpha=0.4, label='Normal range')
handles.append(normal_patch)
labels.append("Normal range")

# frameon : the frame around the whole legend area.
g.fig.legend( 
                handles , 
                labels , 
                loc='center right' , 
                frameon=False 
)

# for text in g._legend.texts:
#     text.set_fontsize(20)  # Adjust as needed

# %%'

# Add a legend to clearly indicate which color corresponds to which group.
# g.add_legend()  # , bbox_to_anchor=(1.05, 0.5), borderaxespad=0 , loc='center left'
# g._legend.set_title("group" )
# # Increase the font size of the legend title
# g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

# for text in g._legend.texts:
#     text.set_fontsize(20)  # Adjust as needed

# %%'

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("Time" , loc='right' , fontsize=24 )

# %%'

# This section was due to different baselines for 'release volum' & 'density'.
# Hence, changing only one of them.

# Retrieve the first subplot (Axes object)
# first_ax = g.axes[0]

# # Set custom tick labels for the first subplot.
# # This assumes there are exactly 8 ticks. If necessary, you can also explicitly set the tick positions.
# first_ax.set_xticklabels(['TI', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7'] , fontsize=16 )


# %%'

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [ 'Release Volume', 'Density' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%'

unit = [ 
        'ml/day' ,
        'Relative density' 
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=20 )


# %%'  normal range

g.col_names
    # Out[19]: ['release', 'density']

# replace these with your real metric names & numeric limits
normal_ranges = {
    "release": (672 , 2772),
    "density": (1.01 , 1.05 ),
}

# %%%'

for ax, metric in zip( g.axes.flatten() , g.col_names ):
    lower, upper = normal_ranges[metric]
    # shade the band
    ax.axhspan( lower , upper , color='lightgray', alpha=0.4)
    # draw the boundary lines
    ax.axhline( lower , color='gray', linestyle='--', linewidth=1)
    ax.axhline( upper , color='gray', linestyle='--', linewidth=1)

# %%' explore

# unpacking a tuple !!

normal_ranges["release"]
    # Out[22]: (672, 772)

a , b = normal_ranges["release"]

a
    # Out[24]: 672

b
    # Out[25]: 772

# %% add subplot indexing letters

# add subplot indexing letters.

# import string

# Suppose g is your FacetGrid / catplot result
# this works for any number of subplots : you do not need to right a list of letter numbers based on the number of subplots.
letters = list( string.ascii_uppercase )  # ['A','B','C','D',...]

# ha , va : text alignment relative to the (x, y) coordinates you gave :
    # ha='right' means the right edge of the letter is anchored at x=-0.1.
    # va='bottom' means the bottom edge of the letter is anchored at y=1.05.
# That combination places the letter just above and slightly to the left of the subplot, with the text extending leftward and upward from that anchor point.
for ax , letter in zip( g.axes.flatten() , letters ):
    ax.text(                           # the most important part !
            -0.1, 1.05, letter,        # position relative to each axis.
            transform=ax.transAxes,    # use axes fraction coords
            fontsize=20, fontweight='bold',
            va='bottom', ha='right'
    )

# transform=ax.transAxes :
    # By default, when you call ax.text(x, y, ...), Matplotlib interprets x and y in data coordinates (the same units as your plotted data).
        # Example: if your y‑axis goes from 0 to 100, then ax.text(0, 120, "label") would place text above the data range.
    # transform=ax.transAxes tells Matplotlib: “Interpret (x, y) in axes fraction coordinates instead of data coordinates.”
        # In this coordinate system:
            # (0, 0) = bottom‑left corner of the subplot’s axes
            # (1, 1) = top‑right corner of the subplot’s axes
        # Values can go slightly outside that range (e.g. -0.1, 1.05) to nudge text just beyond the axes.

# %%'

# x= : the x location of the text in figure coordinates.
# plt.suptitle( 'Urine release & density  accross time'   # Change from baseline of
#              # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
#              , x=0.4 
#              , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%'

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.85 , 1] )

# %%'

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

# %%'

# bc : baseline corrected

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\plot\rd_manuscript_3.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\plot\rd_manuscript_3.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\plot\rd_manuscript_3.eps' )

# %%'

