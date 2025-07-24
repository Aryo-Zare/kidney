

# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'U:\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# %%

# column ranges of the data.
# preparation for later slicing.

begin = column_index_from_string("AEG") - 1
end = column_index_from_string("AFN")

# %%

cols_to_keep = np.r_[ 0:3 , begin:end ] 

# bg : blood gass
df_ELISA = overview_2.iloc[ : , cols_to_keep ]

# %%

df_ELISA.shape
    # Out[10]: (82, 37)


df_ELISA.iloc[:4,:4]
    # Out[11]: 
    #           Sample ID:          Treatment             Group:  \
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1   
    # 0               ZC04            DBD-HTK                  1   
    # 1               ZC05         DBD-Ecosol                  2   
    # 2               ZC06            DBD-HTK                  1   
    # 3               ZC07         DBD-Ecosol                  2   
    
    #   ELISA KIM-1 ng/ml Sensitivitätsgrenze 0.094ng/ml, min. Standard 0,156ng/ml Werte neu berechnet Proben aus Urin  
    #                                                                                                             Expl  
    # 0                                                  -                                                              
    # 1                                           0.270281                                                              
    # 2                                                  -                                                              
    # 3                                           1.285325                                                              

# %%

df_ELISA.iloc[: , :3].columns
    # Out[12]: 
    # MultiIndex([('Sample ID:', 'Unnamed: 0_level_1'),
    #             ( 'Treatment', 'Unnamed: 1_level_1'),
    #             (    'Group:', 'Unnamed: 2_level_1')],
    #            )


df_ELISA_2 = df_ELISA.set_index( [('Sample ID:', 'Unnamed: 0_level_1'),
                            ( 'Treatment', 'Unnamed: 1_level_1'),
                            (    'Group:', 'Unnamed: 2_level_1')] )


# --- Renaming the index levels ---
new_index_names = ['sample_ID', 'treatment', 'group']

df_ELISA_2.index.set_names( new_index_names, inplace=True ) # Use inplace=True to modify directly

df_ELISA_2.iloc[:4 , :2]
    # Out[17]: 
    #                            ELISA KIM-1 ng/ml Sensitivitätsgrenze 0.094ng/ml, min. Standard 0,156ng/ml Werte neu berechnet Proben aus Urin  \
    #                                                                                                                                      Expl   
    # sample_ID treatment  group                                                                                                                  
    # ZC04      DBD-HTK    1                                                      -                                                               
    # ZC05      DBD-Ecosol 2                                               0.270281                                                               
    # ZC06      DBD-HTK    1                                                      -                                                               
    # ZC07      DBD-Ecosol 2                                               1.285325                                                               
    
                                        
    #                            Impl Z3  
    # sample_ID treatment  group          
    # ZC04      DBD-HTK    1           -  
    # ZC05      DBD-Ecosol 2           -  
    # ZC06      DBD-HTK    1           -  
    # ZC07      DBD-Ecosol 2           -  

# %%

df_ELISA_2.columns
# saved in : columns .txt : in this folder.

# %%

# bottom level column labels.
df_ELISA.columns.get_level_values(1)
    # Out[53]: 
    # Index(['Unnamed: 0_level_1', 'Unnamed: 1_level_1', 'Unnamed: 2_level_1',
    #        'Expl', 'Impl Z3', 'POD 1', 'POD 2', 'POD 3', 'POD 4', 'POD 5', 'POD 6',
    #        'POD 7', 'Expl', 'Impl Z1', 'Impl Z3', 'POD 1', 'POD 2', 'POD 3',
    #        'POD 7', 'Expl', 'Impl Z1', 'Impl Z3', 'POD 1', 'POD2', 'POD 3',
    #        'Impl Z1', 'Impl Z3', 'POD 1', 'POD 2', 'POD 3 ', 'POD 7', 'Expl',
    #        'Impl Z1', 'Impl Z3', 'POD 1', 'POD 3', 'POD 7'],
    #       dtype='object')

# %%

