
# env_23

# %%'

# note : as this file is in the 1-drive folder ( autmatically synced ) : the file should not be open in Excel when you are loading it.
    # otherwise : 
        # PermissionError: [Errno 13] Permission denied
multiplex = pd.read_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\Results Multiplex Ernst24 - August-WH.xlsx' , sheet_name=1 )  

# %%'

multiplex.shape
    # Out[12]: (75, 68)


multiplex.iloc[ 10:20,:4]
    # Out[13]: 
    #             Unnamed: 0  ZC40  ZC42  ZC49
    # 10               Zo-1+  1224   353  1948
    # 11           Syndecan+  1045  2316   808
    # 12       HMGB1+ NGal+    305    54   383
    # 13       HMGB1+ Casp3+     1     1     1
    # 14      HMGB1+  Zo-1+     27     1    50
    # 15  HMGB1+  Syndecan+      0     0     4
    # 16      NGal+  Casp3+      1     1     1
    # 17       NGal+  Zo-1+    204   237   272
    # 18   NGal+  Syndecan+     92   656   161
    # 19      Casp3+  Zo-1+      0     0     0


multiplex.iloc[ -10: ,-4:]
    # Out[14]: 
    #    Zc21.1 Zc22.1 Zc29.1 Zc30.1
    # 65      0      0      0      0
    # 66      0      0      0      0
    # 67      0      0      0      0
    # 68      0      2      3      5
    # 69     34    244   1383   2524
    # 70      0     26      2    193
    # 71      0      1      0     16
    # 72     27      3     82      2
    # 73      0      0      0      0
    # 74      0      0      0      0


multiplex.iloc[ -10: , :4 ]
    # Out[15]: 
    #                             Unnamed: 0 ZC40 ZC42 ZC49
    # 65   HMGB1+NGal-Casp3+CD206-Syndecan+     0    0    0
    # 66    HMGB1+NGal-Casp3+Zo-1+Syndecan+     0    0    0
    # 67    HMGB1+NGal+Zo-16-Zo-1+Syndecan+     0    0    0
    # 68   HMGB1+NGal+Zo-16-CD206-Syndecan+     0    0    0
    # 69   HMGB1+NGal+Zo-16-CD206-Syndecan-   278   52  333
    # 70    HMGB1+NGal+Zo-16-Zo-1+Syndecan-    26    1   49
    # 71    HMGB1+NGal+Casp3+Zo-1+Syndecan-     0    0    0
    # 72   HMGB1+NGal+Casp3+CD206-Syndecan-     1    1    1
    # 73    HMGB1+NGal+Casp3+Zo-1+Syndecan+     0    0    0
    # 74   HMGB1+NGal+Casp3+CD206-Syndecan+     0    0    0


multiplex.iloc[ 12:22 , :4 ]
    # Out[16]: 
    #             Unnamed: 0 ZC40 ZC42 ZC49
    # 12       HMGB1+ NGal+   305   54  383
    # 13       HMGB1+ Casp3+    1    1    1
    # 14      HMGB1+  Zo-1+    27    1   50
    # 15  HMGB1+  Syndecan+     0    0    4
    # 16      NGal+  Casp3+     1    1    1
    # 17       NGal+  Zo-1+   204  237  272
    # 18   NGal+  Syndecan+    92  656  161
    # 19      Casp3+  Zo-1+     0    0    0
    # 20  Casp3+  Syndecan+     0    1    0
    # 21   Zo-1+  Syndecan+     0    0    0

# %%'

multiplex.isna().sum().sum()

# %%'

# row index 0,5,6 + 12:  :  are kept.
combined = pd.concat([ 
                        multiplex.loc[[0,5,6]] , 
                        multiplex.loc[12:] 
])

combined.shape
    # Out[20]: (66, 68)

combined.iloc[:8 , :4]
    # Out[31]: 
    #             Unnamed: 0         ZC40         ZC42         ZC49
    # 0                  NaN  DBD-Ecoflow  DBD-Ecoflow  DBD-Ecoflow
    # 5                 Area   289.569564   384.897752   237.515856
    # 6             Zellzahl      1250108      1775207      1358316
    # 12       HMGB1+ NGal+           305           54          383
    # 13       HMGB1+ Casp3+            1            1            1
    # 14      HMGB1+  Zo-1+            27            1           50
    # 15  HMGB1+  Syndecan+             0            0            4
    # 16      NGal+  Casp3+             1            1            1

combined.iloc[ -4: , :4 ]
    # Out[32]: 
    #                            Unnamed: 0 ZC40 ZC42 ZC49
    # 71   HMGB1+NGal+Casp3+Zo-1+Syndecan-     0    0    0
    # 72  HMGB1+NGal+Casp3+CD206-Syndecan-     1    1    1
    # 73   HMGB1+NGal+Casp3+Zo-1+Syndecan+     0    0    0
    # 74  HMGB1+NGal+Casp3+CD206-Syndecan+     0    0    0


# %%' drop blank columns

combined.columns
    # Out[33]: 
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

# there are some blank columns in the dataframe.
    # these columns also have no column name.
    # drop them.

# identify all Unnamed ( blank ) columns except the 1st one ('Unnamed: 0').
blank = [ 
            col 
            for col in combined.columns 
                if col.startswith("Unnamed") and col != "Unnamed: 0" 
]


blank
    # Out[]: 
    # ['Unnamed: 9',
    #  'Unnamed: 17',
    #  'Unnamed: 25',
    #  'Unnamed: 33',
    #  'Unnamed: 41',
    #  'Unnamed: 52',
    #  'Unnamed: 60']

# drop them
combined_2 = combined.drop( columns=blank )


combined_2.shape
    # Out[37]: (66, 61)

combined_2.columns 
    # Out[38]: 
    # Index(['Unnamed: 0', 'ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58',
    #        'ZC59', 'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15', 'ZC27', 'ZC04',
    #        'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC24', 'ZC25', 'ZC26',
    #        'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC44', 'ZC46', 'ZC47', 'ZC48', 'ZC53',
    #        'ZC55', 'ZC56', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC64', 'ZC65', 'ZC66',
    #        'ZC67', 'ZC68', 'ZC69', 'Zc17', 'Zc19', 'Zc20', 'Zc21', 'Zc22', 'Zc29',
    #        'Zc30', 'Zc17.1', 'Zc19.1', 'Zc20.1', 'Zc21.1', 'Zc22.1', 'Zc29.1',
    #        'Zc30.1'],
    #       dtype='object')

# %% detecting the NA values !

combined_2.isna().sum().sum()
    # Out[36]: np.int64(196)


list( combined_2.isna().sum().sum() )
    # TypeError: 'numpy.int64' object is not iterable


combined_2.iloc[ :10 , :10 ]


combined_2.iloc[10,:].isna().sum()
    # Out[41]: np.int64(3)


combined_2.iloc[10,:4]
    # Out[46]: 
    # Unnamed: 0    Casp3+  Zo-1+ 
    # ZC40                       0
    # ZC42                       0
    # ZC49                       0
    # Name: 19, dtype: object

mask_1_column = combined_2.iloc[10,:].isna()
na_1_column = combined_2.iloc[10,:][ mask_1_column ]

na_1_column
    # Out[45]: 
    # ZC46    NaN
    # ZC64    NaN
    # ZC69    NaN
    # Name: 19, dtype: object

'''
    the 3 samples : ZC46 , ZC64 , ZC69 : 
        these have the whole column empty : no entries.
        I had initially mistaken these whole empty columns as the inter-treatment-group empty columns ntentioanlly left blank \
            by the inputting person as a barrier between the groups.
'''

# %%'

combined_2.iloc[ :10 , :5 ]
    # Out[40]: 
    #             Unnamed: 0         ZC40         ZC42         ZC49         ZC50
    # 0                  NaN  DBD-Ecoflow  DBD-Ecoflow  DBD-Ecoflow  DBD-Ecoflow
    # 5                 Area   289.569564   384.897752   237.515856   352.881449
    # 6             Zellzahl      1250108      1775207      1358316      2092334
    # 12       HMGB1+ NGal+           305           54          383          310
    # 13       HMGB1+ Casp3+            1            1            1           37
    # 14      HMGB1+  Zo-1+            27            1           50            9
    # 15  HMGB1+  Syndecan+             0            0            4            6
    # 16      NGal+  Casp3+             1            1            1           36
    # 17       NGal+  Zo-1+           204          237          272           18
    # 18   NGal+  Syndecan+            92          656          161           10


combined_3 = combined_2.T

combined_3.shape
    # Out[42]: (61, 66)


