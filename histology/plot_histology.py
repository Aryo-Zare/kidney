
df_hist_7 = pd.read_pickle( r'U:\kidney\histology\df_hist_7.pkl' )

df_hist_7[:4]
    # Out[91]: 
    #   sample_ID treatment group     metric    cat    value  value_yjt
    # 0      ZC04   DBD-HTK     1  histology  cat_1 2.000000   0.665919
    # 1      ZC04   DBD-HTK     1  histology  cat_2 2.000000   0.665919
    # 2      ZC04   DBD-HTK     1  histology  cat_3 2.000000   0.665919
    # 3      ZC04   DBD-HTK     1  histology  cat_4 1.000000   0.499618


# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}


# %%

# this can not be called as sns.FacetGrid opens its own new window !!
# fig = plt.figure( figsize=(16,12) , constrained_layout=True)

# %%

# Create a FacetGrid where each facet corresponds to a specific metric
# importat note : the default values of share-x-y are : True
    # this is not logical.
    # this should only be an option.
    # setting : share-x = True : would cancel specific x-ticks determination for individual subplots !!
g = sns.FacetGrid( 
                    df_hist_7 , 

                    col="metric",  # columns : subplots.
                    col_wrap=1, 
                    sharex=False , 
                    sharey=False , 
                    height=7, 
                    aspect=1.2 
)

# %%
# %%

# g
# stripplot
g.map_dataframe( 
                    sns.stripplot ,  
                    x='cat' , 
                    y='value' ,   # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                    size = 7 ,   
                    dodge=True
) 

# %%

# g
g.map_dataframe(
                    sns.boxplot ,

                    x='cat' , 
                    y='value' ,   # 'value' or 'value_bc'
                    hue="treatment",
                    palette=custom_palette ,
                    
                    # notch=True, 
                    # boxprops={"facecolor": (.3, .5, .7, .5)},
                    medianprops={"color": "black", "linewidth": 2},
                    
                    whis=1.5 ,
                    flierprops={"marker": "x" , 'markersize': 10 }
)


# whis : If scalar, whiskers are drawn to the farthest datapoint within whis * IQR from the nearest hinge.
# dictionaries for customization : https://matplotlib.org/stable/gallery/statistics/boxplot.html#sphx-glr-gallery-statistics-boxplot-py

# %%


# %%

# g
# pointplot
g.map_dataframe( 
                    sns.pointplot ,    
                    x='cat' , 
                    y='value' ,  # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='sd' ,
                    dodge=True
) 

# %%



# %%
# %%

# Add a legend to clearly indicate which color corresponds to which group.
g.add_legend()  # , bbox_to_anchor=(1.05, 0.5), borderaxespad=0 , loc='center left'
g._legend.set_title("group" )
# Increase the font size of the legend title
g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

for text in g._legend.texts:
    text.set_fontsize(20)  # Adjust as needed

# %%

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=12)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("stage" , loc='right' , fontsize=16 )

# %%

# Retrieve the first subplot (Axes object)
first_ax = g.axes[0]

# Set custom tick labels for the first subplot.
# This assumes there are exactly 8 ticks. If necessary, you can also explicitly set the tick positions.
first_ax.set_xticklabels( [ 
                            'Neutrophil Infiltration',
                            'Hemorrhage',
                            'Lymphocyte Infiltration',
                            'Tubular cell degradation',
                            'Edema',
                            'Bowman capsule dilatation'
] , fontsize=16 )


# %%

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [ 'Histopathology' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=24 )

# %%

unit = [ 'score' ]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )


# %%

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Urine release & density  accross time'   # Change from baseline of
             # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

plt.suptitle( 'Blood gass measurements : change from baseline across time '   # Change from baseline of
             # '\n in different treatment conditions'
             '\n ( after outlier removal , baseline as explantation time )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.8 , 1] )

# %%

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

# %%

# bc : baseline corrected

plt.savefig( r'U:\kidney\histology\plot\3.pdf' )


# %%
# %%
