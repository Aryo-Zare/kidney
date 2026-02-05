
# %%


# %%' outlier removal 

# outlier removal.
# I put no positional arguments to be able to order the parameters as wished.
# this is based on removal of outliers after visual instpection : hence, using <>.
# <> : vaules to exclude.
    # note : after <> : outliers are defined :part of the data that exist as outliers.
        # then on : return : ~ : the part not belonging to outliers are returned.

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
    
    return df.loc[~mask]  # note : ~ : the part of data ousdie the outliers are kept.

# note : you can not trun : ~mask : to : mask : ( removing ~ ) to convert the finction from 'exclusion' to 'keep' !
    # at each run, the mask selects not only, the vluae, but only indiviudal metrics !
    # hence even after filtering for 1 metric, your returned  dataframe does not have any data from other metrics !
        # => shape of your final dataframe : ( 0 , n ) !!-!!
    
# %%

# example usage
# Apply the function for each metric:

# or : outliers removed !
df_serum_chem_6_od_or = df_serum_chem_6_od.copy()


df_serum_chem_6_od_or = remove_outliers( df=df_serum_chem_6_od_or , metric="Total_protein_serum" , case=False , operator="<" , threshold=2 )
df_serum_chem_6_od_or = remove_outliers( df=df_serum_chem_6_od_or , metric="Cl_serum" , case=False , operator="<" , threshold=50 )
df_serum_chem_6_od_or = remove_outliers( df=df_serum_chem_6_od_or , metric="Na_serum" , case=False , operator="<" , threshold=75 )


# %%
# %%

from sklearn.preprocessing import PowerTransformer

# %%'

# wrong !
    # each 'metric''s transformation must be done separately.
    # => C:\code\kidney\retest.py

# # yjt : add a new column to the dataframe based on Yeo_Johnson transformation of an existing column.
# # source_column : the column to be transformed
# # new_column : the trasformations shall be writen in this new column : 
#     # give it a name.
#     # or if not : it will autmatically be named by the convention below.

# def yjt( df=None , source_column=None , new_column=None ):
#     """
#     Applies the Yeo-Johnson transformation to the given column and adds it to the dataframe.
#     If new_column is not provided, it appends '_yjt' to the original column name.
#     """
#     if new_column is None :  # if the user did not define the new column's name.
#         new_column = source_column + '_yjt'
        
#     # standardize=False : output : log‐like but not centered at zero or unit variance
#         # easier interpretation of results ?
#     pt = PowerTransformer(method='yeo-johnson', standardize=False)
#     # Transform the source_column (reshaped as a 2D array [ dataframe, in contrast to a series ][ by double brackets ] )
#     transformed = pt.fit_transform(df[[source_column]])
#     # .flatten : convert the dataframe back to a series.
#     df[new_column] = transformed.flatten() 
#     return df

# %%'

# example usage

df_serum_chem_6_od_or = yjt( df=df_serum_chem_6_od_or , source_column='value' )

df_serum_chem_6_od_or = yjt( df=df_serum_chem_6_od_or , source_column='value_bc' )


# %%'