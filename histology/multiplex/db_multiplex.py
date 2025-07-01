

# %%

multiplex_8 = pd.read_pickle( r'U:\kidney\histology\multiplex\multiplex_8.pkl' )

# %%

multiplex_8.shape
    # Out[9]: (300, 4)


multiplex_8[:4]
    #   sample_ID    treatment biomarker      cnp
    # 0      ZC40  DBD-Ecoflow  HMGB1+_% 0.161346
    # 1      ZC42  DBD-Ecoflow  HMGB1+_% 0.003155
    # 2      ZC49  DBD-Ecoflow  HMGB1+_% 0.061179
    # 3      ZC50  DBD-Ecoflow  HMGB1+_% 0.058404

# %%

# non-standard NAN like '-' are enforced to comply with pandas NA !
multiplex_8['cnp'] = pd.to_numeric( multiplex_8['cnp'] , errors='coerce' )

multiplex_8.isna().sum()
    # Out[12]: 
    # sample_ID     0
    # treatment     0
    # biomarker     0
    # cnp          15
    # dtype: int64

# %%

# drop NA
multiplex_9 = multiplex_8.dropna().reset_index(drop=True) 

# %%

multiplex_9['sample_ID'].unique()
    # Out[14]: 
    # array(['ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58', 'ZC59',
    #        'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15', 'ZC27', 'ZC04',
    #        'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC24', 'ZC25',
    #        'ZC26', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC44', 'ZC47', 'ZC48',
    #        'ZC53', 'ZC55', 'ZC56', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC65',
    #        'ZC66', 'ZC67', 'ZC68', 'Zc17', 'Zc19', 'Zc20', 'Zc21', 'Zc22',
    #        'Zc29', 'Zc30', 'Zc17.1', 'Zc19.1', 'Zc20.1', 'Zc21.1', 'Zc22.1',
    #        'Zc29.1', 'Zc30.1'], dtype=object)


# note : 'Kontrolle' is new !
multiplex_9['treatment'].unique()
    # Out[17]: 
    # array(['DBD-Ecoflow', 'DBD-Ecosol', 'DBD-HTK', 'DCD-Ecoflow',
    #        'DCD-Ecosol', 'NMP', 'Kontrolle'], dtype=object)

multiplex_9['biomarker'].unique()
    # Out[18]: 
    # array(['HMGB1+_%', 'NGAL+_%', 'Casp3+_%', 'Zo-1+_%', 'Syndecan+_%'],
    #       dtype=object)

# %%

# wrong :
    # multiplex_9['sample_ID'] = multiplex_9['sample_ID'].replace({'Zc': 'ZC'})
        # .replace evaluates whole words, not part of them.
        # Hence, nothing would happen after running the above command.

# %%

# example
multiplex_10 = multiplex_9.copy()

# vectorized cleanup
# the parenthesis is only for more clear expression :
    # splitting the line & indentation.
multiplex_10['sample_ID'] = (
                                multiplex_10['sample_ID']
                                  .str.upper()                    # make everything uppercase
                                  .replace( r'\..*$' , '' , regex=True )  # drop dot-suffix and everything after
)

# %%

multiplex_10['sample_ID'].unique()
    # Out[22]: 
    # array(['ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58', 'ZC59',
    #        'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15', 'ZC27', 'ZC04',
    #        'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC24', 'ZC25',
    #        'ZC26', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC44', 'ZC47', 'ZC48',
    #        'ZC53', 'ZC55', 'ZC56', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC65',
    #        'ZC66', 'ZC67', 'ZC68', 'ZC17', 'ZC19', 'ZC20', 'ZC21', 'ZC22',
    #        'ZC29', 'ZC30'], dtype=object)

# %%

multiplex_10.to_pickle( r'U:\kidney\histology\multiplex\multiplex_10.pkl' )


# %%'  filter

# filter based on treatment, sample_ID & time.

# 'ZC6' is ony converted to 'ZC06'.
mask = \
        ( multiplex_10["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~multiplex_10["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) 


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
multiplex_11 = multiplex_10[ mask ]

# %%

multiplex_11.shape
    # Out[25]: (90, 4)

# %%'  order

# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
multiplex_11['treatment'] = pd.Categorical(
                                                multiplex_11['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


# od : ordered
biomarker_order = [ 'HMGB1+_%' , 'NGAL+_%' , 'Casp3+_%' , 'Zo-1+_%' , 'Syndecan+_%' ]
multiplex_11['biomarker'] = pd.Categorical( 
                                            multiplex_11['biomarker'] , 
                                            categories=biomarker_order , 
                                            ordered=True 
)

# %%

multiplex_11['treatment'].unique()
    # Out[27]: 
    # ['DBD-Ecosol', 'DBD-HTK', 'NMP']
    # Categories (3, object): ['DBD-HTK' < 'DBD-Ecosol' < 'NMP']

multiplex_11['biomarker'].unique()
    # Out[28]: 
    # ['HMGB1+_%', 'NGAL+_%', 'Casp3+_%', 'Zo-1+_%', 'Syndecan+_%']
    # Categories (5, object): ['HMGB1+_%' < 'NGAL+_%' < 'Casp3+_%' < 'Zo-1+_%' < 'Syndecan+_%']

# %%

multiplex_11.to_pickle( r'U:\kidney\histology\multiplex\multiplex_11.pkl' )


# %% compatibility for the statistical program

# this is only to make it compatible for the statistical program.

multiplex_11_stat = multiplex_11.copy()

multiplex_11_stat['metric'] = 'multiplex'

multiplex_11_stat.rename( columns={ "biomarker": "time" , 'cnp':'value' } , inplace=True )


# %%

multiplex_11_stat[:4]
    # Out[59]: 
    #    sample_ID   treatment      time    value     metric
    # 8       ZC05  DBD-Ecosol  HMGB1+_% 0.529383  multiplex
    # 9       ZC07  DBD-Ecosol  HMGB1+_% 0.165114  multiplex
    # 10      ZC09  DBD-Ecosol  HMGB1+_% 0.227194  multiplex
    # 11      ZC11  DBD-Ecosol  HMGB1+_% 0.062555  multiplex

# %%

multiplex_11_stat = yjt( df=multiplex_11_stat , source_column='value' )

# %%

multiplex_11_stat[:4]
    # Out[84]: 
    #    sample_ID   treatment      time    value     metric  value_yjt
    # 8       ZC05  DBD-Ecosol  HMGB1+_% 0.529383  multiplex   0.295406
    # 9       ZC07  DBD-Ecosol  HMGB1+_% 0.165114  multiplex   0.133325
    # 10      ZC09  DBD-Ecosol  HMGB1+_% 0.227194  multiplex   0.170775
    # 11      ZC11  DBD-Ecosol  HMGB1+_% 0.062555  multiplex   0.057432

# %%

multiplex_11_stat.to_pickle( r'U:\kidney\histology\multiplex\multiplex_11_stat.pkl' )

# %%



