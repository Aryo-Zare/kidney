
# %%

df_serum_chem_6_od_or_yjt = pd.read_pickle( r'U:\kidney\df_serum_chem_6_od_or_yjt.pkl' )

# %%

df_serum_chem_6_od_or_yjt["metric"].unique()
    # Out[9]: 
    # ['LDH_serum', 'Total_protein_serum', 'Urea_serum', 'Creatinin_serum', 'Uric_acid_serum', 'Na_serum', 'Ka_serum', 'CRP_serum', 'Cl_serum']
    # Categories (9, object): ['Urea_serum' < 'Creatinin_serum' < 'Uric_acid_serum' < 'LDH_serum' < ... <
    #                          'CRP_serum' < 'Na_serum' < 'Ka_serum' < 'Cl_serum']

# %%

mask =  df_serum_chem_6_od_or_yjt["metric"].isin([ 'Urea_serum' , 'Creatinin_serum' , 'Total_protein_serum' , 'Ka_serum' ]) 
df_serum_chem_6_od_or_yjt_2 = df_serum_chem_6_od_or_yjt[ mask ]

# %%

metric_order = [ 'Urea_serum' , 'Creatinin_serum' , 'Total_protein_serum' , 'Ka_serum' ]
df_serum_chem_6_od_or_yjt_2['metric'] = pd.Categorical(
                                            df_serum_chem_6_od_or_yjt_2['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%

df_serum_chem_6_od_or_yjt_2["metric"].unique()
    # Out[14]: 
    # ['Total_protein_serum', 'Urea_serum', 'Creatinin_serum', 'Ka_serum']
    # Categories (4, object): ['Urea_serum' < 'Creatinin_serum' < 'Total_protein_serum' < 'Ka_serum']

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
                    df_serum_chem_6_od_or_yjt_2 , 
                    hue="treatment",
                    palette=custom_palette ,
                    col="metric", 
                    col_wrap=2, 
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
                    y='value_bc' ,  # 'value' or 'value_bc'
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='sd' ,
                    dodge=True
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

new_titles = [
                'Urea',
                'Creatinin',
                'Total protein',
                'K+'
]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%

unit = [ 
        'mmol/L' ,
        'mmol/L' ,
        'g/dL' ,
        'mmol/L' 
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Serum values across time' , x=0.4 , fontsize=24 )


# %%

plt.suptitle( 'Change from baseline of serum values across time,' 
             '\n Explantation time as baseline'
             , x=0.4 , fontsize=24 )


# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.79 , 1] )

# %%

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

# %%

# bc : baseline corrected

plt.savefig( r'U:\kidney\present\serum_values_bc.pdf' )
plt.savefig( r'U:\kidney\present\serum_values_bc.svg' )

# %%




