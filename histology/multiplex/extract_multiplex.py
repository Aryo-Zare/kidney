

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

# %% transpose


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

# %%%'

# calculating the percentage of the number of cells containing each specific biomarker.

# list of biomarker‐count columns
biomarkers = ['HMGB1+', 'NGAL+', 'Casp3+', 'Zo-1+', 'Syndecan+']

# for each marker
for biom in biomarkers :
    pct_col = f"{biom}_%"             # percentage column : e.g. "HMGB1+_%"
    multiplex_6[pct_col] = ( multiplex_6[biom] / multiplex_6['cell_count'] ) * 100

# %%'

multiplex_6.to_pickle( r'U:\kidney\histology\multiplex\multiplex_6.pkl' )
multiplex_6 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_6.pkl' )


# %% *

# * : explore
    # unpacking

biomarkers_percentage = [ f"{b}_%" for b in biomarkers ]

biomarkers_percentage
    # Out[66]: ['HMGB1+_%', 'NGAL+_%', 'Casp3+_%', 'Zo-1+_%', 'Syndecan+_%']

# %%'

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

# %% multiplex_7

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

# %%'

multiplex_7.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_7.pkl' )

multiplex_7 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_7.pkl' )


# %% correlation

# this calculates the correlaion between individual biomarkers.
    # irrespective of groupings.

# via pandas
    # no p-value !
corr = multiplex_7[ biomarkers_percentage ].corr(method="spearman")

corr
    # Out[21]: 
    #              HMGB1+_%   NGAL+_%  Casp3+_%   Zo-1+_%  Syndecan+_%
    # HMGB1+_%     1.000000  0.139033  0.177729 -0.083225    -0.027873
    # NGAL+_%      0.139033  1.000000 -0.067993 -0.147135     0.101770
    # Casp3+_%     0.177729 -0.067993  1.000000  0.202554     0.235042
    # Zo-1+_%     -0.083225 -0.147135  0.202554  1.000000     0.121411
    # Syndecan+_% -0.027873  0.101770  0.235042  0.121411     1.000000


corr.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\corr.pkl' )
corr.to_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\correlation\correlation_individual_biomarkers.xlsx' )


# %%%'

from scipy.stats import spearmanr

# %%%'


multiplex_7.dtypes
    # Out[20]: 
    # sample_ID      object
    # treatment      object
    # HMGB1+_%       object
    # NGAL+_%        object
    # Casp3+_%       object
    # Zo-1+_%        object
    # Syndecan+_%    object
    # dtype: object

# the object-type is a problem for using spearmanr !
# biomarkers_percentage  : your list of marker columns
data = multiplex_7[biomarkers_percentage].apply(
    pd.to_numeric, errors="coerce"
)


data.dtypes
    # Out[22]: 
    # HMGB1+_%       float64
    # NGAL+_%        float64
    # Casp3+_%       float64
    # Zo-1+_%        float64
    # Syndecan+_%    float64
    # dtype: object

# %%%'

# extracting the p-values.

# Initialize matrices
corr = pd.DataFrame(index=biomarkers_percentage, columns=biomarkers_percentage, dtype=float)
pval = pd.DataFrame(index=biomarkers_percentage, columns=biomarkers_percentage, dtype=float)

corr.shape
    # Out[25]: (5, 5)

corr
    # Out[26]: 
    #              HMGB1+_%  NGAL+_%  Casp3+_%  Zo-1+_%  Syndecan+_%
    # HMGB1+_%          NaN      NaN       NaN      NaN          NaN
    # NGAL+_%           NaN      NaN       NaN      NaN          NaN
    # Casp3+_%          NaN      NaN       NaN      NaN          NaN
    # Zo-1+_%           NaN      NaN       NaN      NaN          NaN
    # Syndecan+_%       NaN      NaN       NaN      NaN          NaN

# %%%' 

# Compute pairwise Spearman correlations
for i in biomarkers_percentage:
    for j in biomarkers_percentage:
        rho, p = spearmanr(data[i], data[j], nan_policy="omit")
        corr.loc[i, j] = rho
        pval.loc[i, j] = p

