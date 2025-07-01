

# %%'




# %%'

import os

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests

import matplotlib.pyplot as plt
%matplotlib qt

# %%
# %%' variables

# variables : so that you would not search inside the program to hunt for specific variables if you want to change them.

data_main = multiplex_11_stat
# df_rd_3
# df_hist_7_cat  # the nae of the 'cat' column was changed to 'time' to make it compatible with this program
                        # =>  db_histology.py
# df_rd_4
# df_ELISA_7
# df_urine_8
# df_bg_8
# df_serum_chem_6_od_or_yjt

# Set the outcome variable here:
# Choose between : "value" , "value_bc" , 'value_yjt', 'value_bc_yjt'
outcome_variable = "value_yjt"   

# %%%'

# Define the ordered time points (make sure these match the levels in your "time" column).
time_points = ["Explantation", "POD_1", "POD_2", "POD_3", "POD_4", "POD_5", "POD_6", "POD_7"]

# RD : URINE RELEASE & DENSITY
time_points = ["TI", "POD_1", "POD_2", "POD_3", "POD_4", "POD_5", "POD_6", "POD_7"]
# time_points = ["POD_1", "POD_2", "POD_3", "POD_4", "POD_5", "POD_6", "POD_7"]

# histo-pathology
time_points = ['cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5', 'cat_6']
# this program is not fully compatile with this analysis because of : 
    # if time_point != "Explantation":
        # the you should rename "Explantation" to : 'cat_1'
        # or define a new variable here !

# multiplex histology
time_points = [ 'HMGB1+_%' , 'NGAL+_%' , 'Casp3+_%' , 'Zo-1+_%' , 'Syndecan+_%' ]

# %%%'

# reference time is the first item in te ordered time category.
reference_time = 'HMGB1+_%'
# "TI"
# "Explantation"

# Define the folder for saving Q-Q plots
qq_plot_folder = r"U:\kidney\histology\multiplex\plot\q_q"
if not os.path.exists(qq_plot_folder):
    os.makedirs(qq_plot_folder)

# %%'
# %%'



'''
        Assume df_serum_chem is your original dataframe.
        Also assume that df_serum_chem['treatment'] has been recoded using pd.Categorical with
        "DBD-HTK" as the first (reference) category, e.g.:
        
        df_serum_chem['treatment'] = pd.Categorical(df_serum_chem['treatment'],
                                                     categories=["DBD-HTK", "DBD-Ecosol", "NMP"],
                                                     ordered=True)
'''


# --- Helper Functions ---
# These functions accept both the fitted model and its parameters list.

def get_param_index(param_name, params_list):
    """Return the index of a parameter in the fitted model's parameter list."""
    try:
        return params_list.index(param_name)
    except ValueError:
        return None


def build_contrast_vs_baseline(time_point, treatment, params_list, result):
    """
        Build a contrast vector for the specified treatment relative to the reference (DBD-HTK).
        
        For a given treatment (e.g. "DBD-Ecosol" or "NMP"), the contrast is constructed
        by selecting the main effect coefficient C(treatment)[T.<treatment>], plus the corresponding
        treatment-by-time interaction if time_point is not reference_time (the baseline time).
    """
    contrast = np.zeros((1, result.k_fe))
    main_param = f"C(treatment)[T.{treatment}]"
    idx_main = get_param_index(main_param, params_list)
    if idx_main is None:
        print(f"Main parameter {main_param} not found for treatment {treatment} at time {time_point}.")
        return None
    contrast[0, idx_main] = 1
    if time_point != reference_time :
        interaction_param = f"C(treatment)[T.{treatment}]:C(time)[T.{time_point}]"
        idx_inter = get_param_index(interaction_param, params_list)
        if idx_inter is None:
            print(f"Interaction parameter {interaction_param} not found for time {time_point}.")
            return None
        contrast[0, idx_inter] = 1
    return contrast


def build_contrast_Ecosol_vs_NMP(time_point, params_list, result):
    """
        Compute the contrast for DBD-Ecosol vs NMP when DBD-HTK is the reference.
        
        This is computed as:
             (DBD-Ecosol vs DBD-HTK) - (NMP vs DBD-HTK)
    """
    contrast_Ecosol = build_contrast_vs_baseline(time_point, "DBD-Ecosol", params_list, result)
    contrast_NMP = build_contrast_vs_baseline(time_point, "NMP", params_list, result)
    if contrast_Ecosol is None or contrast_NMP is None:
        return None
    return contrast_Ecosol - contrast_NMP

# --- Main Processing for All Metrics ---
results_all = []

