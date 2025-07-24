

# %%

df_ELISA_4 = pd.read_pickle( r'U:\kidney\ELISA\df_ELISA_4.pkl' )

# %%

df_ELISA_5 = df_ELISA_4.copy()

# %%

df_ELISA_5.shape
    # Out[16]: (4100, 6)

# %%

df_ELISA_5[:4]
    # Out[12]: 
    #   sample_ID treatment group metric          time value
    # 0      ZC04   DBD-HTK     1  KIM-1  Explantation     -
    # 1      ZC04   DBD-HTK     1  KIM-1       Impl_Z3     -
    # 2      ZC04   DBD-HTK     1  KIM-1         POD_1     -
    # 3      ZC04   DBD-HTK     1  KIM-1         POD_2     -

df_ELISA_5['value'] = pd.to_numeric( df_ELISA_5['value'] , errors='coerce' )

df_ELISA_5[:4]
    # Out[14]: 
    #   sample_ID treatment group metric          time  value
    # 0      ZC04   DBD-HTK     1  KIM-1  Explantation    NaN
    # 1      ZC04   DBD-HTK     1  KIM-1       Impl_Z3    NaN
    # 2      ZC04   DBD-HTK     1  KIM-1         POD_1    NaN
    # 3      ZC04   DBD-HTK     1  KIM-1         POD_2    NaN

# %%

df_ELISA_5.isna().sum()
    # Out[15]: 
    # sample_ID     800
    # treatment     800
    # group         800
    # metric          0
    # time            0
    # value        2987
    # dtype: int64

# %%

df_ELISA_6 = df_ELISA_5.dropna().reset_index(drop=True) 

df_ELISA_6.shape
    # Out[18]: (1113, 6)

# %%

# Count the number of unique sample_IDs for each 'metric' & 'treatment'
# when something is inside parentheses, you can switch  to the next line without syntax interruption !!
sample_counts = (
                    df_ELISA_6
                    .groupby(['metric', 'treatment'])['sample_ID']
                    .nunique()
                    .reset_index(name='sample_count')
)

# %%

sample_counts
    # Out[22]: 
    #        metric    treatment  sample_count
    # 0        IL-6   DBD-Ecosol             6
    # 1        IL-6      DBD-HTK             6
    # 2        IL-6  DCD-Ecoflow             5
    # 3        IL-6   DCD-Ecosol             6
    # 4        IL-6      DCD-HTK             6
    # 5       KIM-1  DBD-Ecoflow             8
    # 6       KIM-1   DBD-Ecosol             6
    # 7       KIM-1      DBD-HTK             6
    # 8       KIM-1  DCD-Ecoflow             6
    # 9       KIM-1   DCD-Ecosol             6
    # 10      KIM-1      DCD-HTK             6
    # 11      KIM-1          NMP             9
    # 12      KIM-1          TBB             6
    # 13       NGAL  DBD-Ecoflow             6
    # 14       NGAL   DBD-Ecosol             6
    # 15       NGAL      DBD-HTK             6
    # 16       NGAL  DCD-Ecoflow             6
    # 17       NGAL   DCD-Ecosol             6
    # 18       NGAL      DCD-HTK             6
    # 19       NGAL          NMP             9
    # 20       NGAL          TBB             6
    # 21  TNF-alpha   DBD-Ecosol             6
    # 22  TNF-alpha      DBD-HTK             6
    # 23  TNF-alpha  DCD-Ecoflow             6
    # 24  TNF-alpha   DCD-Ecosol             6
    # 25  TNF-alpha      DCD-HTK             6
    # 26  TNF-alpha          TBB             6
    # 27     pi-GST  DBD-Ecoflow             6
    # 28     pi-GST   DBD-Ecosol             7
    # 29     pi-GST      DBD-HTK             7
    # 30     pi-GST  DCD-Ecoflow             7
    # 31     pi-GST   DCD-Ecosol             6
    # 32     pi-GST      DCD-HTK             6
    # 33     pi-GST          NMP             2
    # 34     pi-GST          TBB             6

# %%'  baseline correction

# baseline correction by subtraction

# Step 1: Extract the baseline data (time == "Explantation")

mask_Exp = df_ELISA_6['time'] == 'Explantation'
baseline_df = df_ELISA_6[ mask_Exp ][['sample_ID', 'metric', 'value']]
baseline_df.rename( columns={'value': 'baseline_value'} , inplace=True )


# Step 2: Merge the baseline values onto the original dataframe.
#         This attaches a baseline_value for each pig and metric.
# bc : baseline-corrected
df_ELISA_6_bc = pd.merge( df_ELISA_6 , baseline_df , on=['sample_ID', 'metric'], how='left')

# bc : baseline-corrected 
df_ELISA_6_bc['value_bc'] = df_ELISA_6_bc.apply(
    lambda row : row['value'] - row['baseline_value'] ,
    axis=1
)

# %%'  filter

# filter based on treatment, sample_ID & time.

