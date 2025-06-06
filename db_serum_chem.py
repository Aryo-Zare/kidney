
# read_csv :  index_col=0 : 
    # the csv file already has the index column. 
    # if you do not apply the parameter, whenver you read the csv file, a new ( additional ) index column will be automatically added to it.

# %%'

'''
        the non-standard '-' NAs are coerced.
        NA values removed.
        
        baseline correction : added as a new column : 'value_bc'.
            original values exist ( the 'value' column ).
            this process is independent from the follow-up processes
                this is because both in filteration & outlier removal, the whole row ( including the bc data ) will be deleted.
                
        filteration
        ordering
        
        outlier removal
            this should be done after filteration, as outliers are sometimes removed by visual inspection ( of filtered  data ! ).

'''

# %%'
# %%'

# df_serum_chem_4   =>  kidney.py

df_serum_chem_4.shape
    # Out[65]: (8118, 6)

df_serum_chem_4[:4]
    # Out[66]: 
    #   sample_ID treatment group time               metric value
    # 0      ZC04   DBD-HTK     1   TI            LDH_serum   752
    # 1      ZC04   DBD-HTK     1   TI  Total_protein_serum   5.1
    # 2      ZC04   DBD-HTK     1   TI           Urea_serum  1.89
    # 3      ZC04   DBD-HTK     1   TI      Creatinin_serum    96

# %%'

# here
    # drop_na , outlier removal , baseline correction
    # removing non-standard entries ('-')(corecion).

# %%'  numeric

# non-standard NAN as '-' are enforced to comply with pandas NA !
df_serum_chem_4['value'] = pd.to_numeric( df_serum_chem_4['value'] , errors='coerce' )


# %%'  NA

# drop NA
df_serum_chem_5 = df_serum_chem_4.dropna().reset_index(drop=True)   # subset=["value"] 
    # putting : subset=["value"] :  does not make any change to the shape of the dataframe ( below ).

df_serum_chem_5.shape
    # Out[85]: (5224, 6)

df_serum_chem_5.to_csv( r'U:\kidney\df_serum_chem_5.csv' )

# %%'

df_serum_chem_5['sample_ID'].unique()
    # Out[139]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC17', 'ZC18', 'ZC19', 'ZC20', 'ZC21',
    #        'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28', 'ZC29',
    #        'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36', 'ZC37',
    #        'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44', 'ZC45',
    #        'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC53',
    #        'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60', 'ZC61',
    #        'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68', 'ZC69'],
    #       dtype=object)

# %%'  baseline correction


# baseline correction by subtraction

# Step 1: Extract the baseline data (time == "Explantation")

mask_Exp = df_serum_chem_5['time'] == 'Explantation'
baseline_df = df_serum_chem_5[ mask_Exp ][['sample_ID', 'metric', 'value']]
baseline_df.rename( columns={'value': 'baseline_value'} , inplace=True )


# Step 2: Merge the baseline values onto the original dataframe.
#         This attaches a baseline_value for each pig and metric.
# bc : baseline-corrected
df_serum_chem_5_bc = pd.merge( df_serum_chem_5, baseline_df, on=['sample_ID', 'metric'], how='left')


# bc : baseline-corrected 
df_serum_chem_5_bc['value_bc'] = df_serum_chem_5_bc.apply(
    lambda row : row['value'] - row['baseline_value'] ,
    axis=1
)

# %%'

# explore

baseline_df.shape
    # Out[141]: (566, 3) :  with basleine as 'Explantation'
    # Out[128]: (382, 3)  :  with basleine as 'TI'

# => not every sample ( animal ) has serum chemistry data at implantation ( TI ) !!-!!
    # this is also visible in the excel file.
    # ? : calculating the baseline is not feasible by using 'TI'
baseline_df['sample_ID'].unique()
    # Out[142]: :  with basleine as 'Explantation'
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC17', 'ZC19', 'ZC20', 'ZC21', 'ZC22',
    #        'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28', 'ZC29', 'ZC30',
    #        'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36', 'ZC37', 'ZC38',
    #        'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44', 'ZC45', 'ZC46',
    #        'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC53', 'ZC54',
    #        'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60', 'ZC61', 'ZC62',
    #        'ZC63', 'ZC65', 'ZC66', 'ZC67', 'ZC68', 'ZC69'], dtype=object)


    # Out[138]: :  with basleine as 'TI'
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC14', 'ZC15', 'ZC17', 'ZC18', 'ZC19', 'ZC20', 'ZC21', 'ZC22',
    #        'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28', 'ZC29', 'ZC30',
    #        'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36', 'ZC37', 'ZC38',
    #        'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67',
    #        'ZC68', 'ZC69'], dtype=object)

df_serum_chem_5_bc.shape
    # Out[143]: (5328, 8)   :  with basleine as 'Explantation'
    # Out[127]: (5317, 8)
    # Out[88]: (5224, 8)

