
# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# if the file would already be open in Excel :
    # PermissionError: [Errno 13] Permission denied: 'F:\\OneDrive - Uniklinik RWTH Aachen\\kidney\\overview_2.xlsx'

# %%

# bw : body weight
bw = overview_2.loc[: , [
                            ('Sample ID:',  'Unnamed: 0_level_1'),
                            ('Treatment',  'Unnamed: 1_level_1'),
                            ('Group:',  'Unnamed: 2_level_1'),
                            ('BW in kg Ex', 'Unnamed: 19_level_1') 
                        ] 
]


bw.shape
    # Out[19]: (82, 4)

bw[:4]
    # Out[15]: 
    #           Sample ID:          Treatment             Group:         BW in kg Ex
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1 Unnamed: 19_level_1
    # 0               ZC04            DBD-HTK                  1                  39
    # 1               ZC05         DBD-Ecosol                  2           36.500000
    # 2               ZC06            DBD-HTK                  1           38.800000
    # 3               ZC07         DBD-Ecosol                  2                  36

# %%



# %%

# first level of the multi-index columns.
first_level = bw.columns.get_level_values(0)

# here, the second-level  may have mistakenly been pasted at the output.
first_level
    # Out[20]: 
    # Index(['Unnamed: 0_level_1', 'Unnamed: 1_level_1', 'Unnamed: 2_level_1',
    #        'Unnamed: 19_level_1'],
    #       dtype='object')


type( first_level )
    # Out[22]: pandas.core.indexes.base.Index

new_header= first_level.tolist()

new_header
    # Out[24]: ['Sample ID:', 'Treatment', 'Group:', 'BW in kg Ex']

# remediting the names : removing the spaces , ... .
new_header_2 = ['sample_ID', 'treatment', 'group', 'bw_ex']

# assigining the newheaders.
bw.columns = new_header_2

bw[:4]
    # Out[32]: 
    #   sample_ID   treatment group     bw_ex
    # 0      ZC04     DBD-HTK     1        39
    # 1      ZC05  DBD-Ecosol     2 36.500000
    # 2      ZC06     DBD-HTK     1 38.800000
    # 3      ZC07  DBD-Ecosol     2        36

# %%

bw['sample_ID'].unique()
    # Out[36]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC6', 'ZC13', 'ZC14', 'ZC15', 'ZC16', 'ZC17', 'ZC18', 'ZC19',
    #        'ZC20', 'ZC21', 'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27',
    #        'ZC28', 'ZC29', 'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35',
    #        'ZC36', 'ZC37', 'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43',
    #        'ZC44', 'ZC45', 'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51',
    #        'ZC52', 'ZC53', 'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59',
    #        'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67',
    #        'ZC68', 'ZC69', nan], dtype=object)


bw['treatment'].unique()
    # Out[15]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP', nan], dtype=object)

# %%


mask = \
        ( bw["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~bw["sample_ID"].isin([ "ZC06", "ZC6" , "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) )   # "ZC6"


bw_2 = bw[mask]


bw_2.shape
    # Out[51]: (19, 4)
    # Out[35]: (20, 4)


bw_2.groupby( 'treatment' ).describe()
    # Out[52]: 
    #            sample_ID                   group                    bw_ex  \
    #                count unique   top freq count unique top freq    count   
    # treatment                                                               
    # DBD-Ecosol         6      6  ZC05    1     6      1   2    6 6.000000   
    # DBD-HTK            7      7  ZC04    1     7      1   1    7 7.000000   
    # NMP                6      6  ZC61    1     6      1   0    6 6.000000   
    
                                            
    #              unique       top     freq  
    # treatment                               
    # DBD-Ecosol 5.000000 34.400000 2.000000  
    # DBD-HTK    7.000000 39.000000 1.000000  
    # NMP        6.000000 32.000000 1.000000  



# bw_2.groupby( 'treatment' ).mean()
    # TypeError: agg function failed [how->mean,dtype->object]


bw_3 = bw_2[[ 'treatment' , 'bw_ex' ]]


bw_3.groupby( 'treatment' ).mean()
    # Out[56]: 
    #                bw_ex
    # treatment           
    # DBD-Ecosol 35.983333
    # DBD-HTK    37.800000
    # NMP        36.600000


bw_3.groupby( 'treatment' ).std()
    # Out[57]: 
    #               bw_ex
    # treatment          
    # DBD-Ecosol 2.688060
    # DBD-HTK    3.356586
    # NMP        4.783304

# %%

bw_2['sample_ID'].unique()
    # Out[37]: 
    # array(['ZC04', 'ZC05', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11', 'ZC6',
    #        'ZC14', 'ZC15', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC61', 'ZC63',
    #        'ZC66', 'ZC67', 'ZC68', 'ZC69'], dtype=object)

# %%