combined_3.iloc[:10 , :5]
    # Out[43]: 
    #                      0          5         6              12             13
    # Unnamed: 0          NaN       Area  Zellzahl  HMGB1+ NGal+   HMGB1+ Casp3+
    # ZC40        DBD-Ecoflow 289.569564   1250108            305              1
    # ZC42        DBD-Ecoflow 384.897752   1775207             54              1
    # ZC49        DBD-Ecoflow 237.515856   1358316            383              1
    # ZC50        DBD-Ecoflow 352.881449   2092334            310             37
    # ZC51        DBD-Ecoflow 291.484567    980051          11173            175
    # ZC52        DBD-Ecoflow 416.984612   2266410             21              0
    # ZC58        DBD-Ecoflow 338.358210   1756854           2179              6
    # ZC59        DBD-Ecoflow 428.934441   2432330           1476              3
    # ZC05         DBD-Ecosol 157.760070   1094671           1309            838



combined_3.isna().sum()
    # Out[32]: 
    # 0     1
    # 5     3
    # 6     3
    # 12    3
    # 13    3
    #      ..
    # 70    3
    # 71    3
    # 72    3
    # 73    3
    # 74    3
    # Length: 66, dtype: int64

combined_3.isna().sum().sum()
    # Out[33]: np.int64(196)

# %%'


# 1) Lift the first row into the columns
new_cols = combined_3.iloc[0].tolist()  # take the first row

new_cols
    # Out[45]: 
    # [ nan,
    #  'Area',
    #  'Zellzahl',
    #  'HMGB1+ NGal+ ',
    #  'HMGB1+ Casp3+',
    #  'HMGB1+  Zo-1+ ',
    #  'HMGB1+  Syndecan+ ',
    #  'NGal+  Casp3+ ',
    #  'NGal+  Zo-1+ ',
    #  'NGal+  Syndecan+ ',
    #  'Casp3+  Zo-1+ ',
    #  'Casp3+  Syndecan+ ',
    #  ' Zo-1+  Syndecan+ ',
    #  'HMGB1+ NGal+ Zo-1+ ',
    #  'HMGB1+ NGal+ Casp3+ ',
    #  'HMGB1+ NGal+ Syndecan+ ',
    #  'HMGB1+ Casp3+ Zo-1+ ',
    #  'HMGB1+ Casp3+ Syndecan+ ',
    #  'HMGB1+ Zo-1+ Syndecan+ ',
    #  'NGal+ Casp3+ Zo-1+ ',
    #  'NGal+ Casp3+ Syndecan+ ',
    #  'NGal+ Zo-1+ Syndecan+ ',
    #  'HMGB1+ NGal+ Casp3+ Zo-1+ ',
    #  'HMGB1+ Casp3+ Syndecan+ Zo-1+ ',
    #  'HMGB1+ Syndecan+ NGal+ Casp3+ ',
    #  'NGal+ Casp3+ Zo-1+ Syndecan+ ',
    #  'NGal+ Casp3+ Zo-1+ Syndecan+ HMGB1+ ',
    #  'Zo-1-NGal+Casp3+ ',
    #  'Zo-1- NGal- Casp3+ ',
    #  ' Zo-1- NGal- Zo-16- ',
    #  'Zo-1- NGal+ Zo-16- ',
    #  'HMGB1+ NGal- Casp3+ ',
    #  'HMGB1+ NGal- Zo-16- ',
    #  'HMGB1+ NGal+ Zo-16- ',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan+ ',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan+ ',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan- ',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan- ',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan- ',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan- ',
    #  ' HMGB1-NGal-Casp3+Zo-1+Syndecan+ ',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan+ ',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan+ ',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan+ ',
    #  ' HMGB1-NGal+Zo-16-CD206-Syndecan- ',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan- ',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan- ',
    #  ' HMGB1-NGal+Casp3+CD206-Syndecan- ',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan+ ',
    #  'HMGB18-NGal+Casp3+CD206-Syndecan+ ',
    #  ' HMGB1+NGal-Zo-16-Zo-1+Syndecan+ ',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan+ ',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan- ',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan- ',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan- ',
    #  'HMGB1+NGal-Casp3+CD206-Syndecan- ',
    #  ' HMGB1+NGal-Casp3+CD206-Syndecan+ ',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan+ ',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan+ ',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan+ ',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan- ',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan- ',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan- ',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan- ',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan+ ',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan+ ']


# assign as new column names
combined_3.columns = new_cols          

combined_3.iloc[:6 , :4]
    # Out[47]: 
    #                     NaN       Area  Zellzahl  HMGB1+ NGal+ 
    # Unnamed: 0          NaN       Area  Zellzahl  HMGB1+ NGal+ 
    # ZC40        DBD-Ecoflow 289.569564   1250108            305
    # ZC42        DBD-Ecoflow 384.897752   1775207             54
    # ZC49        DBD-Ecoflow 237.515856   1358316            383
    # ZC50        DBD-Ecoflow 352.881449   2092334            310
    # ZC51        DBD-Ecoflow 291.484567    980051          11173


combined_3.drop( index='Unnamed: 0' , inplace=True )

combined_3.iloc[:6 , :4]
    # Out[49]: 
    #               NaN       Area Zellzahl HMGB1+ NGal+ 
    # ZC40  DBD-Ecoflow 289.569564  1250108           305
    # ZC42  DBD-Ecoflow 384.897752  1775207            54
    # ZC49  DBD-Ecoflow 237.515856  1358316           383
    # ZC50  DBD-Ecoflow 352.881449  2092334           310
    # ZC51  DBD-Ecoflow 291.484567   980051         11173
    # ZC52  DBD-Ecoflow 416.984612  2266410            21


# the index now is sample_IDs.
# you want sample_IDs to be a column, with the column name : sample_ID.
# Reset the row index to simple 0,1,2…
combined_3.reset_index( inplace=True )


combined_3.iloc[:6 , :4]
    # Out[51]: 
    #   index          NaN       Area Zellzahl
    # 0  ZC40  DBD-Ecoflow 289.569564  1250108
    # 1  ZC42  DBD-Ecoflow 384.897752  1775207
    # 2  ZC49  DBD-Ecoflow 237.515856  1358316
    # 3  ZC50  DBD-Ecoflow 352.881449  2092334
    # 4  ZC51  DBD-Ecoflow 291.484567   980051
    # 5  ZC52  DBD-Ecoflow 416.984612  2266410

# rename first two columns
# tcc : total cell count : in the whole slide.
combined_3.rename(
                    columns={
                                combined_3.columns[0]: 'sample_ID',
                                combined_3.columns[1]: 'treatment',
                                'Zellzahl': 'tcc'
                                },
                    inplace=True
)

combined_3.iloc[:6 , :6]
    # Out[54]: 
    #   sample_ID    treatment       Area      tcc HMGB1+ NGal+  HMGB1+ Casp3+
    # 0      ZC40  DBD-Ecoflow 289.569564  1250108           305             1
    # 1      ZC42  DBD-Ecoflow 384.897752  1775207            54             1
    # 2      ZC49  DBD-Ecoflow 237.515856  1358316           383             1
    # 3      ZC50  DBD-Ecoflow 352.881449  2092334           310            37
    # 4      ZC51  DBD-Ecoflow 291.484567   980051         11173           175
    # 5      ZC52  DBD-Ecoflow 416.984612  2266410            21             0

# %%'

combined_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_3.pkl' )

# %%'

combined_3.columns = combined_3.columns.str.replace(' ', '')

list( combined_3.columns )
    # Out[58]: 
    # ['sample_ID',
    #  'treatment',
    #  'Area',
    #  'tcc',
    #  'HMGB1+NGal+',
    #  'HMGB1+Casp3+',
    #  'HMGB1+Zo-1+',
    #  'HMGB1+Syndecan+',
    #  'NGal+Casp3+',
    #  'NGal+Zo-1+',
    #  'NGal+Syndecan+',
    #  'Casp3+Zo-1+',
    #  'Casp3+Syndecan+',
    #  'Zo-1+Syndecan+',
    #  'HMGB1+NGal+Zo-1+',
    #  'HMGB1+NGal+Casp3+',
    #  'HMGB1+NGal+Syndecan+',
    #  'HMGB1+Casp3+Zo-1+',
    #  'HMGB1+Casp3+Syndecan+',
    #  'HMGB1+Zo-1+Syndecan+',
    #  'NGal+Casp3+Zo-1+',
    #  'NGal+Casp3+Syndecan+',
    #  'NGal+Zo-1+Syndecan+',
    #  'HMGB1+NGal+Casp3+Zo-1+',
    #  'HMGB1+Casp3+Syndecan+Zo-1+',
    #  'HMGB1+Syndecan+NGal+Casp3+',
    #  'NGal+Casp3+Zo-1+Syndecan+',
    #  'NGal+Casp3+Zo-1+Syndecan+HMGB1+',
    #  'Zo-1-NGal+Casp3+',
    #  'Zo-1-NGal-Casp3+',
    #  'Zo-1-NGal-Zo-16-',
    #  'Zo-1-NGal+Zo-16-',
    #  'HMGB1+NGal-Casp3+',
    #  'HMGB1+NGal-Zo-16-',
    #  'HMGB1+NGal+Zo-16-',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan+',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan+',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan-',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan-',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan-',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan-',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan+',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan+',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan+',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan+',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan-',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan-',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan-',
    #  'HMGB1-NGal+Casp3+CD206-Syndecan-',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan+',
    #  'HMGB18-NGal+Casp3+CD206-Syndecan+',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan+',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan+',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan-',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan-',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan-',
    #  'HMGB1+NGal-Casp3+CD206-Syndecan-',
    #  'HMGB1+NGal-Casp3+CD206-Syndecan+',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan+',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan+',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan+',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan-',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan-',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan-',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan-',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan+',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan+']


