

# %%'

histology\multiplex\Results Multiplex Ernst24 - August-WH.xlsx
multiplex = pd.read_excel( r'U:\kidney\histology\multiplex\Results Multiplex Ernst24 - August-WH.xlsx' , sheet_name=1 )  
    # , index_col=0 
    # , header=[0,1]

# %%'

multiplex.shape
    # Out[12]: (75, 68)


multiplex.iloc[:13,:4]
    # Out[14]: 
    #        Unnamed: 0                       ZC40                       ZC42  \
    # 0             NaN                DBD-Ecoflow                DBD-Ecoflow   
    # 1             NaN                       set1                       set1   
    # 2             NaN              5 colours F38              5 colours F38   
    # 3             NaN  slide 1 Zc40 - Region 002  Slide 2 Zc42 - Region 003   
    # 4             NaN  slide 1 Zc40 - Region 002  Slide 2 Zc42 - Region 003   
    # 5            Area                 289.569564                 384.897752   
    # 6        Zellzahl                    1250108                    1775207   
    # 7          HMGB1+                       2017                         56   
    # 8           NGal+                      40142                      84076   
    # 9          Casp3+                         47                         77   
    # 10          Zo-1+                       1224                        353   
    # 11      Syndecan+                       1045                       2316   
    # 12  HMGB1+ NGal+                         305                         54   
    
    #                          ZC49  
    # 0                 DBD-Ecoflow  
    # 1                        set1  
    # 2               5 colours F38  
    # 3   Slide 3 Zc49 - Region 004  
    # 4   Slide 3 Zc49 - Region 004  
    # 5                  237.515856  
    # 6                     1358316  
    # 7                         831  
    # 8                       39337  
    # 9                          18  
    # 10                       1948  
    # 11                        808  
    # 12                        383  


# note : dataframe columns can not be duplicate !
    # excel sheets have their built-in alphabetic columns that are always unique.
    # however, when importing to pandas, these alphabetic columns are not imported : the top row is set as column header.
    # Hence pandas automatically assigns suffixes to the duplicte column names : like : Zc22.1
multiplex.iloc[:13,-4:]
    # Out[16]: 
    #                        Zc21.1                     Zc22.1  \
    # 0                   Kontrolle                  Kontrolle   
    # 1                       set7b                      set7b   
    # 2               5 colours F38              5 colours F38   
    # 3   Slide 4 Zc21 - Region 005  Slide 5 Zc22 - Region 006   
    # 4   Slide 4 Zc21 - Region 005  Slide 5 Zc22 - Region 006   
    # 5                  198.890770                 246.451606   
    # 6                      971111                    1173585   
    # 7                         530                       1081   
    # 8                        6477                       4415   
    # 9                         586                        901   
    # 10                       1112                       1506   
    # 11                        994                       1602   
    # 12                         61                        276   
    
    #                        Zc29.1                     Zc30.1  
    # 0                   Kontrolle                  Kontrolle  
    # 1                       set7b                      set7b  
    # 2               5 colours F38              5 colours F38  
    # 3   Slide 6 Zc29 - Region 008  Slide 7 Zc30 - Region 009  
    # 4   Slide 6 Zc29 - Region 008  Slide 7 Zc30 - Region 009  
    # 5                  384.256080                 205.431771  
    # 6                     1594572                     750866  
    # 7                        4600                      10623  
    # 8                        9525                      12307  
    # 9                         589                        324  
    # 10                        206                        592  
    # 11                       2565                        312  
    # 12                       1470                       2740  


# this eliminates combinations of biomarkers.
multiplex_2 = multiplex.iloc[ :12 , : ]


