

# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# %%

# column ranges of the data.
# preparation for later slicing.

begin = column_index_from_string("TK") - 1
end = column_index_from_string("WP")

# %%

cols_to_keep = np.r_[ 0:3 , begin:end ] 

# bg : blood gass
df_bg = overview_2.iloc[ : , cols_to_keep ]

# %%

# the excel itself has 68 rows, but here it shows 82 rows :
    # some blank excel rows at the bottom was imported when reading it !
    # the reason ? : perhaps
df_bg.shape
    # Out[16]: (82, 87)


df_bg.iloc[:4,:4]
    # Out[21]: 
    #           Sample ID:          Treatment             Group:   BGA TI
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1       pH
    # 0               ZC04            DBD-HTK                  1        -
    # 1               ZC05         DBD-Ecosol                  2 7.399000
    # 2               ZC06            DBD-HTK                  1 7.448000
    # 3               ZC07         DBD-Ecosol                  2 7.384000

df_bg.iloc[:4,-4:]
    # Out[22]: 
    #     BGA POD7                                     
    #   K+ [mmol/] NA+ [mmol/] Ca2+ [mmol/] CL- [mmol/]
    # 0          -           -            -           -
    # 1   4.900000         136     1.190000          99
    # 2          -           -            -           -
    # 3   4.200000         130     1.190000          86

# %%

# blank cells at the end of the sheet are imported to the excel file !
'''
    Even if those cells look completely blank in Excel, they may be part of the sheet’s defined or formatted area, 
    so pandas imports them as rows with NaN values. 
    Essentially, Excel sometimes contains "phantom rows" at the end due to formatting, previously stored data, 
    or a defined print area that extends beyond your visible data.
'''

df_bg.iloc[-4:,:4]
    # Out[75]: 
    #            Sample ID:          Treatment             Group: BGA TI
    #    Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1     pH
    # 78                NaN                NaN                NaN    NaN
    # 79                NaN                NaN                NaN    NaN
    # 80                NaN                NaN                NaN    NaN
    # 81                NaN                NaN                NaN    NaN


df_bg.iloc[-18:-12,:4]
    # Out[79]: 
    #            Sample ID:          Treatment             Group:   BGA TI
    #    Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1       pH
    # 64               ZC68                NMP                  0 7.394000
    # 65               ZC69                NMP                  0 7.360000
    # 66                NaN                NaN                NaN      NaN
    # 67                NaN                NaN                NaN      NaN
    # 68                NaN                NaN                NaN      NaN
    # 69                NaN                NaN                NaN      NaN

# %%

# %%

# there is nan value here.
df_bg.iloc[:,0].unique()
    # Out[70]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC13', 'ZC14', 'ZC15', 'ZC16', 'ZC17', 'ZC18', 'ZC19', 'ZC20',
    #        'ZC21', 'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27', 'ZC28',
    #        'ZC29', 'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35', 'ZC36',
    #        'ZC37', 'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43', 'ZC44',
    #        'ZC45', 'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51', 'ZC52',
    #        'ZC53', 'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59', 'ZC60',
    #        'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67', 'ZC68',
    #        'ZC69', nan], dtype=object)


