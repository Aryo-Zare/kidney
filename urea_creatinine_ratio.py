

# the most important dataframes : 
        # df_serum_chem_ucr_value_3 : with the outliers
        # df_serum_chem_ucr_value_3_ro  :  without the outliers
    # see below

# %%'

df_serum_chem_6_od_or_yjt_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\df_serum_chem_6_od_or_yjt_3.pkl' )

# %%'

df_serum_chem_6_od_or_yjt_3.shape
# Out[20]: (576, 10)]

df_serum_chem_6_od_or_yjt_3.columns
    # Out[9]: 
    # Index(['sample_ID', 'treatment', 'group', 'time', 'metric', 'value',
    #        'baseline_value', 'value_bc', 'value_yjt', 'value_bc_yjt'],
    #       dtype='object')

df_serum_chem_6_od_or_yjt_3['metric'].unique()
    # Out[10]: 
    # ['Total_protein_serum', 'Urea_serum', 'Creatinin_serum', 'CRP_serum']
    # Categories (4, object): ['Urea_serum' < 'Creatinin_serum' < 'Total_protein_serum' < 'CRP_serum']


df_serum_chem_6_od_or_yjt_3['value'].isna().sum()
    # Out[103]: np.int64(0)

# %%' pivot

df_value_wide = df_serum_chem_6_od_or_yjt_3.pivot_table(
                                index=['sample_ID', 'treatment', 'group', 'time'],
                                columns='metric',
                                values='value'
).reset_index()

# %%'

df_value_wide.columns
    # Out[12]: 
    # Index(['sample_ID', 'treatment', 'group', 'time', 'Urea_serum',
    #        'Creatinin_serum', 'Total_protein_serum', 'CRP_serum'],
    #       dtype='object', name='metric')


df_value_wide.shape
    # Out[21]: (146, 9)

# ucr : urea/creatinine ratio
df_value_wide['ucr'] = (
                    df_value_wide['Urea_serum'] / df_value_wide['Creatinin_serum']
)

df_value_wide.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_value_wide.pkl' )


# %%' melt

# melt
df_serum_chem_ucr_value = df_value_wide.melt(
            id_vars=['sample_ID', 'treatment', 'group', 'time'],
            value_vars=[
                        'Urea_serum', 
                        'Creatinin_serum', 
                        'Total_protein_serum',
                        'CRP_serum', 
                        'ucr'
                        ],
            var_name='metric',
            value_name='value'
)

# %%'

