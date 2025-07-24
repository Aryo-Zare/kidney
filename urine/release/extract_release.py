

# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# %%

# column ranges of the data.
# preparation for later slicing.

begin = column_index_from_string("LZ") - 1
end = column_index_from_string("MO")

# %%

cols_to_keep = np.r_[ 0:3 , begin:end ] 

# bg : blood gass
df_release = overview_2.iloc[ : , cols_to_keep ]

# %%

df_release.shape
    # Out[42]: (82, 19)

df_release.iloc[:4,:4]
    # Out[43]: 
    #           Sample ID:          Treatment             Group:  \
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1   
    # 0               ZC04            DBD-HTK                  1   
    # 1               ZC05         DBD-Ecosol                  2   
    # 2               ZC06            DBD-HTK                  1   
    # 3               ZC07         DBD-Ecosol                  2   
    
    #   Urine release (Volume for sample=Urine release at noon)  
    #                                                      Impl  
    # 0                                                  -       
    # 1                                                  -       
    # 2                                                  -       
    # 3                                                  -    


df_release.iloc[:4,-4:]
    # Out[44]: 
    #   Urine release (Volume for sample=Urine release at noon)        \
    #                                       Volume for sample.5  POD7   
    # 0                                                200          -   
    # 1                                                950       1700   
    # 2                                                  -          -   
    # 3                                                400        500   
    
    #                                   Baseline  
    #   Volume for sample.6 Unnamed: 352_level_1  
    # 0                   -                    -  
    # 1                1700                    -  
    # 2                   -                    -  
    # 3                 500                    -  

# %%

df_release_2 = df_release.set_index( [('Sample ID:', 'Unnamed: 0_level_1'),
                            ( 'Treatment', 'Unnamed: 1_level_1'),
                            (    'Group:', 'Unnamed: 2_level_1')] )

# %%

df_release_2.iloc[:4 , :2]
    # Out[46]: 
    #                                                                                               Urine release (Volume for sample=Urine release at noon)  \
    #                                                                                                                                                  Impl   
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)                                                           
    # ZC04                             DBD-HTK                         1                                                                             -        
    # ZC05                             DBD-Ecosol                      2                                                                             -        
    # ZC06                             DBD-HTK                         1                                                                             -        
    # ZC07                             DBD-Ecosol                      2                                                                             -        
    
                                                                                                         
    #                                                                                                POD1  
    # (Sample ID:, Unnamed: 0_level_1) (Treatment, Unnamed: 1_level_1) (Group:, Unnamed: 2_level_1)        
    # ZC04                             DBD-HTK                         1                                -  
    # ZC05                             DBD-Ecosol                      2                              750  
    # ZC06                             DBD-HTK                         1                              300  
    # ZC07                             DBD-Ecosol                      2                             1400  

# %%

# --- Renaming the index levels ---
new_index_names = ['sample_ID', 'treatment', 'group']

df_release_2.index.set_names( new_index_names, inplace=True ) # Use inplace=True to modify directly

df_release_2.iloc[ :4 , :4 ]
    # Out[48]: 
    #                            Urine release (Volume for sample=Urine release at noon)  \
    #                                                                               Impl   
    # sample_ID treatment  group                                                           
    # ZC04      DBD-HTK    1                                                      -        
    # ZC05      DBD-Ecosol 2                                                      -        
    # ZC06      DBD-HTK    1                                                      -        
    # ZC07      DBD-Ecosol 2                                                      -        
    
                                                              
    #                             POD1 Volume for sample  POD2  
    # sample_ID treatment  group                                
    # ZC04      DBD-HTK    1         -               100   110  
    # ZC05      DBD-Ecosol 2       750               500  1700  
    # ZC06      DBD-HTK    1       300               300  1450  
    # ZC07      DBD-Ecosol 2      1400               600  3700 

# %%

df_release_2.columns
    # Out[49]: 
    # MultiIndex([('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             ('Urine release (Volume for sample=Urine release at noon)', ...),
    #             (                                               'Baseline', ...)],
    #            )


for i,j in df_release_2.columns :
    print( f' {i} & {j}' )
     # Urine release (Volume for sample=Urine release at noon) & Impl
     # Urine release (Volume for sample=Urine release at noon) & POD1
     # Urine release (Volume for sample=Urine release at noon) & Volume for sample
     # Urine release (Volume for sample=Urine release at noon) & POD2
     # Urine release (Volume for sample=Urine release at noon) & Volume for sample.1
     # Urine release (Volume for sample=Urine release at noon) & POD3
     # Urine release (Volume for sample=Urine release at noon) & Volume for sample.2
     # Urine release (Volume for sample=Urine release at noon) & POD4
     # Urine release (Volume for sample=Urine release at noon) & Volume for sample.3
     # Urine release (Volume for sample=Urine release at noon) & POD5
     # Urine release (Volume for sample=Urine release at noon) & Volume for sample.4
     # Urine release (Volume for sample=Urine release at noon) & POD6
     # Urine release (Volume for sample=Urine release at noon) & Volume for sample.5
     # Urine release (Volume for sample=Urine release at noon) & POD7
     # Urine release (Volume for sample=Urine release at noon) & Volume for sample.6
     # Baseline & Unnamed: 352_level_1
 
