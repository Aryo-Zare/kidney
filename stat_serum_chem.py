
# %%

# the non-standard '-' NAs are coerced.
# NA values removed.
# contains all metrics.
df_serum_chem_6 = pd.read_csv( r'U:\kidney\df_serum_chem_6.csv' )


# %%

df_serum_chem_4 = pd.read_csv( r'U:\kidney\df_serum_chem.csv' )

df_serum_chem_6 = df_serum_chem_5.reset_index()

df_serum_chem_6['value'] = pd.to_numeric( df_serum_chem_6['value'] , errors='coerce' )

# %%

df_urea_4.to_csv( r'U:\kidney\df_urea_4.csv' )

# the non-standard '-' NAs are coerced.
# NA values removed.
df_urea_4 = pd.read_csv( r'U:\kidney\df_urea_4.csv' )


# %%

import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
import statsmodels.api as sm


# %%

# Subset for one metric (e.g., Urea_serum)
mask_urea =  df_serum_chem_6['metric'] == 'Urea_serum'
df_urea = df_serum_chem_6[ mask_urea ]

df_urea.shape
    # Out[22]: (160, 8)

df_urea[:4]
    # Out[23]: 
    #     index  Unnamed: 0 sample_ID treatment group          time      metric  \
    # 2      11          11      ZC04   DBD-HTK     1  Explantation  Urea_serum   
    # 11     38          38      ZC04   DBD-HTK     1         POD_1  Urea_serum   
    # 20     47          47      ZC04   DBD-HTK     1         POD_2  Urea_serum   
    # 29     56          56      ZC04   DBD-HTK     1         POD_3  Urea_serum   
    
    #        value  
    # 2   2.570000  
    # 11 15.600000  
    # 20 18.730000  
    # 29 24.360000 

df_urea_2 = df_urea.reset_index()

df_urea_2.columns
    # Out[28]: 
    # Index(['level_0', 'index', 'Unnamed: 0', 'sample_ID', 'treatment', 'group',
    #        'time', 'metric', 'value'],
    #       dtype='object')

df_urea_2.iloc[:4 , :4]
    # Out[26]: 
    #    level_0  index  Unnamed: 0 sample_ID
    # 0        2     11          11      ZC04
    # 1       11     38          38      ZC04
    # 2       20     47          47      ZC04
    # 3       29     56          56      ZC04


df_urea_3 = df_urea_2.drop( columns=[ 'level_0', 'index', 'Unnamed: 0' ] )


df_urea_3.shape
    # Out[41]: (160, 6)

df_urea_3.iloc[:4]
    # Out[32]: 
    #   sample_ID treatment group          time      metric     value
    # 0      ZC04   DBD-HTK     1  Explantation  Urea_serum  2.570000
    # 1      ZC04   DBD-HTK     1         POD_1  Urea_serum 15.600000
    # 2      ZC04   DBD-HTK     1         POD_2  Urea_serum 18.730000
    # 3      ZC04   DBD-HTK     1         POD_3  Urea_serum 24.360000

df_urea_3.iloc[-4:]
    # Out[33]: 
    #     sample_ID treatment group   time      metric  value
    # 156      ZC69       NMP     0  POD_4  Urea_serum    NaN
    # 157      ZC69       NMP     0  POD_5  Urea_serum    NaN
    # 158      ZC69       NMP     0  POD_6  Urea_serum    NaN
    # 159      ZC69       NMP     0  POD_7  Urea_serum    NaN


df_urea_3.iloc[145:150]
    # Out[42]: 
    #     sample_ID treatment group   time      metric     value
    # 145      ZC68       NMP     0  POD_1  Urea_serum 10.920000
    # 146      ZC68       NMP     0  POD_2  Urea_serum  9.370000
    # 147      ZC68       NMP     0  POD_3  Urea_serum  3.140000
    # 148      ZC68       NMP     0  POD_4  Urea_serum  1.990000
    # 149      ZC68       NMP     0  POD_5  Urea_serum  3.310000

# %%

df_urea_4 = df_urea_3.dropna(subset=["value"]).reset_index(drop=True)

df_urea_4.shape
    # Out[47]: (147, 6)

# %%

# you should
    # clean index : if your dataframe is filtered, the index is cut in between & is not continuous : possibly not acceptable by statsmodels.
        # example : 1,2,4,5,6,10  :  hence the numbers have interruptions.
    # remove NAs 
        # if they are present, statsmodels automatically removes them, & bases it's indexing on this internally new created dataframe !!!!--!!!!
# otherise you'll get the following error :
    # IndexError: index 147 is out of bounds for axis 0 with size 147
        # 147 : size of the dataframe after NA removal !!

