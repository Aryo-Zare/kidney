


# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# %%

# column ranges of the data.
# preparation for later slicing.

begin = column_index_from_string("AGV") - 1
end = column_index_from_string("AHA")

# %%

cols_to_keep = np.r_[ 0:3 , begin:end ] 

# bg : blood gass
df_hist = overview_2.iloc[ : , cols_to_keep ]

# %%

df_hist.shape
    # Out[12]: (82, 9)

df_hist[:4]
    # Out[17]: 
    #           Sample ID:          Treatment             Group:  \
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1   
    # 0               ZC04            DBD-HTK                  1   
    # 1               ZC05         DBD-Ecosol                  2   
    # 2               ZC06            DBD-HTK                  1   
    # 3               ZC07         DBD-Ecosol                  2   
    
    #   Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%  \
    #                                                                   Infiltration of Neutrophil   
    # 0                                                  2                                           
    # 1                                                  2                                           
    # 2                                                  3                                           
    # 3                                                  2                                           
    
    #                                                                             \
    #   hemorrhage Infiltrationof lymphocytes degradation of tubular cells edema   
    # 0          2                          2                            1     1   
    # 1          2                          2                     2.500000     2   
    # 2          2                          3                            2     2   
    # 3   1.500000                          2                            4     2   
    
                                    
    #   dilatation of bowman capsule  
    # 0                            2  
    # 1                            2  
    # 2                            2  
    # 3                            1  

# %%

df_hist_2 = df_hist.set_index( [('Sample ID:', 'Unnamed: 0_level_1'),
                            ( 'Treatment', 'Unnamed: 1_level_1'),
                            (    'Group:', 'Unnamed: 2_level_1')] )


df_hist_2.iloc[:4 , :2]
    # Out[19]: 
    #                                                                                               Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%  \
    #                                                                                                                                                               Infiltration of Neutrophil   
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)                                                                                              
    # ZC04                             DBD-HTK                         1                                                                             2                                           
    # ZC05                             DBD-Ecosol                      2                                                                             2                                           
    # ZC06                             DBD-HTK                         1                                                                             3                                           
    # ZC07                             DBD-Ecosol                      2                                                                             2                                           
    
                                                                                                              
    #                                                                                               hemorrhage  
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)             
    # ZC04                             DBD-HTK                         1                                     2  
    # ZC05                             DBD-Ecosol                      2                                     2  
    # ZC06                             DBD-HTK                         1                                     2  
    # ZC07                             DBD-Ecosol                      2                              1.500000 


# --- Renaming the index levels ---
new_index_names = ['sample_ID', 'treatment', 'group']

df_hist_2.index.set_names( new_index_names, inplace=True ) # Use inplace=True to modify directly

df_hist_2.iloc[ :4 , :4 ]
    # Out[22]: 
    #                            Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%  \
    #                                                                                            Infiltration of Neutrophil   
    # sample_ID treatment  group                                                                                              
    # ZC04      DBD-HTK    1                                                      2                                           
    # ZC05      DBD-Ecosol 2                                                      2                                           
    # ZC06      DBD-HTK    1                                                      3                                           
    # ZC07      DBD-Ecosol 2                                                      2                                           
    
    #                                                                   \
    #                            hemorrhage Infiltrationof lymphocytes   
    # sample_ID treatment  group                                         
    # ZC04      DBD-HTK    1              2                          2   
    # ZC05      DBD-Ecosol 2              2                          2   
    # ZC06      DBD-HTK    1              2                          3   
    # ZC07      DBD-Ecosol 2       1.500000                          2   
    
                                                             
    #                            degradation of tubular cells  
    # sample_ID treatment  group                               
    # ZC04      DBD-HTK    1                                1  
    # ZC05      DBD-Ecosol 2                         2.500000  
    # ZC06      DBD-HTK    1                                2  
    # ZC07      DBD-Ecosol 2                                4  

# %%

df_hist_2.columns
    # Out[23]: 
    # MultiIndex([('Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%', ...),
    #             ('Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%', ...),
    #             ('Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%', ...),
    #             ('Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%', ...),
    #             ('Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%', ...),
    #             ('Histologie Score: 1=no damage; 2= >0-20%, 3= >20-40%; 4= >40-60%; 5= >60-80%;  6= >80-100%', ...)],
    #            )