multiplex_2.columns
    # Out[16]: 
    # Index(['Unnamed: 0', 'ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58',
    #        'ZC59', 'Unnamed: 9', 'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15',
    #        'ZC27', 'Unnamed: 17', 'ZC04', 'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37',
    #        'ZC38', 'Unnamed: 25', 'ZC24', 'ZC25', 'ZC26', 'ZC31', 'ZC32', 'ZC33',
    #        'ZC34', 'Unnamed: 33', 'ZC44', 'ZC46', 'ZC47', 'ZC48', 'ZC53', 'ZC55',
    #        'ZC56', 'Unnamed: 41', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65',
    #        'ZC66', 'ZC67', 'ZC68', 'ZC69', 'Unnamed: 52', 'Zc17', 'Zc19', 'Zc20',
    #        'Zc21', 'Zc22', 'Zc29', 'Zc30', 'Unnamed: 60', 'Zc17.1', 'Zc19.1',
    #        'Zc20.1', 'Zc21.1', 'Zc22.1', 'Zc29.1', 'Zc30.1'],
    #       dtype='object')


# %% drop blank columns

# there are some blank columns in the dataframe.
    # these columns also have no column name.
    # drop them.

# identify all Unnamed ( blank ) columns except the 1st one ('Unnamed: 0').
blank = [ col for col in multiplex_2.columns 
           if col.startswith("Unnamed") and col != "Unnamed: 0" ]

blank
    # Out[18]: 
    # ['Unnamed: 9',
    #  'Unnamed: 17',
    #  'Unnamed: 25',
    #  'Unnamed: 33',
    #  'Unnamed: 41',
    #  'Unnamed: 52',
    #  'Unnamed: 60']

# drop them
multiplex_3 = multiplex_2.drop( columns=blank )

multiplex_3.shape
# Out[20]: (12, 61)

multiplex_3.columns
    # Out[21]: 
    # Index(['Unnamed: 0', 'ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58',
    #        'ZC59', 'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15', 'ZC27', 'ZC04',
    #        'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC24', 'ZC25', 'ZC26',
    #        'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC44', 'ZC46', 'ZC47', 'ZC48', 'ZC53',
    #        'ZC55', 'ZC56', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66',
    #        'ZC67', 'ZC68', 'ZC69', 'Zc17', 'Zc19', 'Zc20', 'Zc21', 'Zc22', 'Zc29',
    #        'Zc30', 'Zc17.1', 'Zc19.1', 'Zc20.1', 'Zc21.1', 'Zc22.1', 'Zc29.1',
    #        'Zc30.1'],
    #       dtype='object')

# %% drop un-necessary rows.

# drop irrelevanty rows.
# note : the first row in the excel sheet ( zc-n ... ) is already automatically assigned as a column here.
    # so it's not row-0 : it has no row index ; it's a column.
multiplex_4 = multiplex_3.drop( index=[1,2,3,4] )

multiplex_4.iloc[ : , :2 ]
    # Out[26]: 
    #    Unnamed: 0         ZC40
    # 0         NaN  DBD-Ecoflow
    # 5        Area   289.569564
    # 6    Zellzahl      1250108
    # 7      HMGB1+         2017
    # 8       NGal+        40142
    # 9      Casp3+           47
    # 10      Zo-1+         1224
    # 11  Syndecan+         1045

# %%' transpose


# transpose
multiplex_5 = multiplex_4.T

multiplex_5.shape
    # Out[28]: (61, 8)


multiplex_5.iloc[:4]
    # Out[29]: 
    #                      0          5         6       7      8       9      10  \
    # Unnamed: 0          NaN       Area  Zellzahl  HMGB1+  NGal+  Casp3+  Zo-1+   
    # ZC40        DBD-Ecoflow 289.569564   1250108    2017  40142      47   1224   
    # ZC42        DBD-Ecoflow 384.897752   1775207      56  84076      77    353   
    # ZC49        DBD-Ecoflow 237.515856   1358316     831  39337      18   1948   
    
    #                    11  
    # Unnamed: 0  Syndecan+  
    # ZC40             1045  
    # ZC42             2316  
    # ZC49              808  