# %%%'

corr
    # Out[25]: 
    #              HMGB1+_%   NGAL+_%  Casp3+_%   Zo-1+_%  Syndecan+_%
    # HMGB1+_%     1.000000  0.139033  0.177729 -0.083225    -0.027873
    # NGAL+_%      0.139033  1.000000 -0.067993 -0.147135     0.101770
    # Casp3+_%     0.177729 -0.067993  1.000000  0.202554     0.235042
    # Zo-1+_%     -0.083225 -0.147135  0.202554  1.000000     0.121411
    # Syndecan+_% -0.027873  0.101770  0.235042  0.121411     1.000000


# un-corrected p-values.
pval
    # Out[26]: 
    #              HMGB1+_%  NGAL+_%  Casp3+_%  Zo-1+_%  Syndecan+_%
    # HMGB1+_%     1.000000 0.302334  0.185951 0.538234     0.836935
    # NGAL+_%      0.302334 1.000000  0.615283 0.274748     0.451281
    # Casp3+_%     0.185951 0.615283  1.000000 0.130768     0.078414
    # Zo-1+_%      0.538234 0.274748  0.130768 1.000000     0.368303
    # Syndecan+_%  0.836935 0.451281  0.078414 0.368303     0.000000

# %%%'

pval.to_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\correlation\pvalues_uncorrected.xlsx' )


# %%%'

# all these could have been possibly much better have been implemented in pinguin :
    # C:\code\composition\matrix.py
    # however, in the latter, correction for multiple test wre seemingly not done.

from statsmodels.stats.multitest import multipletests

# Flatten upper triangle (excluding diagonal)
# select the upper triangle :
# note : unlike the previous makss that I used to select particular rows from a dataframe, 
    # here, the mask is not a row-mask !
    # it's an array-mask ! : 2 dimensional.
    # its a numpy array, unlike the conventional masks tat I used before that were pandas-series.
    # to review the conventional masks  =  C:\code\kidney\histology\multiplex\combination\combination.py  |  explore-review mask.
mask = np.triu(np.ones(pval.shape), k=1).astype(bool)
mask
    # Out[29]: 
    # array([[False,  True,  True,  True,  True],
    #        [False, False,  True,  True,  True],
    #        [False, False, False,  True,  True],
    #        [False, False, False, False,  True],
    #        [False, False, False, False, False]])

# extract only the selected items.
pvals_flat = pval.values[mask]
pvals_flat
    # Out[31]: 
    # array([0.30233434, 0.1859506 , 0.53823384, 0.83693474, 0.6152826 ,
    #        0.27474848, 0.45128143, 0.13076814, 0.07841368, 0.36830332])

_ , pvals_fdr, _ , _ = multipletests(pvals_flat, method="fdr_bh")

pvals_fdr
    # Out[33]: 
    # array([0.60466868, 0.60466868, 0.67279231, 0.83693474, 0.68364733,
    #        0.60466868, 0.64468775, 0.60466868, 0.60466868, 0.61383887])

# Putting the corrected values back into matrix ( panddas dataframe ) structure
# for the following array-mask-assignment , you can not take a pandas dataframe directly !
        # ValueError: assignment destination is read-only
    # you should 1st convert it to a numpy array !
    # .copy() : you should do this , otherwise the array is not writable ! & you will get the same error :
        # ValueError: assignment destination is read-only
pval_fdr_np_array = pval.to_numpy().copy()
pval_fdr_np_array
    # Out[53]: 
    # array([[1.        , 0.30233434, 0.1859506 , 0.53823384, 0.83693474],
    #        [0.30233434, 1.        , 0.6152826 , 0.27474848, 0.45128143],
    #        [0.1859506 , 0.6152826 , 1.        , 0.13076814, 0.07841368],
    #        [0.53823384, 0.27474848, 0.13076814, 1.        , 0.36830332],
    #        [0.83693474, 0.45128143, 0.07841368, 0.36830332, 0.        ]])

