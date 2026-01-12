


# %%

df_serum_chem__bg = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\df_serum_chem__bg.pkl' )
df_urine_all = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\df_urine_all.pkl' )

# %%

df_serum_chem__bg[:4]
    # Out[11]: 
    #   sample_ID treatment group          time      metric     value
    # 0      ZC04   SCS-HTK     1  Explantation  Urea_serum  2.570000
    # 1      ZC04   SCS-HTK     1         POD_1  Urea_serum 15.600000
    # 2      ZC04   SCS-HTK     1         POD_2  Urea_serum 18.730000
    # 3      ZC04   SCS-HTK     1         POD_3  Urea_serum 24.360000


df_urine_all[:4]
    # Out[12]: 
    #   sample_ID treatment group     metric          time        value
    # 0      ZC04   SCS-HTK     1       Urea  Explantation   169.400000
    # 1      ZC04   SCS-HTK     1  Creatinin  Explantation 16671.000000
    # 2      ZC04   SCS-HTK     1    protein  Explantation    20.000000
    # 3      ZC04   SCS-HTK     1       Urea         POD_1    79.800000


# %%

df_serum_chem__bg['metric'].unique()
    # Out[14]: 
    # ['Urea_serum', 'Creatinin_serum', 'Total_protein_serum', 'CRP_serum', 'pH', 'K+']
    # Categories (6, object): ['Urea_serum' < 'Creatinin_serum' < 'Total_protein_serum' < 'CRP_serum' < 'pH' <
    #                          'K+']

df_urine_all['metric'].unique()
    # Out[13]: 
    # ['Urea', 'Creatinin', 'protein', 'release', 'density']
    # Categories (5, object): ['Urea' < 'Creatinin' < 'protein' < 'release' < 'density']

# %%
# %%


df_crp_serum = (
    df_serum_chem__bg
    .loc[df_serum_chem__bg['metric'] == 'CRP_serum']
    .copy()
)


df_protein_urine = (
    df_urine_all
    .loc[df_urine_all['metric'] == 'protein']
    .copy()
)

# %%

df_protein_urine['metric'] = 'protein_urine'


# %%

df_combined = pd.concat(
    [
        df_crp_serum,
        df_protein_urine
    ],
    ignore_index=True
)


# %%

df_combined['metric'] = pd.Categorical(
    df_combined['metric'],
    categories=['CRP_serum', 'protein_urine'],
    ordered=True
)

# %%

df_combined.shape
    # Out[19]: (287, 6)

df_combined[:4]
    # Out[20]: 
    #   sample_ID treatment group          time     metric     value
    # 0      ZC04   SCS-HTK     1  Explantation  CRP_serum  2.000000
    # 1      ZC04   SCS-HTK     1         POD_1  CRP_serum 13.000000
    # 2      ZC04   SCS-HTK     1         POD_2  CRP_serum 14.000000
    # 3      ZC04   SCS-HTK     1         POD_3  CRP_serum 22.000000


df_combined['metric'].unique()
    # Out[21]: 
    # ['CRP_serum', 'protein_urine']
    # Categories (2, object): ['CRP_serum' < 'protein_urine']

# %%

# cs_pu : 'CRP_serum', 'protein_urine'
df_cs_pu = df_combined.copy()


# %%


df_cs_pu['time'].dtype
    # Out[34]: dtype('O')

df_cs_pu['treatment'].dtype
    # Out[35]: CategoricalDtype(categories=['SCS-HTK', 'SCS-Omnisol', 'NMP-Omnisol'], ordered=True, categories_dtype=object)

# %%

# Define explicit orders (important!)
time_order = [
    'Explantation',
    'POD_1', 'POD_2', 'POD_3',
    'POD_4', 'POD_5', 'POD_6', 'POD_7'
]


df_cs_pu['time'] = pd.Categorical(
    df_cs_pu['time'],
    categories=time_order,
    ordered=True
)

# %%

df_cs_pu['time'].dtype
    # Out[37]: 
    # CategoricalDtype(categories=['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5',
    #                   'POD_6', 'POD_7'],
    # , ordered=True, categories_dtype=object)

# %%

df_cs_pu.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\text_search\df_cs_pu.pkl' )

# %%
# %% plot

# %%

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
                data=df_cs_pu , 
                hue="treatment", 
                legend='full' ,   # may not be needed !
                x='time' , 
                y="value", 
                col="metric",
                col_wrap=1 ,
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
                aspect=2.5,
)

# %%

time_levels = df_cs_pu['time'].cat.categories.tolist()
hue_levels = df_cs_pu['treatment'].cat.categories.tolist()

hue_width = 0.6
hue_offsets = np.linspace(
    -hue_width / 2,
     hue_width / 2,
     len(hue_levels)
)
hue_offset_map = dict(zip(hue_levels, hue_offsets))

# %%

rng = np.random.default_rng(42)  # reproducible jitter

for ax, metric in zip(g.axes.flatten(), df_cs_pu['metric'].cat.categories):
    facet_data = df_cs_pu[df_cs_pu['metric'] == metric]

    for _, row in facet_data.iterrows():
        x_base = time_levels.index(row['time'])
        x = (
            x_base
            + hue_offset_map[row['treatment']]
            + rng.uniform(-0.05, 0.05)  # jitter
        )

        ax.text(
            x,
            row['value'],
            row['sample_ID'],
            fontsize=10,
            ha='left',
            va='center',
            color='black',
            alpha=0.8
        )


# %%


# %%



# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\text_search\text_search.svg' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\text_search\text_search.pdf' )

# %%