# strange markers :
    # Zo-16
    # CD206

# %%'

combined_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_3.pkl' )


# %% calculate

meta_cols = ['sample_ID', 'treatment', 'Area']

# Everything except the metadata columns and 'tcc' is a biomarker:
biomarker_cols = combined_3.columns.difference( meta_cols + ['tcc'] )

# combined_% : this name was not allowed !
# pct : percent
combined_pct = combined_3[biomarker_cols].div( combined_3['tcc'], axis=0 ) * 100

combined_pct.shape
    # Out[66]: (60, 63)


combined_pct.iloc[:5 , :5]
    # Out[67]: 
    #   Casp3+Syndecan+ Casp3+Zo-1+ HMGB1+Casp3+ HMGB1+Casp3+Syndecan+  \
    # 0        0.000000    0.000000     0.000080              0.000000   
    # 1        0.000056    0.000000     0.000056              0.000000   
    # 2        0.000000    0.000000     0.000074              0.000000   
    # 3        0.001195    0.001004     0.001768              0.000000   
    # 4        0.000000    0.000102     0.017856              0.000000   
    
    #   HMGB1+Casp3+Syndecan+Zo-1+  
    # 0                   0.000000  
    # 1                   0.000000  
    # 2                   0.000000  
    # 3                   0.000000  
    # 4                   0.000000  


combined_pct = combined_pct.add_suffix('_%')

# %%'

list( combined_pct.columns )
    # Out[77]: 
    # ['Casp3+Syndecan+_%',
    #  'Casp3+Zo-1+_%',
    #  'HMGB1+Casp3+_%',
    #  'HMGB1+Casp3+Syndecan+_%',
    #  'HMGB1+Casp3+Syndecan+Zo-1+_%',
    #  'HMGB1+Casp3+Zo-1+_%',
    #  'HMGB1+NGal+_%',
    #  'HMGB1+NGal+Casp3+_%',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan+_%',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan-_%',
    #  'HMGB1+NGal+Casp3+Zo-1+_%',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1+NGal+Syndecan+_%',
    #  'HMGB1+NGal+Zo-1+_%',
    #  'HMGB1+NGal+Zo-16-_%',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan+_%',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan-_%',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1+NGal-Casp3+_%',
    #  'HMGB1+NGal-Casp3+CD206-Syndecan+_%',
    #  'HMGB1+NGal-Casp3+CD206-Syndecan-_%',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1+NGal-Zo-16-_%',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan+_%',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan-_%',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1+Syndecan+_%',
    #  'HMGB1+Syndecan+NGal+Casp3+_%',
    #  'HMGB1+Zo-1+_%',
    #  'HMGB1+Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Casp3+CD206-Syndecan-_%',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan+_%',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan-_%',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan+_%',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan-_%',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan+_%',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan-_%',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB18-NGal+Casp3+CD206-Syndecan+_%',
    #  'NGal+Casp3+_%',
    #  'NGal+Casp3+Syndecan+_%',
    #  'NGal+Casp3+Zo-1+_%',
    #  'NGal+Casp3+Zo-1+Syndecan+_%',
    #  'NGal+Casp3+Zo-1+Syndecan+HMGB1+_%',
    #  'NGal+Syndecan+_%',
    #  'NGal+Zo-1+_%',
    #  'NGal+Zo-1+Syndecan+_%',
    #  'Zo-1+Syndecan+_%',
    #  'Zo-1-NGal+Casp3+_%',
    #  'Zo-1-NGal+Zo-16-_%',
    #  'Zo-1-NGal-Casp3+_%',
    #  'Zo-1-NGal-Zo-16-_%']

combined_pct_columns = list( combined_pct.columns )

len( combined_pct_columns )
    # Out[83]: 63

# %% parameter ( metric ) columns

combined_pct_columns = [
     'Casp3+Syndecan+_%',
     'Casp3+Zo-1+_%',
     'HMGB1+Casp3+_%',
     'HMGB1+Casp3+Syndecan+_%',
     'HMGB1+Casp3+Syndecan+Zo-1+_%',
     'HMGB1+Casp3+Zo-1+_%',
     'HMGB1+NGal+_%',
     'HMGB1+NGal+Casp3+_%',
     'HMGB1+NGal+Casp3+CD206-Syndecan+_%',
     'HMGB1+NGal+Casp3+CD206-Syndecan-_%',
     'HMGB1+NGal+Casp3+Zo-1+_%',
     'HMGB1+NGal+Casp3+Zo-1+Syndecan+_%',
     'HMGB1+NGal+Casp3+Zo-1+Syndecan-_%',
     'HMGB1+NGal+Syndecan+_%',
     'HMGB1+NGal+Zo-1+_%',
     'HMGB1+NGal+Zo-16-_%',
     'HMGB1+NGal+Zo-16-CD206-Syndecan+_%',
     'HMGB1+NGal+Zo-16-CD206-Syndecan-_%',
     'HMGB1+NGal+Zo-16-Zo-1+Syndecan+_%',
     'HMGB1+NGal+Zo-16-Zo-1+Syndecan-_%',
     'HMGB1+NGal-Casp3+_%',
     'HMGB1+NGal-Casp3+CD206-Syndecan+_%',
     'HMGB1+NGal-Casp3+CD206-Syndecan-_%',
     'HMGB1+NGal-Casp3+Zo-1+Syndecan+_%',
     'HMGB1+NGal-Casp3+Zo-1+Syndecan-_%',
     'HMGB1+NGal-Zo-16-_%',
     'HMGB1+NGal-Zo-16-CD206-Syndecan+_%',
     'HMGB1+NGal-Zo-16-CD206-Syndecan-_%',
     'HMGB1+NGal-Zo-16-Zo-1+Syndecan+_%',
     'HMGB1+NGal-Zo-16-Zo-1+Syndecan-_%',
     'HMGB1+Syndecan+_%',
     'HMGB1+Syndecan+NGal+Casp3+_%',
     'HMGB1+Zo-1+_%',
     'HMGB1+Zo-1+Syndecan+_%',
     'HMGB1-NGal+Casp3+CD206-Syndecan-_%',
     'HMGB1-NGal+Casp3+Zo-1+Syndecan+_%',
     'HMGB1-NGal+Casp3+Zo-1+Syndecan-_%',
     'HMGB1-NGal+Zo-16-CD206-Syndecan+_%',
     'HMGB1-NGal+Zo-16-CD206-Syndecan-_%',
     'HMGB1-NGal+Zo-16-Zo-1+Syndecan+_%',
     'HMGB1-NGal+Zo-16-Zo-1+Syndecan-_%',
     'HMGB1-NGal-Casp3+CD206-Syndecan+_%',
     'HMGB1-NGal-Casp3+CD206-Syndecan-_%',
     'HMGB1-NGal-Casp3+Zo-1+Syndecan+_%',
     'HMGB1-NGal-Casp3+Zo-1+Syndecan-_%',
     'HMGB1-NGal-Zo-16-CD206-Syndecan+_%',
     'HMGB1-NGal-Zo-16-CD206-Syndecan-_%',
     'HMGB1-NGal-Zo-16-Zo-1+Syndecan+_%',
     'HMGB1-NGal-Zo-16-Zo-1+Syndecan-_%',
     'HMGB18-NGal+Casp3+CD206-Syndecan+_%',
     'NGal+Casp3+_%',
     'NGal+Casp3+Syndecan+_%',
     'NGal+Casp3+Zo-1+_%',
     'NGal+Casp3+Zo-1+Syndecan+_%',
     'NGal+Casp3+Zo-1+Syndecan+HMGB1+_%',
     'NGal+Syndecan+_%',
     'NGal+Zo-1+_%',
     'NGal+Zo-1+Syndecan+_%',
     'Zo-1+Syndecan+_%',
     'Zo-1-NGal+Casp3+_%',
     'Zo-1-NGal+Zo-16-_%',
     'Zo-1-NGal-Casp3+_%',
     'Zo-1-NGal-Zo-16-_%'
]

# %%'

len( combined_pct_columns )
    # Out[63]: 63

# %%'

combined_3.shape
    # Out[70]: (60, 67)

combined_pct.shape
    # Out[71]: (60, 63)

# %%'


