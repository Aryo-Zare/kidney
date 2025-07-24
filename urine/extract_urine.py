

# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# %%

# column ranges of the data.
# preparation for later slicing.

begin = column_index_from_string("HY") - 1
end = column_index_from_string("KF")

# %%

cols_to_keep = np.r_[ 0:3 , begin:end ] 

# bg : blood gass
df_urine = overview_2.iloc[ : , cols_to_keep ]

# %%

df_urine.shape
    # Out[98]: (82, 63)

df_urine.iloc[:4,:4]
    # Out[99]: 
    #           Sample ID:          Treatment             Group:  \
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1   
    # 0               ZC04            DBD-HTK                  1   
    # 1               ZC05         DBD-Ecosol                  2   
    # 2               ZC06            DBD-HTK                  1   
    # 3               ZC07         DBD-Ecosol                  2   
    
    #   Enzyme Baseline (Urin)  
    #            Urea [mmol/L]  
    # 0                      -  
    # 1                      -  
    # 2                      -  
    # 3                      -  

df_urine.iloc[:4,-4:]
    # Out[100]: 
    #   Enzyme POD7 (Urin)                                                         
    #   Creatinin [µmol/L] Sodium [mmol/L] Potassium [mmol/L] Urine protein [mg/dL]
    # 0                  -               -                  -                     -
    # 1               5961              11          23.900000                    80
    # 2                  -               -                  -                     -
    # 3              10783               6          32.600000                    50

# blank cells at the end of the sheet are imported to the excel file !
df_urine.iloc[-4:,:4]
    # Out[101]: 
    #            Sample ID:          Treatment             Group:  \
    #    Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1   
    # 78                NaN                NaN                NaN   
    # 79                NaN                NaN                NaN   
    # 80                NaN                NaN                NaN   
    # 81                NaN                NaN                NaN   
    
    #    Enzyme Baseline (Urin)  
    #             Urea [mmol/L]  
    # 78                    NaN  
    # 79                    NaN  
    # 80                    NaN  
    # 81                    NaN  

# %%

df_urine.iloc[:,0].unique()
    # Out[102]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC16', 'ZC17', 'ZC18', 'ZC19', 'ZC20',
    #        'ZC21', 'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28',
    #        'ZC29', 'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36',
    #        'ZC37', 'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44',
    #        'ZC45', 'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52',
    #        'ZC53', 'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60',
    #        'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68',
    #        'ZC69', nan], dtype=object)

# %%

# hierarchical columns that should be turned into a frozen index !

df_urine.iloc[: , :3].columns
    # Out[103]: 
    # MultiIndex([('Sample ID:', 'Unnamed: 0_level_1'),
    #             ( 'Treatment', 'Unnamed: 1_level_1'),
    #             (    'Group:', 'Unnamed: 2_level_1')],
    #            )

df_urine_2 = df_urine.set_index( [('Sample ID:', 'Unnamed: 0_level_1'),
                                ( 'Treatment', 'Unnamed: 1_level_1'),
                                (    'Group:', 'Unnamed: 2_level_1')] )

# %%

df_urine_2.iloc[:4 , :2]
    # Out[105]: 
    #                                                                                               Enzyme Baseline (Urin)  \
    #                                                                                                        Urea [mmol/L]   
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)                          
    # ZC04                             DBD-HTK                         1                                                 -   
    # ZC05                             DBD-Ecosol                      2                                                 -   
    # ZC06                             DBD-HTK                         1                                                 -   
    # ZC07                             DBD-Ecosol                      2                                                 -   
    
                                                                                                                      
    #                                                                                               Creatinin [µmol/L]  
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)                     
    # ZC04                             DBD-HTK                         1                                             -  
    # ZC05                             DBD-Ecosol                      2                                             -  
    # ZC06                             DBD-HTK                         1                                             -  
    # ZC07                             DBD-Ecosol                      2                                             -  

# %%

# --- Renaming the index levels ---
new_index_names = ['sample_ID', 'treatment', 'group']

