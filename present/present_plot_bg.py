
# %%

df_bg_8 = pd.read_pickle( r'U:\kidney\BG\df_bg_8.pkl' )

# %%

df_bg_8["metric"].unique()
    # Out[37]: 
    # ['pH', 'K+', 'Na+', 'Ca2+', 'Cl-', 'pCO2', 'pO2']
    # Categories (7, object): ['pH' < 'pCO2' < 'pO2' < 'Na+' < 'K+' < 'Ca2+' < 'Cl-']

# %%

mask =  df_bg_8["metric"].isin([ 'pH', 'K+' ]) 
df_bg_8_2 = df_bg_8[ mask ]

# %%

metric_order = [ 'pH', 'K+' ]
df_bg_8_2['metric'] = pd.Categorical(
                                            df_bg_8_2['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%

df_bg_8_2["metric"].unique()
    # Out[40]: 
    # ['pH', 'K+']
    # Categories (2, object): ['pH' < 'K+']

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
                    df_bg_8_2 , 
                    hue="treatment",
                    palette=custom_palette ,
                    col="metric", 
                    # col_wrap=2, 
                    # sharex=True , 
                    sharey=False ,  # this value is True by default !! : change it to False !!
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

new_titles = [ 'pH', 'K+' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%

unit = [ '' , 'mmol/L' ]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Blood gass measurements across time' , x=0.4 , fontsize=24 )


# %%

plt.suptitle( 'Change from baseline of blood gass measurements,' 
             '\n Explantation time as baseline'
             , x=0.4 , fontsize=24 )


# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.79 , 1] )

# %%

# bc : baseline corrected

plt.savefig( r'U:\kidney\present\plot\bg_values_bc_2.pdf' )
plt.savefig( r'U:\kidney\present\plot\bg_values_bc_2.svg' )

# %%