# %%

# Fit a mixed-effects model
# C(treatment) and C(time) treat these as categorical variables. 
# The interaction term allows you to see if the trend over time differs by treatment.
model_full = smf.mixedlm("value ~ C(treatment) * C(time)", 
                         data=df_urea_4,
                         groups=df_urea_4["sample_ID"])


result_full = model_full.fit()

# %%

# the reference here is DBD-ecosol : not written in the resutls. 
# 25 rows ( from 'Intercept until the end' ).

result_full.summary()

    # Out[50]: 
    # <class 'statsmodels.iolib.summary2.Summary'>
    # """
    #                        Mixed Linear Model Regression Results
    # ===================================================================================
    # Model:                      MixedLM          Dependent Variable:          value    
    # No. Observations:           147              Method:                      REML     
    # No. Groups:                 20               Scale:                       16.5990  
    # Min. group size:            1                Log-Likelihood:              -387.2576
    # Max. group size:            8                Converged:                   Yes      
    # Mean group size:            7.3                                                    
    # -----------------------------------------------------------------------------------
    #                                          Coef.  Std.Err.   z    P>|z| [0.025 0.975]
    # -----------------------------------------------------------------------------------
    # Intercept                                 2.610    2.417  1.080 0.280 -2.127  7.347
    # C(treatment)[T.DBD-HTK]                  -0.629    3.197 -0.197 0.844 -6.895  5.637
    # C(treatment)[T.NMP]                      -0.848    3.418 -0.248 0.804 -7.547  5.850
    # C(time)[T.POD_1]                          8.227    2.352  3.497 0.000  3.616 12.837
    # C(time)[T.POD_2]                          9.675    2.352  4.113 0.000  5.065 14.285
    # C(time)[T.POD_3]                         11.388    2.352  4.841 0.000  6.778 15.999
    # C(time)[T.POD_4]                          9.857    2.352  4.190 0.000  5.246 14.467
    # C(time)[T.POD_5]                          8.325    2.352  3.539 0.000  3.715 12.935
    # C(time)[T.POD_6]                          5.987    2.352  2.545 0.011  1.376 10.597
    # C(time)[T.POD_7]                          8.373    2.352  3.560 0.000  3.763 12.984
    # C(treatment)[T.DBD-HTK]:C(time)[T.POD_1]  0.791    3.184  0.248 0.804 -5.449  7.031
    # C(treatment)[T.NMP]:C(time)[T.POD_1]      0.340    3.327  0.102 0.919 -6.180  6.860
    # C(treatment)[T.DBD-HTK]:C(time)[T.POD_2] -1.649    3.184 -0.518 0.605 -7.889  4.591
    # C(treatment)[T.NMP]:C(time)[T.POD_2]     -0.078    3.327 -0.024 0.981 -6.598  6.442
    # C(treatment)[T.DBD-HTK]:C(time)[T.POD_3] -1.484    3.184 -0.466 0.641 -7.723  4.756
    # C(treatment)[T.NMP]:C(time)[T.POD_3]     -0.932    3.327 -0.280 0.779 -7.452  5.588
    # C(treatment)[T.DBD-HTK]:C(time)[T.POD_4]  0.085    3.184  0.027 0.979 -6.154  6.325
    # C(treatment)[T.NMP]:C(time)[T.POD_4]      0.059    3.426  0.017 0.986 -6.656  6.775
    # C(treatment)[T.DBD-HTK]:C(time)[T.POD_5] -0.836    3.253 -0.257 0.797 -7.211  5.540
    # C(treatment)[T.NMP]:C(time)[T.POD_5]      1.453    3.426  0.424 0.671 -5.262  8.168
    # C(treatment)[T.DBD-HTK]:C(time)[T.POD_6]  2.734    3.184  0.859 0.390 -3.506  8.974
    # C(treatment)[T.NMP]:C(time)[T.POD_6]      4.839    3.426  1.412 0.158 -1.876 11.555
    # C(treatment)[T.DBD-HTK]:C(time)[T.POD_7] -1.198    3.253 -0.368 0.713 -7.575  5.178
    # C(treatment)[T.NMP]:C(time)[T.POD_7]      0.137    3.426  0.040 0.968 -6.578  6.852
    # Group Var                                18.445    1.899                           
    # ===================================================================================
    
    # """


# %%
# %%

# the conrast between HTK & NMP is not written in the summary above.
    # it should be derived separately.

# Create a contrast vector (as a 1 x k_fe array) filled with zeros.
contrast = np.zeros((1, result_full.k_fe))