# after melting, some columns loose their order.
metric_order = [ 'Urea_serum' , 'Creatinin_serum' , 'ucr' , 'Total_protein_serum' , 'CRP_serum' ]
df_serum_chem_ucr_value['metric'] = pd.Categorical(
                                            df_serum_chem_ucr_value['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%'

df_serum_chem_ucr_value_2 = (
    df_serum_chem_ucr_value.dropna(subset=['value'])
)

# %%'

df_serum_chem_ucr_value_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_2.pkl' )

# %%' rename

df_serum_chem_ucr_value_2['treatment'].unique()
    # Out[117]: 
    # ['DBD-HTK', 'DBD-Omnisol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Omnisol' < 'NMP']


# on : original name : Ecosol ( instead of omnisol )
df_serum_chem_ucr_value_3 = df_serum_chem_ucr_value_2.copy()

# df_serum_chem_ucr_value_3['treatment'] = (
#                                             df_serum_chem_ucr_value_3['treatment']
#                                             .replace({
#                                                         'DBD-HTK': 'SCS-HTK' ,
#                                                         'DBD-Omnisol' : 'SCS-Omnisol' ,
#                                                         'NMP' : 'NMP-Omnisol'
#                                                       })
# )

rename_dict = {
                'DBD-HTK': 'SCS-HTK' ,
                'DBD-Omnisol' : 'SCS-Omnisol' ,
                'NMP' : 'NMP-Omnisol'
}


df_serum_chem_ucr_value_3['treatment'].replace( to_replace=rename_dict , inplace=True )




df_serum_chem_ucr_value_3['treatment'].unique()
    # Out[120]: 
    # ['SCS-HTK', 'SCS-Omnisol', 'NMP-Omnisol']
    # Categories (3, object): ['SCS-HTK' < 'SCS-Omnisol' < 'NMP-Omnisol']


# this is the most important frame.
df_serum_chem_ucr_value_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_3.pkl' )

# %% remove the outliers

# remove the outliers : for a more logical plotting.

df_serum_chem_ucr_value_3.shape
    # Out[30]: (721, 6)

mask_outlier = (
                        ( df_serum_chem_ucr_value_3['metric'] == 'ucr') & 
                        ( df_serum_chem_ucr_value_3['value'] > 0.15)
)


# ro : remove outliers
df_serum_chem_ucr_value_3_ro = df_serum_chem_ucr_value_3[ ~mask_outlier ]

# 2 outliers removed.
df_serum_chem_ucr_value_3_ro.shape
    # Out[31]: (719, 6)

df_serum_chem_ucr_value_3_ro.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_3_ro.pkl' )


# %%'
# %%'


# on : original name : Ecosol ( instead of omnisol )
df_serum_chem_ucr_value_on = df_serum_chem_ucr_value.copy()

df_serum_chem_ucr_value_on['treatment'] = (
                                        df_serum_chem_ucr_value_on['treatment']
                                        .replace({'DBD-Omnisol': 'DBD-Ecosol'})
)

# %%'

# after melting, some columns loose their order.
metric_order = [ 'Urea_serum' , 'Creatinin_serum' , 'ucr' , 'Total_protein_serum' , 'CRP_serum' ]
df_serum_chem_ucr_value_on['metric'] = pd.Categorical(
                                            df_serum_chem_ucr_value_on['metric'],
                                            categories=metric_order,
                                            ordered=True
)


# %%'

df_serum_chem_ucr_value_on['treatment'].unique()
    # Out[77]: 
    # ['DBD-HTK', 'DBD-Ecosol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

df_serum_chem_ucr_value_on['metric'].unique()
    # Out[111]: 
    # ['Urea_serum', 'Creatinin_serum', 'Total_protein_serum', 'CRP_serum', 'ucr']
    # Categories (5, object): ['Urea_serum' < 'Creatinin_serum' < 'ucr' < 'Total_protein_serum' <
    #                          'CRP_serum']



    # Out[75]: 
    #   sample_ID treatment  group          time      metric     value
    # 0      ZC04   DBD-HTK      1  Explantation  Urea_serum  2.570000
    # 1      ZC04   DBD-HTK      1         POD_1  Urea_serum 15.600000
    # 2      ZC04   DBD-HTK      1         POD_2  Urea_serum 18.730000
    # 3      ZC04   DBD-HTK      1         POD_3  Urea_serum 24.360000

df_serum_chem_ucr_value_on[-4:]
    # Out[76]: 
    #     sample_ID treatment  group          time metric    value
    # 726      ZC69       NMP      0  Explantation    ucr 0.010096
    # 727      ZC69       NMP      0         POD_1    ucr 0.026497
    # 728      ZC69       NMP      0         POD_2    ucr 0.021881
    # 729      ZC69       NMP      0         POD_3    ucr 0.023242

df_serum_chem_ucr_value_on[300:304]
    # Out[79]: 
    #     sample_ID   treatment  group   time               metric    value
    # 300      ZC05  DBD-Ecosol      2  POD_1  Total_protein_serum 4.000000
    # 301      ZC05  DBD-Ecosol      2  POD_2  Total_protein_serum 3.700000
    # 302      ZC05  DBD-Ecosol      2  POD_3  Total_protein_serum 5.500000
    # 303      ZC05  DBD-Ecosol      2  POD_4  Total_protein_serum 6.100000

# %%'

# melted.
df_serum_chem_ucr_value.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value.pkl' )
df_serum_chem_ucr_value_on.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_on.pkl' )


# %%'

# the number of rows increased, s there is one more item in 'metric' column.
df_serum_chem_ucr_value.shape
    # Out[18]: (730, 6)

# %%'
# %%'

# Define a custom palette for the hue levels in the desired order
custom_palette = { 
                    "DBD-HTK": "green", 
                    "DBD-Omnisol": "blue", 
                    "NMP": "red" 
}


# %%'

fig , ax = plt.subplots( 2,1 , figsize=(12,12) )

sns.pointplot(   
                data=df_value_wide ,          
                x='time' , 
                y='ucr' ,  # 'value' or 'value_bc'
                hue="treatment", 
                palette=custom_palette ,
                dodge=0.2 ,  #  TRUE
                marker="o" ,  
                estimator='mean' ,    
                errorbar='se' ,
                ax=ax[0]
)

sns.stripplot(   
                data=df_value_wide ,          
                x='time' , 
                y='ucr' ,  # 'value' or 'value_bc'
                hue="treatment", 
                palette=custom_palette ,
                dodge=0.2 ,  #  TRUE
                marker="o" ,  
                # estimator='mean' ,    
                # errorbar='sd' ,
                ax=ax[1]
)

# %%'

# before
# ax
    # Out[41]: 
    # array([<Axes: xlabel='time', ylabel='ucr'>,
    #        <Axes: xlabel='time', ylabel='ucr'>], dtype=object)

# don't use.
for ax in ax.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)

# # after
    # ax
    # Out[43]: <Axes: xlabel='time', ylabel='ucr'>

# %%'


for ax in ax.flat:
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=16)
    ax.set_xlabel("Time" , loc='right' , fontsize=24 )