g = sns.catplot(
                data=bw_2, 
                x='treatment', 
                y='bw_ex', 
                # hue='treatment',
                kind="strip", 
                size=9 ,
                height=7, 
                aspect=1.5 ,
)

# %%

plt.xlabel( 'treatment' , loc='right' )
plt.ylabel( 'kg' , loc='top' )

plt.title( 'body weight of pigs' )

# %%

plt.savefig( r'U:\kidney\plot\body_weight.pdf' )

# %%
# %%

mask_htk =  bw_2['treatment'] == 'DBD-HTK'

bw_htk = bw_2[ mask_htk ]

bw_htk.shape
    # Out[32]: (8, 4)

bw_htk
    # Out[33]: 
    #    sample_ID treatment group     bw_ex
    # 0       ZC04   DBD-HTK     1        39
    # 4       ZC08   DBD-HTK     1 34.400000
    # 6       ZC10   DBD-HTK     1 34.800000
    # 8        ZC6   DBD-HTK     1 38.800000
    # 19      ZC23   DBD-HTK     1 36.400000
    # 31      ZC35   DBD-HTK     1        36
    # 33      ZC37   DBD-HTK     1 43.600000
    # 34      ZC38   DBD-HTK     1 40.400000

# %%

# useless

df_serum_chem_6.info()
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 1314 entries, 0 to 1313
    # Data columns (total 7 columns):
    #  #   Column      Non-Null Count  Dtype  
    # ---  ------      --------------  -----  
    #  0   Unnamed: 0  1314 non-null   int64  
    #  1   sample_ID   1314 non-null   object 
    #  2   treatment   1314 non-null   object 
    #  3   group       1314 non-null   int64  
    #  4   time        1314 non-null   object 
    #  5   metric      1314 non-null   object 
    #  6   value       1314 non-null   float64
    # dtypes: float64(1), int64(2), object(4)
    # memory usage: 72.0+ KB

# %%

# useless

df_serum_chem_6.describe()
    # Out[11]: 
    #         Unnamed: 0        group        value
    # count  1314.000000  1314.000000  1314.000000
    # mean    656.500000     1.027397   148.518950
    # std     379.463437     0.791719   253.574677
    # min       0.000000     0.000000     0.000000
    # 25%     328.250000     0.000000     5.700000
    # 50%     656.500000     1.000000    13.770000
    # 75%     984.750000     2.000000   140.000000
    # max    1313.000000     2.000000  2031.000000

# %%

# useless

df_serum_chem_6.describe(include='all')
    # Out[13]: 
    #          Unnamed: 0 sample_ID treatment  ...          time      metric        value
    # count   1314.000000      1314      1314  ...          1314        1314  1314.000000
    # unique          NaN        20         3  ...             8           9          NaN
    # top             NaN      ZC14   DBD-HTK  ...  Explantation  Urea_serum          NaN
    # freq            NaN        72       490  ...           179         147          NaN
    # mean     656.500000       NaN       NaN  ...           NaN         NaN   148.518950
    # std      379.463437       NaN       NaN  ...           NaN         NaN   253.574677
    # min        0.000000       NaN       NaN  ...           NaN         NaN     0.000000
    # 25%      328.250000       NaN       NaN  ...           NaN         NaN     5.700000
    # 50%      656.500000       NaN       NaN  ...           NaN         NaN    13.770000
    # 75%      984.750000       NaN       NaN  ...           NaN         NaN   140.000000
    # max     1313.000000       NaN       NaN  ...           NaN         NaN  2031.000000
    
    # [11 rows x 7 columns]


# %%

mask_Creatinin_serum = df_serum_chem_6_od_or_yjt['metric'] == 'Creatinin_serum'
df_serum_chem_6_od_or_yjt_Creatinin = df_serum_chem_6_od_or_yjt[ mask_Creatinin_serum ]

# %%

df_serum_chem_6_od_or_yjt_Creatinin['value'].max()
    # Out[30]: 1163.0

df_serum_chem_6_od_or_yjt_Creatinin['value'].min()
    # Out[31]: 26.0

df_serum_chem_6_od_or_yjt_Creatinin['value_bc'].max()
    # Out[32]: 1059.0

df_serum_chem_6_od_or_yjt_Creatinin['value_bc'].min()
    # Out[33]: -53.0

df_serum_chem_6_od_or_yjt_Creatinin['value_yjt'].max()
    # Out[34]: 3.907305835474281

df_serum_chem_6_od_or_yjt_Creatinin['value_yjt'].min()
    # Out[35]: 2.456272757612795

df_serum_chem_6_od_or_yjt_Creatinin['value_bc_yjt'].max()
    # Out[36]: 683.5150509717719

df_serum_chem_6_od_or_yjt_Creatinin['value_bc_yjt'].min()
    # Out[37]: -66.56330053545943


# %%

