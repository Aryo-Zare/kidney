
df_hist_7 = pd.read_pickle( r'U:\kidney\histology\df_hist_7.pkl' )

df_hist_7[:4]
    # Out[91]: 
    #   sample_ID treatment group     metric    cat    value  value_yjt
    # 0      ZC04   DBD-HTK     1  histology  cat_1 2.000000   0.665919
    # 1      ZC04   DBD-HTK     1  histology  cat_2 2.000000   0.665919
    # 2      ZC04   DBD-HTK     1  histology  cat_3 2.000000   0.665919
    # 3      ZC04   DBD-HTK     1  histology  cat_4 1.000000   0.499618

# %%


# Define the correct order of pathological categories
# here, homerrheage comes first !
# od : ordered
cat_order_3 = [  'cat_2', 'cat_1', 'cat_3', 'cat_4' , 'cat_6' , 'cat_5']
df_hist_7['cat'] = pd.Categorical( 
                                            df_hist_7['cat'] , 
                                            categories=cat_order_3 , 
                                            ordered=True 
)


# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}


# %%

# this can not be called as sns.FacetGrid opens its own new window !!
# fig = plt.figure( figsize=(16,12) , constrained_layout=True)

# %%

                        # yet, there will be no legend at the side of the plot.

g = sns.catplot(
                data=df_hist_7 , 
                hue="treatment", 
                legend='full' ,   # may not be neeed !
                y="value", 
                col="cat",
                col_wrap=3 ,
                kind="strip", 
                size = 9 ,   
                linewidth=1 ,
                edgecolor='gray' ,
                palette=custom_palette ,
                
                dodge=True , # When a hue variable is assigned ( like here ).
                jitter=True , #  You can specify the amount of jitter (half the width of the uniform random variable support), 
                                    # or use True for a good default.
                sharex=True, 
                sharey=False, # despite the unit of all y axes being 'score', the y axis can not be shared.
                                    # because the nature of the parameters are different !
                height=6, 
                aspect=0.6,
)

# %% overlay point

# overlaying this on the previous strip-plot.

# as the handle is g, you should map it.
    # re-running a second plot would plot it in a separate window !

g.map_dataframe(
                sns.pointplot ,
                data=df_hist_7 , 
                hue="treatment", 
                legend='full' ,   # may not be needed !
                y="value", 
                linestyle="none" ,  # this cancels connecting the points ! ( does it have any value here ? no : the organization of hue is different here )
                palette=custom_palette ,
                
                marker="_", 
                markersize=20, 
                markeredgewidth=5,
                errorbar='sd',
                
                dodge=0.5 , # the exact value was defined by trial & error.
                    # if you don't define it, the strip plot & point-plot will separate each hue level differently.
                    # this will result in a non-perfect overlap.

)


# %%

# g
g.map_dataframe(
                    sns.boxplot ,
                    
                    x='cat' , 
                    y='value' ,   # 'value' or 'value_bc'
                    
                    # notch=True, 
                    # boxprops={"facecolor": (.3, .5, .7, .5)},
                    medianprops={"color": "black", "linewidth": 2},
                    
                    whis=1.5 ,
                    flierprops={"marker": "x" , 'markersize': 10 }
)


# whis : If scalar, whiskers are drawn to the farthest datapoint within whis * IQR from the nearest hinge.
# dictionaries for customization : https://matplotlib.org/stable/gallery/statistics/boxplot.html#sphx-glr-gallery-statistics-boxplot-py

# %%

# drop all x-ticks (positions & labels)
g.set( xticks=[] )
g.set( ylim=( 0.8 , 6.2 ) )  # standardize y-lim in all subplots !

# x axes do nbot have any labels !

# %% y-axis label

# put the y-label of the left side subplots.
        # by using a loop over axes, all axes will get the y axis label : not what you want.


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
# once it happended that te tile of one subplot was not changed.
    # the reason was a missing comma in the list below !

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

# Add a legend to clearly indicate which color corresponds to which group.

g._legend.set_title("" )

# Increase the font size of the legend title
# g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

# for text in g._legend.texts:
#     text.set_fontsize(20)  # Adjust as needed


# %%

plt.suptitle( 'Kidney Histopatholgy'    
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.77 , 1] )

# %%

# C:\Users\azare\AppData\Local\miniconda3\envs\env_1\Lib\site-packages\seaborn\axisgrid.py:854: FutureWarning: 
# Setting a gradient palette using color= is deprecated and will be removed in v0.14.0. Set `palette='dark:#4c72b0'` for the same effect.
#   func(*plot_args, **plot_kwargs)

# %%

# bc : baseline corrected

plt.savefig( r'U:\kidney\histology\plot\strip_point.pdf' )
plt.savefig( r'U:\kidney\histology\plot\strip_point.svg' )


# %%
# %%
