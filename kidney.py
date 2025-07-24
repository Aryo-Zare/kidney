
# reformatting the dataset

# %%

from openpyxl.utils import column_index_from_string

# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] , index_col=0 )


# the non-standard 'ZC6' entry was renamed to 'ZC06'
overview_3 = pd.read_excel(  r'U:\kidney\overview_3.xlsx' , header=[0,1] , index_col=0 )

# the long ( tidy ) format.
# non-standard entries ('-') & NA values exist.
# no filtering base on treatmnet group , time or sample_ID .
# no baseline correction
df_serum_chem_4 = pd.read_csv( r'U:\kidney\df_serum_chem_4.csv' , index_col=0 )


# %%

overview.shape
    # Out[5]: (83, 916)



overview.iloc[:4 , :4]
    # Out[8]: 
    #   Sample ID:   Treatment Group: BW Eingang
    # 0        NaN         NaN    NaN        NaN
    # 1       ZC04     DBD-HTK      1  25.600000
    # 2       ZC05  DBD-Ecosol      2  20.200000
    # 3       ZC06     DBD-HTK      1         21

# %%


overview[:4]
    # Out[6]: 
    #   Sample ID:   Treatment Group:  ... Unnamed: 913 Unnamed: 914 Unnamed: 915
    # 0        NaN         NaN    NaN  ...         POD6         POD7         POD7
    # 1       ZC04     DBD-HTK      1  ...            -            -            -
    # 2       ZC05  DBD-Ecosol      2  ...            -            -            -
    # 3       ZC06     DBD-HTK      1  ...            -            -            -
    
    # [4 rows x 916 columns]


overview.columns
    # Out[7]: 
    # Index(['Sample ID:', 'Treatment', 'Group:', 'BW Eingang', 'Ear tag',
    #        'Operation date Ti:', 'Operation TI incisicion time:',
    #        'Operation TI end time (wound closure): ', 'Duration TI', 'BW in kg TI',
    #        ...
    #        'Unnamed: 906', 'Unnamed: 907', 'Unnamed: 908', 'Unnamed: 909',
    #        'Unnamed: 910', 'Unnamed: 911', 'Unnamed: 912', 'Unnamed: 913',
    #        'Unnamed: 914', 'Unnamed: 915'],
    #       dtype='object', length=916)


print(list(overview.columns))

# %%
# %%

# Explore : first column is the number '1' column ( index starts from 1 ).

column_index_from_string("A")
    # Out[9]: 1

column_index_from_string("D")
    # Out[35]: 4

# %%

column_index_from_string("AT")
    # Out[19]: 46

column_index_from_string("EN")
    # Out[18]: 144

# %%

# for later slicing.
# indices for the serum chemistry analytes.
begin = column_index_from_string("AT") - 1
end = column_index_from_string("EN")

# %%

# Option 2: Using numpy's r_ to slice and concatenate the indices:
cols_to_keep = np.r_[ 0:3 , begin:end ]  # np.r_ concatenates slices and arrays

cols_to_keep[-2:]
    # Out[12]: array([142, 143])

df_serum_chem = overview.iloc[:, cols_to_keep]

df_serum_chem.shape
    # Out[25]: (82, 102)

# column is hierarchical.
df_serum_chem.iloc[:4 , :6]
    # Out[15]: 
    #           Sample ID:          Treatment             Group:        TI  \
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1 LDH_serum   
    # 0               ZC04            DBD-HTK                  1       752   
    # 1               ZC05         DBD-Ecosol                  2      1636   
    # 2               ZC06            DBD-HTK                  1       973   
    # 3               ZC07         DBD-Ecosol                  2       669   
    
                                      
    #   Total_protein_serum Urea_serum  
    # 0            5.100000   1.890000  
    # 1            4.800000   1.760000  
    # 2            4.700000   3.680000  
    # 3                   5   2.390000 
    

df_serum_chem.iloc[:4 , -3:]
    # Out[16]: 
    #      POD_7                   
    #   Ka_serum CRP_serum Cl_serum
    # 0        -         -        -
    # 1 3.700000         6      101
    # 2        -         -        -
    # 3 4.200000         7       84

# %%

