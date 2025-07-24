

# %%

df_release_5 = pd.to_pickle( r'U:\kidney\urine\density\df_release_5.pkl' )

# %%

df_release_6 = df_release_5.copy()

# non-standard NAN as '-' are enforced to comply with pandas NA !
df_release_6['value'] = pd.to_numeric( df_release_6['value'] , errors='coerce' )

df_release_6.isna().sum()
    # Out[85]: 
    # sample_ID    144
    # treatment    144
    # group        144
    # metric         0
    # time           0
    # value        332
    # dtype: int64

# %%

# drop NA
df_release_6 = df_release_6.dropna().reset_index(drop=True) 

# %%

# As the intention is to merge this dataset with that of urine density, for more compatibility, the terminology is coordinated ;
df_release_6['time'] = df_release_6['time'].replace( { 'baseline' : 'Explantation' } )


# %%'  baseline correction

# baseline correction by subtraction

# Step 1: Extract the baseline data (time == "Explantation")

mask_Exp = df_release_6['time'] == 'Explantation'
baseline_df = df_release_6[ mask_Exp ][['sample_ID', 'metric', 'value']]
baseline_df.rename( columns={'value': 'baseline_value'} , inplace=True )


# Step 2: Merge the baseline values onto the original dataframe.
#         This attaches a baseline_value for each pig and metric.
# bc : baseline-corrected
df_release_6_bc = pd.merge( df_release_6 , baseline_df , on=['sample_ID', 'metric'], how='left')

# bc : baseline-corrected 
df_release_6_bc['value_bc'] = df_release_6_bc.apply(
    lambda row : row['value'] - row['baseline_value'] ,
    axis=1
)

# %%

# I had forgotten to do this before !

df_release_6_bc['time'] = df_release_6_bc['time'].replace( to_replace=r'^(POD)(\d+)$', value=r'\1_\2', regex=True )

df_release_6_bc['time'].unique()
    # Out[102]: 
    # array(['POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_1', 'POD_7',
    #        'Impl', 'Explantation'], dtype=object)

# %%


# %%

df_release_6_bc.to_pickle( r'U:\kidney\urine\density\df_release_6_bc.pkl' )


# %%