# Loop over each unique metric in your main data.
for met in data_main['metric'].unique():
    # reset_index : otherwise the mixeld-effects-model does not function on an interrupted index following slicing.
    df_met = data_main[ data_main["metric"] == met].copy().reset_index( drop=True )
    
    # Optionally, check for a minimum number of rows or unique subjects.
    # if df_met.shape[0] < 10 or df_met["sample_ID"].nunique() < 5:
    #     print(f"Skipping metric {met} due to insufficient data.")
    #     continue

    # Fit the mixed-effects model.
    try:
        # Use the same formula; treatment is now categorical with "DBD-HTK" as reference.
        formula = f"{outcome_variable} ~ C(treatment) * C(time)"
        model = smf.mixedlm( formula , data=df_met, groups=df_met["sample_ID"] )
        result_metric = model.fit(reml=True)
    except Exception as e:
        print(f"Model did not converge for metric {met}: {e}")
        continue

    # Generate and save the Q-Q plot for model residuals.
    # for each metric, there is one residuals data  =>  1 q-q plot.
    fig = sm.qqplot(result_metric.resid, line='45')
    # Set the overall figure size to 8 x 8 inches
    fig.set_size_inches(8, 8)
    # Get the first (and typically only) axes object from the figure
    ax = fig.axes[0]
    # Set aspect ratio to 'equal' so that one unit on the x-axis
    # is equal in length to one unit on the y-axis.
    ax.set_aspect('equal', adjustable='box')
    plt.title(f"Q-Q Plot for {met}")
    plot_filename = os.path.join(qq_plot_folder, f"qqplot_{met}.pdf")
    plt.tight_layout()
    plt.savefig(plot_filename)
    plt.close()


    # Get current metric's parameter names.
    params_list_metric = result_metric.params.index.tolist()

    # List to hold the results for this modality.
    results_metric = []

    # For each time point, compute the three pairwise comparisons.
    for tp in time_points:
        # 1. DBD-Ecosol vs DBD-HTK
        contrast_Ecosol = build_contrast_vs_baseline(tp, "DBD-Ecosol", params_list_metric, result_metric)
        if contrast_Ecosol is not None:
            test_Ecosol = result_metric.t_test(contrast_Ecosol)
            results_metric.append({
                "metric": met,
                "time_point": tp,
                "comparison": "DBD-Ecosol vs DBD-HTK",
                "contrast_estimate": test_Ecosol.effect.item(),
                "p_value": test_Ecosol.pvalue.item()
            })
        # 2. NMP vs DBD-HTK
        contrast_NMP = build_contrast_vs_baseline(tp, "NMP", params_list_metric, result_metric)
        if contrast_NMP is not None:
            test_NMP = result_metric.t_test(contrast_NMP)
            results_metric.append({
                "metric": met,
                "time_point": tp,
                "comparison": "NMP vs DBD-HTK",
                "contrast_estimate": test_NMP.effect.item(),
                "p_value": test_NMP.pvalue.item()
            })
        # 3. DBD-Ecosol vs NMP
        contrast_Ecosol_vs_NMP = build_contrast_Ecosol_vs_NMP(tp, params_list_metric, result_metric)
        if contrast_Ecosol_vs_NMP is not None:
            test_Ecosol_vs_NMP = result_metric.t_test(contrast_Ecosol_vs_NMP)
            results_metric.append({
                "metric": met,
                "time_point": tp,
                "comparison": "DBD-Ecosol vs NMP",
                "contrast_estimate": test_Ecosol_vs_NMP.effect.item(),
                "p_value": test_Ecosol_vs_NMP.pvalue.item()
            })

    df_metric_results = pd.DataFrame(results_metric)
    if df_metric_results.shape[0] == 0:
        continue

    # --- Global Multiple-Test Correction (per metric) ---
    pvals_global = df_metric_results['p_value'].values
    reject_global, pvals_corr_global, _, _ = multipletests(pvals_global, alpha=0.05, method='bonferroni')
    df_metric_results['p_value_adjusted_global'] = pvals_corr_global
    df_metric_results['reject_null_global'] = reject_global

    # --- Per-Time-Point Correction (per metric) ---
    df_metric_results['p_value_adjusted_per_tp'] = np.nan
    df_metric_results['reject_null_per_tp'] = np.nan
    for t in df_metric_results['time_point'].unique():
        idx = df_metric_results['time_point'] == t
        pvals_tp = df_metric_results.loc[idx, 'p_value'].values
        reject_tp, pvals_corr_tp, _, _ = multipletests(pvals_tp, alpha=0.05, method='bonferroni')
        df_metric_results.loc[idx, 'p_value_adjusted_per_tp'] = pvals_corr_tp
        df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp

    results_all.append(df_metric_results)

# Concatenate results from all metrics.
final_results_df = pd.concat(results_all, axis=0).reset_index(drop=True)
# print("Final Results (with DBD-HTK as the reference):")
# print(final_results_df)


# %%'

# u:\kidney\stat_serum_chem.py:993: FutureWarning: 
    # Setting an item of incompatible dtype is deprecated and will raise an error in a future version of pandas. 
    # Value '[False False False]' has dtype incompatible with float64, please explicitly cast to a compatible dtype first.
    #   df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp

# %%'

final_results_df.shape
    # Out[7]: (216, 9)

# %%'

# final_results_df.to_csv( r'U:\kidney\histology\result\histology_value_yjt.csv' , index=False)
final_results_df.to_excel( r'U:\kidney\histology\multiplex\result\multiplex_value_yjt.xlsx' , index=False)

# %%'
# %%'

    #   df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp
    # u:\kidney\stat_serum_chem.py:435: FutureWarning: Setting an item of incompatible dtype is deprecated and will raise an error in a future version of pandas. Value '[False False False]' has dtype incompatible with float64, please explicitly cast to a compatible dtype first.
    #   df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp

# %%'

# capitalization error :
    # I had many of these warnings or errors : 

        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time Explantation.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time Explantation.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time POD_1.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time POD_1.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time POD_2.        

    # the reason : in the program, it was written 'DBD-ecosol', but the data had 'DBD-Ecosol'.


# %%'

'''

        bc data : LDH :
            Model did not converge for metric LDH_serum: index 137 is out of bounds for axis 0 with size 137

'''

# %%'

