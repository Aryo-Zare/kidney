
df_ELISA_7 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\df_ELISA_7.pkl' )

# %%

df_ELISA_7.shape
    # Out[14]: (176, 10)

df_ELISA_7[:4]
    # Out[9]: 
    #   sample_ID   treatment group metric          time    value  baseline_value  \
    # 0      ZC05  DBD-Ecosol     2  KIM-1  Explantation 0.270281        0.270281   
    # 1      ZC05  DBD-Ecosol     2  KIM-1         POD_1 3.003362        0.270281   
    # 2      ZC05  DBD-Ecosol     2  KIM-1         POD_3 1.807555        0.270281   
    # 3      ZC05  DBD-Ecosol     2  KIM-1         POD_5 7.986841        0.270281   
    
    #    value_bc  value_yjt  value_bc_yjt  
    # 0  0.000000   0.235962      0.000000  
    # 1  2.733082   1.281690      1.360747  
    # 2  1.537274   0.973129      0.952693  
    # 3  7.716560   1.939375      2.284462  

# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}

# %%

df_ELISA_7["metric"].unique()
    # Out[15]: 
    # ['KIM-1', 'NGAL']
    # Categories (2, object): ['KIM-1' < 'NGAL']

# %%

mask_NGAL = df_ELISA_7["metric"] == 'NGAL'
df_NGAL = df_ELISA_7[ mask_NGAL ]

# %%

df_NGAL["time"].unique()
    # Out[10]: 
    # ['Explantation', 'POD_1', 'POD_3', 'POD_5', 'POD_6', 'POD_7', 'POD_2', 'POD_4']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']


# %%

# POD_2 has may missing values : not suitable for statistical analysis : excluded
# there is no data in other POD's.
mask =  df_NGAL["time"].isin([ 'Explantation', 'POD_1', 'POD_3', 'POD_7' ]) 
df_NGAL_2 = df_NGAL[ mask ]

# %%

# despite removing the un-neede items in the previous step, they appear in the order call.
    # this would make trouble when plotting the data, as these removed items will be plotted as blank items !!
    # hence, the order should also be modified.
df_NGAL_2["time"].unique()
    # Out[15]: 
    # ['Explantation', 'POD_1', 'POD_3', 'POD_7']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']

# %%

time_order = ['Explantation', 'POD_1', 'POD_3', 'POD_7']
df_NGAL_2['time'] = pd.Categorical( 
                                            df_NGAL_2['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)

# %%

df_NGAL_2.shape
    # Out[23]: (63, 10)

df_NGAL_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\df_NGAL_2.pkl' )

df_NGAL_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\df_NGAL_2.pkl' )

# %%

# using catplot instead of directly using pointplot lets you direclty control the hight & aspect ratio of the figure !
# dodge : 0.4 : makes a higher dodge , but at the cost of entangled connection lines !!
g = sns.catplot( 
                kind ='point',
                data = df_NGAL_2 ,
                x='time' , 
                y='value' ,  # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                hue="treatment" ,
                marker="o" ,  
                estimator='mean' ,    
                errorbar='se' ,
                dodge=0.2 ,  #  TRUE , 0.4
                height=8, 
                aspect=1 ,
                palette=custom_palette
) 


# %%

g._legend.set_title("" )  # group _ the original legend title is the column name ( treatment )

# Increase the font size of the legend title
g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

for text in g._legend.texts:
    text.set_fontsize(20)  # Adjust as needed

# %%

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=18)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("time" , loc='right' , fontsize=24 )

# %%

plt.ylabel( 'µg/ml' , loc='top' , fontsize=20 )

# %%

# unit = [ 
#         'ng/ml' ,
#         'µg/ml' ,
# ]

# for ax , i in zip( g.axes.flat , unit ) :
#     ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%

# x= : the x location of the text in figure coordinates.
plt.title( 'NGAL (serum)'   # Change from baseline of
             # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.75 , 1] )

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\plot\manuscript\NGAL_2.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\plot\manuscript\NGAL_2.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\plot\manuscript\NGAL_2.eps' )

# %%