# column is hierarchical.
df_serum_chem.iloc[:4 , :3].columns
    # Out[18]: 
    # MultiIndex([('Sample ID:', 'Unnamed: 0_level_1'),
    #             ( 'Treatment', 'Unnamed: 1_level_1'),
    #             (    'Group:', 'Unnamed: 2_level_1')],
    #            )

df_serum_chem.iloc[:4 , -3:].columns
    # Out[17]: 
    # MultiIndex([('POD_7',  'Ka_serum'),
    #             ('POD_7', 'CRP_serum'),
    #             ('POD_7',  'Cl_serum')],
    #            )

# %%

# .stack method does not have the parameter : id_vars : as in .melt.
    # hence this is the trick to freeze the id columns.
# why not using .melt : it does not support multi-index.

df_serum_chem_2 = df_serum_chem.set_index([ 
                ('Sample ID:', 'Unnamed: 0_level_1'),
                ( 'Treatment', 'Unnamed: 1_level_1'),
                (    'Group:', 'Unnamed: 2_level_1')
])


df_serum_chem_2.iloc[ :4 , :3 ]
    # Out[21]: 
    #                                                                                                      TI  \
    #                                                                                               LDH_serum   
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)             
    # ZC04                             DBD-HTK                         1                                  752   
    # ZC05                             DBD-Ecosol                      2                                 1636   
    # ZC06                             DBD-HTK                         1                                  973   
    # ZC07                             DBD-Ecosol                      2                                  669   
    
    #                                                                                                                    \
    #                                                                                               Total_protein_serum   
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)                       
    # ZC04                             DBD-HTK                         1                                       5.100000   
    # ZC05                             DBD-Ecosol                      2                                       4.800000   
    # ZC06                             DBD-HTK                         1                                       4.700000   
    # ZC07                             DBD-Ecosol                      2                                              5   
    
                                                                                                              
    #                                                                                               Urea_serum  
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)             
    # ZC04                             DBD-HTK                         1                              1.890000  
    # ZC05                             DBD-Ecosol                      2                              1.760000  
    # ZC06                             DBD-HTK                         1                              3.680000  
    # ZC07                             DBD-Ecosol                      2                              2.390000  


# --- Renaming the index levels ---
new_index_names = ['sample_ID', 'treatment', 'group']
df_serum_chem_2.index.set_names( new_index_names, inplace=True) # Use inplace=True to modify directly

df_serum_chem_2.iloc[ :4 , :3 ]
    # Out[25]: 
    #                                   TI                               
    #                            LDH_serum Total_protein_serum Urea_serum
    # sample_ID treatment  group                                         
    # ZC04      DBD-HTK    1           752            5.100000   1.890000
    # ZC05      DBD-Ecosol 2          1636            4.800000   1.760000
    # ZC06      DBD-HTK    1           973            4.700000   3.680000
    # ZC07      DBD-Ecosol 2           669                   5   2.390000


df_serum_chem_2.iloc[ :4 , -3: ]
    # Out[26]: 
    #                               POD_7                   
    #                            Ka_serum CRP_serum Cl_serum
    # sample_ID treatment  group                            
    # ZC04      DBD-HTK    1            -         -        -
    # ZC05      DBD-Ecosol 2     3.700000         6      101
    # ZC06      DBD-HTK    1            -         -        -
    # ZC07      DBD-Ecosol 2     4.200000         7       84

# %%

# level=[0,1] : top & bottom levels of the column names ( multi-index ).
df_serum_chem_3 = df_serum_chem_2.stack( level=[0,1] , dropna=False , sort=False )
    # C:\Users\azare\AppData\Local\Temp\ipykernel_32456\1284703087.py:1: 
        # FutureWarning: The previous implementation of stack is deprecated and will be removed in a future version of pandas. 
        # See the What's New notes for pandas 2.1.0 for details. Specify future_stack=True to adopt the new implementation and silence this warning.
    #   df_serum_chem_3 = df_serum_chem_2.stack( level=[0,1] )


type(df_serum_chem_3)
    # Out[29]: pandas.core.series.Series

df_serum_chem_3.shape
    # Out[28]: (6533,)


# if sort = True
df_serum_chem_3[:4]
    # Out[30]: 
    # sample_ID  treatment  group                                   
    # ZC04       DBD-HTK    1      Explantation  LDH_serum                  624
    #                                            Total_protein_serum   5.200000
    #                                            Urea_serum            2.570000
    #                                            Creatinin_serum            115
    # dtype: object