# these are probalby the blank rows at the end of the excel document.
df_bg.loc[ df_bg.iloc[:,0].isna() ]
    # Out[74]: 
    #            Sample ID:          Treatment             Group: BGA TI  \
    #    Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1     pH   
    # 66                NaN                NaN                NaN    NaN   
    # 67                NaN                NaN                NaN    NaN   
    # 68                NaN                NaN                NaN    NaN   
    # 69                NaN                NaN                NaN    NaN   
    # 70                NaN                NaN                NaN    NaN   
    # 71                NaN                NaN                NaN    NaN   
    # 72                NaN                NaN                NaN    NaN   
    # 73                NaN                NaN                NaN    NaN   
    # 74                NaN                NaN                NaN    NaN   
    # 75                NaN                NaN                NaN    NaN   
    # 76                NaN                NaN                NaN    NaN   
    # 77                NaN                NaN                NaN    NaN   
    # 78                NaN                NaN                NaN    NaN   
    # 79                NaN                NaN                NaN    NaN   
    # 80                NaN                NaN                NaN    NaN   
    # 81                NaN                NaN                NaN    NaN   
    
    #                                                                            \
    #    pCO2 [mmHg] pO2 [mmHg] K+ [mmol/] NA+ [mmol/] Ca2+ [mmol/] CL- [mmol/]   
    # 66         NaN        NaN        NaN         NaN          NaN         NaN   
    # 67         NaN        NaN        NaN         NaN          NaN         NaN   
    # 68         NaN        NaN        NaN         NaN          NaN         NaN   
    # 69         NaN        NaN        NaN         NaN          NaN         NaN   
    # 70         NaN        NaN        NaN         NaN          NaN         NaN   
    # 71         NaN        NaN        NaN         NaN          NaN         NaN   
    # 72         NaN        NaN        NaN         NaN          NaN         NaN   
    # 73         NaN        NaN        NaN         NaN          NaN         NaN   
    # 74         NaN        NaN        NaN         NaN          NaN         NaN   
    # 75         NaN        NaN        NaN         NaN          NaN         NaN   
    # 76         NaN        NaN        NaN         NaN          NaN         NaN   
    # 77         NaN        NaN        NaN         NaN          NaN         NaN   
    # 78         NaN        NaN        NaN         NaN          NaN         NaN   
    # 79         NaN        NaN        NaN         NaN          NaN         NaN   
    # 80         NaN        NaN        NaN         NaN          NaN         NaN   
    # 81         NaN        NaN        NaN         NaN          NaN         NaN   
    
    #    BGA Ex                                                             \
    #        pH pCO2 [mmHg] pO2 [mmHg] K+ [mmol/] NA+ [mmol/] Ca2+ [mmol/]   
    # 66    NaN         NaN        NaN        NaN         NaN          NaN   
    # 67    NaN         NaN        NaN        NaN         NaN          NaN   
    # 68    NaN         NaN        NaN        NaN         NaN          NaN   
    # 69    NaN         NaN        NaN        NaN         NaN          NaN   
    # 70    NaN         NaN        NaN        NaN         NaN          NaN   
    # 71    NaN         NaN        NaN        NaN         NaN          NaN   
    # 72    NaN         NaN        NaN        NaN         NaN          NaN   
    # 73    NaN         NaN        NaN        NaN         NaN          NaN   
    # 74    NaN         NaN        NaN        NaN         NaN          NaN   
    # 75    NaN         NaN        NaN        NaN         NaN          NaN   
    # 76    NaN         NaN        NaN        NaN         NaN          NaN   
    # 77    NaN         NaN        NaN        NaN         NaN          NaN   
    # 78    NaN         NaN        NaN        NaN         NaN          NaN   
    # 79    NaN         NaN        NaN        NaN         NaN          NaN   
    # 80    NaN         NaN        NaN        NaN         NaN          NaN   
    # 81    NaN         NaN        NaN        NaN         NaN          NaN   
# ...


# %%

# hierarchical columns that should be turned into a frozen index !

df_bg.iloc[: , :3].columns
# Out[23]: 
# MultiIndex([('Sample ID:', 'Unnamed: 0_level_1'),
#             ( 'Treatment', 'Unnamed: 1_level_1'),
#             (    'Group:', 'Unnamed: 2_level_1')],
#            )


df_bg_2 = df_bg.set_index( [('Sample ID:', 'Unnamed: 0_level_1'),
                            ( 'Treatment', 'Unnamed: 1_level_1'),
                            (    'Group:', 'Unnamed: 2_level_1')] )


# df_bg_2 = df_bg.set_index( frozen_index )
    # ValueError: Length mismatch: Expected 82 rows, received array of length 3

# %%

df_bg_2.iloc[:4 , :2]
    # Out[31]: 
    #                                                                                                 BGA TI  \
    #                                                                                                     pH   
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)            
    # ZC04                             DBD-HTK                         1                                   -   
    # ZC05                             DBD-Ecosol                      2                            7.399000   
    # ZC06                             DBD-HTK                         1                            7.448000   
    # ZC07                             DBD-Ecosol                      2                            7.384000   
    
                                                                                                               
    #                                                                                               pCO2 [mmHg]  
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)              
    # ZC04                             DBD-HTK                         1                                      -  
    # ZC05                             DBD-Ecosol                      2                              45.500000  
    # ZC06                             DBD-HTK                         1                              41.900000  
    # ZC07                             DBD-Ecosol                      2                                     53  

# --- Renaming the index levels ---
new_index_names = ['sample_ID', 'treatment', 'group']

df_bg_2.index.set_names( new_index_names, inplace=True ) # Use inplace=True to modify directly

df_bg_2.iloc[ :4 , :4 ]
    # Out[34]: 
    #                              BGA TI                                  
    #                                  pH pCO2 [mmHg] pO2 [mmHg] K+ [mmol/]
    # sample_ID treatment  group                                           
    # ZC04      DBD-HTK    1            -           -          -          -
    # ZC05      DBD-Ecosol 2     7.399000   45.500000  76.500000   3.300000
    # ZC06      DBD-HTK    1     7.448000   41.900000  73.100000   3.700000
    # ZC07      DBD-Ecosol 2     7.384000          53        182   4.100000


df_bg_2.iloc[ :4 , -4: ]
    # Out[35]: 
    #                              BGA POD7                                     
    #                            K+ [mmol/] NA+ [mmol/] Ca2+ [mmol/] CL- [mmol/]
    # sample_ID treatment  group                                                
    # ZC04      DBD-HTK    1              -           -            -           -
    # ZC05      DBD-Ecosol 2       4.900000         136     1.190000          99
    # ZC06      DBD-HTK    1              -           -            -           -
    # ZC07      DBD-Ecosol 2       4.200000         130     1.190000          86

