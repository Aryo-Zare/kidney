
multiplex_11 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_11.pkl' )

multiplex_11[:4]
    # Out[90]: 
    #    sample_ID   treatment biomarker      cnp
    # 8       ZC05  DBD-Ecosol  HMGB1+_% 0.529383
    # 9       ZC07  DBD-Ecosol  HMGB1+_% 0.165114
    # 10      ZC09  DBD-Ecosol  HMGB1+_% 0.227194
    # 11      ZC11  DBD-Ecosol  HMGB1+_% 0.062555

# %%'


# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}



# %% strip

# instead of :
                    # hue="treatment", 
                    # legend='full' ,
                # you can use : x = "treatment"
                    # as the palette parameter is defined, each group will still have its own color, 
                        # but the x axis will have label for each cateogry too.
                        # yet, there will be no legend at the side of the plot.

g = sns.catplot(
                kind="strip",             
                data=multiplex_11 , 
                hue="treatment", 
                legend='full' ,   # may not be needed !
                y="cnp", 
                col="biomarker",
                col_wrap=3 ,
                size = 9 ,   
                linewidth=1 ,
                edgecolor='gray' ,
                palette=custom_palette ,
                
                dodge=True , # When a hue variable is assigned ( like here ).
                jitter=True , #  You can specify the amount of jitter (half the width of the uniform random variable support), 
                                    # or use True for a good default.
                sharex=True, 
                sharey=False, # despite the unit of all y axes being 'cell count(%)', the y axis can not be shared.
                                    # because the nature of the parameters are different !
                height=6, 
                aspect=0.6,
)


# %%'

# warning :
    # u:\kidney\histology\multiplex\plot_multiplex.py:18: FutureWarning: 

    # Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. 
    # Assign the `x` variable to `hue` and set `legend=False` for the same effect.

    #   g = sns.catplot(
    # u:\kidney\histology\multiplex\plot_multiplex.py:18: 
        # FutureWarning: Use "auto" to set automatic grayscale colors. From v0.14.0, "gray" will default to matplotlib's definition.
    #   g = sns.catplot(

# %% box

# g = sns.catplot(
#                 data=multiplex_11 , 
#                 hue="treatment", 
#                 y="cnp", 
#                 col="biomarker",
#                 col_wrap=3 ,
#                 kind="box", 
#                 whis=1.5 ,
#                 flierprops={"marker": "x" , 'markersize': 10 } ,
#                 palette=custom_palette ,
#                 gap=0.2 ,
#                 sharex=True, 
#                 sharey=False,
#                 height=6, 
#                 aspect=.6,
# )

# %% point _ separate

# g = sns.catplot(
#                 data=multiplex_11 , 
#                 hue="treatment", 
#                 legend='full' ,   # may not be neeed !
#                 y="cnp", 
#                 col="biomarker",
#                 col_wrap=3 ,
#                 kind="point", 
#                 linestyle="none" ,
#                 palette=custom_palette ,
                
#                 marker="_", 
#                 markersize=20, 
#                 markeredgewidth=5,
#                 errorbar=None,
                
#                 dodge=True , # When a hue variable is assigned ( like here ).

#                 sharex=True, 
#                 sharey=False,
#                 height=6, 
#                 aspect=.6,
# )

# %% overlay point

# overlaying this on the previous strip-plot.

# as the handle is g, you should map it.
    # re-running a second plot would plot it in a separate window !

g.map_dataframe(
                sns.pointplot ,
                data=multiplex_11 , 
                hue="treatment", 
                legend='full' ,   # may not be needed !
                y="cnp", 
                linestyle="none" ,  # this cancels connecting the points ! ( does it have any value here ? no : the organization of hue is different here )
                palette=custom_palette ,
                
                marker="_", 
                markersize=20, 
                markeredgewidth=5,
                errorbar='se',
                
                dodge=0.5 , # the exact value was defined by trial & error.
                    # if you don't define it, the strip plot & point-plot will separate each hue level differently.
                    # this will result in a non-perfect overlap.

)


# %%'
# %%'

# drop all x-ticks (positions & labels)
g.set(xticks=[])

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

axes[0].set_ylabel("cell count(%)", loc="top" , rotation=90 )
axes[3].set_ylabel("cell count(%)", loc="top" , rotation=90 )

# %%'

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [ 'HMGB1' , 'NGAL' , 'Casp3' , 'Zo-1' , 'Syndecan' ]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )


# %%'

# x= : the x location of the text in figure coordinates.
plt.suptitle( 'Multiplex histology of renal tissue'  \
             '\n Percentage of cells with each biomarker positive'    
             , x=0.4 
             , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%'

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.8 , 1] )

# %%'
# %%'

# plt.savefig( r'U:\kidney\histology\multiplex\plot\strip_point.pdf' )
# plt.savefig( r'U:\kidney\histology\multiplex\plot\strip_point.svg' )

# plt.savefig( r'U:\kidney\histology\multiplex\plot\box_4.pdf' )

# plt.savefig( r'U:\kidney\histology\multiplex\plot\overlay_2.pdf' )

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\plot\multiplex_manuscript.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\plot\multiplex_manuscript.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\plot\multiplex_manuscript.eps' )

# %%'


# %%'

