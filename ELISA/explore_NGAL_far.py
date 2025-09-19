
df_NGAL_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\df_NGAL_2.pkl' )

# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Ecosol": "blue", 
                    "NMP": "red" 
}

# %%

# Create the stripplot
g = sns.catplot(
    kind='strip',
    data=df_NGAL_2,
    x='time',
    y='value',
    hue='treatment',
    dodge=True,
    jitter=True,
    size=10,
    height=8,
    aspect=1,
    palette=custom_palette
)

# %% text

# add sample-IDs as text next to each datapoint in a scatter.
# biz / F / kidney / AI-stat .docx

# Get the hue and x category orders Seaborn used
hue_levels = list(df_NGAL_2['treatment'].unique())
x_levels   = list(df_NGAL_2['time'].unique())

for ax in g.axes.flatten():
    # collections are ordered by x-category, then hue
    # coll_idx : collections index
    coll_idx = 0
    for x_val in x_levels:
        for hue_val in hue_levels:
            pathcoll = ax.collections[coll_idx]
            offsets = pathcoll.get_offsets()

            # subset the data for this facet, x, and hue
            sub = df_NGAL_2[
                            (df_NGAL_2['time'] == x_val) &
                            (df_NGAL_2['treatment'] == hue_val)
            ]

            # iterate over plotted points and matching rows
            for (x_pt, y_pt), (_, row) in zip(offsets, sub.iterrows()):
                ax.text(
                        x_pt, y_pt,
                        str(row['sample_ID']),
                        ha='left', va='center',
                        fontsize=12, color='black'
                )

            coll_idx += 1


# %%

# explore

Out[40]: 
    # masked_array(
    #   data=[[3.264245216942749, 837.93585],
    #         [3.282048324527086, 738.60165],
    #         [3.2372341261507427, 372.67267499999986],
    #         [3.265554689921772, 490.3136999999999],
    #         [3.235877583677798, 334.084575]],
    #   mask=[[False, False],
    #         [False, False],
    #         [False, False],
    #         [False, False],
    #         [False, False]],
    #   fill_value=1e+20)


hue_levels
    # Out[37]: 
    # ['DBD-Ecosol', 'DBD-HTK', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']


list(df_NGAL_2['time'].unique())
    # Out[41]: ['Explantation', 'POD_1', 'POD_3', 'POD_7']

row['time']
    # Out[40]: 'POD_3'

['Explantation', 'POD_1', 'POD_3', 'POD_7'].index('POD_3')
    # Out[42]: 2

hue_index
    # Out[39]: 2

x_pos
    # Out[38]: 2.2


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



# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ELISA\plot\manuscript\sample_ID\NGAL_sample_ID_2.pdf' )


# %%



