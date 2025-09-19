
# %%

df_bg_8 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_bg_8.pkl' )

# %%

df_bg_8["metric"].unique()
    # Out[37]: 
    # ['pH', 'K+', 'Na+', 'Ca2+', 'Cl-', 'pCO2', 'pO2']
    # Categories (7, object): ['pH' < 'pCO2' < 'pO2' < 'Na+' < 'K+' < 'Ca2+' < 'Cl-']

# %%

mask =  df_bg_8["metric"].isin([ 'pH', 'K+' , 'pCO2', 'pO2' ]) 
df_bg_8_2 = df_bg_8[ mask ]

# %%

metric_order = [ 'pH', 'K+' , 'pCO2', 'pO2' ]
df_bg_8_2['metric'] = pd.Categorical(
                                            df_bg_8_2['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%

df_bg_8_2["metric"].unique()
    # Out[99]: 
    # ['pH', 'K+', 'pCO2', 'pO2']
    # Categories (4, object): ['pH' < 'K+' < 'pCO2' < 'pO2']

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
                    col="metric", 
                    col_wrap=2, 
                    sharex=False , 
                    sharey=False ,  # this value is True by default !! : change it to False !!
                    height=6, 
                    aspect=1.2 
)

# %%

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

new_titles = [ 'pH', 'K+' , 'pCO2', 'pO2' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%

unit = [ '' , 'mmol/L' , 'mmHg' , 'mmHg' ]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%'  normal range

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

'pH' in normal_ranges
    # Out[111]: True

'g' in normal_ranges
    # Out[110]: False

# %%

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Blood gass measurements across time' , x=0.4 , fontsize=24 )


# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.82 , 1] )

# %%

# bc : baseline corrected

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\plot\manuscript_bg_values_3.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\plot\manuscript_bg_values_3.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\plot\manuscript_bg_values_3.eps' )

# %%


