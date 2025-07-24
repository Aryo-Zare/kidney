

# %%

# NGAL : does not contain time-points for POD_4_5_6
# Model did not converge for metric NGAL: Singular matrix

mask = df_ELISA_7['metric'] == 'NGAL'

df_NGAL = df_ELISA_7[ mask ]

df_NGAL.shape
    # Out[117]: (75, 10)

# %%

# If metric is categorical, remove unused categories:
    # otherwise, the unused categoreis ( 'KIM_1' ) is embedded inside it ( as before you ordered the categories ).
    # this unused categories will show up after groupby operation as NaN.
df_NGAL['metric'] = df_NGAL['metric'].cat.remove_unused_categories()

# %%

mask = df_ELISA_7['metric'] == 'KIM-1'

df_KIM_1 = df_ELISA_7[ mask ]

df_KIM_1.shape
    # Out[130]: (101, 10)

# %%

df_NGAL_2 = df_NGAL.copy()

df_NGAL_2.shape
    # Out[50]: (75, 10)

df_NGAL_2[:4]
    # Out[177]: 
    #    sample_ID   treatment group metric          time       value  \
    # 6       ZC05  DBD-Ecosol     2   NGAL  Explantation  116.882698   
    # 8       ZC05  DBD-Ecosol     2   NGAL         POD_1  373.998355   
    # 9       ZC05  DBD-Ecosol     2   NGAL         POD_2 1730.848011   
    # 10      ZC05  DBD-Ecosol     2   NGAL         POD_3  666.030528   
    
    #     baseline_value    value_bc  value_yjt  value_bc_yjt  
    # 6       116.882698    0.000000   3.666988      0.000000  
    # 8       116.882698  257.115657   4.291279      6.383963  
    # 9       116.882698 1613.965313   4.998392      8.903861  
    # 10      116.882698  549.147830   4.572210      7.396555  

# %%

# averaging the 'Explantation' & 'POD_1' time-points as 1 time : 'Explantation_POD_1'

# First, define the time points you want to combine
selected_times = ['Explantation', 'POD_1']

# Filter the DataFrame to only include these two time points.
df_temp = df_NGAL_2[df_NGAL_2['time'].isin(selected_times)]

df_temp.shape
    # Out[32]: (35, 10)

df_temp.reset_index( inplace=True )

df_temp.columns
    # Out[36]: 
    # Index(['index', 'sample_ID', 'treatment', 'group', 'metric', 'time', 'value',
    #        'baseline_value', 'value_bc', 'value_yjt', 'value_bc_yjt'],
    #       dtype='object')


# Now group by identifying columns.
# You can group by additional columns if needed (like 'treatment', 'group', 'metric').
df_combined = df_temp.groupby(['sample_ID', 'treatment', 'metric'] ).agg({
    'value': 'mean',            # average of the raw measurements
    'baseline_value': 'mean',   # average baseline (if identical, mean will be the same)
    'value_bc': 'mean',         # average baseline-corrected values
    'value_yjt': 'mean',        # average Yeo-Johnson transformed values
    'value_bc_yjt': 'mean'      # average Yeo-Johnson baseline-corrected values
})


# when : after groupby : as_index=False :
    # ValueError: Length of values (18) does not match length of index (108)
    

# %%

# note, the original dataframe was filtered only for NGAL.
    # however, below, there is also KIM_1 in the categories, showing up.
    # this may be due to the slicing way of creating  he dataframe.
df_combined
    # Out[40]: 
    #                                  value  baseline_value   value_bc  value_yjt  \
    # sample_ID treatment  metric                                                    
    # ZC05      DBD-HTK    KIM-1         NaN             NaN        NaN        NaN   
    #                      NGAL          NaN             NaN        NaN        NaN   
    #           DBD-Ecosol KIM-1         NaN             NaN        NaN        NaN   
    #                      NGAL   245.440526      116.882698 128.557829   3.979133   
    #           NMP        KIM-1         NaN             NaN        NaN        NaN   
    #                                ...             ...        ...        ...   
    # ZC69      DBD-HTK    NGAL          NaN             NaN        NaN        NaN   
    #           DBD-Ecosol KIM-1         NaN             NaN        NaN        NaN   
    #                      NGAL          NaN             NaN        NaN        NaN   
    #           NMP        KIM-1         NaN             NaN        NaN        NaN   
    #                      NGAL   390.814072      140.639344 250.174728   4.162902   
    
    #                              value_bc_yjt  
    # sample_ID treatment  metric                
    # ZC05      DBD-HTK    KIM-1            NaN  
    #                      NGAL             NaN  
    #           DBD-Ecosol KIM-1            NaN  
    #                      NGAL        3.191981  
    #           NMP        KIM-1            NaN  
    #                                   ...  
    # ZC69      DBD-HTK    NGAL             NaN  
    #           DBD-Ecosol KIM-1            NaN  
    #                      NGAL             NaN  
    #           NMP        KIM-1            NaN  
    #                      NGAL        3.635120  
    
    # [108 rows x 5 columns]


