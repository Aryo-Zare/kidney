
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
                    height=6, 
                    aspect=1.8 
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

# %%

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Urinalysis'   # Change from baseline of
             # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.8 , 1] )

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\plot\manuscript_urinalysis_value_3.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\plot\manuscript_urinalysis_value_3.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\plot\manuscript_urinalysis_value_3.eps' )

# %%


