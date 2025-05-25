
# %%

# the non-standard '-' NAs are coerced.
# NA values removed.
df_serum_chem_6 = pd.read_csv( r'U:\kidney\df_serum_chem_6.csv' )


# %%

df_serum_chem_4 = pd.read_csv( r'U:\kidney\df_serum_chem.csv' )

df_serum_chem_6 = df_serum_chem_5.reset_index()

df_serum_chem_6['value'] = pd.to_numeric( df_serum_chem_6['value'] , errors='coerce' )

# %%

df_urea_4.to_csv( r'U:\kidney\df_urea_4.csv' )

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
# %%

# Suppose you've performed three pairwise contrasts and obtained p-values:
# 1. Comparison: DBD-HTK vs DBD-Ecosol (this is usually given directly in the model summary)
# 2. Comparison: NMP vs DBD-Ecosol (also directly available)
# 3. Comparison: DBD-HTK vs NMP (from your custom contrast test)
#
# For demonstration, let's assume these p-values (example values):
pvals = np.array([0.844, 0.804, 0.945])

# Apply Bonferroni correction for 3 tests
reject, pvals_corrected, alphacSidak, alphacBonf = multipletests(pvals, alpha=0.05, method="bonferroni")

print("Raw p-values:", pvals)
    # Raw p-values: [0.844 0.804 0.945]

print("Adjusted p-values (Bonferroni):", pvals_corrected)
    # Adjusted p-values (Bonferroni): [1. 1. 1.]

print("Reject at alpha=0.05:", reject)
    # Reject at alpha=0.05: [False False False]


# %%

# Extract residuals from your fitted model
resid = result_full.resid

# Produce a Q-Q plot
sm.qqplot(resid, line='45')
plt.title("Q-Q Plot of Residuals")
plt.show()


plt.savefig( r'U:\kidney\plot\serum_chem_q_q.pdf' ) 

# %%
# %%

# import pandas as pd
# import numpy as np
# import statsmodels.formula.api as smf
# import statsmodels.api as sm
# import matplotlib.pyplot as plt
# from statsmodels.stats.multitest import multipletests

# Suppose 'df' is your DataFrame with columns: 
# 'metric' (e.g., "Urea_serum", "Creatinin_serum", etc.),
# 'value', 'treatment' (e.g., "DBD-HTK", "DBD-Ecosol", "NMP"),
# 'time', and 'sample_ID'

# List to store the pairwise comparison results.
results_list = []

# Get the list of unique metrics.
metrics = df_serum_chem_6['metric'].unique()

for met in metrics:
    # resetting index, as after slicing the original dataframe, the index will have interrupted numbers ( see above ).
    data_met = df_serum_chem_6[ df_serum_chem_6['metric'] == met ].reset_index(drop=True)
    
    # Optionally, you may also want to check that each treatment group has enough pigs
    # if data_met.shape[0] < 10 or data_met['sample_ID'].nunique() < 5:
    #     print(f"Skipping {met} due to insufficient data")
    #     continue
    
    # Fit the mixed-effects model. We assume that the baseline (reference) for treatment is DBD-Ecosol.
    try:
        model = smf.mixedlm("value ~ C(treatment) * C(time)", 
                            data=data_met, 
                            groups=data_met["sample_ID"])
        result = model.fit(reml=True)
    except Exception as e:
        print(f"Model failed for {met}: {e}")
        continue
    
    # --- Extract pairwise p-values for 'treatment' ---
    # 1. DBD-HTK vs DBD-Ecosol:
    #    Directly from the model, the coefficient for C(treatment)[T.DBD-HTK] represents this difference.
    try:
        p_val_1 = result.pvalues["C(treatment)[T.DBD-HTK]"]
    except KeyError:
        p_val_1 = np.nan

    # 2. NMP vs DBD-Ecosol:
    try:
        p_val_2 = result.pvalues["C(treatment)[T.NMP]"]
    except KeyError:
        p_val_2 = np.nan

    # 3. DBD-HTK vs NMP:
    #    We need to form the contrast: [0, 1, -1, 0,...]
    k_fe = result.k_fe  # total number of fixed effect parameters
    if k_fe < 3:
        print(f"Not enough fixed effects in model for metric {met}")
        continue
    contrast = np.zeros((1, k_fe))
    contrast[0, 1] = 1   # coefficient for DBD-HTK
    contrast[0, 2] = -1  # coefficient for NMP
    
    contrast_test = result.t_test(contrast)
    # Ensure we get a scalar p-value:
    p_val_3 = float(contrast_test.pvalue)
    
    # Gather the three original p-values in a list
    orig_pvals = np.array([p_val_1, p_val_2, p_val_3])
    comp_names = ["DBD-HTK vs DBD-Ecosol", "NMP vs DBD-Ecosol", "DBD-HTK vs NMP"]
    
    # Adjust the three p-values; here we use the Bonferroni method.
    # The adjustment is per metric; you can also pool over metrics if desired.
    reject, pvals_corrected, alphacSidak, alphacBonf = multipletests(orig_pvals, alpha=0.05, method="bonferroni")
    
    # Log the results for each pairwise comparison under this metric.
    for comp, orig_p, corr_p in zip(comp_names, orig_pvals, pvals_corrected):
        results_list.append({
            "metric": met,
            "comparison": comp,
            "p_original": orig_p,
            "p_adjusted": corr_p
        })
    
    # --- Generate and save Q-Q plot of residuals ---
    fig = sm.qqplot(result.resid, line='45')
    plt.title(f"Q-Q Plot of Residuals for {met}")
    plt.savefig( fr'U:\kidney\plot\q_q\qqplot_{met}.pdf' )
    plt.close()

# Convert the results list to a DataFrame.
result_all = pd.DataFrame(results_list)
# print("Pairwise treatment comparison p-values for each metric:")
# print(results_df)

# Optionally, save these results to a CSV file.
result_all.to_csv( r'U:\kidney\pairwise_treatment_comparisons.csv' , index=False)
result_all.to_excel( r'U:\kidney\pairwise_treatment_comparisons.xlsx' , index=False)



# %%

result_all.shape
    # Out[33]: (27, 4)


result_all[:4]

# %%

# explore
len( results_list )
    # Out[38]: 27



# %%