df_combined.iloc[ :12 , :4 ]

# Optionally, you might want to set a new label indicating that these two time points are combined:
df_combined['time'] = 'Explantation_POD_1'


# lots of NaN values :
    # many samples do not have the values for both time points ( 'Explantation', 'POD_1' )
    # in this case the mena value will be NaN.
df_combined.iloc[:,:4]
    # Out[48]: 
    #                                  value  baseline_value   value_bc  value_yjt
    # sample_ID treatment  metric                                                 
    # ZC05      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL   245.440526      116.882698 128.557829   3.979133
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC07      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL   426.130787      110.761089 315.369698   4.129312
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC08      DBD-HTK    NGAL   268.875695      145.765043 123.110652   4.053271
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC09      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL   588.873933      265.763035 323.110898   4.416887
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC10      DBD-HTK    NGAL   473.654528      187.726195 285.928334   4.282317
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC11      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL   286.077902       68.417470 217.660432   3.895402
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC14      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL   392.395156       82.051306 310.343850   4.029201
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC15      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL   644.918736      130.270293 514.648443   4.276948
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC23      DBD-HTK    NGAL   366.257551      101.515101 264.742449   4.066257
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC35      DBD-HTK    NGAL   398.603770       65.102354 333.501416   3.969359
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC37      DBD-HTK    NGAL   333.592928      108.208905 225.384023   4.055793
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC38      DBD-HTK    NGAL   454.844991      110.306964 344.538027   4.145544
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL          NaN             NaN        NaN        NaN
    # ZC61      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL   433.618735      171.406605 262.212130   4.237063
    # ZC63      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL   842.174318             NaN        NaN   4.681276
    # ZC66      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL   354.355362      163.922219 190.433143   4.166638
    # ZC67      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL   513.622927      173.049106 340.573821   4.287174
    # ZC68      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL   392.259883      136.566958 255.692925   4.157212
    # ZC69      DBD-HTK    NGAL          NaN             NaN        NaN        NaN
    #           DBD-Ecosol NGAL          NaN             NaN        NaN        NaN
    #           NMP        NGAL   390.814072      140.639344 250.174728   4.162902



df_combined_2 = df_combined.reset_index()
df_combined_2['time'] = 'E_1'


# E_1 = explantation + POD_1
df_combined_2

# %%

# %%

# since I want to concatenate it with the df_combined dataframe, & in the latter the 'group' columns is removed.
df_NGAL_2.drop( columns=['group'] , inplace=True )


# Create a copy of df_NGAL that excludes the original rows for those two time points:
df_remaining = df_NGAL_2[~df_NGAL_2['time'].isin(selected_times)].copy()

# Now, append the aggregated results from df_combined to these remaining rows.
# This concatenation will stack the dataframes vertically.
df_updated_NGAL = pd.concat([df_remaining, df_combined_2], ignore_index=True)

# Optional: If you want the resulting dataframe sorted by sample_ID, time, etc.
# df_updated = df_updated.sort_values(by=['sample_ID', 'time']).reset_index(drop=True)

df_updated_NGAL.iloc[ :4 , : ]
    # Out[60]: 
    #   sample_ID   treatment metric   time       value  baseline_value    value_bc  \
    # 0      ZC05  DBD-Ecosol   NGAL  POD_2 1730.848011      116.882698 1613.965313   
    # 1      ZC05  DBD-Ecosol   NGAL  POD_3  666.030528      116.882698  549.147830   
    # 2      ZC07  DBD-Ecosol   NGAL  POD_3  476.935628      110.761089  366.174539   
    # 3      ZC08     DBD-HTK   NGAL  POD_2  315.000000      145.765043  169.234957   
    
    #    value_yjt  value_bc_yjt  
    # 0   4.998392      8.903861  
    # 1   4.572210      7.396555  
    # 2   4.411879      6.850846  
    # 3   4.204109      5.842863  

