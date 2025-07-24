

# %%


df_NGAL.columns
    # Out[82]: 
    # Index(['sample_ID', 'treatment', 'metric', 'time', 'value',
    #        'baseline_value', 'value_bc', 'value_yjt', 'value_bc_yjt'],
    #       dtype='object')



df_NGAL['time'].unique()
    # Out[83]: 
    # ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_7']
    # Categories (8, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_4' < 'POD_5' < 'POD_6' < 'POD_7']


time_order = ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_7']
df_NGAL['time'] = pd.Categorical( 
                                            df_NGAL['time'] , 
                                            categories=time_order , 
                                            ordered=True 
)


df_NGAL['time'].unique()
    # Out[85]: 
    # ['Explantation', 'POD_1', 'POD_2', 'POD_3', 'POD_7']
    # Categories (5, object): ['Explantation' < 'POD_1' < 'POD_2' < 'POD_3' < 'POD_7']

# %%

df_NGAL.shape
    # Out[88]: (75, 10)

# %%

import pandas as pd
from scipy.stats import kruskal
from statsmodels.stats.multitest import multipletests

# %%

# Define the measurement columns you want to analyze.
measurement_cols = ['value', 'value_bc', 'value_yjt', 'value_bc_yjt']

results_list = []

# Loop through each measurement and time point.
for measure in measurement_cols:
    for t in df_NGAL['time'].cat.categories:
        df_time = df_NGAL[df_NGAL['time'] == t]
        
        group_HTK    = df_time.loc[df_time['treatment'] == 'DBD-HTK', measure]
        group_Ecosol = df_time.loc[df_time['treatment'] == 'DBD-Ecosol', measure]
        group_NMP    = df_time.loc[df_time['treatment'] == 'NMP', measure]
        
        # Check that there is data in all three groups.
        if len(group_HTK) > 0 and len(group_Ecosol) > 0 and len(group_NMP) > 0:
            # Option 1: Pre-check for identical values across all groups.
            combined = pd.concat([group_HTK, group_Ecosol, group_NMP])
            if combined.nunique() == 1:
                stat, p_val = 0.0, 1.0
            else:
                # Run the test with error handling.
                try:
                    stat, p_val = kruskal(group_HTK, group_Ecosol, group_NMP)
                
                # ValueError: All numbers are identical in kruskal
                    # this error occurs i baseline-corrected data at 'Explantation' time.
                    # because all data is 0 here ( look @ the plots ).
                    # Kruskal demands some variability in the data !
                except ValueError as e:
                    if str(e) == "All numbers are identical in kruskal":
                        stat, p_val = 0.0, 1.0
                    else:
                        raise
        else:
            stat, p_val = None, None
        
        # kruskal-wallis test yields one value for each test.
            # it's not like a post-hoc test wwith 2-by-2 comparison.
            # all 3 treatment groups are pulled together to yield a result. 
        results_list.append({
            'measurement': measure,
            'time': t,
            'kw_statistic': stat,
            'raw_p_value': p_val
        })

# Create a DataFrame from the results.
df_results = pd.DataFrame(results_list)

# Apply multiple testing correction separately per measurement.
df_results['corrected_p_value'] = None
df_results['reject_null'] = None

# the p-values are corrected for each measurement ( value , value_bc , ... ) separately.
for measurement, group in df_results.groupby('measurement'):
    mask = group['raw_p_value'].notnull()
    if mask.sum() > 0:
        pvals = group.loc[mask, 'raw_p_value']
        # Bonferroni correction applied to tests within the same measurement.
        reject, pvals_corrected, _, _ = multipletests(pvals, alpha=0.05, method='bonferroni')
        df_results.loc[group.index[mask], 'corrected_p_value'] = pvals_corrected
        df_results.loc[group.index[mask], 'reject_null'] = reject
    else:  # the following 2 lines are probably not needed, since these two columns were initally filled with 'None'.
        df_results.loc[group.index, 'corrected_p_value'] = None
        df_results.loc[group.index, 'reject_null'] = None

# %%

df_results.to_excel( r'U:\kidney\ELISA\result\NGAL_KW.xlsx' )

# %%

print(df_results)
    #      measurement          time  kw_statistic  raw_p_value corrected_p_value  \
    # 0          value  Explantation      3.613072     0.164222          0.821110   
    # 1          value         POD_1      0.327485     0.848960          1.000000   
    # 2          value         POD_2      3.553846     0.169158          0.845789   
    # 3          value         POD_3      1.718954     0.423383          1.000000   
    # 4          value         POD_7      6.593939     0.036995          0.184976   
    # 5       value_bc  Explantation      0.000000     1.000000          1.000000   
    # 6       value_bc         POD_1           NaN          NaN              None   
    # 7       value_bc         POD_2           NaN          NaN              None   
    # 8       value_bc         POD_3      1.307190     0.520173          1.000000   
    # 9       value_bc         POD_7           NaN          NaN              None   
    # 10     value_yjt  Explantation      3.613072     0.164222          0.821110   
    # 11     value_yjt         POD_1      0.327485     0.848960          1.000000   
    # 12     value_yjt         POD_2      3.553846     0.169158          0.845789   
    # 13     value_yjt         POD_3      1.718954     0.423383          1.000000   
    # 14     value_yjt         POD_7      6.593939     0.036995          0.184976   
    # 15  value_bc_yjt  Explantation      0.000000     1.000000          1.000000   
    # 16  value_bc_yjt         POD_1           NaN          NaN              None   
    # 17  value_bc_yjt         POD_2           NaN          NaN              None   
    # 18  value_bc_yjt         POD_3      1.307190     0.520173          1.000000   
    # 19  value_bc_yjt         POD_7           NaN          NaN              None   
    
    #    reject_null  
    # 0        False  
    # 1        False  
    # 2        False  
    # 3        False  
    # 4        False  
    # 5        False  
    # 6         None  
    # 7         None  
    # 8        False  
    # 9         None  
    # 10       False  
    # 11       False  
    # 12       False  
    # 13       False  
    # 14       False  
    # 15       False  
    # 16        None  
    # 17        None  
    # 18       False  
    # 19        None  

# %%

