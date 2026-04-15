
# a combined plot of serum chemistry items & blood-gas.
# the datframe : is generated & saved in a few cells further.

# %%

# all items in this combined cell are commented.

# # remove ucr ( urea / creatinine )
# df1_filtered = df_serum_chem_ucr_value_3_ro[
#     df_serum_chem_ucr_value_3_ro['metric'] != 'ucr'
# ].copy()

# # %%

# metrics_keep = ['pH', 'K+']

# df2_filtered = df_bg_8_4[
#     df_bg_8_4['metric'].isin(metrics_keep)
# ].copy()


# # %%

# # concatenate the common columns ( only columns from the 1st dataframe ).

# common_cols = df1_filtered.columns.intersection(df2_filtered.columns)


# df1_common = df1_filtered[common_cols]
# df2_common = df2_filtered[common_cols]

# # %%


# df_serum_chem__bg = pd.concat(
#     [df1_common, df2_common],
#     ignore_index=True
# )


# # %%

# # sanity checks

# df_serum_chem__bg['metric'].unique()
#     # Out[51]: 
#     # array(['Urea_serum', 'Creatinin_serum', 'Total_protein_serum',
#     #        'CRP_serum', 'pH', 'K+'], dtype=object)

# df_serum_chem__bg.columns
#     # Out[52]: Index(['sample_ID', 'treatment', 'group', 'time', 'metric', 'value'], dtype='object')

# # %%

# metric_order = [ 'Urea_serum', 'Creatinin_serum', 'Total_protein_serum', 'CRP_serum', 'pH', 'K+' ]
# df_serum_chem__bg['metric'] = pd.Categorical(
#                                             df_serum_chem__bg['metric'],
#                                             categories=metric_order,
#                                             ordered=True
# )


# df_serum_chem__bg['metric'].unique()
#     # Out[55]: 
#     # ['Urea_serum', 'Creatinin_serum', 'Total_protein_serum', 'CRP_serum', 'pH', 'K+']
#     # Categories (6, object): ['Urea_serum' < 'Creatinin_serum' < 'Total_protein_serum' < 'CRP_serum' < 'pH' <
#     #                          'K+']

# %%

df_serum_chem__bg.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\df_serum_chem__bg.pkl' )
df_serum_chem__bg = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\df_serum_chem__bg.pkl' )

df_serum_chem__bg[:5]
    # Out[6]: 
    #   sample_ID treatment group          time      metric  value
    # 0      ZC04   SCS-HTK     1  Explantation  Urea_serum   2.57
    # 1      ZC04   SCS-HTK     1         POD_1  Urea_serum  15.60
    # 2      ZC04   SCS-HTK     1         POD_2  Urea_serum  18.73
    # 3      ZC04   SCS-HTK     1         POD_3  Urea_serum  24.36
    # 4      ZC04   SCS-HTK     1         POD_4  Urea_serum  29.00

# %%

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "SCS-HTK": "orange", 
                    "SCS-Omnisol": "blue", 
                    "NMP-Omnisol": "green" 
}

# %% grid

# Create a FacetGrid where each facet corresponds to a specific metric
# col ( column ) is the main argument for .FacetGrid
    # to group the dataframe into multiple sub-frames.
# aspect : when you removed the title, the height of the figure increased is automatically increased.
    # hence the aspect of the figure area is changed  =>  you should increase the aspect here !
g = sns.FacetGrid( 
                    df_serum_chem__bg , 
                    col="metric", 
                    col_wrap=2, 
                    sharex=False , 
                    sharey=False , 
                    height=6, 
                    aspect=1.6 ,
)

# %%

# g
# pointplot
# hue & palette : belong to here, & not to .FacetGrid
g.map_dataframe( 
                    sns.pointplot ,    
                    x='time' , 
                    y='value' ,  # 'value' or 'value_bc'
                    hue="treatment", 
                    palette=custom_palette ,
                    dodge=0.2 ,  #  TRUE
                    marker="o" ,  
                    estimator='mean' ,    
                    errorbar='se' 
) 


# %% Legend

# also adding a legend for the overlapping gray normal range area, under the conventional legend.

# import matplotlib.patches as mpatches

# Get handles/labels from one of the axes
ax0 = g.axes.flatten()[0]
handles , labels = ax0.get_legend_handles_labels()

# gray patch
# Add the proxy patch
# for the normal ranges.
normal_patch = mpatches.Patch(color='lightgray', alpha=0.4, label='Physiological range')
handles.append(normal_patch)
labels.append("Physiological range")

# frameon : the frame around the whole legend area.
g.fig.legend( 
                handles , 
                labels , 
                loc='center right' , 
                frameon=False 
)

# for text in g._legend.texts:
#     text.set_fontsize(20)  # Adjust as needed

# %%

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
    # for the last subplot
g.axes.flat[-1].set_xlabel("Time" , loc='right' , fontsize=24 )

# %%

# as this rewrites the tiles :
    # first check the plot without running this cell to make sure each plot corresponds to your desired order-title.

new_titles = [
                'Urea',
                'Creatinine',
                'Total protein',
                'CRP',
                'pH', 
                'K+'
]

for ax , i in zip( g.axes.flat , new_titles ):
    ax.set_title( i , fontsize=20 )