# Set the value corresponding to C(treatment)[T.DBD-HTK] to 1
# and the coefficient for C(treatment)[T.NMP] to -1.
# In our assumed ordering, these are positions 1 and 2, respectively.
contrast[0, 1] = 1
contrast[0, 2] = -1

# Now run the t-test on the contrast.
t_test_DBD_HTK_NMP = result_full.t_test(contrast)

# %%

print( t_test_DBD_HTK_NMP.summary() )

    #                              Test for Constraints                             
    # ==============================================================================
    #                  coef    std err          z      P>|z|      [0.025      0.975]
    # ------------------------------------------------------------------------------
    # c0             0.2196      3.197      0.069      0.945      -6.047       6.486
    # ==============================================================================

# %%

#  ?  :  8 * 3 = 24  "   8 time-points & 3 pairwise comparisons ( between DBD-HTK , ... ).
result_full.k_fe
    # Out[21]: 24


contrast
# Out[23]: 
    # array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
    #         0., 0., 0., 0., 0., 0., 0., 0.]])


# after editing particular values.
contrast
    # Out[27]: 
    # array([[ 0.,  1., -1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
    #          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])

# %%
# %%

# for each metric, there is one residuals data  =>  1 q-q plot.

# Extract residuals from your fitted model
resid = result_full.resid

type(resid)
    # Out[29]: pandas.core.series.Series

resid.shape
    # Out[30]: (147,)

resid[:4]
    # Out[31]: 
    # 0   -7.465841
    # 1   -3.453517
    # 2    0.667912
    # 3    4.419341
    # dtype: float64

# %%

# Produce a Q-Q plot
sm.qqplot(resid, line='45')
plt.title("Q-Q Plot of Residuals")
plt.show()

plt.savefig( r'U:\kidney\plot\serum_chem_q_q.pdf' ) 

# %%
# %%

# %%



# %%

# import os
# import numpy as np
# import pandas as pd
# import statsmodels.formula.api as smf
# import statsmodels.api as sm
# from statsmodels.stats.multitest import multipletests

# import matplotlib.pyplot as plt
# %matplotlib qt

# %%

# Define the folder for saving Q-Q plots
qq_plot_folder = r"U:\kidney\plot\q_q"
if not os.path.exists(qq_plot_folder):
    os.makedirs(qq_plot_folder)


# --- Helper Functions ---
# These functions now accept both the fitted model and its parameters list.
def get_param_index(param_name, params_list):
    """Return the index of a parameter in the model's coefficients (or None if not found)."""
    try:
        return params_list.index(param_name)
    except ValueError:
        return None

def build_contrast_vs_baseline(time_point, treatment, params_list, result):
    """
    Build a contrast vector to obtain the effect for a given treatment relative to the reference (DBD-Ecosol)
    at a specified time point.
    For the baseline time ("Explantation"), the contrast returns just the main effect.
    For other time points, the interaction effect is added.
    """
    contrast = np.zeros((1, result.k_fe))
    main_param = f"C(treatment)[T.{treatment}]"
    idx_main = get_param_index(main_param, params_list)
    if idx_main is None:
        print(f"Main parameter {main_param} not found.")
        return None
    contrast[0, idx_main] = 1
    if time_point != "Explantation":
        interaction_param = f"C(treatment)[T.{treatment}]:C(time)[T.{time_point}]"
        idx_inter = get_param_index(interaction_param, params_list)
        if idx_inter is None:
            print(f"Interaction parameter {interaction_param} not found for time {time_point}.")
            return None
        contrast[0, idx_inter] = 1
    return contrast

def build_contrast_htk_vs_nmp(time_point, params_list, result):
    """
    Build the contrast vector for the difference between DBD-HTK and NMP at a given time point.
    This contrast equals:
         (effect for DBD-HTK relative to baseline) - (effect for NMP relative to baseline).
    """
    contr_htk = build_contrast_vs_baseline(time_point, "DBD-HTK", params_list, result)
    contr_nmp = build_contrast_vs_baseline(time_point, "NMP", params_list, result)
    if (contr_htk is None) or (contr_nmp is None):
        return None
    return contr_htk - contr_nmp

# --- Main Processing for All Metrics ---
# Define the ordered time points (ensure these match the levels in your "time" variable).
time_points = ["Explantation", "POD_1", "POD_2", "POD_3", "POD_4", "POD_5", "POD_6", "POD_7"]

# This list will hold the results for every modality/metric.
results_all = []