# %%

# tuples, to later be used for the multi-index.
tups = [
            (
                'release' ,      # Level 0: remove "BGA " prefix
                col1      # Level 1: if not "pH", keep only the analyte name (first part)
            )
        for col0 , col1 in df_release_2.columns
]


tups
    # Out[55]: 
    # [('release', 'Impl'),
    #  ('release', 'POD1'),
    #  ('release', 'Volume for sample'),
    #  ('release', 'POD2'),
    #  ('release', 'Volume for sample.1'),
    #  ('release', 'POD3'),
    #  ('release', 'Volume for sample.2'),
    #  ('release', 'POD4'),
    #  ('release', 'Volume for sample.3'),
    #  ('release', 'POD5'),
    #  ('release', 'Volume for sample.4'),
    #  ('release', 'POD6'),
    #  ('release', 'Volume for sample.5'),
    #  ('release', 'POD7'),
    #  ('release', 'Volume for sample.6'),
    #  ('release', 'Unnamed: 352_level_1')]

# %%

# Using a list comprehension to reconstruct the MultiIndex
df_release_2.columns = pd.MultiIndex.from_tuples( tups )

# %%

df_release_3 = df_release_2.stack( level=[0,1] , dropna=False , sort=False )

df_release_3.shape
    # Out[58]: (1312,)

df_release_3[:4]
    # Out[59]: 
    # sample_ID  treatment  group                            
    # ZC04       DBD-HTK    1      release  Impl                   -
    #                                       POD1                   -
    #                                       Volume for sample    100
    #                                       POD2                 110
    # dtype: object

df_release_4 = df_release_3.reset_index()

df_release_4[:4]
    # Out[61]: 
    #   sample_ID treatment group  level_3            level_4    0
    # 0      ZC04   DBD-HTK     1  release               Impl    -
    # 1      ZC04   DBD-HTK     1  release               POD1    -
    # 2      ZC04   DBD-HTK     1  release  Volume for sample  100
    # 3      ZC04   DBD-HTK     1  release               POD2  110

df_release_4.rename(columns= {
                                    'level_3' : 'metric' ,
                                    'level_4' : 'time' ,
                                    0 : 'value'
                                } ,
                        inplace=True )


df_release_4[:4]
    # Out[64]: 
    #   sample_ID treatment group   metric               time value
    # 0      ZC04   DBD-HTK     1  release               Impl     -
    # 1      ZC04   DBD-HTK     1  release               POD1     -
    # 2      ZC04   DBD-HTK     1  release  Volume for sample   100
    # 3      ZC04   DBD-HTK     1  release               POD2   110

# %%

df_release_4['time'].unique()
    # Out[65]: 
    # array(['Impl', 'POD1', 'Volume for sample', 'POD2', 'Volume for sample.1',
    #        'POD3', 'Volume for sample.2', 'POD4', 'Volume for sample.3',
    #        'POD5', 'Volume for sample.4', 'POD6', 'Volume for sample.5',
    #        'POD7', 'Volume for sample.6', 'Unnamed: 352_level_1'],
    #       dtype=object)

df_release_4['metric'].unique()
    # Out[66]: array(['release'], dtype=object)

# %%

# removing un-wanted entities !
mask = ~df_release_4['time'].str.contains( 'Volume', na=False )

df_release_5 = df_release_4[ mask ]

df_release_5['time'].unique()
    # Out[69]: 
    # array(['Impl', 'POD1', 'POD2', 'POD3', 'POD4', 'POD5', 'POD6', 'POD7',
    #        'Unnamed: 352_level_1'], dtype=object)

df_release_5['time'] = df_release_5['time'].replace( {'Unnamed: 352_level_1': 'baseline'} )

# df_release_5['time'].replace( {'Unnamed: 352_level_1': 'baseline'} , inplace=True )
# warning : if doing it directly with : inplace=True
    # The behavior will change in pandas 3.0. 
    # This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    # For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


df_release_5['time'].unique()
    # Out[78]: 
    # array(['Impl', 'POD1', 'POD2', 'POD3', 'POD4', 'POD5', 'POD6', 'POD7',
    #        'baseline'], dtype=object)

# %%

df_release_5.to_pickle( r'U:\kidney\urine\density\df_release_5.pkl' )


# %%


