
'''

        rd : release _ density
            combining the urine release & density datasets.
        
        continued from db_release.py & db_density.py
            kidney / urine / 
                release
                density
        note : df_releaase : under the 'time' column : initially, the item 'baseline' was converted to 'Explantation'.
        
        this is done after Mareike & Lisa defined new baseline values for both urine release & density.
      
'''

# %%

df_release_6_bc[:4]
    # Out[104]: 
    #   sample_ID treatment group   metric   time       value  baseline_value  \
    # 0      ZC04   DBD-HTK     1  release  POD_2  110.000000             NaN   
    # 1      ZC04   DBD-HTK     1  release  POD_3 1500.000000             NaN   
    # 2      ZC04   DBD-HTK     1  release  POD_4 3200.000000             NaN   
    # 3      ZC04   DBD-HTK     1  release  POD_5 1700.000000             NaN   
    
    #    value_bc  
    # 0       NaN  
    # 1       NaN  
    # 2       NaN  
    # 3       NaN  


df_density_6_bc[:4]
    # Out[105]: 
    #   sample_ID treatment group   metric   time    value  baseline_value  value_bc
    # 0      ZC04   DBD-HTK     1  density     Ti 1.017000             NaN       NaN
    # 1      ZC04   DBD-HTK     1  density     Z1 1.010000             NaN       NaN
    # 2      ZC04   DBD-HTK     1  density     Z3 1.033000             NaN       NaN
    # 3      ZC04   DBD-HTK     1  density  POD_1 1.023000             NaN       NaN

# %%


df_rd = pd.concat([ df_release_6_bc , df_density_6_bc ] , axis=0 , ignore_index=True )

df_rd.shape
    # Out[107]: (923, 8)

df_rd.columns
    # Out[108]: 
    # Index(['sample_ID', 'treatment', 'group', 'metric', 'time', 'value',
    #        'baseline_value', 'value_bc'],
    #       dtype='object')


# %%


df_rd['metric'].unique()
    # Out[109]: array(['release', 'density'], dtype=object)


df_rd[:4]
    # Out[110]: 
    #   sample_ID treatment group   metric   time       value  baseline_value  \
    # 0      ZC04   DBD-HTK     1  release  POD_2  110.000000             NaN   
    # 1      ZC04   DBD-HTK     1  release  POD_3 1500.000000             NaN   
    # 2      ZC04   DBD-HTK     1  release  POD_4 3200.000000             NaN   
    # 3      ZC04   DBD-HTK     1  release  POD_5 1700.000000             NaN   
    
    #    value_bc  
    # 0       NaN  
    # 1       NaN  
    # 2       NaN  
    # 3       NaN  

# %%

df_rd.to_pickle( r'U:\kidney\urine\rd\df_rd.pkl' )

df_rd = pd.read_pickle( r'U:\kidney\urine\rd\df_rd.pkl' )

# %%

df_rd[:4]
    # Out[12]: 
    #   sample_ID treatment group   metric   time       value  baseline_value  \
    # 0      ZC04   DBD-HTK     1  release  POD_2  110.000000             NaN   
    # 1      ZC04   DBD-HTK     1  release  POD_3 1500.000000             NaN   
    # 2      ZC04   DBD-HTK     1  release  POD_4 3200.000000             NaN   
    # 3      ZC04   DBD-HTK     1  release  POD_5 1700.000000             NaN   
    
    #    value_bc  
    # 0       NaN  
    # 1       NaN  
    # 2       NaN  
    # 3       NaN  

# %%

# 'Impl' ( belongs to urine release data ) is the same 'TI' : transponder implantation.

df_rd['time'].unique()
    # Out[13]: 
    # array(['POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_1', 'POD_7',
    #        'Impl', 'Explantation', 'Ti', 'Z1', 'Z3'], dtype=object)

# %%

  
df_rd['time'] = df_rd['time'].replace({
                                        'Impl' : 'TI' ,
                                        'Ti' : 'TI'
})

# %%

df_rd['time'].unique()
    # Out[16]: 
    # array(['POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_1', 'POD_7',
    #        'TI', 'Explantation', 'Z1', 'Z3'], dtype=object)

# %%'  filter

# filter based on treatment, sample_ID & time.

# 'ZC6' is ony converted to 'ZC06'.
mask = \
        ( df_rd["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~df_rd["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) & \
        ( df_rd['time'].isin(['TI', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']) )


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
df_rd_2 = df_rd[ mask ]

df_rd_2.shape
    # Out[18]: (283, 8)


# %%'  order

# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

# Define the correct time order
# od : ordered
time_order = ['TI', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']
df_rd_2['time'] = pd.Categorical( 
                                            df_rd_2['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)

####################

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
df_rd_2['treatment'] = pd.Categorical(
                                                df_rd_2['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


####################


# take care : no typo on the 1st lineeeee.
    # once I typed 'NA+' instead of 'Na+' & the corresponding dataframe had NaN values for 'Na+' !!-!!
metric_order = [ 'release' , 'density' ]
df_rd_2['metric'] = pd.Categorical(
                                            df_rd_2['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%

df_rd_2['metric'].unique()
    # Out[20]: 
    # ['release', 'density']
    # Categories (2, object): ['release' < 'density']

df_rd_2['time'].unique()
    # Out[21]: 
    # ['POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_1', 'POD_7', 'TI']
    # Categories (8, object): ['TI' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']

df_rd_2['treatment'].unique()
    # Out[22]: 
    # ['DBD-HTK', 'DBD-Ecosol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

# %%

df_rd_2.to_pickle( r'U:\kidney\urine\rd\new_baseline\df_rd_2.pkl' )

# %%

df_rd_2.drop( columns=['baseline_value' , 'value_bc'] , inplace=True )

df_rd_2[:4]
    # Out[29]: 
    #   sample_ID treatment group   metric   time       value
    # 0      ZC04   DBD-HTK     1  release  POD_2  110.000000
    # 1      ZC04   DBD-HTK     1  release  POD_3 1500.000000
    # 2      ZC04   DBD-HTK     1  release  POD_4 3200.000000
    # 3      ZC04   DBD-HTK     1  release  POD_5 1700.000000

# %%'  baseline correction

# baseline correction by subtraction

# Step 1: Extract the baseline data (time == "TI")

mask = df_rd_2['time'] == 'TI'
baseline_df = df_rd_2[ mask ][['sample_ID', 'metric', 'value']]
baseline_df.rename( columns={'value': 'baseline_value'} , inplace=True )


# Step 2: Merge the baseline values onto the original dataframe.
#         This attaches a baseline_value for each pig and metric.
# bc : baseline-corrected
df_rd_2_bc = pd.merge( df_rd_2 , baseline_df , on=['sample_ID', 'metric'], how='left')

# bc : baseline-corrected 
df_rd_2_bc['value_bc'] = df_rd_2_bc.apply(
    lambda row : row['value'] - row['baseline_value'] ,
    axis=1
)

# %%

# plot : detect outliers.
    # no datapoints merit designation as an outlier.
    
# %%
    
df_rd_3 = yjt( df=df_rd_2_bc , source_column='value' )

df_rd_3 = yjt( df=df_rd_2_bc , source_column='value_bc' )

# %%

df_rd_3[:4]

# %%

df_rd_3.to_pickle( r'U:\kidney\urine\rd\new_baseline\df_rd_3.pkl' )

df_rd_3 = pd.read_pickle( r'U:\kidney\urine\rd\df_rd_3.pkl' )


# %%