# Loop over each unique test modality in df_serum_chem.
for met in df_serum_chem_6['metric'].unique():
    # Subset the data for the current modality.
    df_met = df_serum_chem_6[ df_serum_chem_6["metric"] == met ].copy()
    
    # (Optional) Check that there is a sufficient number of observations and subjects.
    # if df_met.shape[0] < 10 or df_met["sample_ID"].nunique() < 5:
    #     print(f"Skipping metric {met} due to insufficient data.")
    #     continue

    # Fit the mixed-effects model.
    try:
        model = smf.mixedlm("value ~ C(treatment) * C(time)", data=df_met, groups=df_met["sample_ID"])
        result_metric = model.fit(reml=True)
    except Exception as e:
        print(f"Model did not converge for metric {met}: {e}")
        continue

    # Get current metric's parameter names.
    params_list_metric = result_metric.params.index.tolist()

    # List to hold the results for this modality.
    results_metric = []

    # For each time point, compute the three pairwise comparisons.
    for tp in time_points:
        # 1. DBD-HTK vs DBD-Ecosol  
        contrast_htk = build_contrast_vs_baseline(tp, "DBD-HTK", params_list_metric, result_metric)
        if contrast_htk is not None:
            test_htk = result_metric.t_test(contrast_htk)
            results_metric.append({
                "metric": met,
                "time_point": tp,
                "comparison": "DBD-HTK vs DBD-Ecosol",
                "contrast_estimate": test_htk.effect.item(),
                "p_value": test_htk.pvalue.item()
            })
        # 2. NMP vs DBD-Ecosol  
        contrast_nmp = build_contrast_vs_baseline(tp, "NMP", params_list_metric, result_metric)
        if contrast_nmp is not None:
            test_nmp = result_metric.t_test(contrast_nmp)
            results_metric.append({
                "metric": met,
                "time_point": tp,
                "comparison": "NMP vs DBD-Ecosol",
                "contrast_estimate": test_nmp.effect.item(),
                "p_value": test_nmp.pvalue.item()
            })
        # 3. DBD-HTK vs NMP  
        contrast_htk_nmp = build_contrast_htk_vs_nmp(tp, params_list_metric, result_metric)
        if contrast_htk_nmp is not None:
            test_htk_nmp = result_metric.t_test(contrast_htk_nmp)
            results_metric.append({
                "metric": met,
                "time_point": tp,
                "comparison": "DBD-HTK vs NMP",
                "contrast_estimate": test_htk_nmp.effect.item(),
                "p_value": test_htk_nmp.pvalue.item()
            })
    
    # Convert the results for the current metric into a DataFrame.
    df_metric_results = pd.DataFrame(results_metric)
    
    if df_metric_results.shape[0] == 0:
        continue


    # --- Global Multiple-Test Correction (per modality) ---
    # Correct all comparisons for this metric at once.
    # correcting the p-values based on all 24 p-values :  8*3 = 24 values
        # 8 time points 
        # 3 p-values / time-point.
    pvals_global = df_metric_results['p_value'].values
    reject_global, pvals_corr_global, _, _ = multipletests(pvals_global, alpha=0.05, method='bonferroni')
    df_metric_results['p_value_adjusted_global'] = pvals_corr_global
    df_metric_results['reject_null_global'] = reject_global

    # --- Per-Time-Point Correction (per modality) ---
    # correcting the p-values for each time-point separately.
        # each time point has 3 p-values : these 3 would be incorporate together separately for each of th 8 corrections.
    df_metric_results['p_value_adjusted_per_tp'] = np.nan
    df_metric_results['reject_null_per_tp'] = np.nan
    for tp in df_metric_results['time_point'].unique():
        idx = df_metric_results['time_point'] == tp
        pvals_tp = df_metric_results.loc[idx, 'p_value'].values
        reject_tp, pvals_corr_tp, _, _ = multipletests(pvals_tp, alpha=0.05, method='bonferroni')
        df_metric_results.loc[idx, 'p_value_adjusted_per_tp'] = pvals_corr_tp
        df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp
    
    # Append the current modality's results to the overall list.
    results_all.append(df_metric_results)


        
    # Generate Q-Q plot for the residuals of the model for this metric
    # for each metric, there is one residuals data  =>  1 q-q plot.
    fig = sm.qqplot(result_metric.resid, line='45')
    plt.title(f"Q-Q Plot for {met}")
    # Save the plot in the designated folder
    plot_filename = os.path.join(qq_plot_folder, f"qqplot_{met}.pdf")
    plt.savefig(plot_filename)
    plt.close()  # Close the figure to free memory


# Concatenate the results from all modalities into one DataFrame.
final_results_df = pd.concat(results_all, axis=0).reset_index(drop=True)

# print("Final results for all test modalities (each modality's 24 comparisons) with both correction methods:")
# print(final_results_df)

# %%

