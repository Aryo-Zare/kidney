


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
                data=multiplex_11 , 
                hue="treatment", 
                legend='full' ,   # may not be neeed !
                y="cnp", 
                col="biomarker",
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
                sharey=False,
                height=6, 
                aspect=.6,
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

# %%'

g = sns.catplot(
                data=multiplex_11 , 
                hue="treatment", 
                y="cnp", 
                col="biomarker",
                col_wrap=3 ,
                kind="box", 
                whis=1.5 ,
                flierprops={"marker": "x" , 'markersize': 10 } ,
                palette=custom_palette ,
                gap=0.2 ,
                sharex=True, 
                sharey=False,
                height=6, 
                aspect=.6,
)

# %% point

g = sns.catplot(
                data=multiplex_11 , 
                hue="treatment", 
                legend='full' ,   # may not be neeed !
                y="cnp", 
                col="biomarker",
                col_wrap=3 ,
                kind="point", 
                linestyle="none" ,
                palette=custom_palette ,
                
                marker="_", 
                markersize=20, 
                markeredgewidth=5,
                errorbar=None,
                
                dodge=True , # When a hue variable is assigned ( like here ).

                sharex=True, 
                sharey=False,
                height=6, 
                aspect=.6,
)

# %% overlay point

# overlaying this on the previous strip-plot.

# as the handle is g, you should map it.
    # re-running a second plot would plot it in a separate window !

g.map_dataframe(
                sns.pointplot ,
                data=multiplex_11 , 
                hue="treatment", 
                legend='full' ,   # may not be neeed !
                y="cnp", 
                linestyle="none" ,
                palette=custom_palette ,
                
                marker="_", 
                markersize=20, 
                markeredgewidth=5,
                errorbar=None,
                
                dodge=0.5 , # the exact value was defined by trial & error.
                    # if you don't define it, the strip plot & point-plot will separate each hue level differently.
                    # this will result in a non-perfect overlap.

)


# %%'
# %%'

# Method 1: reset both x and y in one call
    # the first item is the x axis label.
g.set_axis_labels( "", "cell count(%)" )

# Method 2: if you only want to touch the y-label
    # g.set(ylabel="cell number")


# If you ever need to customize each subplot individually, you can also loop over the axes:
    # for ax in g.axes.flatten():
    #     ax.set_ylabel("cell number")


# drop all x-ticks (positions & labels)
g.set(xticks=[])

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

plt.savefig( r'U:\kidney\histology\multiplex\plot\strip_3.pdf' )
plt.savefig( r'U:\kidney\histology\multiplex\plot\strip_3.svg' )


plt.savefig( r'U:\kidney\histology\multiplex\plot\box_4.pdf' )


plt.savefig( r'U:\kidney\histology\multiplex\plot\overlay_2.pdf' )

# %%'
# %%'


# %%'