combined_pct_2 = pd.concat( 
                            [ 
                                 combined_3[meta_cols], 
                                 combined_pct 
                             ], 
                            axis=1
                           )

# %%'

combined_pct_2.shape
    # Out[73]: (60, 66)

combined_pct_2.iloc[ :5 , :5 ]
    # Out[74]: 
    #   sample_ID    treatment       Area Casp3+Syndecan+_% Casp3+Zo-1+_%
    # 0      ZC40  DBD-Ecoflow 289.569564          0.000000      0.000000
    # 1      ZC42  DBD-Ecoflow 384.897752          0.000056      0.000000
    # 2      ZC49  DBD-Ecoflow 237.515856          0.000000      0.000000
    # 3      ZC50  DBD-Ecoflow 352.881449          0.001195      0.001004
    # 4      ZC51  DBD-Ecoflow 291.484567          0.000000      0.000102

# %%'

combined_pct_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_2.pkl' )

combined_pct_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_2.pkl' )

# %% NA values : count

combined_pct_2.isna().sum()
    # Out[14]: 
    # sample_ID             0
    # treatment             0
    # Area                  3
    # Casp3+Syndecan+_%     3
    # Casp3+Zo-1+_%         3
    #                      ..
    # Zo-1+Syndecan+_%      3
    # Zo-1-NGal+Casp3+_%    3
    # Zo-1-NGal+Zo-16-_%    3
    # Zo-1-NGal-Casp3+_%    3
    # Zo-1-NGal-Zo-16-_%    3
    # Length: 66, dtype: int64


combined_pct_2.isna().sum().sum()
    # Out[23]: np.int64(192)

192/3
    # Out[24]: 64.0
    # 64 columns of metrics, 3 NAs per-column ?

mask_wide = combined_pct_2.isna()
combined_pct_2_NA = combined_pct_2[ mask_wide ]

combined_pct_2_NA


# %%'

combined_pct_2.iloc[ : , 3 ]


# %% melt

combined_pct_3 = pd.melt(
                        combined_pct_2 ,
                        
                        id_vars=[ 'sample_ID' , 'treatment' ] ,
                        
                        value_vars = list( combined_pct.columns ) ,
                        var_name = 'biomarker' ,
                        value_name = 'cnp'  # cell umber percentage
)

# %%'

combined_pct_3.shape
    # Out[79]: (3780, 4)

combined_pct_3.columns
    # Out[80]: Index(['sample_ID', 'treatment', 'biomarker', 'cnp'], dtype='object')

# %%'

combined_pct_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_3.pkl' )

combined_pct_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_3.pkl' )

# %%' detect abnormal values.

# detect non‑numeric, abnormal, or unexpected entries in a column before you coerce it with pd.to_numeric.
    # entries like : '-', '?', 'n/a', '--', ' ' , ... .

# pd.to_numeric(..., errors='coerce')  
    # → converts valid numbers, turns invalid ones into NaN
# & multiplex_8['cnp'].notna()  
    # → ensures we don’t count real NaN values that were already missing

mask = pd.to_numeric( combined_pct_3['cnp'], errors='coerce').isna() & combined_pct_3['cnp'].notna()
abnormal_values = combined_pct_3.loc[mask, 'cnp']

abnormal_values
    # Out[11]: Series([], Name: cnp, dtype: object)


'''
        There are no non‑numeric strings in the column.
        Everything that is not numeric is already a real NaN.
'''


# %%'

combined_pct_3['cnp'].isna().sum()
    # Out[12]: np.int64(189)

# There are 189 missing values.

# %%'

# We can use the drop parameter to avoid the old index being added as a column.
combined_pct_4 = combined_pct_3.dropna(how='any').reset_index(drop=True) 

combined_pct_4.shape
    # Out[48]: (3591, 4)

# %%'

combined_pct_4['sample_ID'].unique()
    # Out[52]: 
    # array(['ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58', 'ZC59',
    #        'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15', 'ZC27', 'ZC04',
    #        'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC24', 'ZC25',
    #        'ZC26', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC44', 'ZC47', 'ZC48',
    #        'ZC53', 'ZC55', 'ZC56', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC65',
    #        'ZC66', 'ZC67', 'ZC68', 'Zc17', 'Zc19', 'Zc20', 'Zc21', 'Zc22',
    #        'Zc29', 'Zc30', 'Zc17.1', 'Zc19.1', 'Zc20.1', 'Zc21.1', 'Zc22.1',
    #        'Zc29.1', 'Zc30.1'], dtype=object)


combined_pct_4['treatment'].unique()
    # Out[53]: 
    # array(['DBD-Ecoflow', 'DBD-Ecosol', 'DBD-HTK', 'DCD-Ecoflow',
    #        'DCD-Ecosol', 'NMP', 'Kontrolle'], dtype=object)


list( combined_pct_4['biomarker'].unique() )
    # ['Casp3+Syndecan+_%',
    #  'Casp3+Zo-1+_%',
    #  'HMGB1+Casp3+_%',
    #  'HMGB1+Casp3+Syndecan+_%',
    #  'HMGB1+Casp3+Syndecan+Zo-1+_%',
    #  'HMGB1+Casp3+Zo-1+_%',
    #  'HMGB1+NGal+_%',
    #  'HMGB1+NGal+Casp3+_%',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan+_%',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan-_%',
    #  'HMGB1+NGal+Casp3+Zo-1+_%',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1+NGal+Syndecan+_%',
    #  'HMGB1+NGal+Zo-1+_%',
    #  'HMGB1+NGal+Zo-16-_%',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan+_%',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan-_%',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1+NGal-Casp3+_%',
    #  'HMGB1+NGal-Casp3+CD206-Syndecan+_%',
    #  'HMGB1+NGal-Casp3+CD206-Syndecan-_%',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1+NGal-Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1+NGal-Zo-16-_%',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan+_%',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan-_%',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1+Syndecan+_%',
    #  'HMGB1+Syndecan+NGal+Casp3+_%',
    #  'HMGB1+Zo-1+_%',
    #  'HMGB1+Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Casp3+CD206-Syndecan-_%',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan+_%',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan-_%',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan+_%',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan-_%',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan+_%',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan+_%',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan-_%',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB18-NGal+Casp3+CD206-Syndecan+_%',
    #  'NGal+Casp3+_%',
    #  'NGal+Casp3+Syndecan+_%',
    #  'NGal+Casp3+Zo-1+_%',
    #  'NGal+Casp3+Zo-1+Syndecan+_%',
    #  'NGal+Casp3+Zo-1+Syndecan+HMGB1+_%',
    #  'NGal+Syndecan+_%',
    #  'NGal+Zo-1+_%',
    #  'NGal+Zo-1+Syndecan+_%',
    #  'Zo-1+Syndecan+_%',
    #  'Zo-1-NGal+Casp3+_%',
    #  'Zo-1-NGal+Zo-16-_%',
    #  'Zo-1-NGal-Casp3+_%',
    #  'Zo-1-NGal-Zo-16-_%']

len( list( combined_pct_4['biomarker'].unique() ) )
    # Out[64]: 63

# %%'

combined_pct_5 = combined_pct_4.copy()

# %%'

# vectorized cleanup
# the parenthesis is only for more clear expression :
    # splitting the line & indentation.
combined_pct_5['sample_ID'] = (
                                combined_pct_5['sample_ID']
                                .str.upper()                    # make everything uppercase
                                .replace( r'\..*$' , '' , regex=True )  # drop dot-suffix and everything after.
)

# %%'

combined_pct_5['sample_ID'].unique()
    # Out[58]: 
    # array(['ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58', 'ZC59',
    #        'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15', 'ZC27', 'ZC04',
    #        'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC24', 'ZC25',
    #        'ZC26', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC44', 'ZC47', 'ZC48',
    #        'ZC53', 'ZC55', 'ZC56', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC65',
    #        'ZC66', 'ZC67', 'ZC68', 'ZC17', 'ZC19', 'ZC20', 'ZC21', 'ZC22',
    #        'ZC29', 'ZC30'], dtype=object)

# %%'

combined_pct_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_5.pkl' )

combined_pct_5 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_5.pkl' )


# %%'  filter

# filter based on treatment, sample_ID & time.

