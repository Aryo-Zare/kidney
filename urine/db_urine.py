

# %%

df_urine_5 = df_urine_4.copy()

# %%

# non-standard NAN as '-' are enforced to comply with pandas NA !
df_urine_5['value'] = pd.to_numeric( df_urine_5['value'] , errors='coerce' )


# drop NA
df_urine_6 = df_urine_5.dropna().reset_index(drop=True) 

# %%

df_urine_6.shape
    # Out[63]: (2835, 6)


df_urine_6['sample_ID'].unique()
    # Out[64]: 
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

mask_Exp = df_urine_6['time'] == 'Explantation'
baseline_df = df_urine_6[ mask_Exp ][['sample_ID', 'metric', 'value']]
baseline_df.rename( columns={'value': 'baseline_value'} , inplace=True )


# Step 2: Merge the baseline values onto the original dataframe.
#         This attaches a baseline_value for each pig and metric.
# bc : baseline-corrected
df_urine_6_bc = pd.merge( df_urine_6 , baseline_df , on=['sample_ID', 'metric'], how='left')

# bc : baseline-corrected 
df_urine_6_bc['value_bc'] = df_urine_6_bc.apply(
    lambda row : row['value'] - row['baseline_value'] ,
    axis=1
)

# %%

df_urine_6_bc[:4]
    # Out[67]: 
    #   sample_ID treatment group time     metric       value  baseline_value  \
    # 0      ZC04   DBD-HTK     1   TI       Urea   97.800000      169.400000   
    # 1      ZC04   DBD-HTK     1   TI  Creatinin 6959.000000    16671.000000   
    # 2      ZC04   DBD-HTK     1   TI        Na+   36.000000       26.000000   
    # 3      ZC04   DBD-HTK     1   TI         K+   15.500000       33.100000   
    
    #       value_bc  
    # 0   -71.600000  
    # 1 -9712.000000  
    # 2    10.000000  
    # 3   -17.600000  

# %%

df_urine_6_bc['metric'].unique()
    # Out[66]: array(['Urea', 'Creatinin', 'Na+', 'K+', 'protein'], dtype=object)

# %%
# %%'  filter

# filter based on treatment, sample_ID & time.

mask = \
        ( df_urine_6_bc["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~df_urine_6_bc["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) & \
        ( df_urine_6_bc['time'].isin(['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']) )


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
df_urine_7 = df_urine_6_bc[ mask ]

# %%

df_urine_7.shape
    # Out[69]: (720, 8)

# %%
# %%'  order


# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

# Define the correct time order
# od : ordered
time_order = ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']
df_urine_7['time'] = pd.Categorical( 
                                            df_urine_7['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)

####################

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
df_urine_7['treatment'] = pd.Categorical(
                                                df_urine_7['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


####################


# take care : no typo on the 1st lineeeee.
    # once I typed 'NA+' instead of 'Na+' & the corresponding dataframe had NaN values for 'Na+' !!-!!
metric_order = [ 'Urea', 'Creatinin' , 'protein' , 'Na+', 'K+']
df_urine_7['metric'] = pd.Categorical(
                                            df_urine_7['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%

df_urine_7['metric'].unique()
    # Out[71]: 
    # ['Urea', 'Creatinin', 'Na+', 'K+', 'protein']
    # Categories (5, object): ['Urea' < 'Creatinin' < 'protein' < 'Na+' < 'K+']

df_urine_7['treatment'].unique()
    # Out[72]: 
    # ['DBD-HTK', 'DBD-Ecosol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

df_urine_7['time'].unique()
    # Out[73]: 
    # ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']

# %%

df_urine_7.to_pickle( r'U:\kidney\BG\df_urine_7.pkl' )

# %%

# plot : detect outliers.
    # both higher & lower ranges of y axis were magnified to show the corresponding outliers.

df_urine_7.shape
    # Out[96]: (720, 8)

df_urine_8 = df_urine_7.copy()

# %%

# Apply the function for each metric:
# put <> for values you want to exclude.

df_urine_8 = remove_outliers( df=df_urine_8 , metric='protein' , case=False , operator=">" , threshold=5000 )
df_urine_8 = remove_outliers( df=df_urine_8 , metric='K+' , case=False , operator=">" , threshold=200 )

# %%

df_urine_8.shape
    # Out[94]: (717, 8)

# %%

df_urine_8 = yjt( df=df_urine_8 , source_column='value' )

df_urine_8 = yjt( df=df_urine_8 , source_column='value_bc' )

# %%

df_urine_8[:4]
    # Out[98]: 
    #   sample_ID treatment group          time     metric        value  \
    # 5      ZC04   DBD-HTK     1  Explantation       Urea   169.400000   
    # 6      ZC04   DBD-HTK     1  Explantation  Creatinin 16671.000000   
    # 7      ZC04   DBD-HTK     1  Explantation        Na+    26.000000   
    # 8      ZC04   DBD-HTK     1  Explantation         K+    33.100000   
    
    #    baseline_value  value_bc  value_yjt  value_bc_yjt  
    # 5      169.400000  0.000000   2.953313      0.000000  
    # 6    16671.000000  0.000000   3.763891      0.000000  
    # 7       26.000000  0.000000   2.277912      0.000000  
    # 8       33.100000  0.000000   2.380890      0.000000  

# %%

df_urine_8.to_pickle( r'U:\kidney\BG\df_urine_8.pkl' )

df_urine_8 = pd.read_pickle( r'U:\kidney\BG\df_urine_8.pkl' )



# %%