df_serum_chem_5_bc[:4]
    # Out[144]: :  with basleine as 'Explantation'
    #   sample_ID treatment group time               metric      value  \
    # 0      ZC04   DBD-HTK     1   TI            LDH_serum 752.000000   
    # 1      ZC04   DBD-HTK     1   TI  Total_protein_serum   5.100000   
    # 2      ZC04   DBD-HTK     1   TI           Urea_serum   1.890000   
    # 3      ZC04   DBD-HTK     1   TI      Creatinin_serum  96.000000   
    
    #    baseline_value   value_bc  
    # 0      624.000000 128.000000  
    # 1        5.200000  -0.100000  
    # 2        2.570000  -0.680000  
    # 3      115.000000 -19.000000  




    # Out[89]: :  with basleine as 'TI'
    #   sample_ID treatment group time               metric      value  \
    # 0      ZC04   DBD-HTK     1   TI            LDH_serum 752.000000   
    # 1      ZC04   DBD-HTK     1   TI  Total_protein_serum   5.100000   
    # 2      ZC04   DBD-HTK     1   TI           Urea_serum   1.890000   
    # 3      ZC04   DBD-HTK     1   TI      Creatinin_serum  96.000000   
    
    #    baseline_value  value_bc  
    # 0      752.000000  0.000000  
    # 1        5.100000  0.000000  
    # 2        1.890000  0.000000  
    # 3       96.000000  0.000000  

# %%'

df_serum_chem_5_bc['sample_ID'].unique()
    # Out[118]:  both with basleine as 'Explantation' or 'TI' 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC17', 'ZC18', 'ZC19', 'ZC20', 'ZC21',
    #        'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28', 'ZC29',
    #        'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36', 'ZC37',
    #        'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44', 'ZC45',
    #        'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC53',
    #        'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60', 'ZC61',
    #        'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68', 'ZC69'],
    #       dtype=object)

# %%'

# not needed aymore
# df_serum_chem_5_bc.rename( columns={ 'value_corrected' : 'value_bc' } , inplace=True )

# %%'

df_serum_chem_5_bc.to_csv( r'U:\kidney\df_serum_chem_5_bc.csv' )

# %%'
# %%'

# baseline correction  =>  baseline.py
# df_serum_chem_5_bc

# %%'  filter

# filter based on treatment, sample_ID & time.

