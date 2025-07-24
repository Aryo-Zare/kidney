

# %%

df_density_4 = pd.read_pickle( r'U:\kidney\urine\density\df_density_4.pkl' )

# %%

df_density_5 = df_density_4.copy()

# non-standard NAN as '-' are enforced to comply with pandas NA !
df_density_5['value'] = pd.to_numeric( df_density_5['value'] , errors='coerce' )

df_density_5.isna().sum()
    # Out[81]: 
    # sample_ID    176
    # treatment    176
    # group        176
    # metric         0
    # time           0
    # value        385
    # dtype: int64

# %%

# drop NA
df_density_6 = df_density_5.dropna().reset_index(drop=True) 

df_density_6.shape
    # Out[83]: (517, 6)

# %%'  baseline correction

# baseline correction by subtraction

# Step 1: Extract the baseline data (time == "Explantation")

mask_Exp = df_density_6['time'] == 'Explantation'
baseline_df = df_density_6[ mask_Exp ][['sample_ID', 'metric', 'value']]
baseline_df.rename( columns={'value': 'baseline_value'} , inplace=True )


# Step 2: Merge the baseline values onto the original dataframe.
#         This attaches a baseline_value for each pig and metric.
# bc : baseline-corrected
df_density_6_bc = pd.merge( df_density_6 , baseline_df , on=['sample_ID', 'metric'], how='left')

# bc : baseline-corrected 
df_density_6_bc['value_bc'] = df_density_6_bc.apply(
    lambda row : row['value'] - row['baseline_value'] ,
    axis=1
)

# %%

df_density_6_bc.to_pickle( r'U:\kidney\urine\density\df_density_6_bc.pkl' )


# %%