'''

        Suppose the columns you want to fix are in the top level of a MultiIndex:
        let's assume df_ELISA_2 is your DataFrame and its top-level columns are verbose:
        For example, df_ELISA_2.columns might look like:
        MultiIndex([('Some verbose text with KIM-1 included', '...'),
                    ('Other text with NGAL somewhere', '...'),
                    ...])

        
        I want to replacce any verbose sentence containing any of my keywords to only that keyword !

'''


# %%

# import re

# List of biomarkers to detect.
biomarkers = ["KIM-1", "NGAL", "pi-GST", "IL-6", "TNF-alpha"]

# Build a regex pattern that matches any of them.
# "|" is a pipe : it's in italics due to being inside a a double cuote ( string ).
    # hence, it may look like a : /
pattern = r"(" + "|".join(map(re.escape, biomarkers)) + r")"

pattern
    # Out[24]: '(KIM\\-1|NGAL|pi\\-GST|IL\\-6|TNF\\-alpha)'

# %%

# explore

re.escape
    # Out[25]: <function re.escape(pattern)>

re.escape('qerq')
    # Out[27]: 'qerq'


"|".join(map(re.escape, biomarkers))
    # Out[32]: 'KIM\\-1|NGAL|pi\\-GST|IL\\-6|TNF\\-alpha'

# %%

# label : column name
def replace_with_biomarker(label):
    """
    Searches for any of the specified biomarkers in the given text.
    If a match is found, return that biomarker; otherwise, return the original.
    """
    match = re.search( pattern, label )
    if match:
        return match.group(1)
    else:
        return label

# %%

# explore

re.search( pattern, 'ELISA TNF-alpha minimaler Standard 31,25pg/ml, Sensitivitätsgrenze')
    # Out[29]: <re.Match object; span=(6, 15), match='TNF-alpha'>

test = re.search( pattern, 'ELISA TNF-alpha minimaler Standard 31,25pg/ml, Sensitivitätsgrenze')

test
    # Out[34]: <re.Match object; span=(6, 15), match='TNF-alpha'>

test.group(1)
    # Out[35]: 'TNF-alpha'

# %%

# explore
# no natch !

# no output !!
re.search( pattern, 'no match included here')

test_2 = re.search( pattern, 'no match included here')

test_2

type( test_2 )
    # Out[46]: NoneType

# %%

# Suppose the columns you want to fix are in the top level of a MultiIndex:
# For demonstration, let's assume df_urine is your DataFrame and its top-level columns are verbose:
# For example, df_urine.columns might look like:
# MultiIndex([('Some verbose text with KIM-1 included', '...'),
#             ('Other text with NGAL somewhere', '...'),
#             ...])


new_top_level = [ replace_with_biomarker(label) for label in df_ELISA_2.columns.get_level_values(0) ]

# %%

def clean_bottom_label(label):
    # First, replace 'Expl' (exact match) with 'Explantation'
    if label.strip() == 'Expl':
        label = 'Explantation'
    # Then replace all spaces with underscores
    label = label.replace(" ", "_")
    return label

# %%

# Apply cleaning to bottom levels
new_bottom_level = [ clean_bottom_label(label) for label in df_ELISA_2.columns.get_level_values(1) ]

# %%

# Rebuild the MultiIndex
df_ELISA_2.columns = pd.MultiIndex.from_arrays([ new_top_level , new_bottom_level ])

# %%

df_ELISA_2.columns
    # Out[52]: 
    # MultiIndex([(    'KIM-1', 'Explantation'),
    #             (    'KIM-1',      'Impl_Z3'),
    #             (    'KIM-1',        'POD_1'),
    #             (    'KIM-1',        'POD_2'),
    #             (    'KIM-1',        'POD_3'),
    #             (    'KIM-1',        'POD_4'),
    #             (    'KIM-1',        'POD_5'),
    #             (    'KIM-1',        'POD_6'),
    #             (    'KIM-1',        'POD_7'),
    #             (     'NGAL', 'Explantation'),
    #             (     'NGAL',      'Impl_Z1'),
    #             (     'NGAL',      'Impl_Z3'),
    #             (     'NGAL',        'POD_1'),
    #             (     'NGAL',        'POD_2'),
    #             (     'NGAL',        'POD_3'),
    #             (     'NGAL',        'POD_7'),
    #             (   'pi-GST', 'Explantation'),
    #             (   'pi-GST',      'Impl_Z1'),
    #             (   'pi-GST',      'Impl_Z3'),
    #             (   'pi-GST',        'POD_1'),
    #             (   'pi-GST',         'POD2'),
    #             (   'pi-GST',        'POD_3'),
    #             (     'IL-6',      'Impl_Z1'),
    #             (     'IL-6',      'Impl_Z3'),
    #             (     'IL-6',        'POD_1'),
    #             (     'IL-6',        'POD_2'),
    #             (     'IL-6',       'POD_3_'),
    #             (     'IL-6',        'POD_7'),
    #             ('TNF-alpha', 'Explantation'),
    #             ('TNF-alpha',      'Impl_Z1'),
    #             ('TNF-alpha',      'Impl_Z3'),
    #             ('TNF-alpha',        'POD_1'),
    #             ('TNF-alpha',        'POD_3'),
    #             ('TNF-alpha',        'POD_7')],
    #            )

