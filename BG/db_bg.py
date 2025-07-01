

# the saving format should be changed to pickle.

# %%

# this was prepared in extract_BG.py
df_bg_4 = pd.read_csv( r'U:\kidney\BG\df_bg_4.csv' , index_col=0 )

# %%

df_bg_5 = df_bg_4.copy()

# non-standard NAN as '-' are enforced to comply with pandas NA !
df_bg_5['value'] = pd.to_numeric( df_bg_5['value'] , errors='coerce' )

df_bg_5.isna().sum()
    # Out[63]: 
    # sample_ID    1344
    # treatment    1344
    # group        1344
    # time            0
    # metric          0
    # value        2504
    # dtype: int64

# %%

# explore
# the NaN under 'sample_ID' is because of initially importing blank rows from excel.

# Filter rows where 'sample_ID' is NA
na_sample_id_rows = df_bg_5.loc[ df_bg_5['sample_ID'].isna() ]


na_sample_id_rows[:4]
    # Out[67]: 
    #      sample_ID treatment group time metric  value
    # 5544       NaN       NaN   NaN   TI     pH    NaN
    # 5545       NaN       NaN   NaN   TI   pCO2    NaN
    # 5546       NaN       NaN   NaN   TI    pO2    NaN
    # 5547       NaN       NaN   NaN   TI     K+    NaN

na_sample_id_rows.shape
    # Out[69]: (1344, 6)

na_sample_id_rows['time'].unique()
    # Out[68]: 
    # array(['TI', 'Ex', 'Imp Z1', 'Imp Z2', 'Imp Z3', 'POD_1', 'POD_2',
    #        'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7'], dtype=object)


# %%

# drop NA
df_bg_6 = df_bg_5.dropna().reset_index(drop=True) 

# inplace=True  : can not be chained with another operation !
    # df_bg_5.dropna( inplace=True ).reset_index(drop=True) 
        # ---------------------------------------------------------------------------
        # AttributeError                            Traceback (most recent call last)
        # Cell In[92], line 1
        # ----> 1 df_bg_5.dropna( inplace=True ).reset_index(drop=True)
        
        # AttributeError: 'NoneType' object has no attribute 'reset_index'

df_bg_6.shape
    # Out[62]: (4384, 6)


# 4384 : the size of the datafrme after dropping NAs.
# 2504 : the number of NAs in 'value'.
# hence, the number ; 1344 : depicting the number of NA values in sample_ID, should be a subset of 'value'.
    # : all roows with NA in 'sample_ID' also have NA in 'value'
    # 1344  <-  2504
4384 + 2504
    # Out[64]: 6888


df_bg_6.to_csv( r'U:\kidney\BG\df_bg_6.csv' )

# %%

df_bg_6['sample_ID'].unique()
    # Out[96]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC17', 'ZC18', 'ZC19', 'ZC20', 'ZC21',
    #        'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28', 'ZC29',
    #        'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36', 'ZC37',
    #        'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44', 'ZC45',
    #        'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC53',
    #        'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60', 'ZC61',
    #        'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68', 'ZC69'],
    #       dtype=object)

# %%
# %%'  baseline correction

# baseline correction by subtraction

# Step 1: Extract the baseline data (time == "Explantation")

mask_Exp = df_bg_6['time'] == 'Explantation'
baseline_df = df_bg_6[ mask_Exp ][['sample_ID', 'metric', 'value']]
baseline_df.rename( columns={'value': 'baseline_value'} , inplace=True )


# Step 2: Merge the baseline values onto the original dataframe.
#         This attaches a baseline_value for each pig and metric.
# bc : baseline-corrected
df_bg_6_bc = pd.merge( df_bg_6 , baseline_df , on=['sample_ID', 'metric'], how='left')

# bc : baseline-corrected 
df_bg_6_bc['value_bc'] = df_bg_6_bc.apply(
    lambda row : row['value'] - row['baseline_value'] ,
    axis=1
)

# %%