# %%'

plt.suptitle( 'UCR , SEM' , fontsize=20 )

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout( rect=[0, 0, 0.82 , 1] )

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\ucr_sem.pdf' )   # serum_values
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\ucr_sem.svg' )

# %%'
# %%' rooting out the problem

# rooting out the problem of 'index out of bound' errors by mixed-model test.

test_original = df_serum_chem_ucr_value_on['metric'] != 'ucr'

# mv : main values
df_serum_chem_ucr_value_on_mv = df_serum_chem_ucr_value_on[test_original]

# this is higher than the number of rows of the original dataframe.
df_serum_chem_ucr_value_on_mv.shape
    # Out[84]: (584, 6)

# %%'

df_serum_chem_ucr_value_on_mv[-4:]
    # Out[85]: 
    #     sample_ID treatment  group          time     metric    value
    # 580      ZC69       NMP      0  Explantation  CRP_serum 5.000000
    # 581      ZC69       NMP      0         POD_1  CRP_serum 7.000000
    # 582      ZC69       NMP      0         POD_2  CRP_serum 9.000000
    # 583      ZC69       NMP      0         POD_3  CRP_serum 8.000000

# %%'


test_df= df_serum_chem_6_od_or_yjt_3.copy()

test_df['treatment'] = (
                        test_df['treatment']
                        .replace({'DBD-Omnisol': 'DBD-Ecosol'})
)


test_df['treatment'].unique()
    # Out[87]: 
    # ['DBD-HTK', 'DBD-Ecosol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

test_df.shape
    # Out[88]: (576, 10)

test_df.dtypes
    # Out[92]: 
    # sample_ID           object
    # treatment         category
    # group                int64
    # time              category
    # metric            category
    # value              float64
    # baseline_value     float64
    # value_bc           float64
    # value_yjt          float64
    # value_bc_yjt       float64
    # dtype: object


# before ordering te categories.
df_serum_chem_ucr_value_on.dtypes
    # Out[93]: 
    # sample_ID      object
    # treatment    category
    # group           int64
    # time         category
    # metric         object
    # value         float64
    # dtype: object

# before ordering te categories.
df_serum_chem_ucr_value_on['metric'].unique()
    # Out[94]: 
    # array(['Urea_serum', 'Creatinin_serum', 'Total_protein_serum',
    #        'CRP_serum', 'ucr'], dtype=object)


test_df['metric'].unique()
    # Out[96]: 
    # ['Total_protein_serum', 'Urea_serum', 'Creatinin_serum', 'CRP_serum']
    # Categories (4, object): ['Urea_serum' < 'Creatinin_serum' < 'Total_protein_serum' < 'CRP_serum']


df_serum_chem_ucr_value_on['value'].isna().sum()
    # Out[104]: np.int64(9)

# %%' mixed-model test

# this is used for the mixed-model test.
    # sice the test can not be performed with NaN values present in the dataframe.

df_serum_chem_ucr_value_on_clean = (
    df_serum_chem_ucr_value_on.dropna(subset=['value'])
)


df_serum_chem_ucr_value_on_clean.to_pickle(
    r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_on_clean.pkl' 
    )

df_serum_chem_ucr_value_on_clean = pd.read_pickle(
    r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_on_clean.pkl' 
    )


# %%

# for statistical test without outliers ( sensetivity test )

df_serum_chem_ucr_value_on_clean.shape
    # Out[12]: (721, 6)

mask_outlier = (
                        ( df_serum_chem_ucr_value_on_clean['metric'] == 'ucr') & 
                        ( df_serum_chem_ucr_value_on_clean['value'] > 0.15)
)


# ro : remove outliers
df_serum_chem_ucr_value_on_clean_ro = df_serum_chem_ucr_value_on_clean[ ~mask_outlier ]

# 2 outliers removed.
df_serum_chem_ucr_value_on_clean_ro.shape
    # Out[16]: (719, 6)

# %%'

df_serum_chem_ucr_value_on_clean_ro.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_on_clean_ro.pkl' )


# %%