df_urine_2.index.set_names( new_index_names, inplace=True ) # Use inplace=True to modify directly

# %%

df_urine_2.iloc[ :4 , :4 ]
    # Out[107]: 
    #                            Enzyme Baseline (Urin)                     \
    #                                     Urea [mmol/L] Creatinin [µmol/L]   
    # sample_ID treatment  group                                             
    # ZC04      DBD-HTK    1                          -                  -   
    # ZC05      DBD-Ecosol 2                          -                  -   
    # ZC06      DBD-HTK    1                          -                  -   
    # ZC07      DBD-Ecosol 2                          -                  -   
    
                                                                   
    #                            Sodium [mmol/L] Potassium [mmol/L]  
    # sample_ID treatment  group                                     
    # ZC04      DBD-HTK    1                   -                  -  
    # ZC05      DBD-Ecosol 2                   -                  -  
    # ZC06      DBD-HTK    1                   -                  -  
    # ZC07      DBD-Ecosol 2                   -                  -  

# %%

# explore : 
    # hirarchical index structure
    

df_urine_2.columns
    # Out[108]: 
    # MultiIndex([('Enzyme Baseline (Urin)',         'Urea [mmol/L]'),
    #             ('Enzyme Baseline (Urin)',    'Creatinin [µmol/L]'),
    #             ('Enzyme Baseline (Urin)',       'Sodium [mmol/L]'),
    #             ('Enzyme Baseline (Urin)',    'Potassium [mmol/L]'),
    #             ('Enzyme Baseline (Urin)', 'Urine protein [mg/dL]'),
    #             (      'Enzyme TI (Urin)',         'Urea [mmol/L]'),
    #             (      'Enzyme TI (Urin)',    'Creatinin [µmol/L]'),
    #             (      'Enzyme TI (Urin)',       'Sodium [mmol/L]'),
    #             (      'Enzyme TI (Urin)',    'Potassium [mmol/L]'),
    #             (      'Enzyme TI (Urin)', 'Urine protein [mg/dL]'),
    #             ...

# tuple operation
for i,j in df_urine_2.columns :
    print( f' {i} & {j}' )
     # Enzyme Baseline (Urin) & Urea [mmol/L]
     # Enzyme Baseline (Urin) & Creatinin [µmol/L]
     # Enzyme Baseline (Urin) & Sodium [mmol/L]
     # Enzyme Baseline (Urin) & Potassium [mmol/L]
     # Enzyme Baseline (Urin) & Urine protein [mg/dL]
     # Enzyme TI (Urin) & Urea [mmol/L]
     # Enzyme TI (Urin) & Creatinin [µmol/L]
     # Enzyme TI (Urin) & Sodium [mmol/L]
     # Enzyme TI (Urin) & Potassium [mmol/L]
     # Enzyme TI (Urin) & Urine protein [mg/dL]

# %%

# don't save in .csv format : it will not save the multi-index columns.

df_urine_2.to_pickle( r'U:\kidney\urine\df_urine_2.pkl' )

test = pd.read_pickle( r'U:\kidney\urine\df_urine_2.pkl' )

# %%


# rename the columns

# import re         # regular expression


# Functions to clean the levels
def clean_top_label(top_label):
    # Remove "Enzyme " prefix and " (Urin)" suffix
    prefix = "Enzyme "
    suffix = " (Urin)"
    if top_label.startswith(prefix) and top_label.endswith(suffix):
        return top_label[len(prefix):-len(suffix)]
    else:
        return top_label

def clean_bottom_label(bottom_label):
    # Remove the units inside square brackets. This replaces " [anything]" with an empty string.
    cleaned = re.sub( r" \[.*\]" , "" , bottom_label )
    # Special renaming for "Urine protein"
    if cleaned.strip().lower() == "urine protein":
        return "protein"
    return cleaned.strip()

# %%

# explore
# r" \[.*\]" : note : after ']' there should be no space ( I made it once by mistake ).
    # the pattern searches for an exact match, hence adding a space will return the original string, unformatted !!
