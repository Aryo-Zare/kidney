
# %%'

# df_urine_8_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_urine_8_3.pkl' )

# df_rd_4 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\df_rd_4.pkl' )

# %%'

# df_urine_8_3[:4]
#     # Out[9]: 
#     #    sample_ID treatment group          time     metric        value  \
#     # 5       ZC04   DBD-HTK     1  Explantation       Urea   169.400000   
#     # 6       ZC04   DBD-HTK     1  Explantation  Creatinin 16671.000000   
#     # 9       ZC04   DBD-HTK     1  Explantation    protein    20.000000   
#     # 20      ZC04   DBD-HTK     1         POD_1       Urea    79.800000   
    
#     #     baseline_value   value_bc  value_yjt  value_bc_yjt  
#     # 5       169.400000   0.000000   2.953313      0.000000  
#     # 6     16671.000000   0.000000   3.763891      0.000000  
#     # 9        20.000000   0.000000   2.160419      0.000000  
#     # 20      169.400000 -89.600000   2.715086    -71.476239  


# df_rd_4[:4]
#     # Out[10]: 
#     #   sample_ID treatment group   metric   time       value  baseline_value  \
#     # 0      ZC04   DBD-HTK     1  release  POD_2  110.000000             NaN   
#     # 1      ZC04   DBD-HTK     1  release  POD_3 1500.000000             NaN   
#     # 2      ZC04   DBD-HTK     1  release  POD_4 3200.000000             NaN   
#     # 3      ZC04   DBD-HTK     1  release  POD_5 1700.000000             NaN   
    
#     #    value_bc  value_yjt  value_bc_yjt  
#     # 0       NaN   3.932110           NaN  
#     # 1       NaN   5.554058           NaN  
#     # 2       NaN   5.966349           NaN  
#     # 3       NaN   5.623867           NaN  

# %%'

# # Define the columns you want to keep
# cols_keep = ['sample_ID', 'treatment', 'group', 'metric', 'time', 'value']

# # Subset each dataframe
# df1 = df_urine_8_3[cols_keep]
# df2 = df_rd_4[cols_keep]

# # Concatenate
# df_urine_all = pd.concat([df1, df2], ignore_index=True)

# %%'

# df_urine_all[:4]
#     # Out[14]: 
#     #   sample_ID treatment group     metric          time        value
#     # 0      ZC04   DBD-HTK     1       Urea  Explantation   169.400000
#     # 1      ZC04   DBD-HTK     1  Creatinin  Explantation 16671.000000
#     # 2      ZC04   DBD-HTK     1    protein  Explantation    20.000000
#     # 3      ZC04   DBD-HTK     1       Urea         POD_1    79.800000


# df_urine_all['metric'].unique()
# # Out[15]: array(['Urea', 'Creatinin', 'protein', 'release', 'density'], dtype=object)

# df_urine_all['time'].unique()
#     # Out[16]: 
#     # array(['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5',
#     #        'POD_6', 'POD_7', 'TI'], dtype=object)

# %%'  order


# metric_order = ['Urea', 'Creatinin', 'protein', 'release', 'density' ]
# df_urine_all['metric'] = pd.Categorical(
#                                             df_urine_all['metric'],
#                                             categories=metric_order,
#                                             ordered=True
# )


# time_order = [ 'TI' , 'Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7' ]
# df_urine_all['time'] = pd.Categorical(
#                                             df_urine_all['time'],
#                                             categories=time_order,
#                                             ordered=True
# )

# %%'

# df_urine_all['metric'].unique()
#     # Out[20]: 
#     # ['Urea', 'Creatinin', 'protein', 'release', 'density']
#     # Categories (5, object): ['Urea' < 'Creatinin' < 'protein' < 'release' < 'density']

# df_urine_all['time'].unique()
#     # Out[21]: 
#     # ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7', 'TI']
#     # Categories (9, object): ['TI' < 'Explantation' < 'POD_1' < 'POD_2' ... 'POD_4' < 'POD_5' < 'POD_6' <
#     #                          'POD_7']

# %%'


# df_urine_all['treatment'].unique()
#     # Out[22]: 
#     # ['DBD-HTK', 'DBD-Omnisol', 'NMP']
#     # Categories (3, object): ['DBD-HTK' < 'DBD-Omnisol' < 'NMP']

# %%' rename


# rename_dict = {
#                 'DBD-HTK': 'SCS-HTK' ,
#                 'DBD-Omnisol' : 'SCS-Omnisol' ,
#                 'NMP' : 'NMP-Omnisol'
# }


# df_urine_all['treatment'].replace( to_replace=rename_dict , inplace=True )

# %%'

# df_urine_all['treatment'].unique()
#     # Out[24]: 
#     # ['SCS-HTK', 'SCS-Omnisol', 'NMP-Omnisol']
#     # Categories (3, object): ['SCS-HTK' < 'SCS-Omnisol' < 'NMP-Omnisol']

# %%'

# df_urine_all.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\df_urine_all.pkl' )

df_urine_all = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\df_urine_all.pkl' )


# %% plot

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "SCS-HTK": "green", 
                    "SCS-Omnisol": "blue", 
                    "NMP-Omnisol": "red" 
}


# %% separate orders

# after combining the urinalysis & release-volume dataframes : the 2 dataframes have different x-axis ( 'Time' ) values.
# if defining a single cateogircal order ( TI , explanataion , pod-1 , ...  ) :
    # those suplots without  'TI' or 'explanataion' will irrelevantly havean extra tick for the abscent category with empty data on it.
# so the 'Time' order should be defined separatly for each 'metric' !