mask = \
        ( combined_pct_5["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~combined_pct_5["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) 


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
combined_pct_6 = combined_pct_5[ mask ]

# %%'

combined_pct_6.shape
    # Out[61]: (1134, 4)

# %%'  order

# order
    # this will define how they appear in the plots : axes , subplots, ... .
    # cat

treatment_order = ["DBD-HTK", "DBD-Ecosol", "NMP"]
combined_pct_6['treatment'] = pd.Categorical(
                                                combined_pct_6['treatment'],
                                                categories=treatment_order ,
                                                ordered=True
)


# od : ordered
biomarker_order = combined_pct_columns
combined_pct_6['biomarker'] = pd.Categorical( 
                                            combined_pct_6['biomarker'] , 
                                            categories=biomarker_order , 
                                            ordered=True 
)

# %% compatibility for the statistical program

# this is only to make it compatible for the statistical program.

combined_pct_6.columns
    # Out[66]: Index(['sample_ID', 'treatment', 'biomarker', 'cnp'], dtype='object')

combined_pct_7 = combined_pct_6.copy()

# adding a new column.
combined_pct_7['metric'] = 'multiplex'

combined_pct_7.rename( columns={ "biomarker": "time" , 'cnp':'value' } , inplace=True )

# %%'

combined_pct_7.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_7.pkl' )

combined_pct_7 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_7.pkl' )


# %%'


combined_pct_7[:10]
    # Out[20]: 
    #    sample_ID   treatment               time     value     metric
    # 8       ZC05  DBD-Ecosol  Casp3+Syndecan+_%  0.006577  multiplex
    # 9       ZC07  DBD-Ecosol  Casp3+Syndecan+_%       0.0  multiplex
    # 10      ZC09  DBD-Ecosol  Casp3+Syndecan+_%  0.001696  multiplex
    # 11      ZC11  DBD-Ecosol  Casp3+Syndecan+_%  0.003047  multiplex
    # 12      ZC14  DBD-Ecosol  Casp3+Syndecan+_%  0.001476  multiplex
    # 13      ZC15  DBD-Ecosol  Casp3+Syndecan+_%  0.001223  multiplex
    # 15      ZC04     DBD-HTK  Casp3+Syndecan+_%       0.0  multiplex
    # 16      ZC08     DBD-HTK  Casp3+Syndecan+_%       0.0  multiplex
    # 17      ZC10     DBD-HTK  Casp3+Syndecan+_%       0.0  multiplex
    # 18      ZC23     DBD-HTK  Casp3+Syndecan+_%       0.0  multiplex

combined_pct_7[-10:]
    # Out[21]: 
    #      sample_ID treatment                time      value     metric
    # 3551      ZC10   DBD-HTK  Zo-1-NGal-Zo-16-_%  98.978956  multiplex
    # 3552      ZC23   DBD-HTK  Zo-1-NGal-Zo-16-_%  96.676203  multiplex
    # 3553      ZC35   DBD-HTK  Zo-1-NGal-Zo-16-_%  95.126126  multiplex
    # 3554      ZC37   DBD-HTK  Zo-1-NGal-Zo-16-_%  99.839289  multiplex
    # 3555      ZC38   DBD-HTK  Zo-1-NGal-Zo-16-_%  99.832316  multiplex
    # 3570      ZC61       NMP  Zo-1-NGal-Zo-16-_%  99.803564  multiplex
    # 3572      ZC63       NMP  Zo-1-NGal-Zo-16-_%  99.143559  multiplex
    # 3574      ZC66       NMP  Zo-1-NGal-Zo-16-_%  96.733372  multiplex
    # 3575      ZC67       NMP  Zo-1-NGal-Zo-16-_%  99.711395  multiplex
    # 3576      ZC68       NMP  Zo-1-NGal-Zo-16-_%  99.376355  multiplex

# %% unique number of samples.

combined_pct_7.groupby("treatment")["sample_ID"].nunique()
    # Out[10]: 
    # treatment
    # DBD-HTK       7
    # DBD-Ecosol    6
    # NMP           5
    # Name: sample_ID, dtype: int64

# %%'

# useless.
combined_pct_7.groupby(["time", "treatment"])['sample_ID'].nunique()
    # C:\Users\azare\AppData\Local\Temp\ipykernel_26264\3721433731.py:1: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
    #   combined_pct_7.groupby(["time", "treatment"])['sample_ID'].nunique()
    # Out[9]: 
    # time                treatment 
    # Casp3+Syndecan+_%   DBD-HTK       7
    #                     DBD-Ecosol    6
    #                     NMP           5
    # Casp3+Zo-1+_%       DBD-HTK       7
    #                     DBD-Ecosol    6
    #                                  ..
    # Zo-1-NGal-Casp3+_%  DBD-Ecosol    6
    #                     NMP           5
    # Zo-1-NGal-Zo-16-_%  DBD-HTK       7
    #                     DBD-Ecosol    6
    #                     NMP           5
    # Name: sample_ID, Length: 189, dtype: int64



# %%  useless !

test = (
    combined_pct_7
    .assign(nonzero=lambda df: df["value"] > 0)  # creates a new column.
    .groupby(["time", "treatment"])
    ["sample_ID"].nunique() # this does not take into account the new column created ! : is not done over the new column !

)


test[:10]
    # Out[16]: 
    # time                     treatment 
    # Casp3+Syndecan+_%        DBD-HTK       7
    #                          DBD-Ecosol    6
    #                          NMP           5
    # Casp3+Zo-1+_%            DBD-HTK       7
    #                          DBD-Ecosol    6
    #                          NMP           5
    # HMGB1+Casp3+_%           DBD-HTK       7
    #                          DBD-Ecosol    6
    #                          NMP           5
    # HMGB1+Casp3+Syndecan+_%  DBD-HTK       7
    # Name: sample_ID, dtype: int64


# mask for non-zero elements.
# on the new dataframe : groupby ["time", "treatment"]
# counting unique numbers of samle_IDs !

# %% non-0 filtering

# filtering to avoid 0-inflation !

'''
        Goal 
        You want to keep only those biomarker combinations (time) for which:
        In each treatment group, at least 3 pigs have value > 0.
            Key points:
            •	Filtering is done per pattern
            •	Support is checked within each treatment
            •	Zeros are allowed, but not too many
            •	This happens before any statistical testing
        Conceptual steps
            For each biomarker combination (time):
            1.	Split the data by treatment
            2.	Count how many unique pigs have value > 0
            3.	Check whether each treatment group has ≥ 3 such pigs
            4.	Keep only those patterns that satisfy this condition
'''

# nzsic :  non-0 sample-ID counts per ["time", "treatment"].   ( non-zero ).

nzsic = (
    combined_pct_7
    .assign(nonzero=lambda df: df["value"] > 0)   # boolean output.
    .groupby(["time", "treatment"])
    .apply(lambda x: x.loc[x["nonzero"], "sample_ID"].nunique())  # boolean indexing  ( explanation below ).
    .reset_index(name="n_nonzero")
)


# x.loc[x["nonzero"], "sample_ID"] :
    # boolean indexing : 
        # Select rows where nonzero == True
        # From those rows, select only the "sample_ID" column

# %%'

nzsic[:10]
    # Out[20]: 
    #                       time   treatment  n_nonzero
    # 0        Casp3+Syndecan+_%     DBD-HTK          1
    # 1        Casp3+Syndecan+_%  DBD-Ecosol          5
    # 2        Casp3+Syndecan+_%         NMP          4
    # 3            Casp3+Zo-1+_%     DBD-HTK          6
    # 4            Casp3+Zo-1+_%  DBD-Ecosol          6
    # 5            Casp3+Zo-1+_%         NMP          5
    # 6           HMGB1+Casp3+_%     DBD-HTK          5
    # 7           HMGB1+Casp3+_%  DBD-Ecosol          6
    # 8           HMGB1+Casp3+_%         NMP          5
    # 9  HMGB1+Casp3+Syndecan+_%     DBD-HTK          1


nzsic.shape
    # Out[27]: (189, 3)

# %%'

mask_3_nz = nzsic['n_nonzero'] >= 3
nzsic_3_nz = nzsic[ mask_3_nz ]

# %%'

nzsic_3_nz.shape
    # Out[25]: (151, 3)


nzsic_3_nz[:10]
    # Out[26]: 
    #                        time   treatment  n_nonzero
    # 1         Casp3+Syndecan+_%  DBD-Ecosol          5
    # 2         Casp3+Syndecan+_%         NMP          4
    # 3             Casp3+Zo-1+_%     DBD-HTK          6
    # 4             Casp3+Zo-1+_%  DBD-Ecosol          6
    # 5             Casp3+Zo-1+_%         NMP          5
    # 6            HMGB1+Casp3+_%     DBD-HTK          5
    # 7            HMGB1+Casp3+_%  DBD-Ecosol          6
    # 8            HMGB1+Casp3+_%         NMP          5
    # 10  HMGB1+Casp3+Syndecan+_%  DBD-Ecosol          4
    # 11  HMGB1+Casp3+Syndecan+_%         NMP          4

# %% valid_patterns

valid_patterns = (
    nonzero_counts
    .groupby("time")
    .filter( lambda x: (x["n_nonzero"] >= 3).all() )
    ["time"]
    .unique()
)

# wrong :
# I removed : .all() :
    # test = (
    #     nonzero_counts
    #     .groupby("time")
    #     .filter( lambda x: (x["n_nonzero"] >= 3) )
    #     ["time"]
    #     .unique()
    # )


    # TypeError: filter function returned a Series, but expected a scalar bool


'''
        Why?
            groupby().filter() expects the lambda to return:
                a single True or False per group
                    True → keep this entire time group
                    False → drop this entire time group
                It does NOT filter individual rows.
                It filters whole groups.
            
            .all() checks:
                Are all values in this boolean Series True?
                It returns:
                    True → if every value is True
                    False → if at least one value is False
            
            But this expression ( without .all() ) :
                    (x["n_nonzero"] >= 3)
                returns a boolean Series ( for 1 group from groupby operation ), not a single boolean.
                Example inside one group:
                    0     True
                    1     True
                    2    False
                    Name: n_nonzero, dtype: bool
                That’s multiple True/False values — not one.
                .filter() doesn’t know what to do with that.
'''

# %%'

type( valid_patterns )
    # Out[31]: pandas.core.arrays.categorical.Categorical

valid_patterns_list = list(valid_patterns)

valid_patterns_list
    # Out[30]: 
    # ['Casp3+Zo-1+_%',
    #  'HMGB1+Casp3+_%',
    #  'HMGB1+Casp3+Zo-1+_%',
    #  'HMGB1+NGal+_%',
    #  'HMGB1+NGal+Casp3+_%',
    #  'HMGB1+NGal+Casp3+CD206-Syndecan-_%',
    #  'HMGB1+NGal+Casp3+Zo-1+_%',
    #  'HMGB1+NGal+Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1+NGal+Syndecan+_%',
    #  'HMGB1+NGal+Zo-1+_%',
    #  'HMGB1+NGal+Zo-16-_%',
    #  'HMGB1+NGal+Zo-16-CD206-Syndecan-_%',
    #  'HMGB1+NGal+Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1+NGal-Casp3+_%',
    #  'HMGB1+NGal-Zo-16-_%',
    #  'HMGB1+NGal-Zo-16-CD206-Syndecan-_%',
    #  'HMGB1+NGal-Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1+Syndecan+_%',
    #  'HMGB1+Zo-1+_%',
    #  'HMGB1+Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Casp3+CD206-Syndecan-_%',
    #  'HMGB1-NGal+Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan+_%',
    #  'HMGB1-NGal+Zo-16-CD206-Syndecan-_%',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1-NGal+Zo-16-Zo-1+Syndecan-_%',
    #  'HMGB1-NGal-Casp3+CD206-Syndecan-_%',
    #  'HMGB1-NGal-Casp3+Zo-1+Syndecan-_%',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan+_%',
    #  'HMGB1-NGal-Zo-16-CD206-Syndecan-_%',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan+_%',
    #  'HMGB1-NGal-Zo-16-Zo-1+Syndecan-_%',
    #  'NGal+Casp3+_%',
    #  'NGal+Casp3+Zo-1+_%',
    #  'NGal+Syndecan+_%',
    #  'NGal+Zo-1+_%',
    #  'NGal+Zo-1+Syndecan+_%',
    #  'Zo-1-NGal+Casp3+_%',
    #  'Zo-1-NGal+Zo-16-_%',
    #  'Zo-1-NGal-Casp3+_%',
    #  'Zo-1-NGal-Zo-16-_%']

len( valid_patterns_list )
    # Out[36]: 41

# %% filter

# This keeps only patterns where all three treatments meet the ≥3 rule.

combined_pct_8 = combined_pct_7[
                                combined_pct_7["time"].isin( valid_patterns )
].copy()

# %%'

combined_pct_8.shape
    # Out[39]: (738, 5)

combined_pct_8[:10]
    # Out[40]: 
    #    sample_ID   treatment           time    value     metric
    # 65      ZC05  DBD-Ecosol  Casp3+Zo-1+_% 0.011236  multiplex
    # 66      ZC07  DBD-Ecosol  Casp3+Zo-1+_% 0.032665  multiplex
    # 67      ZC09  DBD-Ecosol  Casp3+Zo-1+_% 0.002450  multiplex
    # 68      ZC11  DBD-Ecosol  Casp3+Zo-1+_% 0.021529  multiplex
    # 69      ZC14  DBD-Ecosol  Casp3+Zo-1+_% 0.001723  multiplex
    # 70      ZC15  DBD-Ecosol  Casp3+Zo-1+_% 0.023068  multiplex
    # 72      ZC04     DBD-HTK  Casp3+Zo-1+_% 0.032740  multiplex
    # 73      ZC08     DBD-HTK  Casp3+Zo-1+_% 0.014186  multiplex
    # 74      ZC10     DBD-HTK  Casp3+Zo-1+_% 0.000421  multiplex
    # 75      ZC23     DBD-HTK  Casp3+Zo-1+_% 0.000000  multiplex

# %% combined_pct_8

combined_pct_8.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_8.pkl' )
combined_pct_8 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_8.pkl' )


# %% kruskal

from scipy.stats import kruskal

kw_results = []

# %%'

for pattern, df_pat in combined_pct_8.groupby("time"):
    # for each pattern : treatment-groups are separated  =>  separate Kruskal test for that group.
    groups = [
                df_pat.loc[df_pat["treatment"] == tr, "value"].values
                for tr in df_pat["treatment"].unique()
    ]
    
    # Kruskal–Wallis requires at least 2 groups with data
    if len(groups) >= 2:
        stat, p = kruskal(*groups)
        kw_results.append({
            "time": pattern,
            "kw_stat": stat,
            "p_value": p
        })

# %%'

kw_df = pd.DataFrame(kw_results)

kw_df.shape
    # Out[46]: (41, 3)

kw_df
    # Out[47]: 
    #                                   time  kw_stat  p_value
    # 0                        Casp3+Zo-1+_% 2.890226 0.235719
    # 1                       HMGB1+Casp3+_% 5.060862 0.079625
    # 2                  HMGB1+Casp3+Zo-1+_% 4.800099 0.090713
    # 3                        HMGB1+NGal+_% 0.500084 0.778768
    # 4                  HMGB1+NGal+Casp3+_% 7.205765 0.027245
    # 5   HMGB1+NGal+Casp3+CD206-Syndecan-_% 4.290223 0.117055
    # 6             HMGB1+NGal+Casp3+Zo-1+_% 5.106627 0.077823
    # 7    HMGB1+NGal+Casp3+Zo-1+Syndecan-_% 5.797197 0.055100
    # 8               HMGB1+NGal+Syndecan+_% 3.645154 0.161609
    # 9                   HMGB1+NGal+Zo-1+_% 0.882540 0.643219
    # 10                 HMGB1+NGal+Zo-16-_% 0.249457 0.882737
    # 11  HMGB1+NGal+Zo-16-CD206-Syndecan-_% 0.327820 0.848819
    # 12   HMGB1+NGal+Zo-16-Zo-1+Syndecan-_% 0.327820 0.848819
    # 13                 HMGB1+NGal-Casp3+_% 0.078187 0.961661
    # 14                 HMGB1+NGal-Zo-16-_% 0.315789 0.853940
    # 15  HMGB1+NGal-Zo-16-CD206-Syndecan-_% 0.315789 0.853940
    # 16   HMGB1+NGal-Zo-16-Zo-1+Syndecan-_% 0.513951 0.773387
    # 17                   HMGB1+Syndecan+_% 2.971439 0.226339
    # 18                       HMGB1+Zo-1+_% 0.577778 0.749095
    # 19              HMGB1+Zo-1+Syndecan+_% 2.383706 0.303658
    # 20  HMGB1-NGal+Casp3+CD206-Syndecan-_% 4.676517 0.096496
    # 21   HMGB1-NGal+Casp3+Zo-1+Syndecan-_% 3.739164 0.154188
    # 22  HMGB1-NGal+Zo-16-CD206-Syndecan+_% 4.023032 0.133786
    # 23  HMGB1-NGal+Zo-16-CD206-Syndecan-_% 0.682038 0.711045
    # 24   HMGB1-NGal+Zo-16-Zo-1+Syndecan+_% 4.103578 0.128505
    # 25   HMGB1-NGal+Zo-16-Zo-1+Syndecan-_% 2.842105 0.241460
    # 26  HMGB1-NGal-Casp3+CD206-Syndecan-_% 2.342189 0.310027
    # 27   HMGB1-NGal-Casp3+Zo-1+Syndecan-_% 2.848052 0.240743
    # 28  HMGB1-NGal-Zo-16-CD206-Syndecan+_% 1.847452 0.397037
    # 29  HMGB1-NGal-Zo-16-CD206-Syndecan-_% 1.739850 0.418983
    # 30   HMGB1-NGal-Zo-16-Zo-1+Syndecan+_% 0.321970 0.851305
    # 31   HMGB1-NGal-Zo-16-Zo-1+Syndecan-_% 1.326316 0.515222
    # 32                       NGal+Casp3+_% 7.205765 0.027245
    # 33                  NGal+Casp3+Zo-1+_% 4.342828 0.114016
    # 34                    NGal+Syndecan+_% 3.612030 0.164308
    # 35                        NGal+Zo-1+_% 1.683041 0.431055
    # 36               NGal+Zo-1+Syndecan+_% 3.334875 0.188730
    # 37                  Zo-1-NGal+Casp3+_% 5.491381 0.064204
    # 38                  Zo-1-NGal+Zo-16-_% 0.682038 0.711045
    # 39                  Zo-1-NGal-Casp3+_% 2.537176 0.281228
    # 40                  Zo-1-NGal-Zo-16-_% 0.572264 0.751163

# %% Benjamini–Hochberg FDR

# Benjamini–Hochberg FDR ( false discovery rate ) correction (across patterns)

from statsmodels.stats.multitest import multipletests

kw_df["p_fdr"] = multipletests(
    kw_df["p_value"],
    method="fdr_bh"
)[1]

kw_df
    # Out[50]: 
    #                                   time  kw_stat  p_value    p_fdr
    # 0                        Casp3+Zo-1+_% 2.890226 0.235719 0.494992
    # 1                       HMGB1+Casp3+_% 5.060862 0.079625 0.449107
    # 2                  HMGB1+Casp3+Zo-1+_% 4.800099 0.090713 0.449107
    # 3                        HMGB1+NGal+_% 0.500084 0.778768 0.897731
    # 4                  HMGB1+NGal+Casp3+_% 7.205765 0.027245 0.449107
    # 5   HMGB1+NGal+Casp3+CD206-Syndecan-_% 4.290223 0.117055 0.449107
    # 6             HMGB1+NGal+Casp3+Zo-1+_% 5.106627 0.077823 0.449107
    # 7    HMGB1+NGal+Casp3+Zo-1+Syndecan-_% 5.797197 0.055100 0.449107
    # 8               HMGB1+NGal+Syndecan+_% 3.645154 0.161609 0.449107
    # 9                   HMGB1+NGal+Zo-1+_% 0.882540 0.643219 0.897731
    # 10                 HMGB1+NGal+Zo-16-_% 0.249457 0.882737 0.904805
    # 11  HMGB1+NGal+Zo-16-CD206-Syndecan-_% 0.327820 0.848819 0.897731
    # 12   HMGB1+NGal+Zo-16-Zo-1+Syndecan-_% 0.327820 0.848819 0.897731
    # 13                 HMGB1+NGal-Casp3+_% 0.078187 0.961661 0.961661
    # 14                 HMGB1+NGal-Zo-16-_% 0.315789 0.853940 0.897731
    # 15  HMGB1+NGal-Zo-16-CD206-Syndecan-_% 0.315789 0.853940 0.897731
    # 16   HMGB1+NGal-Zo-16-Zo-1+Syndecan-_% 0.513951 0.773387 0.897731
    # 17                   HMGB1+Syndecan+_% 2.971439 0.226339 0.494992
    # 18                       HMGB1+Zo-1+_% 0.577778 0.749095 0.897731
    # 19              HMGB1+Zo-1+Syndecan+_% 2.383706 0.303658 0.552658
    # 20  HMGB1-NGal+Casp3+CD206-Syndecan-_% 4.676517 0.096496 0.449107
    # 21   HMGB1-NGal+Casp3+Zo-1+Syndecan-_% 3.739164 0.154188 0.449107
    # 22  HMGB1-NGal+Zo-16-CD206-Syndecan+_% 4.023032 0.133786 0.449107
    # 23  HMGB1-NGal+Zo-16-CD206-Syndecan-_% 0.682038 0.711045 0.897731
    # 24   HMGB1-NGal+Zo-16-Zo-1+Syndecan+_% 4.103578 0.128505 0.449107
    # 25   HMGB1-NGal+Zo-16-Zo-1+Syndecan-_% 2.842105 0.241460 0.494992
    # 26  HMGB1-NGal-Casp3+CD206-Syndecan-_% 2.342189 0.310027 0.552658
    # 27   HMGB1-NGal-Casp3+Zo-1+Syndecan-_% 2.848052 0.240743 0.494992
    # 28  HMGB1-NGal-Zo-16-CD206-Syndecan+_% 1.847452 0.397037 0.678271
    # 29  HMGB1-NGal-Zo-16-CD206-Syndecan-_% 1.739850 0.418983 0.679740
    # 30   HMGB1-NGal-Zo-16-Zo-1+Syndecan+_% 0.321970 0.851305 0.897731
    # 31   HMGB1-NGal-Zo-16-Zo-1+Syndecan-_% 1.326316 0.515222 0.782374
    # 32                       NGal+Casp3+_% 7.205765 0.027245 0.449107
    # 33                  NGal+Casp3+Zo-1+_% 4.342828 0.114016 0.449107
    # 34                    NGal+Syndecan+_% 3.612030 0.164308 0.449107
    # 35                        NGal+Zo-1+_% 1.683041 0.431055 0.679740
    # 36               NGal+Zo-1+Syndecan+_% 3.334875 0.188730 0.483621
    # 37                  Zo-1-NGal+Casp3+_% 5.491381 0.064204 0.449107
    # 38                  Zo-1-NGal+Zo-16-_% 0.682038 0.711045 0.897731
    # 39                  Zo-1-NGal-Casp3+_% 2.537176 0.281228 0.549065
    # 40                  Zo-1-NGal-Zo-16-_% 0.572264 0.751163 0.897731

# %%


kw_df.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\kw_df.pkl' )
kw_df.to_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\kw_df.xlsx' , index=False )

# %%'

# patterns with significant statistical result.
sig_patterns = kw_df.loc[kw_df["p_fdr"] < 0.05, "time"]

sig_patterns
    # Out[52]: Series([], Name: time, dtype: object)

# %% plot  _  NGal+Casp3+

pattern = "NGal+Casp3+_%"

df_plot = combined_pct_8[
    combined_pct_8["time"] == pattern
].copy()

# %%%'

rename_dict = {
                'DBD-HTK': 'SCS-HTK' ,
                'DBD-Ecosol' : 'SCS-Omnisol' ,
                'NMP' : 'NMP-Omnisol'
}


df_plot['treatment'].replace( to_replace=rename_dict , inplace=True )


# %%%'

# no colors for different treatment groups !
    # they are distinguished on the x-axis.

# Define a custom palette for the hue levels in the desired order

# custom_palette = { 
#                     "SCS-HTK": "green", 
#                     "SCS-Omnisol": "blue", 
#                     "NMP-Omnisol": "red" 
# }

# %%%'

# using catplot instead of directly using pointplot lets you direclty control the hight & aspect ratio of the figure !
# dodge : 0.4 : makes a higher dodge , but at the cost of entangled connection lines !!
g = sns.catplot( 
                kind ='point',
                data = df_plot ,
                x='treatment' , 
                y='value' ,  # choose between : 'value' , 'value_bc' , 'value_yjt', 'value_bc_yjt'
                # hue="treatment" ,
                estimator='median' ,    
                marker="_" ,  # for the median.
                markersize=40, # length ( breadth ) of the median lines.
                markeredgewidth=5,  # thickness of the median lines.
                color='black' ,
                errorbar=None ,
                # err_kws={"color": "black", "linewidth": 2} ,  # cap can also be defined here.
                # dodge=0.2 ,  #  TRUE , 0.4
                height=8, 
                aspect=1 ,
                # palette=custom_palette,
                linestyles=""
) 

# %%%'

# Create the stripplot
g.map_dataframe(
                sns.stripplot,
                x='treatment',
                y='value',
                # hue='treatment',
                dodge=0.01,
                jitter=False,
                size=12,
                linewidth=2 ,
                color='cornflowerblue' ,   # #6C757D
                edgecolor = 'black' ,  
                # palette=custom_palette
)

# %%%'

# Set y-axis to log scale
# g.set(yscale="log")

# g.set(ylim=(0, 1500))


# %%%'

g._legend.set_title("" )  # group _ the original legend title is the column name ( treatment )

# Increase the font size of the legend title
g._legend.get_title().set_fontsize(20)  # Adjust the size as needed

for text in g._legend.texts:
    text.set_fontsize(20)  # Adjust as needed

# %%%'

for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=0 , fontsize=18)