# if sort = Flase
df_serum_chem_3[:4]
    # Out[33]: 
    # sample_ID  treatment  group                         
    # ZC04       DBD-HTK    1      TI  LDH_serum                  752
    #                                  Total_protein_serum   5.100000
    #                                  Urea_serum            1.890000
    #                                  Creatinin_serum             96
    # dtype: object


df_serum_chem_4 = df_serum_chem_3.reset_index()

# note : as it was originally a series, the last column has no name ( 0 ).
df_serum_chem_4[:4]
    # Out[35]: 
    #   sample_ID treatment group level_3              level_4        0
    # 0      ZC04   DBD-HTK     1      TI            LDH_serum      752
    # 1      ZC04   DBD-HTK     1      TI  Total_protein_serum 5.100000
    # 2      ZC04   DBD-HTK     1      TI           Urea_serum 1.890000
    # 3      ZC04   DBD-HTK     1      TI      Creatinin_serum       96


# parameters :  ‘var_name’ , ‘value_name’ : exist in .melt 
    # but not in .stack
# 'value' is actually : blood level !!
df_serum_chem_4.rename(columns= {
                                    'level_3' : 'time' ,
                                    'level_4' : 'metric' ,
                                    0 : 'value'
                                } ,
                        inplace=True )


df_serum_chem_4[:3]
    # Out[40]: 
    #   sample_ID treatment group time               metric    value
    # 0      ZC04   DBD-HTK     1   TI            LDH_serum      752
    # 1      ZC04   DBD-HTK     1   TI  Total_protein_serum 5.100000
    # 2      ZC04   DBD-HTK     1   TI           Urea_serum 1.890000

# %%

# this is done here, becasue : overview_3.xlsx : file was changed afterwards.
df_serum_chem_4.iloc[ : , 0 ].replace( to_replace='ZC6' , value='ZC06' , inplace=True )


# %%

df_serum_chem_4.to_csv( r'U:\kidney\df_serum_chem_4.csv' )

# %%

df_serum_chem_4['treatment'].unique()
    # Out[46]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP', nan], dtype=object)

df_serum_chem_4['time'].unique()
    # Out[48]: 
    # array(['TI', 'Explantation', 'Implantation_Z1', 'Implantation_Z3',
    #        'POD_1', 'POD_2', 'POD_3', 'POD_4', 'POD_5', 'POD_6', 'POD_7'],
    #       dtype=object)

df_serum_chem_4['metric'].unique()
    # Out[52]: 
    # array(['LDH_serum', 'Total_protein_serum', 'Urea_serum',
    #        'Creatinin_serum', 'Uric_acid_serum', 'Na_serum', 'Ka_serum',
    #        'CRP_serum', 'Cl_serum'], dtype=object)


df_serum_chem_4['sample_ID'].unique()
# Out[112]: 
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
# %%

# explore

excel_col_number = column_index_from_string("EN")  # returns 144
# Use .iloc to select by position. This returns columns 0 to 143.
df_selected = df.iloc[:, :144]

print(df_selected.head())

# %%

overview.iloc[ :4 , 40:44 ].columns
    # Out[20]: 
    # Index(['Surgeon sacrifice', 'Kidney samples after sacrifice',
    #        'Spleen samples after sacrifice', 'Lymphnode samples after sacrifice'],
    #       dtype='object')

overview.iloc[ :4 , 41 ]
    # Out[14]: 
    # 0    Histology
    # 1            x
    # 2            x
    # 3            x
    # Name: Kidney samples after sacrifice, dtype: object


# %%

# it's just when you read the same 'overview' file with : header=[0,1]  !!
overview_2 = pd.read_excel( r'U:\kidney\overview.xlsx' , header=[0,1] )

overview_2.shape
    # Out[16]: (82, 916)

overview_2.iloc[:4,:4]
    # Out[93]: 
    #           Sample ID:          Treatment             Group:         BW Eingang
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1 Unnamed: 3_level_1
    # 0               ZC04            DBD-HTK                  1          25.600000
    # 1               ZC05         DBD-Ecosol                  2          20.200000
    # 2               ZC06            DBD-HTK                  1                 21
    # 3               ZC07         DBD-Ecosol                  2          18.700000


