
df_NGAL_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\df_NGAL_2.pkl' )

# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}

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
                errorbar='sd' ,
                dodge=0.2 ,  #  TRUE , 0.4
                height=8, 
                aspect=1 ,
                palette=custom_palette
) 

# %%

# Create the stripplot
g.map_dataframe(
                sns.stripplot,
                x='time',
                y='value',
                hue='treatment',
                dodge=0.01,
                jitter=True,
                size=10,
                palette=custom_palette
)

# %%

# Set y-axis to log scale
g.set(yscale="log")


g.set(ylim=(0, 1500))


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
plt.title( 'NGAL (serum) \n SD'   # Change from baseline of
             # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.75 , 1] )

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\plot\test_NGAL\point_strip_ylim.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\plot\test_NGAL\point_strip_ylim.svg' )


# %%


