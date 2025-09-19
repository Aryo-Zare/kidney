
# %%'

df_serum_chem_6_od_or_yjt = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\df_serum_chem_6_od_or_yjt.pkl' )

# %%'

df_serum_chem_6_od_or_yjt["metric"].unique()
    # Out[9]: 
    # ['LDH_serum', 'Total_protein_serum', 'Urea_serum', 'Creatinin_serum', 'Uric_acid_serum', 'Na_serum', 'Ka_serum', 'CRP_serum', 'Cl_serum']
    # Categories (9, object): ['Urea_serum' < 'Creatinin_serum' < 'Uric_acid_serum' < 'LDH_serum' < ... <
    #                          'CRP_serum' < 'Na_serum' < 'Ka_serum' < 'Cl_serum']

# %%'

mask =  df_serum_chem_6_od_or_yjt["metric"].isin([ 'Urea_serum' , 'Creatinin_serum' , 'Total_protein_serum' , 'CRP_serum' ]) 
df_serum_chem_6_od_or_yjt_2 = df_serum_chem_6_od_or_yjt[ mask ]

# %%'

metric_order = [ 'Urea_serum' , 'Creatinin_serum' , 'Total_protein_serum' , 'CRP_serum' ]
df_serum_chem_6_od_or_yjt_2['metric'] = pd.Categorical(
                                            df_serum_chem_6_od_or_yjt_2['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%'

df_serum_chem_6_od_or_yjt_2["metric"].unique()
    # Out[14]: 
    # ['Total_protein_serum', 'Urea_serum', 'Creatinin_serum', 'CRP_serum']
    # Categories (4, object): ['Urea_serum' < 'Creatinin_serum' < 'Total_protein_serum' < 'CRP_serum']

# %%'

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}

# %% grid

# Create a FacetGrid where each facet corresponds to a specific metric
# col ( column ) is the main argument for .FacetGrid
    # to group the dataframe into multiple sub-frames.
g = sns.FacetGrid( 
                    df_serum_chem_6_od_or_yjt_2 , 
                    col="metric", 
                    col_wrap=2, 
                    sharex=False , 
                    sharey=False , 
                    height=6, 
                    aspect=1.2 ,
)

'''
            the following 2 arguments were present inside parnethesis before :
                    # hue="treatment",
                    # palette=custom_palette ,
            but as they are both needed in : g.map_dataframe :they do not need to be expressed here.
            however, their existence here would no make any problem !-!
'''

# %%'

# g
# pointplot
# hue & palette : belong to here, & not to .FacetGrid
g.map_dataframe( 
                    sns.pointplot ,    
                    x='time' , 
                    y='value' ,  # 'value' or 'value_bc'
                    hue="treatment", 
                    palette=custom_palette ,
                    dodge=0.2 ,  #  TRUE
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='se' 
) 

'''
            if putting : hue="treatment" : only in : sns.FacetGrid( :& not here :
                   AttributeError: 'NoneType' object has no attribute 'index'
           without : legend=False , ( this is only true when hue="treatment" would exist under .FacetGrid ) : 
                   TypeError: functools.partial(<class 'matplotlib.lines.Line2D'>, [], []) got multiple values for keyword argument 'label'
           without : palette=custom_palette : :even if it would be in sns.FacetGrid : the pallete clors will be default.
'''

# %%'

# Add a legend to clearly indicate which color corresponds to which group.
g.add_legend()  # , bbox_to_anchor=(1.05, 0.5), borderaxespad=0 , loc='center left'

# g._legend.set_title("group" )

# Increase the font size of the legend title
g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

for text in g._legend.texts:
    text.set_fontsize(20)  # Adjust as needed

# %%'

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=12)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("stage" , loc='right' , fontsize=16 )

# %%'

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [
                'Urea',
                'Creatinin',
                'Total protein',
                'CRP'
]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )

# %%'

unit = [ 
        'mmol/L' ,
        'mmol/L' ,
        'g/dL' ,
        'mg/dL' 
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%'  normal range

g.col_names
    # Out[58]: ['Urea_serum', 'Creatinin_serum', 'Total_protein_serum', 'CRP_serum']

# replace these with your real metric names & numeric limits
normal_ranges = {
                    'Urea_serum' : ( 3.3 , 8.3 ) , 
                    'Creatinin_serum' : ( 40 , 133 ) , 
                    'Total_protein_serum' : ( 4.5 , 8.5 ) , 
                    'CRP_serum' : ( 0 , 5 ) 
}

# %%%'

for ax, metric in zip( g.axes.flatten() , g.col_names ):
    lower, upper = normal_ranges[metric]
    # shade the band
    ax.axhspan( lower , upper , color='lightgray', alpha=0.4)
    # draw the boundary lines
    ax.axhline( lower , color='gray', linestyle='--', linewidth=1)
    ax.axhline( upper , color='gray', linestyle='--', linewidth=1)

# %%'

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Serum values across time' , x=0.4 , fontsize=24 )


# %%'

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.82 , 1] )

# %%'

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

# %%'

# bc : baseline corrected

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\plot\manuscript\serum_values_3.pdf' )   # serum_values
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\plot\manuscript\serum_values_3.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\plot\manuscript\serum_values_3.eps' )

# %%'