multiplex_5.columns
    # Out[32]: Index([0, 5, 6, 7, 8, 9, 10, 11], dtype='int64')

# note : first index is : Unnamed: 0
# wrong thought : the 1st row is the index of the parent dataframe.
# correct :  the columns are the index of the parent dataframe
    # multiplex_6 = multiplex_5.drop( index=0 )
        # KeyError: '[0] not found in axis'

# assigning new column names.

# 1) Lift the first row into the columns
new_cols = multiplex_5.iloc[0].tolist()  # take the first row

new_cols
    # Out[34]: [nan, 'Area', 'Zellzahl', 'HMGB1+', 'NGal+', 'Casp3+', 'Zo-1+', 'Syndecan+']


multiplex_5.columns = new_cols          # assign as new column names

multiplex_5[:4]
    # Out[36]: 
    #                     NaN       Area  Zellzahl  HMGB1+  NGal+  Casp3+  Zo-1+  \
    # Unnamed: 0          NaN       Area  Zellzahl  HMGB1+  NGal+  Casp3+  Zo-1+   
    # ZC40        DBD-Ecoflow 289.569564   1250108    2017  40142      47   1224   
    # ZC42        DBD-Ecoflow 384.897752   1775207      56  84076      77    353   
    # ZC49        DBD-Ecoflow 237.515856   1358316     831  39337      18   1948   
    
    #             Syndecan+  
    # Unnamed: 0  Syndecan+  
    # ZC40             1045  
    # ZC42             2316  
    # ZC49              808  


# 2) Drop that first row from the data
multiplex_6 = multiplex_5.drop( index='Unnamed: 0' )

# the index now is sample_IDs.
# you want sample_IDs to be a column, with the column name : sample_ID.
# Reset the row index to simple 0,1,2…
multiplex_6 = multiplex_6.reset_index()

multiplex_6[:4]
    # Out[44]: 
    #   index          NaN       Area Zellzahl HMGB1+  NGal+ Casp3+ Zo-1+ Syndecan+
    # 0  ZC40  DBD-Ecoflow 289.569564  1250108   2017  40142     47  1224      1045
    # 1  ZC42  DBD-Ecoflow 384.897752  1775207     56  84076     77   353      2316
    # 2  ZC49  DBD-Ecoflow 237.515856  1358316    831  39337     18  1948       808
    # 3  ZC50  DBD-Ecoflow 352.881449  2092334   1222   1533    537    34      5411

# further editing the columns.
new_cols_2 = [ 'sample_ID' , 'treatment' , 'area', 'cell_count', 'HMGB1+' , 'NGAL+' , 'Casp3+' , 'Zo-1+' , 'Syndecan+' ]

multiplex_6.columns = new_cols_2

multiplex_6[:4]
    # Out[47]: 
    #   sample_ID    treatment       Area cell_count HMGB1+  NGAL+ Casp3+ Zo-1+  \
    # 0      ZC40  DBD-Ecoflow 289.569564    1250108   2017  40142     47  1224   
    # 1      ZC42  DBD-Ecoflow 384.897752    1775207     56  84076     77   353   
    # 2      ZC49  DBD-Ecoflow 237.515856    1358316    831  39337     18  1948   
    # 3      ZC50  DBD-Ecoflow 352.881449    2092334   1222   1533    537    34   
    
    #   Syndecan+  
    # 0      1045  
    # 1      2316  
    # 2       808  
    # 3      5411  

# %%'

multiplex_6.to_pickle( r'U:\kidney\histology\multiplex\multiplex_6.pkl' )

# %%'

# to avoid dividsion by 0.
multiplex_6['cell_count'].min()
    # Out[52]: 26883

# %% %

# calculating the percentage of the number of cells containing each specific biomarker.

# list of biomarker‐count columns
biomarkers = ['HMGB1+', 'NGAL+', 'Casp3+', 'Zo-1+', 'Syndecan+']