time_order_df1 = ['Explantation','POD_1','POD_2','POD_3','POD_4','POD_5','POD_6','POD_7']
time_order_df2 = ['TI','POD_1','POD_2','POD_3','POD_4','POD_5','POD_6','POD_7']

metrics_df1 = ['Urea','Creatinin','protein']   # first 3 metrics
metrics_df2 = ['release','density']            # last 2 metrics


# %% grid

# Create a FacetGrid where each facet corresponds to a specific metric
# col ( column ) is the main argument for .FacetGrid
    # to group the dataframe into multiple sub-frames.
# aspect : when you removed the title, the height of the figure increased is automatically increased.
    # hence the aspect of the figure area is changed  =>  you should increase the aspect here !
g = sns.FacetGrid( 
                    df_urine_all , 
                    col="metric", 
                    col_wrap=2, 
                    sharex=False , 
                    sharey=False , 
                    height=6, 
                    aspect=1.6 ,
)

'''
            the following 2 arguments were present inside parnethesis before :
                    # hue="treatment",
                    # palette=custom_palette ,
            but as they are both needed in : g.map_dataframe :they do not need to be expressed here.
            however, their existence here would no make any problem !-!
'''

# %%' separate definition of orders

# according to a few above cells : the 'Time' order should be defined separatly for each 'metric' !

# quetions
    # <data> is automatically provided by map_dataframe.
        # It’s the subset of your dataframe corresponding to the facet being drawn.
        # Example: if the facet is for metric == "Urea", then data will contain only the rows where metric == "Urea".
    # Why include **kwargs?
        # By including **kwargs, your function can accept and forward them to sns.pointplot (or whatever plotting function you call inside).
        # For example:
                # g.map_dataframe(plot_with_order, x="time", y="value", hue="treatment")
            # will call:
                # plot_with_order(data=subset, x="time", y="value", hue="treatment")
        # If you do not put **kwargs, Python will raise an error if extra arguments are passed.
        # So **kwargs is a safety net that makes your wrapper function flexible.
    # Why use .iloc[0] ?
        # Inside the function, you want to know which metric this facet corresponds to.
        # Since all rows in <data> ( subset selected by g.map_dataframe later ) have the same metric value, you can just look at the first row.
def plot_with_order(data, **kwargs):
    metric = data['metric'].iloc[0]

    if metric in metrics_df1:
        order = time_order_df1

    elif metric == "release":
        # Explicitly remove TI for release
        order = [t for t in time_order_df2 if t != "TI"]

    else:
        order = time_order_df2
        
    sns.pointplot( 
                    data=data ,
                    x='time' , 
                    y='value' ,  # 'value' or 'value_bc'
                    hue="treatment", 
                    palette=custom_palette ,
                    dodge=0.2 ,  #  TRUE
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='se' ,
                    order=order ,
    )

# %%


# FacetGrid.map_dataframe is designed to apply a plotting function separately to each facet (subplot).
# For each facet, Seaborn subsets the dataframe to just the rows belonging to that facet (e.g. all rows where metric == "Urea").
# It then calls the function you provide, passing that subset as the first argument (data).
# That’s why you can pass either a built‑in function like sns.pointplot or your own custom function.
# means: 
    # “For each facet, call : 
        # plot_with_order( data=subset, **kwargs )  
        # where subset is the dataframe slice for that facet.”
g.map_dataframe( plot_with_order )


'''
            if putting : hue="treatment" : only in : sns.FacetGrid( :& not here :
                   AttributeError: 'NoneType' object has no attribute 'index'
           without : legend=False , ( this is only true when hue="treatment" would exist under .FacetGrid ) : 
                   TypeError: functools.partial(<class 'matplotlib.lines.Line2D'>, [], []) got multiple values for keyword argument 'label'
           without : palette=custom_palette : :even if it would be in sns.FacetGrid : the pallete clors will be default.
'''

# %%'

# Add a legend to clearly indicate which color corresponds to which group.
# g.add_legend()  # , bbox_to_anchor=(1.05, 0.5), borderaxespad=0 , loc='center left'

# g._legend.set_title("group" )

# Increase the font size of the legend title
# g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

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

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"

# the one on the bottom right.
g.axes.flat[3].set_xlabel("Time" , loc='right' , fontsize=24 )

# for the last subplot
g.axes.flat[-1].set_xlabel("Time" , loc='right' , fontsize=24 )

# %%'

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [
                'Urea',
                'Creatinine',
                'Protein',
                'Release Volume', 
                'Density' 
]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%'

unit = [ 
        'mmol/L' ,
        'µmol/L' ,
        'mg/dL' ,
        'ml/day' ,
        'Relative density' 
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=20 )

# %%'  normal range

g.col_names
    # Out[58]: ['Urea_serum', 'Creatinin_serum', 'Total_protein_serum', 'CRP_serum']

# replace these with your real metric names & numeric limits
normal_ranges = {
                    "release": (672 , 2772),
                    "density": (1.01 , 1.05 ),
}

# %%%'

for ax , metric in zip( g.axes.flatten() , g.col_names ):
    if metric in normal_ranges :  # I don't know the normal value for ucr.
        lower, upper = normal_ranges[metric]
        # shade the band
        ax.axhspan( lower , upper , color='lightgray', alpha=0.4)
        # draw the boundary lines
        ax.axhline( lower , color='gray', linestyle='--', linewidth=1)
        ax.axhline( upper , color='gray', linestyle='--', linewidth=1)

# %%'

# x= : the x location of the text in figure coordinates.
# plt.suptitle( 'Serum values across time' , x=0.4 , fontsize=24 )


# %%'

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

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

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.82 , 1] )

# %%'

# bc : baseline corrected

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\urine_all.pdf' )   # serum_values
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\urine_all.svg' ) 

# %%'




# %%

