

# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# %%

# column ranges of the data.
# preparation for later slicing.

begin = column_index_from_string("AFU") - 1
end = column_index_from_string("AGE")

# %%

cols_to_keep = np.r_[ 0:3 , begin:end ] 

# bg : blood gass
df_density = overview_2.iloc[ : , cols_to_keep ]

# %%

df_density.shape
    # Out[13]: (82, 14)


df_density.iloc[:4,:4]
    # Out[14]: 
    #           Sample ID:          Treatment             Group:  \
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1   
    # 0               ZC04            DBD-HTK                  1   
    # 1               ZC05         DBD-Ecosol                  2   
    # 2               ZC06            DBD-HTK                  1   
    # 3               ZC07         DBD-Ecosol                  2   
    
    #   Urin Dichtebestimmung  
    #                      Ti  
    # 0              1.017000  
    # 1              1.016000  
    # 2              1.012000  
    # 3              1.026000  


df_density.iloc[:4,-4:]
    # Out[15]: 
    #   Urin Dichtebestimmung                           
    #                    POD4     POD5     POD6     POD7
    # 0              1.002000 1.004000 1.004000        -
    # 1                     - 1.002000 1.009000 1.004000
    # 2                     - 1.003000        -        -
    # 3              1.014000        1 1.006000 1.008000

# %%


df_density_2 = df_density.set_index( [('Sample ID:', 'Unnamed: 0_level_1'),
                            ( 'Treatment', 'Unnamed: 1_level_1'),
                            (    'Group:', 'Unnamed: 2_level_1')] )

# --- Renaming the index levels ---
new_index_names = ['sample_ID', 'treatment', 'group']

df_density_2.index.set_names( new_index_names, inplace=True ) # Use inplace=True to modify directly

# %%

df_density_2.iloc[ :4 , :4 ]
    # Out[19]: 
    #                            Urin Dichtebestimmung                       
    #                                               Ti Expl       Z1       Z3
    # sample_ID treatment  group                                             
    # ZC04      DBD-HTK    1                  1.017000    - 1.010000 1.033000
    # ZC05      DBD-Ecosol 2                  1.016000    - 1.019000 1.014000
    # ZC06      DBD-HTK    1                  1.012000    - 1.013000 1.015000
    # ZC07      DBD-Ecosol 2                  1.026000    - 1.014000 1.016000

df_density_2.iloc[ :4 , -4: ]
    # Out[20]: 
    #                            Urin Dichtebestimmung                           
    #                                             POD4     POD5     POD6     POD7
    # sample_ID treatment  group                                                 
    # ZC04      DBD-HTK    1                  1.002000 1.004000 1.004000        -
    # ZC05      DBD-Ecosol 2                         - 1.002000 1.009000 1.004000
    # ZC06      DBD-HTK    1                         - 1.003000        -        -
    # ZC07      DBD-Ecosol 2                  1.014000        1 1.006000 1.008000


# %%

df_density_2.columns
    # Out[21]: 
    # MultiIndex([('Urin Dichtebestimmung',   'Ti'),
    #             ('Urin Dichtebestimmung', 'Expl'),
    #             ('Urin Dichtebestimmung',   'Z1'),
    #             ('Urin Dichtebestimmung',   'Z3'),
    #             ('Urin Dichtebestimmung', 'POD1'),
    #             ('Urin Dichtebestimmung', 'POD2'),
    #             ('Urin Dichtebestimmung', 'POD3'),
    #             ('Urin Dichtebestimmung', 'POD4'),
    #             ('Urin Dichtebestimmung', 'POD5'),
    #             ('Urin Dichtebestimmung', 'POD6'),
    #             ('Urin Dichtebestimmung', 'POD7')],
    #            )

# %%

df_density_2.to_pickle( r'U:\kidney\urine\density\df_density_2.pkl' )

# %%

df_density_3 = df_density_2.stack( level=[0,1] , dropna=False , sort=False )

# %%

df_density_3.shape
    # Out[24]: (902,)

df_density_3[:4]
    # Out[25]: 
    # sample_ID  treatment  group                             
    # ZC04       DBD-HTK    1      Urin Dichtebestimmung  Ti     1.017000
    #                                                     Expl          -
    #                                                     Z1     1.010000
    #                                                     Z3     1.033000
    # dtype: object

df_density_4 = df_density_3.reset_index()

df_density_4[:4]
    # Out[27]: 
    #   sample_ID treatment group                level_3 level_4        0
    # 0      ZC04   DBD-HTK     1  Urin Dichtebestimmung      Ti 1.017000
    # 1      ZC04   DBD-HTK     1  Urin Dichtebestimmung    Expl        -
    # 2      ZC04   DBD-HTK     1  Urin Dichtebestimmung      Z1 1.010000
    # 3      ZC04   DBD-HTK     1  Urin Dichtebestimmung      Z3 1.033000

df_density_4.rename(columns= {
                                    'level_3' : 'metric' ,
                                    'level_4' : 'time' ,
                                    0 : 'value'
                                } ,
                        inplace=True )


df_density_4[:4]
    # Out[29]: 
    #   sample_ID treatment group                 metric  time    value
    # 0      ZC04   DBD-HTK     1  Urin Dichtebestimmung    Ti 1.017000
    # 1      ZC04   DBD-HTK     1  Urin Dichtebestimmung  Expl        -
    # 2      ZC04   DBD-HTK     1  Urin Dichtebestimmung    Z1 1.010000
    # 3      ZC04   DBD-HTK     1  Urin Dichtebestimmung    Z3 1.033000

# %%

df_density_4['sample_ID'].unique()
    # Out[30]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC16', 'ZC17', 'ZC18', 'ZC19', 'ZC20',
    #        'ZC21', 'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28',
    #        'ZC29', 'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36',
    #        'ZC37', 'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44',
    #        'ZC45', 'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52',
    #        'ZC53', 'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60',
    #        'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68',
    #        'ZC69', nan], dtype=object)

df_density_4['treatment'].unique()
    # Out[31]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP', nan], dtype=object)

df_density_4['time'].unique()
    # Out[32]: 
    # array(['Ti', 'Expl', 'Z1', 'Z3', 'POD1', 'POD2', 'POD3', 'POD4', 'POD5',
    #        'POD6', 'POD7'], dtype=object)

df_density_4['metric'].unique()
    # Out[33]: array(['Urin Dichtebestimmung'], dtype=object)

# %%

df_density_4['time'] = df_density_4['time'].replace( to_replace=r'^(POD)(\d+)$', value=r'\1_\2', regex=True )

df_density_4['time'] = df_density_4['time'].replace({'Expl': 'Explantation'})

# Update the 'metric' column replacing 'NA+' with 'Na+'
df_density_4['metric'] = df_density_4['metric'].replace( { 'Urin Dichtebestimmung' : 'density' } )

# %%

df_density_4['time'].unique()
    # Out[37]: 
    # array(['Ti', 'Explantation', 'Z1', 'Z3', 'POD_1', 'POD_2', 'POD_3',
    #        'POD_4', 'POD_5', 'POD_6', 'POD_7'], dtype=object)

df_density_4['metric'].unique()
    # Out[38]: array(['density'], dtype=object)

# %%

df_density_4.to_pickle( r'U:\kidney\urine\density\df_density_4.pkl' )

# %%



# %%