# re.sub( r" \[.*\]", "" , 'Urea [mmol/L]' )
    # Out[15]: 'Urea'

# %%


# Reassign the MultiIndex columns using the cleaning functions for each level
df_urine_2.columns = pd.MultiIndex.from_tuples([
    (clean_top_label(col[0]), clean_bottom_label(col[1])) 
    for col in df_urine_2.columns
])

# %%

df_urine_2.columns
    # Out[37]: 
    # MultiIndex([('Baseline',      'Urea'),
    #             ('Baseline', 'Creatinin'),
    #             ('Baseline',    'Sodium'),
    #             ('Baseline', 'Potassium'),
    #             ('Baseline',   'protein'),
    #             (      'TI',      'Urea'),
    #             (      'TI', 'Creatinin'),
    #             (      'TI',    'Sodium'),
    #             (      'TI', 'Potassium'),
    #             (      'TI',   'protein'),
    #             (    'EXPL',      'Urea'),
    #             (    'EXPL', 'Creatinin'),
    #             (    'EXPL',    'Sodium'),
    #             (    'EXPL', 'Potassium'),
    #             (    'EXPL',   'protein'),
    #             ( 'IMPL Z1',      'Urea'),
    #             ( 'IMPL Z1', 'Creatinin'),
    #             ( 'IMPL Z1',    'Sodium'),
    #             ( 'IMPL Z1', 'Potassium'),
    #             ( 'IMPL Z1',   'protein'),
    #             ( 'IMPL Z3',      'Urea'),
    #             ( 'IMPL Z3', 'Creatinin'),
    #             ( 'IMPL Z3',    'Sodium'),
    #             ( 'IMPL Z3', 'Potassium'),
    #             ( 'IMPL Z3',   'protein'),
    #             (    'POD1',      'Urea'),
    #             (    'POD1', 'Creatinin'),
    #             (    'POD1',    'Sodium'),
    #             (    'POD1', 'Potassium'),
    #             (    'POD1',   'protein'),
    #             (    'POD2',      'Urea'),
    #             (    'POD2', 'Creatinin'),
    #             (    'POD2',    'Sodium'),
    #             (    'POD2', 'Potassium'),
    #             (    'POD2',   'protein'),
    #             (    'POD3',      'Urea'),
    #             (    'POD3', 'Creatinin'),
    #             (    'POD3',    'Sodium'),
    #             (    'POD3', 'Potassium'),
    #             (    'POD3',   'protein'),
    #             (    'POD4',      'Urea'),
    #             (    'POD4', 'Creatinin'),
    #             (    'POD4',    'Sodium'),
    #             (    'POD4', 'Potassium'),
    #             (    'POD4',   'protein'),
    #             (    'POD5',      'Urea'),
    #             (    'POD5', 'Creatinin'),
    #             (    'POD5',    'Sodium'),
    #             (    'POD5', 'Potassium'),
    #             (    'POD5',   'protein'),
    #             (    'POD6',      'Urea'),
    #             (    'POD6', 'Creatinin'),
    #             (    'POD6',    'Sodium'),
    #             (    'POD6', 'Potassium'),
    #             (    'POD6',   'protein'),
    #             (    'POD7',      'Urea'),
    #             (    'POD7', 'Creatinin'),
    #             (    'POD7',    'Sodium'),
    #             (    'POD7', 'Potassium'),
    #             (    'POD7',   'protein')],
    #            )

# %%

df_urine_2.shape
    # Out[38]: (82, 60)

# %%


df_urine_3 = df_urine_2.stack( level=[0,1] , dropna=False , sort=False )

    # C:\Users\azare\AppData\Local\Temp\ipykernel_5200\1640318314.py:1: FutureWarning: 
    #     The previous implementation of stack is deprecated and will be removed in a future version of pandas. 
    #     See the What's New notes for pandas 2.1.0 for details. Specify future_stack=True to adopt the new implementation and silence this warning.
    #   df_urine_3 = df_urine_2.stack( level=[0,1] , dropna=False , sort=False )
  