# Remove automatic axis ( row & column in the grid ) labels from all subplots
g.set_axis_labels("", "")

# Set the x-axis label for the bottom-right subplot to "stage"
g.axes.flat[-1].set_xlabel("\n Treatment group" , loc='right' , fontsize=22 )

# %%%'

plt.ylabel( "cell count(%)", loc="top" , rotation=90  )

# %%%'

plt.title('Cells with NGal+ & Casp3+ markers.'
          '\n Horizontal bars are medians. \n'
          )

# %%%'

# unit = [ 
#         'ng/ml' ,
#         'µg/ml' ,
# ]

# for ax , i in zip( g.axes.flat , unit ) :
#     ax.set_ylabel( i , loc='top' , fontsize=16 )

# %%%'

# x= : the x location of the text in figure coordinates.
# plt.title( 'NGAL (serum) \n SD'   # Change from baseline of
#              # '\n ( after outlier removal )'    # outlier removal_   after baseline correction _ baseline as explantation time
#              , x=0.4 
#              , fontsize=24 )
#  \n mean_sd   #  for pointplot

# %%%'

# rect : to avoid overlapping of the legend on the figure.
plt.tight_layout()

# %%%'

# FileNotFoundError: you mistakenly pasted C/code ... path instead of the one-drive path !
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\plot\NGal_Casp3.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\plot\NGal_Casp3.svg' )