# %%

df_updated_NGAL.to_pickle( r'U:\kidney\ELISA\df_updated_NGAL.pkl' )

# %%

times_KIM_1 = ["Explantation", "POD_1", "POD_2", "POD_3" , "POD_4" , "POD_5" , "POD_6" , "POD_7"]
times_NGAL = ["Explantation", "POD_1", "POD_2", "POD_3" , "POD_7"]

# first 2 time-points are combined.
times_updated_NGAL = ["E_1", "POD_2", "POD_3" , "POD_7"]

# %%

# for KIM-1 , its also needed to analyze it separately.
    # since the whole program may run into trouble :

# --> 208 final_results_df = pd.concat(results_all, axis=0).reset_index(drop=True)
    # ValueError: No objects to concatenate

# %%

import os

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests

import matplotlib.pyplot as plt
%matplotlib qt

# %%

# so that you would not search inside the program to hunt for specific variables if you want to change them.

data_main = df_updated_NGAL  

time_points = times_KIM_1
time_points = times_NGAL
time_points = times_updated_NGAL


# df_KIM_1
# df_NGAL

# df_urine_8
# df_bg_8
# df_serum_chem_6_od_or_yjt

# Set the outcome variable here:
# Choose between : "value" , "value_bc" , 'value_yjt', 'value_bc_yjt'
outcome_variable = "value_bc_yjt"   

# Define the folder for saving Q-Q plots
qq_plot_folder = r"U:\kidney\ELISA\plot\q_q"
if not os.path.exists(qq_plot_folder):
    os.makedirs(qq_plot_folder)

# %%

'''
        Assume df_serum_chem is your original dataframe.
        Also assume that df_serum_chem['treatment'] has been recoded using pd.Categorical with
        "DBD-HTK" as the first (reference) category, e.g.:
        
        df_serum_chem['treatment'] = pd.Categorical(df_serum_chem['treatment'],
                                                     categories=["DBD-HTK", "DBD-Ecosol", "NMP"],
                                                     ordered=True)


        note : there are 2 variables here :
            result_metric : for the main model's results.
            results_metric : to hold the reslts for individual contrasts.

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
    treatment-by-time interaction if time_point is not "Explantation" (the baseline time).
    """
    contrast = np.zeros((1, result.k_fe))
    main_param = f"C(treatment)[T.{treatment}]"
    idx_main = get_param_index(main_param, params_list)
    if idx_main is None:
        print(f"Main parameter {main_param} not found for treatment {treatment} at time {time_point}.")
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

# Define the ordered time points (make sure these match the levels in your "time" column).
time_points = time_points

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


# %%

# u:\kidney\stat_serum_chem.py:993: FutureWarning: 
    # Setting an item of incompatible dtype is deprecated and will raise an error in a future version of pandas. 
    # Value '[False False False]' has dtype incompatible with float64, please explicitly cast to a compatible dtype first.
    #   df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp

# %%

final_results_df.shape
    # Out[7]: (216, 9)

# %%

final_results_df.to_csv( r'U:\kidney\ELISA\result\KIM-1_original_yjt.csv' , index=False)
final_results_df.to_excel( r'U:\kidney\ELISA\result\KIM-1_original_yjt.xlsx' , index=False)

# %%
# %%

    #   df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp
    # u:\kidney\stat_serum_chem.py:435: FutureWarning: Setting an item of incompatible dtype is deprecated and will raise an error in a future version of pandas. Value '[False False False]' has dtype incompatible with float64, please explicitly cast to a compatible dtype first.
    #   df_metric_results.loc[idx, 'reject_null_per_tp'] = reject_tp

# %%

# capitalization error :
    # I had many of these warnings or errors : 

        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time Explantation.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time Explantation.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time POD_1.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time POD_1.
        # Main parameter C(treatment)[T.DBD-ecosol] not found for treatment DBD-ecosol at time POD_2.        

    # the reason : in the program, it was written 'DBD-ecosol', but the data had 'DBD-Ecosol'.


# %%

'''

        bc data : LDH :
            Model did not converge for metric LDH_serum: index 137 is out of bounds for axis 0 with size 137

'''

# %%

# Model did not converge for metric KIM-1: index 39 is out of bounds for axis 0 with size 39
    # ValueError: No objects to concatenate

# %%

print(result_metric.params.index.tolist())
print("Number of fixed effects:", result_metric.k_fe)


# %%