df_urine_3.shape    
    # Out[40]: (4920,)

df_urine_3[:4]
    # Out[41]: 
    # sample_ID  treatment  group                     
    # ZC04       DBD-HTK    1      Baseline  Urea         -
    #                                        Creatinin    -
    #                                        Sodium       -
    #                                        Potassium    -
    # dtype: object


df_urine_4 = df_urine_3.reset_index()

df_urine_4[:4]
    # Out[43]: 
    #   sample_ID treatment group   level_3    level_4  0
    # 0      ZC04   DBD-HTK     1  Baseline       Urea  -
    # 1      ZC04   DBD-HTK     1  Baseline  Creatinin  -
    # 2      ZC04   DBD-HTK     1  Baseline     Sodium  -
    # 3      ZC04   DBD-HTK     1  Baseline  Potassium  -

df_urine_4.rename(columns= {
                                    'level_3' : 'time' ,
                                    'level_4' : 'metric' ,
                                    0 : 'value'
                                } ,
                        inplace=True )

df_urine_4[:4]
    # Out[45]: 
    #   sample_ID treatment group      time     metric value
    # 0      ZC04   DBD-HTK     1  Baseline       Urea     -
    # 1      ZC04   DBD-HTK     1  Baseline  Creatinin     -
    # 2      ZC04   DBD-HTK     1  Baseline     Sodium     -
    # 3      ZC04   DBD-HTK     1  Baseline  Potassium     -

df_urine_4[-4:]
    # Out[46]: 
    #      sample_ID treatment group  time     metric value
    # 4916       NaN       NaN   NaN  POD7  Creatinin   NaN
    # 4917       NaN       NaN   NaN  POD7     Sodium   NaN
    # 4918       NaN       NaN   NaN  POD7  Potassium   NaN
    # 4919       NaN       NaN   NaN  POD7    protein   NaN

# %%

df_urine_4['treatment'].unique()
    # Out[47]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP', nan], dtype=object)

df_urine_4['time'].unique()
    # Out[48]: 
    # array(['Baseline', 'TI', 'EXPL', 'IMPL Z1', 'IMPL Z3', 'POD1', 'POD2',
    #        'POD3', 'POD4', 'POD5', 'POD6', 'POD7'], dtype=object)

df_urine_4['metric'].unique()
    # Out[49]: 
    # array(['Urea', 'Creatinin', 'Sodium', 'Potassium', 'protein'],
    #       dtype=object)

df_urine_4['sample_ID'].unique()
    # Out[50]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC16', 'ZC17', 'ZC18', 'ZC19', 'ZC20',
    #        'ZC21', 'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28',
    #        'ZC29', 'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36',
    #        'ZC37', 'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44',
    #        'ZC45', 'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52',
    #        'ZC53', 'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60',
    #        'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68',
    #        'ZC69', nan], dtype=object)

# %%

# explanation => extract_BG.py
df_urine_4['time'] = df_urine_4['time'].replace( to_replace=r'^(POD)(\d+)$', value=r'\1_\2', regex=True )

df_urine_4['time'] = df_urine_4['time'].replace({'EXPL': 'Explantation'})

# Update the 'metric' column replacing 'NA+' with 'Na+'
df_urine_4['metric'] = df_urine_4['metric'].replace( {'Sodium': 'Na+' , 'Potassium' : 'K+' } )

# %%

df_urine_4['time'].unique()
    # Out[54]: 
    # array(['Baseline', 'TI', 'Explantation', 'IMPL Z1', 'IMPL Z3', 'POD_1',
    #        'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7'], dtype=object)

df_urine_4['metric'].unique()
    # Out[55]: array(['Urea', 'Creatinin', 'Na+', 'K+', 'protein'], dtype=object)

# %%

df_urine_4.to_pickle( r'U:\kidney\urine\df_urine_4.pkl' )


# %%