# %% PCA

combined_pct_8.rename( columns={ 'time' : 'pattern' } , inplace=True )

rename_dict = {
                'DBD-HTK': 'SCS-HTK' ,
                'DBD-Ecosol' : 'SCS-Omnisol' ,
                'NMP' : 'NMP-Omnisol'
}


combined_pct_8['treatment'].replace( to_replace=rename_dict , inplace=True )

# %%%'

X = (
        combined_pct_8
        .pivot(index="sample_ID", columns="pattern", values="value")
        .fillna(0)
)

# %%%'

X.shape
    # Out[11]: (18, 41)

X.iloc[ :4 , :4 ]
    # Out[18]: 
    # pattern    Casp3+Zo-1+_%  HMGB1+Casp3+_%  HMGB1+Casp3+Zo-1+_%  HMGB1+NGal+_%
    # sample_ID                                                                   
    # ZC04            0.032740        0.003720             0.002020       0.431469
    # ZC05            0.011236        0.076553             0.001279       0.119579
    # ZC07            0.032665        0.016690             0.015856       0.053051
    # ZC08            0.014186        0.033017             0.008913       0.046952

# %%%'

meta = (
        combined_pct_8
        .drop_duplicates("sample_ID")
        .set_index("sample_ID")[["treatment"]]
)