# %%

new_bottom_level
Out[56]: 
    # ['Explantation',
    #  'Impl_Z3',
    #  'POD_1',
    #  'POD_2',
    #  'POD_3',
    #  'POD_4',
    #  'POD_5',
    #  'POD_6',
    #  'POD_7',
    #  'Explantation',
    #  'Impl_Z1',
    #  'Impl_Z3',
    #  'POD_1',
    #  'POD_2',
    #  'POD_3',
    #  'POD_7',
    #  'Explantation',
    #  'Impl_Z1',
    #  'Impl_Z3',
    #  'POD_1',
    #  'POD2',
    #  'POD_3',
    #  'Impl_Z1',
    #  'Impl_Z3',
    #  'POD_1',
    #  'POD_2',
    #  'POD_3_',
    #  'POD_7',
    #  'Explantation',
    #  'Impl_Z1',
    #  'Impl_Z3',
    #  'POD_1',
    #  'POD_3',
    #  'POD_7']


# manual cleaning the rest of the mess from the bottom-level labels !
new_bottom_level_2 = ['Explantation',
 'Impl_Z3',
 'POD_1',
 'POD_2',
 'POD_3',
 'POD_4',
 'POD_5',
 'POD_6',
 'POD_7',
 'Explantation',
 'Impl_Z1',
 'Impl_Z3',
 'POD_1',
 'POD_2',
 'POD_3',
 'POD_7',
 'Explantation',
 'Impl_Z1',
 'Impl_Z3',
 'POD_1',
 'POD_2',
 'POD_3',
 'Impl_Z1',
 'Impl_Z3',
 'POD_1',
 'POD_2',
 'POD_3',
 'POD_7',
 'Explantation',
 'Impl_Z1',
 'Impl_Z3',
 'POD_1',
 'POD_3',
 'POD_7'
 ]

# %%

df_ELISA_2.columns = pd.MultiIndex.from_arrays([ new_top_level , new_bottom_level_2 ])

# %%

df_ELISA_2.columns
    # Out[59]: 
    # MultiIndex([(    'KIM-1', 'Explantation'),
    #             (    'KIM-1',      'Impl_Z3'),
    #             (    'KIM-1',        'POD_1'),
    #             (    'KIM-1',        'POD_2'),
    #             (    'KIM-1',        'POD_3'),
    #             (    'KIM-1',        'POD_4'),
    #             (    'KIM-1',        'POD_5'),
    #             (    'KIM-1',        'POD_6'),
    #             (    'KIM-1',        'POD_7'),
    #             (     'NGAL', 'Explantation'),
    #             (     'NGAL',      'Impl_Z1'),
    #             (     'NGAL',      'Impl_Z3'),
    #             (     'NGAL',        'POD_1'),
    #             (     'NGAL',        'POD_2'),
    #             (     'NGAL',        'POD_3'),
    #             (     'NGAL',        'POD_7'),
    #             (   'pi-GST', 'Explantation'),
    #             (   'pi-GST',      'Impl_Z1'),
    #             (   'pi-GST',      'Impl_Z3'),
    #             (   'pi-GST',        'POD_1'),
    #             (   'pi-GST',        'POD_2'),
    #             (   'pi-GST',        'POD_3'),
    #             (     'IL-6',      'Impl_Z1'),
    #             (     'IL-6',      'Impl_Z3'),
    #             (     'IL-6',        'POD_1'),
    #             (     'IL-6',        'POD_2'),
    #             (     'IL-6',        'POD_3'),
    #             (     'IL-6',        'POD_7'),
    #             ('TNF-alpha', 'Explantation'),
    #             ('TNF-alpha',      'Impl_Z1'),
    #             ('TNF-alpha',      'Impl_Z3'),
    #             ('TNF-alpha',        'POD_1'),
    #             ('TNF-alpha',        'POD_3'),
    #             ('TNF-alpha',        'POD_7')],
    #            )