df_bg_6_bc['metric'].unique()
    # Out[139]: array(['pH', 'pCO2', 'pO2', 'K+', 'Na+', 'Ca2+', 'Cl-'], dtype=object)

# %%'  filter

# filter based on treatment, sample_ID & time.

# 'ZC6' is ony converted to 'ZC06'.
mask = \
        ( df_bg_6_bc["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~df_bg_6_bc["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) & \
        ( df_bg_6_bc['time'].isin(['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']) )


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
df_bg_7 = df_bg_6_bc[ mask ]

# %%

df_bg_7.shape
    # Out[99]: (977, 8)

# %%'  order

# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

# Define the correct time order
# od : ordered
time_order = ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']
df_bg_7['time'] = pd.Categorical( 
                                            df_bg_7['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)

####################

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
df_bg_7['treatment'] = pd.Categorical(
                                                df_bg_7['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


####################


# take care : no typo on the 1st lineeeee.
    # once I typed 'NA+' instead of 'Na+' & the corresponding dataframe had NaN values for 'Na+' !!-!!
metric_order = [ 'pH' , 'pCO2' , 'pO2' , 'Na+' , 'K+' , 'Ca2+' , 'Cl-' ]
df_bg_7['metric'] = pd.Categorical(
                                            df_bg_7['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%

df_bg_7['metric'].unique()
    # Out[143]: 
    # ['pH', 'pCO2', 'pO2', 'K+', 'Na+', 'Ca2+', 'Cl-']
    # Categories (7, object): ['pH' < 'pCO2' < 'pO2' < 'Na+' < 'K+' < 'Ca2+' < 'Cl-']

df_bg_7['treatment'].unique()
    # Out[113]: 
    # ['DBD-HTK', 'DBD-Ecosol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

df_bg_7['time'].unique()
    # Out[114]: 
    # ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']

# %%

df_bg_7.to_pickle( r'U:\kidney\BG\df_bg_7.pkl' )

df_bg_7 = pd.read_pickle( r'U:\kidney\BG\df_bg_7.pkl' )

# %%

# plot : detect outliers.

# %%'

# create a copy to keep the dataframe with outliers intact.
df_bg_8 = df_bg_7.copy()

# %%

# Apply the function for each metric:
# put <> for values you want to exclude.

# df_bg_8 = remove_outliers( df=df_bg_8 , metric='pH' , case=False , operator="<" , threshold=7.5 )
# df_bg_8 = remove_outliers( df=df_bg_8 , metric='pH' , case=False , operator=">" , threshold=7.3 )

df_bg_8 = remove_outliers( df=df_bg_8 , metric='pCO2' , case=False , operator=">" , threshold=60 )
df_bg_8 = remove_outliers( df=df_bg_8 , metric='pCO2' , case=False , operator="<" , threshold=36.4 )

df_bg_8 = remove_outliers( df=df_bg_8 , metric='pO2' , case=False , operator=">" , threshold=100 )
df_bg_8 = remove_outliers( df=df_bg_8 , metric='Na+' , case=False , operator="<" , threshold=100 )
df_bg_8 = remove_outliers( df=df_bg_8 , metric='K+' , case=False , operator=">" , threshold=5.91 )

df_bg_8 = remove_outliers( df=df_bg_8 , metric='Ca2+' , case=False , operator=">" , threshold=1.44 )
df_bg_8 = remove_outliers( df=df_bg_8 , metric='Ca2+' , case=False , operator="<" , threshold=1.03 )

df_bg_8 = remove_outliers( df=df_bg_8 , metric='Cl-' , case=False , operator="<" , threshold=50 )

# %%

df_bg_8.shape
    # Out[61]: (958, 8)

# %%

df_bg_8 = yjt( df=df_bg_8 , source_column='value' )

df_bg_8 = yjt( df=df_bg_8 , source_column='value_bc' )


# %%

df_bg_8.to_pickle( r'U:\kidney\BG\df_bg_8.pkl' )

df_bg_8 = pd.read_pickle( r'U:\kidney\BG\df_bg_8.pkl' )


# %%