# u:\kidney\stat_serum_chem.py:993: FutureWarning: 
    # Setting an item of incompatible dtype is deprecated and will raise an error in a future version of pandas. 
    # Value '[False False False]' has dtype incompatible with float64, please explicitly cast to a compatible dtype first.
    #   df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp

# %%

final_results_df.shape
    # Out[7]: (216, 9)

# %%

final_results_df.to_csv( r'U:\kidney\final_results_df.csv' , index=False)
final_results_df.to_excel( r'U:\kidney\final_results_df.xlsx' , index=False)

# %%
# %%

# explore
params_list_metric
    # Out[41]: 
    # ['Intercept',
    #  'C(treatment)[T.DBD-HTK]',
    #  'C(treatment)[T.NMP]',
    #  'C(time)[T.POD_1]',
    #  'C(time)[T.POD_2]',
    #  'C(time)[T.POD_3]',
    #  'C(time)[T.POD_4]',
    #  'C(time)[T.POD_5]',
    #  'C(time)[T.POD_6]',
    #  'C(time)[T.POD_7]',
    #  'C(treatment)[T.DBD-HTK]:C(time)[T.POD_1]',
    #  'C(treatment)[T.NMP]:C(time)[T.POD_1]',
    #  'C(treatment)[T.DBD-HTK]:C(time)[T.POD_2]',
    #  'C(treatment)[T.NMP]:C(time)[T.POD_2]',
    #  'C(treatment)[T.DBD-HTK]:C(time)[T.POD_3]',
    #  'C(treatment)[T.NMP]:C(time)[T.POD_3]',
    #  'C(treatment)[T.DBD-HTK]:C(time)[T.POD_4]',
    #  'C(treatment)[T.NMP]:C(time)[T.POD_4]',
    #  'C(treatment)[T.DBD-HTK]:C(time)[T.POD_5]',
    #  'C(treatment)[T.NMP]:C(time)[T.POD_5]',
    #  'C(treatment)[T.DBD-HTK]:C(time)[T.POD_6]',
    #  'C(treatment)[T.NMP]:C(time)[T.POD_6]',
    #  'C(treatment)[T.DBD-HTK]:C(time)[T.POD_7]',
    #  'C(treatment)[T.NMP]:C(time)[T.POD_7]',
    #  'Group Var']

# %%

# useless

df_serum_chem_6.info()
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 1314 entries, 0 to 1313
    # Data columns (total 7 columns):
    #  #   Column      Non-Null Count  Dtype  
    # ---  ------      --------------  -----  
    #  0   Unnamed: 0  1314 non-null   int64  
    #  1   sample_ID   1314 non-null   object 
    #  2   treatment   1314 non-null   object 
    #  3   group       1314 non-null   int64  
    #  4   time        1314 non-null   object 
    #  5   metric      1314 non-null   object 
    #  6   value       1314 non-null   float64
    # dtypes: float64(1), int64(2), object(4)
    # memory usage: 72.0+ KB

# %%

# useless

df_serum_chem_6.describe()
    # Out[11]: 
    #         Unnamed: 0        group        value
    # count  1314.000000  1314.000000  1314.000000
    # mean    656.500000     1.027397   148.518950
    # std     379.463437     0.791719   253.574677
    # min       0.000000     0.000000     0.000000
    # 25%     328.250000     0.000000     5.700000
    # 50%     656.500000     1.000000    13.770000
    # 75%     984.750000     2.000000   140.000000
    # max    1313.000000     2.000000  2031.000000

# %%

# useless

df_serum_chem_6.describe(include='all')
    # Out[13]: 
    #          Unnamed: 0 sample_ID treatment  ...          time      metric        value
    # count   1314.000000      1314      1314  ...          1314        1314  1314.000000
    # unique          NaN        20         3  ...             8           9          NaN
    # top             NaN      ZC14   DBD-HTK  ...  Explantation  Urea_serum          NaN
    # freq            NaN        72       490  ...           179         147          NaN
    # mean     656.500000       NaN       NaN  ...           NaN         NaN   148.518950
    # std      379.463437       NaN       NaN  ...           NaN         NaN   253.574677
    # min        0.000000       NaN       NaN  ...           NaN         NaN     0.000000
    # 25%      328.250000       NaN       NaN  ...           NaN         NaN     5.700000
    # 50%      656.500000       NaN       NaN  ...           NaN         NaN    13.770000
    # 75%      984.750000       NaN       NaN  ...           NaN         NaN   140.000000
    # max     1313.000000       NaN       NaN  ...           NaN         NaN  2031.000000
    
    # [11 rows x 7 columns]

# %%




# %%


