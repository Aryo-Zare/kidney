
multiplex_11 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_11.pkl' )

# %%

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

# %%

# Get the hue levels in the order Seaborn used
hue_levels = list(multiplex_11['treatment'].unique())

for ax, biomarker_val in zip(g.axes.flatten(), multiplex_11['biomarker'].unique()):
    # Subset the data for this facet
    facet_data = multiplex_11[multiplex_11['biomarker'] == biomarker_val]

    coll_idx = 0
    for hue_val in hue_levels:
        # Get the PathCollection for this hue in this facet
        pathcoll = ax.collections[coll_idx]
        offsets = pathcoll.get_offsets()

        # Subset the data for this hue in this facet
        sub = facet_data[facet_data['treatment'] == hue_val]

        # Loop over plotted points and matching rows
        for (x_pt, y_pt), (_, row) in zip(offsets, sub.iterrows()):
            ax.text(
                x_pt, y_pt,
                str(row['sample_ID']),
                ha='left', va='center',
                fontsize=12, color='black'
            )

        coll_idx += 1


# %%

g.set(xticks=[])

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

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\plot\overlap_text__multiplex.pdf' )


# %%


