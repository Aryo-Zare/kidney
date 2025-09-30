
# strangely, this data is stored in BG folder !!
df_urine_8 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_urine_8.pkl' )

# df_urine_8 = pd.read_pickle( r'U:\kidney\BG\df_urine_8.pkl' )

# %%

df_urine_8["metric"].unique()
    # Out[120]: 
    # ['Urea', 'Creatinin', 'Na+', 'K+', 'protein']
    # Categories (5, object): ['Urea' < 'Creatinin' < 'protein' < 'Na+' < 'K+']

# %%

mask =  df_urine_8["metric"].isin([ 'Urea', 'Creatinin', 'protein' ]) 
df_urine_8_2 = df_urine_8[ mask ]

# %%

metric_order = [ 'Urea', 'Creatinin', 'protein'  ]
df_urine_8_2['metric'] = pd.Categorical(
                                            df_urine_8_2['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%

df_urine_8_2["metric"].unique()
    # Out[123]: 
    # ['Urea', 'Creatinin', 'protein']
    # Categories (3, object): ['Urea' < 'Creatinin' < 'protein']

# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}

# %%

# Create a FacetGrid where each facet corresponds to a specific metric
g = sns.FacetGrid( 
                    df_urine_8_2 , 
                    col="metric",  # columns : subplots.
                    col_wrap=1, 
                    sharex=False , 
                    sharey=False , 
                    height=6,  # chane the size of the figure here, & at te line below !
                    aspect=2.4
)

# %%

# g
# pointplot
g.map_dataframe( 
                    sns.pointplot ,    
                    x='time' , 
                    y='value' ,  # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                    hue="treatment",
                    palette=custom_palette ,
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='se' ,
                    dodge=0.2
) 


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


# %%

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("Time" , loc='right' , fontsize=24 )

# %%

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [ 'Urea' , 'Creatinin' , 'protein' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%

unit = [ 
        'mmol/L' ,
        'µmol/L' ,
        'mg/dL' ,
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )

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

# %%

# x= : the x location of the text in figure coordinates.
# plt.suptitle( 'Urinalysis'   # Change from baseline of
#              # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
#              , x=0.4 
#              , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.8 , 1] )

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\plot\manuscript_urinalysis_value_5.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\plot\manuscript_urinalysis_value_5.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\plot\manuscript_urinalysis_value_5.eps' )

# %%


