

# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}

# %%

df_ELISA_7["time"].unique()
    # Out[10]: 
    # ['Explantation', 'POD_1', 'POD_3', 'POD_5', 'POD_6', 'POD_7', 'POD_2', 'POD_4']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']

# %%

# POD_2 has may missing values : not suitable for statistical analysis : excluded
# there is no data in other POD's.
mask =  df_ELISA_7["time"].isin([ 'Explantation', 'POD_1', 'POD_3', 'POD_7' ]) 
df_ELISA_8 = df_ELISA_7[ mask ]

# %%

# despite removing the un-neede items in the previous step, they appear in the order call.
    # this would make trouble when plotting the data, as these removed items will be plotted as blank items !!
    # hence, the order should also be modified.
df_ELISA_8["time"].unique()
    # Out[15]: 
    # ['Explantation', 'POD_1', 'POD_3', 'POD_7']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']

# %%

time_order = ['Explantation', 'POD_1', 'POD_3', 'POD_7']
df_ELISA_8['time'] = pd.Categorical( 
                                            df_ELISA_8['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)


# %%

# using catplot instead of directly using pointplot lets you direclty control the hight & aspect ratio of the figure !
# dodge : 0.4 : makes a higher dodge , but at the cost of entangled connection lines !!
g = sns.catplot( 
                kind ='point',
                data = df_ELISA_8 ,
                x='time' , 
                y='value' ,  # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                hue="treatment" ,
                marker="o" ,  
                estimator='mean' ,    
                errorbar='sd' ,
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

plt.ylabel( 'µg/ml' , loc='top' )

# %%

unit = [ 
        'ng/ml' ,
        'µg/ml' ,
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%

# x= : the x location of the text in figure coordinates.
plt.title( 'NGAL (serum)'   # Change from baseline of
             # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%


# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.75 , 1] )

# %%


# %%


# %%

plt.savefig( r'U:\kidney\ELISA\plot\manuscript\NGAL.pdf' )
plt.savefig( r'U:\kidney\ELISA\plot\manuscript\NGAL.svg' )



# %%