# 'ZC6' is ony converted to 'ZC06'.
mask = \
        ( df_serum_chem_5_bc["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~df_serum_chem_5_bc["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) & \
        ( df_serum_chem_5_bc['time'].isin(['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']) )


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
df_serum_chem_6 = df_serum_chem_5_bc[ mask ]

# %%'

df_serum_chem_6.to_csv( r'U:\kidney\df_serum_chem_6.csv' )

# %%'

# df_serum_chem_5_bc +
        # filteration for animal, test & time.        
    # => baseline.py
df_serum_chem_6 = pd.read_csv( r'U:\kidney\df_serum_chem_6.csv' , index_col=0 )

# %%'


df_serum_chem_6.shape
    # Out[121]: (1305, 8)
    # Out[57]: (1314, 8)  :  'ZC6' is present here !

# %%'  order


# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

# Define the correct time order
# od : ordered
time_order = ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7']
df_serum_chem_6['time'] = pd.Categorical( 
                                            df_serum_chem_6['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)

####################

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
df_serum_chem_6['treatment'] = pd.Categorical(
                                                df_serum_chem_6['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


####################

metric_order = [
                'Urea_serum', 'Creatinin_serum', 'Uric_acid_serum', 
                'LDH_serum', 'Total_protein_serum', 'CRP_serum', 
                'Na_serum', 'Ka_serum', 'Cl_serum'
]
df_serum_chem_6['metric'] = pd.Categorical(
                                            df_serum_chem_6['metric'],
                                            categories=metric_order,
                                            ordered=True
)

# %%'

# od = ordered
df_serum_chem_6_od = df_serum_chem_6.copy()

df_serum_chem_6_od.to_pickle( r'U:\kidney\df_serum_chem_6_od.pkl' )


df_serum_chem_6_od = pd.read_pickle( r'U:\kidney\df_serum_chem_6_od.pkl' )


# %%'

# metadaa regarding the categorical order is not saved in a csv file !!

# df_serum_chem_6.to_csv( r'U:\kidney\df_serum_chem_7.csv'  )

# df_serum_chem_7 = pd.read_csv( r'U:\kidney\df_serum_chem_7.csv' , index_col=0 )

# df_serum_chem_7['treatment'].unique()

# df_serum_chem_7['metric'].unique()


# %%'

# u:\kidney\filter.py:233: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead

# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df_serum_chem_6['time'] = pd.Categorical(

# %%' outlier removal 

# outlier removal.
# I put no positional arguments to be able to order the parameters as wished.
# this is based on removal of outliers after visual instpection : hence, using <>.

def remove_outliers(
                    df=None , 
                    metric=None , 
                    case=False ,  # case-sensetivity for the metric name.
                    operator="<", 
                    threshold=None
):
    
    """
    Remove rows for which df['metric'] contains metric_keyword and the value is below (or above) a threshold.
    operator: '<' removes if value < threshold, while '>' would remove if value > threshold.
    """
    # optional : 
    # Check that required parameters were provided
    # this is because there are no positiona ( required ) argumnents in the 1st line of function definition.
    # if df is None or metric_keyword is None or threshold is None:
    #     raise ValueError("df, metric_keyword, and threshold must be provided")

    if operator == "<":
        mask = (df['metric'].str.contains(metric, case=case)) & (df['value'] < threshold)
    elif operator == ">":
        mask = (df['metric'].str.contains(metric, case=case)) & (df['value'] > threshold)
    else:
        raise ValueError("Unsupported operator. Use '<' or '>'")
    
    return df.loc[~mask]

# %%'

# Apply the function for each metric:

# or : outliers removed !
df_serum_chem_6_od_or = df_serum_chem_6_od.copy()


df_serum_chem_6_od_or = remove_outliers( df=df_serum_chem_6_od_or , metric="Total_protein_serum" , case=False , operator="<" , threshold=2 )
df_serum_chem_6_od_or = remove_outliers( df=df_serum_chem_6_od_or , metric="Cl_serum" , case=False , operator="<" , threshold=50 )
df_serum_chem_6_od_or = remove_outliers( df=df_serum_chem_6_od_or , metric="Na_serum" , case=False , operator="<" , threshold=75 )

# %%'

df_serum_chem_6_od_or.shape
    # Out[187]: (1298, 8)
    # Out[63]: (1307, 8)

# df_serum_chem_6_or.to_csv( r'U:\kidney\df_serum_chem_6_or.csv' )

# # after removal of outliers.
# df_serum_chem_6_or = pd.read_csv( r'U:\kidney\df_serum_chem_6_or.csv' , index_col=0 )

# %%'

df_serum_chem_6_od_or.to_pickle( r'U:\kidney\df_serum_chem_6_od_or.pkl' )

df_serum_chem_6_od_or = pd.read_pickle( r'U:\kidney\df_serum_chem_6_od_or.pkl' )

# %%'

# checking if pickle conserves the categorical order !!

df_serum_chem_6_od_or['treatment'].unique()
    # Out[27]: 
    # ['DBD-HTK', 'DBD-Ecosol', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

# %%'
# %%'

# checking for negative or 0 values before log-transformation.

df_serum_chem_6_od_or['value'].min()
    # Out[12]: 0.0

df_serum_chem_6_od_or.sort_values(by=['value'])[[ 'metric' , 'treatment' , 'time' , 'value']][:4]
    # Out[17]: 
    #           metric   treatment          time    value
    # 4683   CRP_serum         NMP  Explantation 0.000000
    # 718   Urea_serum  DBD-Ecosol  Explantation 0.820000
    # 5187  Urea_serum         NMP  Explantation 0.980000
    # 795    CRP_serum  DBD-Ecosol         POD_6 1.000000


# %%'

from sklearn.preprocessing import PowerTransformer

# %%'

# yjt : add a new column to the dataframe based on Yeo_Johnson transformation of an existing column.
# source_column : the column to be transformed
# new_column : the trasformations shall be writen in this new column : 
    # ]give it a name.
    # or if not : it will autmatically be named by the convention below.

def yjt( df=None , source_column=None , new_column=None ):
    """
    Applies the Yeo-Johnson transformation to the given column and adds it to the dataframe.
    If new_column is not provided, it appends '_yjt' to the original column name.
    """
    if new_column is None :  # if the user did not define the new column's name.
        new_column = source_column + '_yjt'
        
    # standardize=False : output : log‐like but not centered at zero or unit variance
        # easier interpretation of results ?
    pt = PowerTransformer(method='yeo-johnson', standardize=False)
    # Transform the source_column (reshaped as a 2D array [ dataframe, in contrast to a series ][ by double brackets ] )
    transformed = pt.fit_transform(df[[source_column]])
    # .flatten : convert the dataframe back to a series.
    df[new_column] = transformed.flatten() 
    return df

# %%'

# Example usage:
df_serum_chem_6_od_or = yjt( df=df_serum_chem_6_od_or , source_column='value' )

df_serum_chem_6_od_or = yjt( df=df_serum_chem_6_od_or , source_column='value_bc' )

# %%'

df_serum_chem_6_od_or[:4]
    # Out[15]: 
    #    sample_ID treatment  group          time               metric      value  \
    # 9       ZC04   DBD-HTK      1  Explantation            LDH_serum 624.000000   
    # 10      ZC04   DBD-HTK      1  Explantation  Total_protein_serum   5.200000   
    # 11      ZC04   DBD-HTK      1  Explantation           Urea_serum   2.570000   
    # 12      ZC04   DBD-HTK      1  Explantation      Creatinin_serum 115.000000   
    
    #     baseline_value  value_bc  value_yjt  value_bc_yjt  
    # 9       624.000000  0.000000   3.732470      0.000000  
    # 10        5.200000  0.000000   1.544398      0.000000  
    # 11        2.570000  0.000000   1.131715      0.000000  
    # 12      115.000000  0.000000   3.142166      0.000000  


# %%'

df_serum_chem_6_od_or.to_pickle( r'U:\kidney\df_serum_chem_6_od_or_yjt.pkl' )

df_serum_chem_6_od_or_yjt = df_serum_chem_6_od_or.copy()


# %%


