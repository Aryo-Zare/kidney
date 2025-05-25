
# reformatting the dataset

# %%

from openpyxl.utils import column_index_from_string

# %%

overview = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )

overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )


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
begin = column_index_from_string("AT") - 1
end = column_index_from_string("EN")

# %%

# Option 2: Using numpy's r_ to slice and concatenate the indices:
cols_to_keep = np.r_[0:3, begin:end]  # np.r_ concatenates slices and arrays

cols_to_keep[-2:]
    # Out[12]: array([142, 143])

df_serum_chem = overview.iloc[:, cols_to_keep]

df_serum_chem.shape
    # Out[25]: (82, 102)

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

df_serum_chem_4.to_csv( r'U:\kidney\df_serum_chem.csv' )

# %%


# %%
# %%



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


overview_2 = pd.read_excel( r'U:\kidney\overview.xlsx' , header=[0,1] )

overview_2.shape
    # Out[16]: (82, 916)

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

    
print(list(overview_2.columns))

# %%