# 'ZC6' is ony converted to 'ZC06'.
mask = \
        ( df_ELISA_6_bc["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~df_ELISA_6_bc["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) & \
        ( df_ELISA_6_bc['time'].isin(['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']) ) & \
        ( df_ELISA_6_bc["metric"].isin(["KIM-1", "NGAL"]) )


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
df_ELISA_7 = df_ELISA_6_bc[ mask ]

# %%

df_ELISA_7.shape
    # Out[25]: (176, 8)

# %%

sample_counts = (
                    df_ELISA_7
                    .groupby(['metric', 'treatment'])['sample_ID']
                    .nunique()
                    .reset_index(name='sample_count')
)

# %%

sample_counts
    # Out[104]: 
    #   metric   treatment  sample_count
    # 0  KIM-1     DBD-HTK             6
    # 1  KIM-1  DBD-Ecosol             6
    # 2  KIM-1         NMP             6
    # 3   NGAL     DBD-HTK             6
    # 4   NGAL  DBD-Ecosol             6
    # 5   NGAL         NMP             6

# %%'  order

# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

# Define the correct time order
# od : ordered
time_order = ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']
df_ELISA_7['time'] = pd.Categorical( 
                                            df_ELISA_7['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)

####################

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
df_ELISA_7['treatment'] = pd.Categorical(
                                                df_ELISA_7['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


####################


# take care : no typo on the 1st lineeeee.
    # once I typed 'NA+' instead of 'Na+' & the corresponding dataframe had NaN values for 'Na+' !!-!!
metric_order = [ "KIM-1" , "NGAL" ]
df_ELISA_7['metric'] = pd.Categorical(
                                            df_ELISA_7['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# u:\kidney\elisa\db_elisa.py:158: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead

# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df_ELISA_7['time'] = pd.Categorical(

# %%

df_ELISA_7['metric'].unique()
    # Out[27]: 
    # ['KIM-1', 'NGAL']
    # Categories (2, object): ['KIM-1' < 'NGAL']

df_ELISA_7['treatment'].unique()
    # Out[28]: 
    # ['DBD-Ecosol', 'DBD-HTK', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

df_ELISA_7['time'].unique()
    # Out[29]: 
    # ['Explantation', 'POD_1', 'POD_3', 'POD_5', 'POD_6', 'POD_7', 'POD_2', 'POD_4']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']

# %%

df_ELISA_7.to_pickle( r'U:\kidney\ELISA\df_ELISA_7.pkl' )

# %%

# plot : detect outliers.

# %%

# mistake :
    # the mask was from another dataframe !!

# df_ELISA_7.loc[ df_ELISA_5['metric'] == 'KIM-1', 'value'].min()

# I then got incompatible find-outs from the frame & the plot.

# %%

min_value = df_ELISA_7.loc[ df_ELISA_7['metric'] == 'KIM-1', 'value'].min()

min_value
    # Out[72]: 0.19024934999999982


max_value = df_ELISA_7.loc[df_ELISA_7['metric'] == 'KIM-1', 'value'].max()

max_value 
    # Out[74]: 15.966269800000001

# %%

# according to box-plots & visual inspection, no datapoints merits exclusion as an outlier.

# %%

df_ELISA_7 = yjt( df=df_ELISA_7 , source_column='value' )

df_ELISA_7 = yjt( df=df_ELISA_7 , source_column='value_bc' )

# typo : 'value-bc'
    # KeyError: "None of [Index(['value-bc'], dtype='object')] are in the [columns]"

# %%

df_ELISA_7[:4]
    # Out[112]: 
    #   sample_ID   treatment group metric          time    value  baseline_value  \
    # 0      ZC05  DBD-Ecosol     2  KIM-1  Explantation 0.270281        0.270281   
    # 1      ZC05  DBD-Ecosol     2  KIM-1         POD_1 3.003362        0.270281   
    # 2      ZC05  DBD-Ecosol     2  KIM-1         POD_3 1.807555        0.270281   
    # 3      ZC05  DBD-Ecosol     2  KIM-1         POD_5 7.986841        0.270281   
    
    #    value_bc  value_yjt  value_bc_yjt  
    # 0  0.000000   0.235962      0.000000  
    # 1  2.733082   1.281690      1.360747  
    # 2  1.537274   0.973129      0.952693  
    # 3  7.716560   1.939375      2.284462  


df_ELISA_7[-4:]
    # Out[171]: 
    #      sample_ID treatment group metric          time       value  \
    # 1107      ZC69       NMP     0   NGAL  Explantation  140.639344   
    # 1109      ZC69       NMP     0   NGAL         POD_1  640.988800   
    # 1110      ZC69       NMP     0   NGAL         POD_2 1436.644050   
    # 1111      ZC69       NMP     0   NGAL         POD_3  156.206925   
    
    #       baseline_value    value_bc  value_yjt  value_bc_yjt  
    # 1107      140.639344    0.000000   3.771685      0.000000  
    # 1109      140.639344  500.349456   4.554119      7.270239  
    # 1110      140.639344 1296.004706   4.918875      8.590477  
    # 1111      140.639344   15.567581   3.830171      3.010069  

# %%

df_ELISA_7.to_pickle( r'U:\kidney\ELISA\df_ELISA_7.pkl' )

df_ELISA_7 = pd.read_pickle( r'U:\kidney\ELISA\df_ELISA_7.pkl' )

df_ELISA_7.to_excel( r'U:\kidney\ELISA\df_ELISA_7.xlsx' )

# %%

