
# multiplex_11 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_11.pkl' )

# %%'

# multiplex_11[:4]
#     # Out[90]: 
#     #    sample_ID   treatment biomarker      cnp
#     # 8       ZC05  DBD-Ecosol  HMGB1+_% 0.529383
#     # 9       ZC07  DBD-Ecosol  HMGB1+_% 0.165114
#     # 10      ZC09  DBD-Ecosol  HMGB1+_% 0.227194
#     # 11      ZC11  DBD-Ecosol  HMGB1+_% 0.062555

# %%'

# multiplex_11['treatment'] = (
#                                 multiplex_11['treatment']
#                                 .replace({'DBD-Ecosol': 'DBD-Omnisol'})
# )

# multiplex_12 = multiplex_11.copy()

# %%'

# multiplex_12.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_12.pkl' )

# multiplex_12 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_12.pkl' )

# %%'

# rename_dict = {
#                 'DBD-HTK': 'SCS-HTK' ,
#                 'DBD-Omnisol' : 'SCS-Omnisol' ,
#                 'NMP' : 'NMP-Omnisol'
# }


# multiplex_12['treatment'].replace( to_replace=rename_dict , inplace=True )

# %%'

# multiplex_13 = multiplex_12.copy()

# multiplex_13.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_13.pkl' )

multiplex_13 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_13.pkl' )

# %%'


# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "SCS-HTK": "green", 
                    "SCS-Omnisol": "blue", 
                    "NMP-Omnisol": "red" 
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
                data=multiplex_13 , 
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
                jitter=False , #  You can specify the amount of jitter (half the width of the uniform random variable support), 
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
                data=multiplex_13 , 
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

# %%'

g._legend.set_title("" )  # group _ the original legend title is the column name ( treatment )

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
# plt.suptitle( 'Multiplex histology of renal tissue'  \
#              '\n Percentage of cells with each biomarker positive'    
#              , x=0.4 
#              , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %% add subplot indexing letters

# add subplot indexing letters.

# import string

# Suppose g is your FacetGrid / catplot result
# this works for any number of subplots : you do not need to right a list of letter numbers based on the number of subplots.
letters = list( string.ascii_uppercase )  # ['A','B','C','D',...]

# ha , va : text alignment relative to the (x, y) coordinates you gave :
    # ha='right' means the right edge of the letter is anchored at x=-0.1.
    # va='bottom' means the bottom edge of the letter is anchored at y=1.05.
# That combination places the letter just above and slightly to the left of the subplot, with the text extending leftward and upward from that anchor point.
for ax , letter in zip( g.axes.flatten() , letters ):
    ax.text(                           # the most important part !
            -0.1, 1.05, letter,        # position relative to each axis.
            transform=ax.transAxes,    # use axes fraction coords
            fontsize=20, fontweight='bold',
            va='bottom', ha='right'
    )

# transform=ax.transAxes :
    # By default, when you call ax.text(x, y, ...), Matplotlib interprets x and y in data coordinates (the same units as your plotted data).
        # Example: if your y‑axis goes from 0 to 100, then ax.text(0, 120, "label") would place text above the data range.
    # transform=ax.transAxes tells Matplotlib: “Interpret (x, y) in axes fraction coordinates instead of data coordinates.”
        # In this coordinate system:
            # (0, 0) = bottom‑left corner of the subplot’s axes
            # (1, 1) = top‑right corner of the subplot’s axes
        # Values can go slightly outside that range (e.g. -0.1, 1.05) to nudge text just beyond the axes.

# %%' annotate

# note : the different colors ( treatment categories ) are dodge-separated : not tick-separated !
    # possibly most annotation programs work on ticks & not dodging !
    # Original seaborn plot : No x-axis input : instead ; hue
    # Dodging the hue : all 3 'treatment' categories were originally overlapped on 1 tick : at position : 0 : on x-axis
    # after dodging, this position 0  was expendad +/- 0.25 .
    # the package ; statannotations : does not work with dodged separations !
        # this is generally expected , since 
            # few instances are so wide dodges
            # without x-axis input into the face-grid ( only hue at x-axis ).
            # dodge is usually a small amount to improve visualization.


# Suppose subplot-4 corresponds to index 3 (0-based)
ax = g.axes.flatten()[3]

# left & right ends of the line.
x1, x2 = -0.25, 0


y = ax.get_ylim()[1] * 0.75   # place bar near the top of the y-axis
h = 0.6                      # height of the bracket ( vertical thickness ).
col = 'k'

# Draw the bar
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=3, c=col)

# Add the star (or "**" depending on p-value)
# va : vertical alignment : means the bottom of the text sits at y+h+0.01.
ax.text((x1+x2)*.5, y+h+0.01, "*", ha='center', va='bottom', color=col, fontsize=24)

# after the annotation, the x-axis range gets ruined !
# re-adjust it.
plt.xlim( -0.5 , 0.5 )

# %%'

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.8 , 1] )

# %%'


# plt.savefig( r'U:\kidney\histology\multiplex\plot\strip_point.pdf' )
# plt.savefig( r'U:\kidney\histology\multiplex\plot\strip_point.svg' )

# plt.savefig( r'U:\kidney\histology\multiplex\plot\box_4.pdf' )

# plt.savefig( r'U:\kidney\histology\multiplex\plot\overlay_2.pdf' )

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\multiplex.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\multiplex.svg' )


# %%'

# %% mean

# incorrect for multiplex : mean : 
    # reason : unlike the conventional histology, where all metrics had the same range ( 0-6 ), \
    # multiplex study has different ranges for differnet metrics.
    # hence, one sample with a big sizze on a metric with big ranges, will corrupt the whole mean !!

multiplex_13.groupby('treatment', as_index=False)['cnp'].mean()
    #      treatment      cnp
    # 0      SCS-HTK 1.953287
    # 1  SCS-Omnisol 0.673771
    # 2  NMP-Omnisol 0.914337

# %%


