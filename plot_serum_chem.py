
# overview : plotting the serum markers.

# %%


# %%



# df_serum_chem_4.shape
#     # Out[10]: (8118, 7)

# df_serum_chem_4[:4]
#     # Out[42]: 
#     #   sample_ID treatment group time               metric    value
#     # 0      ZC04   DBD-HTK     1   TI            LDH_serum      752
#     # 1      ZC04   DBD-HTK     1   TI  Total_protein_serum 5.100000
#     # 2      ZC04   DBD-HTK     1   TI           Urea_serum 1.890000
#     # 3      ZC04   DBD-HTK     1   TI      Creatinin_serum       96


# %%


# df_serum_chem_5.shape
#     # Out[50]: (1440, 6)

# df_serum_chem_5.columns
#     # Out[10]: 
#     # Index(['Unnamed: 0', 'sample_ID', 'treatment', 'group', 'time', 'metric',
#     #        'value'],
#     #       dtype='object')


# df_serum_chem_5[:4]
#     # Out[11]: 
#     #     Unnamed: 0 sample_ID treatment group          time               metric  \
#     # 9            9      ZC04   DBD-HTK     1  Explantation            LDH_serum   
#     # 10          10      ZC04   DBD-HTK     1  Explantation  Total_protein_serum   
#     # 11          11      ZC04   DBD-HTK     1  Explantation           Urea_serum   
#     # 12          12      ZC04   DBD-HTK     1  Explantation      Creatinin_serum   
    
#     #    value  
#     # 9    624  
#     # 10   5.2  
#     # 11  2.57  
#     # 12   115  


# # the name 'df_serum_chem_6' has been modified elsewhere : ignore this.
#         df_serum_chem_6 = df_serum_chem_5.reset_index()
#             # Out[20]: 
#             #    index  Unnamed: 0 sample_ID treatment group          time  \
#             # 0      9           9      ZC04   DBD-HTK     1  Explantation   
#             # 1     10          10      ZC04   DBD-HTK     1  Explantation   
#             # 2     11          11      ZC04   DBD-HTK     1  Explantation   
#             # 3     12          12      ZC04   DBD-HTK     1  Explantation   
            
#             #                 metric      value  
#             # 0            LDH_serum 624.000000  
#             # 1  Total_protein_serum   5.200000  
#             # 2           Urea_serum   2.570000  
#             # 3      Creatinin_serum 115.000000  
        
#         df_serum_chem_6[:4]

                                  
# %%

# df_serum_chem_5['sample_ID'].unique()
#     # Out[47]: 
#     # array(['ZC04', 'ZC05', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11', 'ZC6',
#     #        'ZC14', 'ZC15', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC61', 'ZC63',
#     #        'ZC66', 'ZC67', 'ZC68', 'ZC69'], dtype=object)

# %%

# # non-standard NAN as '-' are enforced to comply with pandas NA !
# df_serum_chem_5['value'] = pd.to_numeric( df_serum_chem_5['value'] , errors='coerce' )


# df_serum_chem_5.shape
#     # Out[15]: (1440, 7)

# df_serum_chem_5.columns
#     # Out[20]: 
#     # Index(['Unnamed: 0', 'sample_ID', 'treatment', 'group', 'time', 'metric',
#     #        'value'],
#     #       dtype='object')

# df_serum_chem_6 = df_serum_chem_5.dropna(subset=["value"]).reset_index(drop=True)

# df_serum_chem_6.shape
#     # Out[17]: (1314, 7)


# # this redundant column was inherited from the previous dataframe.
#     # the previous dataframe has this probably because it had undergone the 'reset_index' method without calling : rop=True : 
#         # ( not droppin the old index )
# df_serum_chem_6.drop( columns=[ 'Unnamed: 0' ] , inplace=True )

# df_serum_chem_6.columns
#     # Out[25]: Index(['sample_ID', 'treatment', 'group', 'time', 'metric', 'value'], dtype='object')

# df_serum_chem_6[:4]
#     # Out[24]: 
#     #   sample_ID treatment group          time               metric      value
#     # 0      ZC04   DBD-HTK     1  Explantation            LDH_serum 624.000000
#     # 1      ZC04   DBD-HTK     1  Explantation  Total_protein_serum   5.200000
#     # 2      ZC04   DBD-HTK     1  Explantation           Urea_serum   2.570000
#     # 3      ZC04   DBD-HTK     1  Explantation      Creatinin_serum 115.000000

# df_serum_chem_6.to_csv( r'U:\kidney\df_serum_chem_6.csv' )


# df_serum_chem_6.columns



# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "blue", 
                    "DBD-Ecosol": "red", 
                    "NMP": "black" 
}


# %%

# this can not be called as sns.FacetGrid opens its own new window !!
# fig = plt.figure( figsize=(16,12) , constrained_layout=True)

# %%

# Create a FacetGrid where each facet corresponds to a specific metric
g = sns.FacetGrid( 
                    df_serum_chem_6_od_or , 
                    hue="treatment",
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
# pointplot
g.map_dataframe( 
                    sns.pointplot ,    
                    x='time' , 
                    y='value' ,  # 'value' or 'value_bc'
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
                    y='value' ,   # 'value' or 'value_bc'
                    size = 7 ,   
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
    'Uric acid',
    'LDH',
    'Total protein',
    'CRP',
    'Na+',
    'K+',
    'Cl-'
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

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Serum values for various metabolites & electrolytes across time '   # Change from baseline of
             '\n in different treatment conditions'
             '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

plt.suptitle( 'Change from baseline of serum values for various metabolites & electrolytes across time '   # Change from baseline of
             '\n in different treatment conditions'
             '\n ( after outlier removal _ baseline as Explantation time )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.83 , 1] )

# %%

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

# %%

# bc : baseline corrected

plt.savefig( r'U:\kidney\plot\serum_chem_6_od_or__point.pdf' )

# %%
# %%

mask_LDH = df_serum_chem_6['metric'] == 'LDH_serum'
df_serum_chem_6_LDH = df_serum_chem_6[ mask_LDH ]

# %%

g = sns.catplot(
                data=df_serum_chem_6_LDH , 
                x="time", 
                y="value", 
                hue="treatment",
                kind="strip", 
                palette=custom_palette ,
                size = 7 , 
                height=6, 
                aspect=2
)

# %%

g.set_axis_labels( "time" , "U/L")


plt.xticks(rotation=45, fontsize=16)
# or this way : 
# g.set_xticklabels(rotation=45, fontsize=12)


plt.title( 'LDH' , fontsize=20 ) 

# %%

plt.savefig( r'U:\kidney\plot\LDH.pdf' )

# %%



# %%


