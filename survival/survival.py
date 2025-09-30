
# %%

# the non-standard 'ZC6' entry was renamed to 'ZC06' via Excel itself.
overview_2 = pd.read_excel( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\overview_2.xlsx' , header=[0,1] )  # , index_col=0 

# %%

survival_column_index = column_index_from_string("AN") - 1

survival_column_index 
    # Out[14]: 39


cols_to_keep = np.r_[ 0:3 , survival_column_index ] 

cols_to_keep
    # Out[16]: array([ 0,  1,  2, 39])

# bg : blood gass
df_survival = overview_2.iloc[ : , cols_to_keep ]

df_survival[:4]
    # Out[18]: 
    #           Sample ID:          Treatment             Group:       Survival days
    #   Unnamed: 0_level_1 Unnamed: 1_level_1 Unnamed: 2_level_1 Unnamed: 39_level_1
    # 0               ZC04            DBD-HTK                  1                   6
    # 1               ZC05         DBD-Ecosol                  2                   7
    # 2               ZC06            DBD-HTK                  1                   5
    # 3               ZC07         DBD-Ecosol                  2                   7

df_survival.shape
    # Out[19]: (82, 4)

# %%

df_survival.iloc[:,0].unique()
    # Out[20]: 
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

df_survival.columns
    # Out[21]: 
    # MultiIndex([(   'Sample ID:',  'Unnamed: 0_level_1'),
    #             (    'Treatment',  'Unnamed: 1_level_1'),
    #             (       'Group:',  'Unnamed: 2_level_1'),
    #             ('Survival days', 'Unnamed: 39_level_1')],
    #            )


# first level of the multi-index columns.
first_level = df_survival.columns.get_level_values(0)

first_level
    # Out[23]: Index(['Sample ID:', 'Treatment', 'Group:', 'Survival days'], dtype='object')


new_header = first_level.tolist()

new_header
    # Out[25]: ['Sample ID:', 'Treatment', 'Group:', 'Survival days']

# remediting the names : removing the spaces , ... .
new_header_2 = ['sample_ID', 'treatment', 'group', 'survival']

# assigining the newheaders.
df_survival.columns = new_header_2

df_survival[:4]
    # Out[28]: 
    #   sample_ID   treatment group survival
    # 0      ZC04     DBD-HTK     1        6
    # 1      ZC05  DBD-Ecosol     2        7
    # 2      ZC06     DBD-HTK     1        5
    # 3      ZC07  DBD-Ecosol     2        7


# %%

mask = (
        ( df_survival["treatment"].isin(["DBD-HTK", "DBD-Ecosol", "NMP"]) ) & 
        ( ~df_survival["sample_ID"].isin([ "ZC06" , "ZC28" , 'ZC27' , 'ZC60' , 'ZC62' , 'ZC64' , 'ZC65' ]) )  
)

df_survival_2 = df_survival[mask]

df_survival_2.shape
    # Out[32]: (19, 4)

# %%

df_survival_2.groupby( 'treatment' ).describe()
    # Out[33]: 
    #            sample_ID                   group                 survival         \
    #                count unique   top freq count unique top freq    count unique   
    # treatment                                                                      
    # DBD-Ecosol         6      6  ZC05    1     6      1   2    6        6      1   
    # DBD-HTK            7      7  ZC04    1     7      1   1    7        7      2   
    # NMP                6      6  ZC61    1     6      1   0    6        6      2   
    
                         
    #            top freq  
    # treatment            
    # DBD-Ecosol   7    6  
    # DBD-HTK      7    6  
    # NMP          7    5  

# %%

df_survival_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\survival.pkl' )

# %%

g = sns.catplot(
                kind="strip" ,
                data=df_survival_2 , 
                x='treatment', 
                y='survival', 
                # hue='treatment',\
                size=9 ,
                height=7, 
                aspect=1.5 ,
)

# %%
    
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\plot\survival.pdf' )


# %%