# %%

# explore : 
    # hirarchical index structure
    # tuple operation

df_bg_2.columns
    # Out[36]: 
    # MultiIndex([(    'BGA TI',           'pH'),
    #             (    'BGA TI',  'pCO2 [mmHg]'),
    #             (    'BGA TI',   'pO2 [mmHg]'),


for i,j in df_bg_2.columns :
    print( f' {i} & {j}' )
     # BGA TI & pH
     # BGA TI & pCO2 [mmHg]
     # BGA TI & pO2 [mmHg]
     # BGA TI & K+ [mmol/]

# %%

# rename the columns

# Using a list comprehension to reconstruct the MultiIndex
df_bg_2.columns = pd.MultiIndex.from_tuples(
            [
                        (
                            col0.replace("BGA ", ""),      # Level 0: remove "BGA " prefix
                            col1 if col1 == "pH" else col1.split(" ")[0]     # Level 1: if not "pH", keep only the analyte name (first part)
                        )
                    for col0, col1 in df_bg_2.columns
            ]
)


df_bg_2.columns
    # Out[39]: 
    # MultiIndex([(    'TI',   'pH'),
    #             (    'TI', 'pCO2'),
    #             (    'TI',  'pO2'),
    #             (    'TI',   'K+'),

# %%

df_bg_3 = df_bg_2.stack( level=[0,1] , dropna=False , sort=False )

df_bg_3.shape
    # Out[41]: (6888,)

df_bg_3[:4]
    # Out[42]: 
    # sample_ID  treatment  group          
    # ZC04       DBD-HTK    1      TI  pH      -
    #                                  pCO2    -
    #                                  pO2     -
    #                                  K+      -
    # dtype: object


df_bg_4 = df_bg_3.reset_index()

df_bg_4[:4]
    # Out[44]: 
    #   sample_ID treatment group level_3 level_4  0
    # 0      ZC04   DBD-HTK     1      TI      pH  -
    # 1      ZC04   DBD-HTK     1      TI    pCO2  -
    # 2      ZC04   DBD-HTK     1      TI     pO2  -
    # 3      ZC04   DBD-HTK     1      TI      K+  -

df_bg_4.rename(columns= {
                                    'level_3' : 'time' ,
                                    'level_4' : 'metric' ,
                                    0 : 'value'
                                } ,
                        inplace=True )


df_bg_4[:4]
    # Out[46]: 
    #   sample_ID treatment group time metric value
    # 0      ZC04   DBD-HTK     1   TI     pH     -
    # 1      ZC04   DBD-HTK     1   TI   pCO2     -
    # 2      ZC04   DBD-HTK     1   TI    pO2     -
    # 3      ZC04   DBD-HTK     1   TI     K+     -

# %%

df_bg_4['treatment'].unique()
    # Out[48]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP', nan], dtype=object)

df_bg_4['time'].unique()
    # Out[49]: 
    # array(['TI', 'Ex', 'Imp Z1', 'Imp Z2', 'Imp Z3', 'POD1', 'POD2', 'POD3',
    #        'POD4', 'POD5', 'POD6', 'POD7'], dtype=object)

df_bg_4['metric'].unique()
    # Out[50]: array(['pH', 'pCO2', 'pO2', 'K+', 'NA+', 'Ca2+', 'CL-'], dtype=object)

df_bg_4['sample_ID'].unique()
    # Out[51]: 
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

# Update the 'time' column using regex to insert an underscore between 'POD' and the number.
# The regular expression r'^(POD)(\d+)$' works as follows:
    # ^ and $ ensure we match the entire string.
    # (POD) captures the string "POD".
    # (\d+) captures one or more digits.
    # The replacement string r'\1_\2' recombines the two captured groups with an underscore between them.
# I initially tested with : ... df_bg_4['time'].str.replace ...  :
    # but te below should work.
df_bg_4['time'] = df_bg_4['time'].replace( to_replace=r'^(POD)(\d+)$', value=r'\1_\2', regex=True )

df_bg_4['time'] = df_bg_4['time'].replace({'Ex': 'Explantation'})

# Update the 'metric' column replacing 'NA+' with 'Na+'
df_bg_4['metric'] = df_bg_4['metric'].replace( {'NA+': 'Na+' , 'CL-' : 'Cl-' } )


# %%

df_bg_4['time'].unique()
    # Out[54]: 
    # array(['TI', 'Ex', 'Imp Z1', 'Imp Z2', 'Imp Z3', 'POD_1', 'POD_2',
    #        'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7'], dtype=object)

df_bg_4['metric'].unique()
    # Out[130]: array(['pH', 'pCO2', 'pO2', 'K+', 'Na+', 'Ca2+', 'Cl-'], dtype=object)

# %%

df_bg_4.to_csv( r'U:\kidney\BG\df_bg_4.csv' )

# %%