# %%%'

meta.shape
    # Out[20]: (18, 1)

meta[:10]
    # Out[21]: 
    #             treatment
    # sample_ID            
    # ZC05       DBD-Ecosol
    # ZC07       DBD-Ecosol
    # ZC09       DBD-Ecosol
    # ZC11       DBD-Ecosol
    # ZC14       DBD-Ecosol
    # ZC15       DBD-Ecosol
    # ZC04          DBD-HTK
    # ZC08          DBD-HTK
    # ZC10          DBD-HTK
    # ZC23          DBD-HTK

# %%%'

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# %%%'


# z_score !
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
pcs = pca.fit_transform(X_scaled)

# %%%'

pcs.shape
    # Out[27]: (18, 2)

pcs[:10]
    # Out[28]: 
    # array([[ 5.11760428,  4.46182894],
    #        [-2.47705254,  4.51309221],
    #        [-3.26899102,  3.58624909],
    #        [-1.91222503,  2.00065323],
    #        [ 2.2046287 , -3.85119903],
    #        [-1.58335273, -2.31715449],
    #        [-1.6961007 , -1.21581561],
    #        [ 1.35351656, -2.44524944],
    #        [-0.89058975,  5.03219145],
    #        [ 0.85386526, -1.14518222]])

# %%%'

pca_df = pd.DataFrame(
                        pcs, columns=["PC1", "PC2"], index=X.index
                    ).join(meta)


pca_df.shape
    # Out[30]: (18, 3)

pca_df[:10]
    # Out[31]: 
    #                 PC1       PC2   treatment
    # sample_ID                                
    # ZC04       5.117604  4.461829     DBD-HTK
    # ZC05      -2.477053  4.513092  DBD-Ecosol
    # ZC07      -3.268991  3.586249  DBD-Ecosol
    # ZC08      -1.912225  2.000653     DBD-HTK
    # ZC09       2.204629 -3.851199  DBD-Ecosol
    # ZC10      -1.583353 -2.317154     DBD-HTK
    # ZC11      -1.696101 -1.215816  DBD-Ecosol
    # ZC14       1.353517 -2.445249  DBD-Ecosol
    # ZC15      -0.890590  5.032191  DBD-Ecosol
    # ZC23       0.853865 -1.145182     DBD-HTK

# Plot PC1 vs PC2 colored by treatment.

# %%% plot

custom_palette = { 
                    "SCS-HTK": "green", 
                    "SCS-Omnisol": "blue", 
                    "NMP-Omnisol": "red" 
}

# %%%'

fig, ax = plt.subplots(figsize=(11, 8))

sns.scatterplot(
    data=pca_df,
    x="PC1",
    y="PC2",
    hue="treatment",
    s=120,
    edgecolor="black",
    linewidth=1,
    palette=custom_palette,
    ax=ax
)

ax.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
ax.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")

ax.set_title("PCA of multiplex co-expression profiles")

ax.legend(
    title="Treatment",
    frameon=False,
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

fig.tight_layout()
plt.show()


# %%%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\plot\PCA.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\plot\PCA.svg' )

# %% permanova

from skbio.stats.distance import permanova
from skbio.stats.distance import DistanceMatrix
from scipy.spatial.distance import pdist, squareform

# %%%'

dist = squareform(pdist(X, metric="braycurtis"))
dm = DistanceMatrix(dist, ids=X.index)

permanova(
    dm,
    meta["treatment"],
    permutations=999
)

    # Out[18]: 
    # method name               PERMANOVA
    # test statistic name        pseudo-F
    # sample size                      18
    # number of groups                  3
    # test statistic             1.139122
    # p-value                    0.345000
    # number of permutations          999
    # Name: PERMANOVA results, dtype: object

# %% heatmap

# from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage

# %%%'

dist = pdist( X, metric="braycurtis")

Z = linkage( dist, method="average")

# %%%'

# treatment_colors = {
#     "DBD-HTK": 'green' ,    # "#1f77b4",
#     "DBD-Ecosol": 'blue' ,  # "#ff7f0e",
#     "NMP": 'red'            # "#2ca02c"
# }

treatment_colors = { 
                    "SCS-HTK": "green", 
                    "SCS-Omnisol": "blue", 
                    "NMP-Omnisol": "red" 
}

# col_colors = meta["treatment"].map(treatment_colors)
row_colors = meta["treatment"].map(treatment_colors)


col_colors
    # Out[40]: 
    # sample_ID
    # ZC05     blue
    # ZC07     blue
    # ZC09     blue
    # ZC11     blue
    # ZC14     blue
    # ZC15     blue
    # ZC04    green
    # ZC08    green
    # ZC10    green
    # ZC23    green
    # ZC35    green
    # ZC37    green
    # ZC38    green
    # ZC61      red
    # ZC63      red
    # ZC66      red
    # ZC67      red
    # ZC68      red
    # Name: treatment, dtype: category
    # Categories (3, object): ['green' < 'blue' < 'red']

# %%%'

X_plot = X.copy()
X_plot.columns = X_plot.columns.str.replace("_%", "", regex=False)

# %%%'

g = sns.clustermap(
                    X_plot,
                    row_cluster=True,
                    col_cluster=True,
                    metric="braycurtis",
                    method="average",
                    # col_colors=col_colors,
                    row_colors = row_colors ,
                    cmap="viridis",
                    
                    # ← increase height & width substantially
                    # otherwise all of the row & olumn names will not be shown.
                    figsize=(25, 18),   
                    z_score=0 ,  # : axis = 0  :  •	Z score per column (pattern) !
                    
                    # dendrogram_ratio=(0.15, 0.15), 
                    # colors_ratio=0.05 # ← makes the color bar thicker
    )

# %%% color-bar

# Move colorbar
g.cax.set_position([0.02, 0.05, 0.02, 0.25])
g.cax.set_ylabel("Z-score" , loc='bottom' )  # (per pattern)

# %%% treatment-group legend 

from matplotlib.patches import Patch

# %%%%' 

# treatment-legend

handles = [
    Patch(facecolor=color, label=label)
    for label, color in treatment_colors.items()
]

g.ax_heatmap.legend(
    handles=handles,
    title="Treatment",
    loc="lower left",
    bbox_to_anchor=(-0.35, -0.4 ),
    frameon=False
)

# %%%'

plt.suptitle('Exploratory hierarchical clustering and heatmap of multiplex co-expression patterns' , 
             x=0.6 ,
             fontsize=24 
             )

# %%%'


# no effect.
# plt.setp(
#     g.ax_heatmap.get_xticklabels(),
#     rotation=90,
#     ha="center"
# )

    # Out[31]: 
    # [None,
    #  None,
    #  None,
    #  None,
    #  None,
    #  None,
    #  ...]

    # in total 28 ?

# %%%'

# not good : disruts the dendrogram & color-bar.
# plt.tight_layout()

# %%%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\plot\heatmap_7.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\plot\heatmap_7.svg' )

# %%'

# C:\code\kidney\histology\multiplex\extract_multiplex.py
multiplex_7 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\multiplex_7.pkl' )

# %%




