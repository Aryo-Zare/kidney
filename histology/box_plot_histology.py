
df_hist_7 = pd.read_pickle( r'U:\kidney\histology\df_hist_7.pkl' )

# %%

# Define the correct order of pathological categories
# here, homerrheage comes first !
# od : ordered
# this order is changed , correspondingly the titles.
cat_order_3 = [  'cat_2', 'cat_1', 'cat_3', 'cat_4', 'cat_6' , 'cat_5' ]
df_hist_7['cat'] = pd.Categorical( 
                                            df_hist_7['cat'] , 
                                            categories=cat_order_3 , 
                                            ordered=True 
)


# %%

g = sns.catplot(
                data=df_hist_7 , 
                hue="treatment", 
                legend='full' ,   # may not be neeed !
                y="value", 
                col="cat",
                col_wrap=3 ,
                kind="box", 
                # size = 9 ,   
                # linewidth=1 ,
                # edgecolor='gray' ,
                palette=custom_palette ,
                
                medianprops={"color": "black", "linewidth": 2},
                
                # dodge=True , # When a hue variable is assigned ( like here ).
                # jitter=True , #  You can specify the amount of jitter (half the width of the uniform random variable support), 
                                    # or use True for a good default.
                sharex=True, 
                sharey=False, # despite the unit of all y axes being 'cell count(%)', the y axis can not be shared.
                                    # because the nature of the parameters are different !
                height=6, 
                aspect=0.6,
)

# %%

g.set(xticks=[])
g.set( ylim=( 0.8 , 6.2 ) )  # standardize y-lim in all subplots !

# %%

axes = g.axes.flatten()

# explore
    # axes
        # Out[72]: 
        # array([<Axes: title={'center': 'biomarker = HMGB1+_%'}>,
        #        <Axes: title={'center': 'biomarker = NGAL+_%'}>,
        #        <Axes: title={'center': 'biomarker = Casp3+_%'}, ylabel='cell number'>,
        #        <Axes: title={'center': 'biomarker = Zo-1+_%'}>,
        #        <Axes: title={'center': 'biomarker = Syndecan+_%'}>], dtype=object)

axes[0].set_ylabel("score", loc="top" , rotation=90 )
axes[3].set_ylabel("score", loc="top" , rotation=90 )

# %%

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [              
                'Hemorrhage',
                'Neutrophil Infiltration',
                'Lymphocyte Infiltration',
                'Tubular cell degradation',
                'Bowman capsule dilatation' ,
                'Edema'
]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=18 )

# %%

g._legend.set_title("" )

# %%

plt.suptitle( 'Kidney Histopatholgy'    
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.77 , 1] )

# %%

plt.savefig( r'U:\kidney\histology\plot\boxplot_histology.pdf' )
plt.savefig( r'U:\kidney\histology\plot\boxplot_histology.svg' )

# %%