# %%

df_ELISA_2.to_pickle( r'U:\kidney\ELISA\df_ELISA_2.pkl' )


# %%

# If it's a MultiIndex and you only want to modify the top-level:
# as I know already that the columns of the dataframe is multi-index, : if isinstance : is not needed !!

# if isinstance(df_urine_2.columns, pd.MultiIndex):
#     new_top_level = [replace_with_biomarker(col) for col in df_urine_2.columns.get_level_values(0)]
#     # Leave the bottom level unchanged:
#     new_bottom_level = df_urine_2.columns.get_level_values(1)
#     df_urine_2.columns = pd.MultiIndex.from_arrays([new_top_level, new_bottom_level])
# else:
#     # If you simply have a single-level index, update all column names.
#     df_urine_2.columns = [replace_with_biomarker(col) for col in df_urine_2.columns]


# %%

df_ELISA_3 = df_ELISA_2.stack( level=[0,1] , dropna=False , sort=False )

df_ELISA_3.shape
    # Out[62]: (4100,)

df_ELISA_3[:4]
    # Out[63]: 
    # sample_ID  treatment  group                     
    # ZC04       DBD-HTK    1      KIM-1  Explantation    -
    #                                     Impl_Z3         -
    #                                     POD_1           -
    #                                     POD_2           -
    # dtype: object

df_ELISA_4 = df_ELISA_3.reset_index()

df_ELISA_4[:4]
    # Out[66]: 
    #   sample_ID treatment group level_3       level_4  0
    # 0      ZC04   DBD-HTK     1   KIM-1  Explantation  -
    # 1      ZC04   DBD-HTK     1   KIM-1       Impl_Z3  -
    # 2      ZC04   DBD-HTK     1   KIM-1         POD_1  -
    # 3      ZC04   DBD-HTK     1   KIM-1         POD_2  -


df_ELISA_4.rename(columns= {
                                    'level_3' : 'metric' ,
                                    'level_4' : 'time' ,
                                    0 : 'value'
                                } ,
                        inplace=True )


df_ELISA_4[:4]
    # Out[69]: 
    #   sample_ID treatment group metric          time value
    # 0      ZC04   DBD-HTK     1  KIM-1  Explantation     -
    # 1      ZC04   DBD-HTK     1  KIM-1       Impl_Z3     -
    # 2      ZC04   DBD-HTK     1  KIM-1         POD_1     -
    # 3      ZC04   DBD-HTK     1  KIM-1         POD_2     -

# %%

df_ELISA_4['treatment'].unique()
    # Out[70]: 
    # array(['DBD-HTK', 'DBD-Ecosol', '-', 'DCD-HTK', 'DCD-Ecoflow', 'TBB',
    #        'DBD-Ecoflow', 'DCD-Ecosol', 'NMP', nan], dtype=object)

df_ELISA_4['time'].unique()
    # Out[71]: 
    # array(['Explantation', 'Impl_Z3', 'POD_1', 'POD_2', 'POD_3', 'POD_4',
    #        'POD_5', 'POD_6', 'POD_7', 'Impl_Z1'], dtype=object)

df_ELISA_4['metric'].unique()
    # Out[72]: array(['KIM-1', 'NGAL', 'pi-GST', 'IL-6', 'TNF-alpha'], dtype=object)

# `/
df_ELISA_4['sample_ID'].unique()
    # Out[73]: 
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

df_ELISA_4.to_pickle( r'U:\kidney\ELISA\df_ELISA_4.pkl' )


# %%

