

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
                    df_urine_8 , 
                    hue="treatment",
                    palette=custom_palette ,
                    col="metric",  # columns : subplots.
                    col_wrap=3, 
                    sharex=True , 
                    sharey=False , 
                    height=4, 
                    aspect=1.2 
)

# %%

# g
# pointplot
g.map_dataframe( 
                    sns.pointplot ,    
                    x='time' , 
                    y='value' ,  # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='sd' ,
                    dodge=True
) 

# %%

# g
# stripplot
g.map_dataframe( 
                    sns.stripplot ,  
                    x='time' , 
                    y='value' ,   # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                    size = 7 ,   
                    dodge=True
) 

# %%

# g
# box-plot
g.map_dataframe(
                    sns.boxplot ,
                    
                    x='time' , 
                    y='value' ,   # 'value' or 'value_bc'
                    
                    # notch=True, 
                    # boxprops={"facecolor": (.3, .5, .7, .5)},
                    medianprops={"color": "black", "linewidth": 2},
                    
                    whis=1.5 ,
                    flierprops={"marker": "x" , 'markersize': 10 }
)

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

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [ 'Urea' , 'Creatinin' , 'protein' , 'Na+' , 'K+' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%

unit = [ 
        'mmol/L' ,
        'µmol/L' ,
        'mg/dL' ,
        'mmol/L' ,
        'mmol/L'
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Urinalysis'   # Change from baseline of
             # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

plt.suptitle( 'Urinalysis : change from baseline across time '   # Change from baseline of
             # '\n in different treatment conditions'
             '\n ( after outlier removal , baseline as explantation time )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.83 , 1] )

# %%

plt.savefig( r'U:\kidney\urine\plot\urinalysis_original.pdf' )

# %%


