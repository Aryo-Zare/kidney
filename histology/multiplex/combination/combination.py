
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


# %%'

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

# %%

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


# %%'

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

# %%

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

# %%

# vectorized cleanup
# the parenthesis is only for more clear expression :
    # splitting the line & indentation.
combined_pct_5['sample_ID'] = (
                                combined_pct_5['sample_ID']
                                .str.upper()                    # make everything uppercase
                                .replace( r'\..*$' , '' , regex=True )  # drop dot-suffix and everything after.
)

# %%

combined_pct_5['sample_ID'].unique()
    # Out[58]: 
    # array(['ZC40', 'ZC42', 'ZC49', 'ZC50', 'ZC51', 'ZC52', 'ZC58', 'ZC59',
    #        'ZC05', 'ZC07', 'ZC09', 'ZC11', 'ZC14', 'ZC15', 'ZC27', 'ZC04',
    #        'ZC08', 'ZC10', 'ZC23', 'ZC35', 'ZC37', 'ZC38', 'ZC24', 'ZC25',
    #        'ZC26', 'ZC31', 'ZC32', 'ZC33', 'ZC34', 'ZC44', 'ZC47', 'ZC48',
    #        'ZC53', 'ZC55', 'ZC56', 'ZC60', 'ZC61', 'ZC62', 'ZC63', 'ZC65',
    #        'ZC66', 'ZC67', 'ZC68', 'ZC17', 'ZC19', 'ZC20', 'ZC21', 'ZC22',
    #        'ZC29', 'ZC30'], dtype=object)

# %%

combined_pct_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_5.pkl' )

combined_pct_5 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_5.pkl' )


# %%'  filter

# filter based on treatment, sample_ID & time.

mask = \
        ( combined_pct_5["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & \
        ( ~combined_pct_5["sample_ID"].isin([ "ZC06", "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) ) 


# Sample DataFrame (assuming df_serum_chem_5_bc is already loaded)
combined_pct_6 = combined_pct_5[ mask ]

# %%

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

# %%

combined_pct_7.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\histology\multiplex\combined\combined_pct_7.pkl' )

# %%


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

# %%