overview_2.iloc[ :4 , 0 ]
    # Out[96]: 
    # 0    ZC04
    # 1    ZC05
    # 2    ZC06
    # 3    ZC07
    # Name: (Sample ID:, Unnamed: 0_level_1), dtype: object


overview_2.iloc[ : , 0 ].unique()
    # Out[97]: 
    # array(['ZC04', 'ZC05', 'ZC06', 'ZC07', 'ZC08', 'ZC09', 'ZC10', 'ZC11',
    #        'ZC6', 'ZC13', 'ZC14', 'ZC15', 'ZC16', 'ZC17', 'ZC18', 'ZC19',
    #        'ZC20', 'ZC21', 'ZC22', 'ZC23', 'ZC24', 'ZC25', 'ZC26', 'ZC27',
    #        'ZC28', 'ZC29', 'ZC30', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC35',
    #        'ZC36', 'ZC37', 'ZC38', 'ZC39', 'ZC40', 'ZC41', 'ZC42', 'ZC43',
    #        'ZC44', 'ZC45', 'ZC46', 'ZC47', 'ZC48', 'ZC49', 'ZC50', 'ZC51',
    #        'ZC52', 'ZC53', 'ZC54', 'ZC55', 'ZC56', 'ZC57', 'ZC58', 'ZC59',
    #        'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66', 'ZC67',
    #        'ZC68', 'ZC69', nan], dtype=object)


# the non-standard 'ZC6' entry is renamed to 'ZC06'.
overview_2.iloc[ : , 0 ].replace( to_replace='ZC6' , value='ZC06' , inplace=True )

overview_2.to_excel(  r'U:\kidney\overview_3.xlsx' , engine='xlsxwriter' )


# %%



overview_2.iloc[ :4 , 40:44 ]
    # Out[17]: 
    #     Surgeon sacrifice Kidney samples after sacrifice  \
    #   Unnamed: 40_level_1                      Histology   
    # 0               ZC/LE                              x   
    # 1                  LE                              x   
    # 2                  LE                              x   
    # 3               LE/WL                              x   
    
    
    #   Spleen samples after sacrifice Lymphnode samples after sacrifice  
    #                        Histology                         Histology  
    # 0                              x                                 -  
    # 1                              x                                 -  
    # 2                              x                                 x  
    # 3                              x                                 x  

overview_2.iloc[ :4 , 40:44 ].columns
overview_2.iloc[ :4 , 40:44 ].columns
    # Out[19]: 
    # MultiIndex([(                'Surgeon sacrifice', 'Unnamed: 40_level_1'),
    #             (   'Kidney samples after sacrifice',           'Histology'),
    #             (   'Spleen samples after sacrifice',           'Histology'),
    #             ('Lymphnode samples after sacrifice',           'Histology')],
           )

# %%
   
# propagates the value for all the original cells in a merged cell. 
overview_2.iloc[ :4 , 44:48 ].columns
    # Out[21]: 
    # MultiIndex([('Liver samples after sacrifice',            'Histology'),
    #             (            'Enzyme TI (Serum)',            'LDH [U/L]'),
    #             (            'Enzyme TI (Serum)', 'Total protein [g/dL]'),
    #             (            'Enzyme TI (Serum)',        'Urea [mmol/L]')],
    #            )

# %%

overview_2.columns
    # Out[8]: 
    # MultiIndex([(                             'Sample ID:', 'Unnamed: 0_level_1'),
    #             (                              'Treatment', 'Unnamed: 1_level_1'),
    #             (                                 'Group:', 'Unnamed: 2_level_1'),
    #             (                             'BW Eingang', 'Unnamed: 3_level_1'),
    #             (                                'Ear tag', 'Unnamed: 4_level_1'),
    #             (                     'Operation date Ti:', 'Unnamed: 5_level_1'),
    #             (          'Operation TI incisicion time:', 'Unnamed: 6_level_1'),
    #             ('Operation TI end time (wound closure): ', 'Unnamed: 7_level_1'),
    #             (                            'Duration TI', 'Unnamed: 8_level_1'),
    #             (                            'BW in kg TI', 'Unnamed: 9_level_1'),
    #             ...
    #             (                         'Temperaturchip',             'POD4.1'),
    #             (                         'Temperaturchip',             'POD4.2'),
    #             (                         'Temperaturchip',               'POD5'),
    #             (                         'Temperaturchip',             'POD5.1'),
    #             (                         'Temperaturchip',             'POD5.2'),
    #             (                         'Temperaturchip',               'POD6'),
    #             (                         'Temperaturchip',             'POD6.1'),
    #             (                         'Temperaturchip',             'POD6.2'),
    #             (                         'Temperaturchip',               'POD7'),
    #             (                         'Temperaturchip',             'POD7.1')],
    #            length=916)