# for each marker
for biom in biomarkers :
    pct_col = f"{biom}_%"             # percentage column : e.g. "HMGB1+_%"
    multiplex_6[pct_col] = ( multiplex_6[biom] / multiplex_6['cell_count'] ) * 100

# %%

multiplex_6.to_pickle( r'U:\kidney\histology\multiplex\multiplex_6.pkl' )

# %% *

# * : explore
    # unpacking

biomarkers_percentage = [ f"{b}_%" for b in biomarkers ]

biomarkers_percentage
    # Out[66]: ['HMGB1+_%', 'NGAL+_%', 'Casp3+_%', 'Zo-1+_%', 'Syndecan+_%']

# %%

# peek at the new columns
multiplex_6[[ *biomarkers , *biomarkers_percentage ]].head()
        # Out[61]: 
        #   HMGB1+  NGAL+ Casp3+ Zo-1+ Syndecan+ HMGB1+_%  NGAL+_% Casp3+_%  Zo-1+_%  \
        # 0   2017  40142     47  1224      1045 0.161346 3.211083 0.003760 0.097912   
        # 1     56  84076     77   353      2316 0.003155 4.736124 0.004338 0.019885   
        # 2    831  39337     18  1948       808 0.061179 2.896012 0.001325 0.143413   
        # 3   1222   1533    537    34      5411 0.058404 0.073267 0.025665 0.001625   
        # 4  12507  29540    622     4         6 1.276158 3.014129 0.063466 0.000408   
        
        #   Syndecan+_%  
        # 0    0.083593  
        # 1    0.130464  
        # 2    0.059485  
        # 3    0.258611  
        # 4    0.000612  
# without unpacking ( without pitting the star before the list ), I get the following error :
    # KeyError: "None of [Index([('HMGB1+', 'NGAL+', 'Casp3+', 'Zo-1+', 'Syndecan+')], dtype='object')] are in the [columns]"

# %%

# build the list of columns you want
selected_cols = ['sample_ID', 'treatment'] + biomarkers_percentage

# use .loc to select all rows and exactly those columns
multiplex_7 = multiplex_6.loc[ : , selected_cols]

multiplex_7.shape
    # Out[75]: (60, 7)

multiplex_7.head()
    # Out[72]: 
    #   sample_ID    treatment HMGB1+_%  NGAL+_% Casp3+_%  Zo-1+_% Syndecan+_%
    # 0      ZC40  DBD-Ecoflow 0.161346 3.211083 0.003760 0.097912    0.083593
    # 1      ZC42  DBD-Ecoflow 0.003155 4.736124 0.004338 0.019885    0.130464
    # 2      ZC49  DBD-Ecoflow 0.061179 2.896012 0.001325 0.143413    0.059485
    # 3      ZC50  DBD-Ecoflow 0.058404 0.073267 0.025665 0.001625    0.258611
    # 4      ZC51  DBD-Ecoflow 1.276158 3.014129 0.063466 0.000408    0.000612

# %%

multiplex_8 = pd.melt(
                        multiplex_7 ,
                        
                        id_vars=[ 'sample_ID' , 'treatment' ] ,
                        
                        value_vars = biomarkers_percentage ,
                        var_name = 'biomarker' ,
                        value_name = 'cnp'  # cell umber percentage
)

# %%

multiplex_8.shape
    # Out[74]: (300, 4)

multiplex_8[:4]
    # Out[76]: 
    #   sample_ID    treatment biomarker      cnp
    # 0      ZC40  DBD-Ecoflow  HMGB1+_% 0.161346
    # 1      ZC42  DBD-Ecoflow  HMGB1+_% 0.003155
    # 2      ZC49  DBD-Ecoflow  HMGB1+_% 0.061179
    # 3      ZC50  DBD-Ecoflow  HMGB1+_% 0.058404

# %%'

multiplex_8.to_pickle( r'U:\kidney\histology\multiplex\multiplex_8.pkl' )

# %%