# tuples, to later be used for the multi-index.
tups = [
            (
                'histology' ,      # Level 0: remove "BGA " prefix
                col1      # Level 1: if not "pH", keep only the analyte name (first part)
            )
        for col0 , col1 in df_hist_2.columns
]


tupsOut[24]: 
    # [('histology', 'Infiltration of Neutrophil'),
    #  ('histology', 'hemorrhage'),
    #  ('histology', 'Infiltrationof lymphocytes'),
    #  ('histology', 'degradation of tubular cells'),
    #  ('histology', 'edema'),
    #  ('histology', 'dilatation of bowman capsule')]

# %%

# explore

# cat : category : to replace the long column names in the original data.
level_2 = [ f'cat_{n}' for n in range(1,7) ]

level_2
    # Out[29]: ['cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5', 'cat_6']

# %%

tups_2 = [
            (
                'histology' ,      # Level 0: remove "BGA " prefix
                f'cat_{n}'      # Level 1: if not "pH", keep only the analyte name (first part)
            )
        for n in range(1,7)
]


tups_2
    # Out[32]: 
    # [('histology', 'cat_1'),
    #  ('histology', 'cat_2'),
    #  ('histology', 'cat_3'),
    #  ('histology', 'cat_4'),
    #  ('histology', 'cat_5'),
    #  ('histology', 'cat_6')]

# %%

# Using a list comprehension to reconstruct the MultiIndex
df_hist_2.columns = pd.MultiIndex.from_tuples( tups_2 )

df_hist_2.columns
    # Out[34]: 
    # MultiIndex([('histology', 'cat_1'),
    #             ('histology', 'cat_2'),
    #             ('histology', 'cat_3'),
    #             ('histology', 'cat_4'),
    #             ('histology', 'cat_5'),
    #             ('histology', 'cat_6')],
    #            )

# %%

df_hist_3 = df_hist_2.stack( level=[0,1] , dropna=False , sort=False )

df_hist_3.shape
    # Out[36]: (492,)
    
    
df_hist_4 = df_hist_3.reset_index()

df_hist_4[:4]
    # Out[38]: 
    #   sample_ID treatment group    level_3 level_4  0
    # 0      ZC04   DBD-HTK     1  histology   cat_1  2
    # 1      ZC04   DBD-HTK     1  histology   cat_2  2
    # 2      ZC04   DBD-HTK     1  histology   cat_3  2
    # 3      ZC04   DBD-HTK     1  histology   cat_4  1

# 'cat' replaces 'time' in othere datasets.
df_hist_4.rename(columns= {
                                    'level_3' : 'metric' ,
                                    'level_4' : 'cat' ,
                                    0 : 'value'
                                } ,
                        inplace=True )


df_hist_4[:4]
    # Out[40]: 
    #   sample_ID treatment group     metric    cat value
    # 0      ZC04   DBD-HTK     1  histology  cat_1     2
    # 1      ZC04   DBD-HTK     1  histology  cat_2     2
    # 2      ZC04   DBD-HTK     1  histology  cat_3     2
    # 3      ZC04   DBD-HTK     1  histology  cat_4     1

# %%


df_hist_4['metric'].unique()
    # Out[41]: array(['histology'], dtype=object)

df_hist_4['cat'].unique()
    # Out[42]: array(['cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5', 'cat_6'], dtype=object)

df_hist_4['sample_ID'].unique()
    # Out[43]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC16', 'ZC17', 'ZC18', 'ZC19', 'ZC20',
    #        'ZC21', 'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28',
    #        'ZC29', 'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36',
    #        'ZC37', 'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44',
    #        'ZC45', 'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52',
    #        'ZC53', 'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60',
    #        'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68',
    #        'ZC69', nan], dtype=object)

df_hist_4['treatment'].unique()
    # Out[44]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP', nan], dtype=object)

df_hist_4['value'].unique()
    # Out[45]: array([2, 1, 2.5, 3, 1.5, 4, 5, 3.5, ' -', 6, 5.5, '-', nan], dtype=object)

# %%

df_hist_4.to_pickle( r'U:\kidney\histology\df_hist_4.pkl' )


# %%