# %%

overview_2.columns[:44]
    # Out[13]: 
    # MultiIndex([(                             'Sample ID:',  'Unnamed: 0_level_1'),
    #             (                              'Treatment',  'Unnamed: 1_level_1'),
    #             (                                 'Group:',  'Unnamed: 2_level_1'),
    #             (                             'BW Eingang',  'Unnamed: 3_level_1'),
    #             (                                'Ear tag',  'Unnamed: 4_level_1'),
    #             (                     'Operation date Ti:',  'Unnamed: 5_level_1'),
    #             (          'Operation TI incisicion time:',  'Unnamed: 6_level_1'),
    #             ('Operation TI end time (wound closure): ',  'Unnamed: 7_level_1'),
    #             (                            'Duration TI',  'Unnamed: 8_level_1'),
    #             (                            'BW in kg TI',  'Unnamed: 9_level_1'),
    #             (                         'transponder ID', 'Unnamed: 10_level_1'),
    #             (                            'Surgeon NTx', 'Unnamed: 11_level_1'),
    #             (                  'Operation date Expl.:', 'Unnamed: 12_level_1'),
    #             (      'Operation Expl.  incisicion time:', 'Unnamed: 13_level_1'),
    #             (  'Operation Expl.  End (wound closure):', 'Unnamed: 14_level_1'),
    #             (                    'OP Expl. time [min]', 'Unnamed: 15_level_1'),
    #             (                'Cold Storage start time', 'Unnamed: 16_level_1'),
    #             (                  'Cold storage End time', 'Unnamed: 17_level_1'),
    #             (                      'Cold storage time', 'Unnamed: 18_level_1'),
    #             (                            'BW in kg Ex', 'Unnamed: 19_level_1'),
    #             (                  'Operation date Impl.:', 'Unnamed: 20_level_1'),
    #             (             'Operation incisision time:', 'Unnamed: 21_level_1'),
    #             (         'Operation end (wound closure):', 'Unnamed: 22_level_1'),
    #             (                          'OP time [min]', 'Unnamed: 23_level_1'),
    #             (                        'Blood loss (ml)', 'Unnamed: 24_level_1'),
    #             (                 'Anastomosis start time', 'Unnamed: 25_level_1'),
    #             (                   'Anastomosis end time', 'Unnamed: 26_level_1'),
    #             (                   'Anastomosis duration', 'Unnamed: 27_level_1'),
    #             (         'Impl. End of cold storage time', 'Unnamed: 28_level_1'),
    #             (        'Impl. Start of reperfusion time', 'Unnamed: 29_level_1'),
    #             (                     'warm ischemia time', 'Unnamed: 30_level_1'),
    #             (         'Control kidney sample in -80°C', 'Unnamed: 31_level_1'),
    #             (                           'BW in kg Imp', 'Unnamed: 32_level_1'),
    #             (   'Weight Kidney after Explantation [g]', 'Unnamed: 33_level_1'),
    #             (       'Weight Kidney after Flushing [g]', 'Unnamed: 34_level_1'),
    #             (        'Weight Kidney after storage [g]', 'Unnamed: 35_level_1'),
    #             (      'Weight Kidney after sacrifice [g]', 'Unnamed: 36_level_1'),
    #             (                         'Sacrifice date', 'Unnamed: 37_level_1'),
    #             (                            'BW in kg F:', 'Unnamed: 38_level_1'),
    #             (                          'Survival days', 'Unnamed: 39_level_1'),
    #             (                      'Surgeon sacrifice', 'Unnamed: 40_level_1'),
    #             (         'Kidney samples after sacrifice',           'Histology'),
    #             (         'Spleen samples after sacrifice',           'Histology'),
    #             (      'Lymphnode samples after sacrifice',           'Histology')],
    #            )

# %%    

print(list(overview_2.columns))

# %%
# %%


# %%