pval_fdr_np_array[mask] = pvals_fdr
pval_fdr_np_array
    # Out[59]: 
    # array([[1.        , 0.60466868, 0.60466868, 0.67279231, 0.83693474],
    #        [0.30233434, 1.        , 0.68364733, 0.60466868, 0.64468775],
    #        [0.1859506 , 0.6152826 , 1.        , 0.60466868, 0.60466868],
    #        [0.53823384, 0.27474848, 0.13076814, 1.        , 0.61383887],
    #        [0.83693474, 0.45128143, 0.07841368, 0.36830332, 0.        ]])

pval_fdr_np_array[(mask.T)] = pvals_fdr
pval_fdr_np_array
    # Out[61]: 
    # array([[1.        , 0.60466868, 0.60466868, 0.67279231, 0.83693474],
    #        [0.60466868, 1.        , 0.68364733, 0.60466868, 0.64468775],
    #        [0.60466868, 0.67279231, 1.        , 0.60466868, 0.60466868],
    #        [0.83693474, 0.68364733, 0.60466868, 1.        , 0.61383887],
    #        [0.64468775, 0.60466868, 0.60466868, 0.61383887, 0.        ]])


# to initially get a pandas datarame with a similar shape.
pval_fdr_matrix = pval.copy()
pval_fdr_matrix.iloc[:, :] = pval_fdr_np_array

# again the same error occurs.
# np.fill_diagonal(pval_fdr_matrix.values, np.nan)
    # ValueError: underlying array is read-only

# filling the diagonal line with NaN , as '1' is meaningless.
pval_fdr_matrix_arr = pval_fdr_matrix.to_numpy().copy()  # force, creating a writable copy
np.fill_diagonal( pval_fdr_matrix_arr , np.nan )
pval_fdr_matrix.iloc[:, :] = pval_fdr_matrix_arr


# these are the multiple-test corrected p-values.
pval_fdr_matrix
    # Out[71]: 
    #              HMGB1+_%  NGAL+_%  Casp3+_%  Zo-1+_%  Syndecan+_%
    # HMGB1+_%          NaN 0.604669  0.604669 0.672792     0.836935
    # NGAL+_%      0.604669      NaN  0.683647 0.604669     0.644688
    # Casp3+_%     0.604669 0.672792       NaN 0.604669     0.604669
    # Zo-1+_%      0.836935 0.683647  0.604669      NaN     0.613839
    # Syndecan+_%  0.644688 0.604669  0.604669 0.613839          NaN

# %%%'

pval_fdr_matrix.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\pval_fdr_matrix.pkl' )
pval_fdr_matrix = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\pval_fdr_matrix.pkl' )

pval_fdr_matrix.to_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\correlation\pval_fdr_matrix.xlsx' )


# %%%'

# Create a custom annotation matrix 
labels = corr.round(2).astype(str)

column_labels = [ col[:-2] for col in corr.columns ]

column_labels
    # Out[25]: ['HMGB1+', 'NGAL+', 'Casp3+', 'Zo-1+', 'Syndecan+']]

# %%% plot


# Plot the heatmap.
plt.figure(figsize=( 9 , 8 ))
ax = sns.heatmap(
                    corr, 
                    annot=labels,     # Use our new custom labels (e.g., "0.75 ***")
                    fmt='',           # IMPORTANT: Set fmt='' to use string annotations
                    
                    cmap='coolwarm',
                    vmin=-1, 
                    vmax=1,
                    
                    xticklabels = column_labels,
                    yticklabels = column_labels,
                    annot_kws={"size": 11} 
)

plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
ax.set_title(' Pairwise Spearman ranked correlation coefficients of \n'
             ' individual biomarkers in multiplex immunoassay ', 
             fontsize=20
             )
plt.tight_layout()

# %%%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\correlation\correlation_individual_markers_multiplex.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\correlation\correlation_individual_markers_multiplex.svg' )


# %% melt

multiplex_8 = pd.melt(
                        multiplex_7 ,
                        
                        id_vars=[ 'sample_ID' , 'treatment' ] ,
                        
                        value_vars = biomarkers_percentage ,
                        var_name = 'biomarker' ,
                        value_name = 'cnp'  # cell umber percentage
)

# %%'

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

# %%'






