

# %%

df_hist_4 = pd.read_pickle( r'U:\kidney\histology\df_hist_4.pkl' )

# %%

df_hist_5 = df_hist_4.copy()

# non-standard NAN as '-' are enforced to comply with pandas NA !
df_hist_5['value'] = pd.to_numeric( df_hist_5['value'] , errors='coerce' )

df_hist_5.isna().sum()
    # Out[49]: 
    # sample_ID     96
    # treatment     96
    # group         96
    # metric         0
    # cat            0
    # value        151
    # dtype: int64

# %%

# drop NA
df_hist_6 = df_hist_5.dropna().reset_index(drop=True) 

df_hist_6.shape
    # Out[51]: (341, 6)

# %%

# baseline correction has no meaning here !

# %%'  filter

# filter based on treatment, sample_ID & time.

# 'ZC6' is ony converted to 'ZC06'.
mask = \
        ( df_hist_6["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~df_hist_6["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) 


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
df_hist_7 = df_hist_6[ mask ]

df_hist_7.shape
    # Out[53]: (107, 6)


# %%'  order

# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

# Define the correct time order
# od : ordered
cat_order = [ 'cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5', 'cat_6' ]
df_hist_7['cat'] = pd.Categorical( 
                                            df_hist_7['cat'] , 
                                            categories=cat_order , 
                                            ordered=True 
)

####################

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
df_hist_7['treatment'] = pd.Categorical(
                                                df_hist_7['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


# %%

df_hist_7['cat'].unique()
    # Out[56]: 
    # ['cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5', 'cat_6']
    # Categories (6, object): ['cat_1' < 'cat_2' < 'cat_3' < 'cat_4' < 'cat_5' < 'cat_6']


df_hist_7['treatment'].unique()
    # Out[57]: 
    # ['DBD-HTK', 'DBD-Ecosol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

# %%

# # plot : detect outliers.

# no outliers to remove : its a human defined  scoring.

# %%

df_hist_7 = yjt( df=df_hist_7 , source_column='value' )

# %%

df_hist_7.to_pickle( r'U:\kidney\histology\df_hist_7.pkl' )

# %%

df_hist_7[:4]
    # Out[88]: 
    #   sample_ID treatment group     metric    cat    value  value_yjt
    # 0      ZC04   DBD-HTK     1  histology  cat_1 2.000000   0.665919
    # 1      ZC04   DBD-HTK     1  histology  cat_2 2.000000   0.665919
    # 2      ZC04   DBD-HTK     1  histology  cat_3 2.000000   0.665919
    # 3      ZC04   DBD-HTK     1  histology  cat_4 1.000000   0.499618

# %%

# this is only to make it compatible for the statistical program.

df_hist_7_cat = df_hist_7.copy()

df_hist_7_cat.rename( columns={ "cat": "time" } , inplace=True )

df_hist_7_cat[:4]
    # Out[98]: 
    #   sample_ID treatment group     metric   time    value  value_yjt
    # 0      ZC04   DBD-HTK     1  histology  cat_1 2.000000   0.665919
    # 1      ZC04   DBD-HTK     1  histology  cat_2 2.000000   0.665919
    # 2      ZC04   DBD-HTK     1  histology  cat_3 2.000000   0.665919
    # 3      ZC04   DBD-HTK     1  histology  cat_4 1.000000   0.499618

# %%

