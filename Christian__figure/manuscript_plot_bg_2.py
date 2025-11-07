
# %%'

# df_bg_8 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_bg_8.pkl' )

# %%'

# df_bg_8["metric"].unique()
#     # Out[37]: 
#     # ['pH', 'K+', 'Na+', 'Ca2+', 'Cl-', 'pCO2', 'pO2']
#     # Categories (7, object): ['pH' < 'pCO2' < 'pO2' < 'Na+' < 'K+' < 'Ca2+' < 'Cl-']

# %%'

# mask =  df_bg_8["metric"].isin([ 'pH', 'K+' , 'pCO2', 'pO2' ]) 
# df_bg_8_2 = df_bg_8[ mask ]

# %%'

# metric_order = [ 'pH', 'K+' , 'pCO2', 'pO2' ]
# df_bg_8_2['metric'] = pd.Categorical(
#                                             df_bg_8_2['metric'],
#                                             categories=metric_order,
#                                             ordered=True
# )

# %%'

# df_bg_8_2["metric"].unique()
#     # Out[99]: 
#     # ['pH', 'K+', 'pCO2', 'pO2']
#     # Categories (4, object): ['pH' < 'K+' < 'pCO2' < 'pO2']

# %%

# df_bg_8_2['treatment'] = (
#                             df_bg_8_2['treatment']
#                             .replace({'DBD-Ecosol': 'DBD-Omnisol'})
# )

# df_bg_8_3 = df_bg_8_2.copy()

# %%

# df_bg_8_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_bg_8_3.pkl' )

# df_bg_8_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_bg_8_3.pkl' )

# %%

# rename_dict = {
#                 'DBD-HTK': 'SCS-HTK' ,
#                 'DBD-Omnisol' : 'SCS-Omnisol' ,
#                 'NMP' : 'NMP-Omnisol'
# }


# df_bg_8_3['treatment'].replace( to_replace=rename_dict , inplace=True )

# %%

# df_bg_8_4 = df_bg_8_3.copy()

# df_bg_8_4.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_bg_8_4.pkl' )

df_bg_8_4 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_bg_8_4.pkl' )



# %%'

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "SCS-HTK": "green", 
                    "SCS-Omnisol": "blue", 
                    "NMP-Omnisol": "red" 
}

# %%'


# Create a FacetGrid where each facet corresponds to a specific metric
g = sns.FacetGrid( 
                    df_bg_8_4 , 
                    col="metric", 
                    col_wrap=2, 
                    sharex=False , 
                    sharey=False ,  # this value is True by default !! : change it to False !!
                    height=6, 
                    aspect=1.6
)

# %%'

# g
# pointplot
g.map_dataframe( 
                    sns.pointplot ,    
                    x='time' , 
                    y='value' ,  # 'value' or 'value_bc'
                    hue="treatment",
                    palette=custom_palette ,
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='se' ,
                    dodge= 0.2
) 

# %% Legend

# also adding a legend for the overlapping gray normal range area, under the conventional legend.

# import matplotlib.patches as mpatches

# Get handles/labels from one of the axes
ax0 = g.axes.flatten()[0]
handles , labels = ax0.get_legend_handles_labels()

# gray patch
# Add the proxy patch
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

# # Add a legend to clearly indicate which color corresponds to which group.
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

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [ 'pH', 'K+' , 'pCO2', 'pO2' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%'

unit = [ '' , 'mmol/L' , 'mmHg' , 'mmHg' ]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=20 )

# %%  normal range

g.col_names
    # Out[19]: ['release', 'density']

# replace these with your real metric names & numeric limits
normal_ranges = {
    "pH": ( 7.35 , 7.45 ),
    "K+": ( 3.8 , 5 ),
}

# %%%'

for ax, metric in zip( g.axes.flatten() , g.col_names ):
    if metric in normal_ranges :  # I don't know the normal values of pCO2 & pO2.
        lower, upper = normal_ranges[metric]
        # shade the band
        ax.axhspan( lower , upper , color='lightgray', alpha=0.4)
        # draw the boundary lines
        ax.axhline( lower , color='gray', linestyle='--', linewidth=1)
        ax.axhline( upper , color='gray', linestyle='--', linewidth=1)

# %%  explore

# check the existence of an item in a dictionary :
    # it checks the keys of the dictionary.

# 'pH' in normal_ranges
#     # Out[111]: True

# 'g' in normal_ranges
#     # Out[110]: False

# %%'

# x= : the x location of the text in figure coordinates.
# plt.suptitle( 'Blood gass measurements across time' , x=0.4 , fontsize=24 )

# %% add subplot indexing letters

# add subplot indexing letters.

# import string

# Suppose g is your FacetGrid / catplot result
# this works for any number of subplots : you do not need to right a list of letter numbers based on the number of subplots.
letters = list(string.ascii_uppercase)  # ['A','B','C','D',...]

# ha , va : text alignment relative to the (x, y) coordinates you gave :
    # ha='right' means the right edge of the letter is anchored at x=-0.1.
    # va='bottom' means the bottom edge of the letter is anchored at y=1.05.
# That combination places the letter just above and slightly to the left of the subplot, with the text extending leftward and upward from that anchor point.
for ax, letter in zip(g.axes.flatten(), letters):
    ax.text(
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

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.82 , 1] )

# %%'

# bc : baseline corrected

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\blood_gas.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\blood_gas.svg' )


# %%'


