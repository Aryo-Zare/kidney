
# this file may need to be deleted !


# %% custom_palette

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "blue", 
                    "DBD-Ecosol": "red", 
                    "NMP": "black" 
}

# %%

# Create a FacetGrid where each facet corresponds to a specific metric
g = sns.FacetGrid( 
                    df_serum_chem_6_od_or , 
                    # hue="treatment",
                    palette=custom_palette ,
                    col="metric", 
                    col_wrap=3, 
                    sharex=True , 
                    sharey=False , 
                    height=4, 
                    aspect=1.2 
)

# %%

# g
# stripplot
g.map_dataframe( 
                    sns.stripplot ,  
                    x='treatment' , 
                    y='value_bc' , 
                    size = 7 ,   
                    dodge=True
) 


# %%

# not appropriate
# this shows values of all metrics with different units on one single y axis !

    # g = sns.catplot(
    #                 data=df_serum_chem_5_bc_TI, 
    #                 x='metric', 
    #                 y='value', 
    #                 hue='treatment',
    #                 kind="strip", 
    #                 height=4, 
    #                 aspect=2 ,
    # )


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
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("" , "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("group" , loc='right' , fontsize=16 )

# %%

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [
    'Urea',
    'Creatinin',
    'Uric acid',
    'LDH',
    'Total protein',
    'CRP',
    'Na',
    'K',
    'Cl'
]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%

unit = [ 
        'mmol/L' ,
        'mmol/L' ,
        'µmol/L' ,
        
        'U/L' ,
        'g/dL' ,
        'mg/dL' ,
        
        'mmol/L' ,
        'mmol/L' ,	
        'mmol/L' ,
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )


# %%

plt.suptitle( 'Baseline serum values at TI ( Transponder Implantation ) stage \n in 3 different groups ' , 
             fontsize=24 )
#  \n mean_sd   #  for pointplot


# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout()

# %%

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

# %%

plt.savefig( r'U:\kidney\plot\baseline.pdf' )

# %%

# %%