# %%

unit = [ 
        'mmol/L' ,
        'mmol/L' ,
        'g/dL' ,
        'mg/dL' ,
        '' , 
        'mmol/L' 
]

for ax , i in zip( g.axes.flat , unit ) :
    ax.set_ylabel( i , loc='top' , fontsize=20 )


# %%'  normal range

g.col_names
    # Out[65]: 
    # ['Urea_serum',
    #  'Creatinin_serum',
    #  'Total_protein_serum',
    #  'CRP_serum',
    #  'pH',
    #  'K+']

# replace these with your real metric names & numeric limits
normal_ranges = {
                    'Urea_serum' : ( 3.3 , 8.3 ) , 
                    'Creatinin_serum' : ( 40 , 133 ) , 
                    'Total_protein_serum' : ( 4.5 , 8.5 ) , 
                    'CRP_serum' : ( 0 , 5 ) ,
                    "pH": ( 7.35 , 7.45 ),
                    "K+": ( 3.8 , 5 )
}

# %%

for ax, metric in zip( g.axes.flatten() , g.col_names ):
    lower, upper = normal_ranges[metric]
    # shade the band
    ax.axhspan( lower , upper , color='lightgray', alpha=0.4)
    # draw the boundary lines
    ax.axhline( lower , color='gray', linestyle='--', linewidth=1)
    ax.axhline( upper , color='gray', linestyle='--', linewidth=1)

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


# %%

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.82 , 1] )

# %%


plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\2026_04_15\serum_chem__bg.pdf' )   # serum_values
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\2026_04_15\serum_chem__bg.svg' )   # serum_values


# %% number of values

pivot_counts = (
    df_serum_chem__bg
    .groupby(["metric", "treatment", "time"])
    .agg(n_values=("value", "count"))
    .reset_index()
    .pivot_table(
        index="time",
        columns=["metric", "treatment"],
        values="n_values",
        fill_value=0
    )
)


pivot_counts
    # Out[8]: 
    # metric       Urea_serum                          ...      K+                        
    # treatment       SCS-HTK SCS-Omnisol NMP-Omnisol  ... SCS-HTK SCS-Omnisol NMP-Omnisol
    # time                                             ...                                
    # Explantation        7.0         6.0         6.0  ...     7.0         6.0         6.0
    # POD_1               7.0         6.0         6.0  ...     7.0         6.0         6.0
    # POD_2               7.0         6.0         6.0  ...     7.0         5.0         6.0
    # POD_3               7.0         6.0         6.0  ...     7.0         5.0         5.0
    # POD_4               7.0         6.0         5.0  ...     7.0         6.0         4.0
    # POD_5               6.0         6.0         5.0  ...     6.0         6.0         5.0
    # POD_6               7.0         6.0         5.0  ...     5.0         6.0         5.0
    # POD_7               6.0         6.0         5.0  ...     5.0         5.0         5.0


pivot_counts_2 = pivot_counts.astype(int)

pivot_counts_2.head()
    # Out[10]: 
    # metric       Urea_serum                          ...      K+                        
    # treatment       SCS-HTK SCS-Omnisol NMP-Omnisol  ... SCS-HTK SCS-Omnisol NMP-Omnisol
    # time                                             ...                                
    # Explantation          7           6           6  ...       7           6           6
    # POD_1                 7           6           6  ...       7           6           6
    # POD_2                 7           6           6  ...       7           5           6
    # POD_3                 7           6           6  ...       7           5           5
    # POD_4                 7           6           5  ...       7           6           4

pivot_counts_2_T = pivot_counts_2.T

pivot_counts_2_T
    # Out[48]: 
    # time                             Explantation  POD_1  ...  POD_6  POD_7
    # metric              treatment                         ...              
    # Urea_serum          SCS-HTK                 7      7  ...      7      6
    #                     SCS-Omnisol             6      6  ...      6      6
    #                     NMP-Omnisol             6      6  ...      5      5
    # Creatinin_serum     SCS-HTK                 7      7  ...      7      6
    #                     SCS-Omnisol             6      6  ...      6      6
    #                     NMP-Omnisol             6      6  ...      5      5
    # Total_protein_serum SCS-HTK                 7      7  ...      7      6
    #                     SCS-Omnisol             6      5  ...      6      5
    #                     NMP-Omnisol             6      6  ...      5      5
    # CRP_serum           SCS-HTK                 7      7  ...      6      6
    #                     SCS-Omnisol             6      6  ...      6      6
    #                     NMP-Omnisol             6      6  ...      5      5
    # pH                  SCS-HTK                 7      7  ...      5      5
    #                     SCS-Omnisol             6      6  ...      6      5
    #                     NMP-Omnisol             6      6  ...      5      5
    # K+                  SCS-HTK                 7      7  ...      5      5
    #                     SCS-Omnisol             6      6  ...      6      5
    #                     NMP-Omnisol             6      6  ...      5      5


# %%%'

pivot_counts_2.to_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\number_of_values\df_serum_chem__bg_pivot_counts_2.xlsx' )
pivot_counts_2_T.to_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\number_of_values\df_serum_chem__bg_pivot_counts_2_T.xlsx' )


# %%'

