

# %%

df_urine_8_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_urine_8_3.pkl' )

df_rd_4 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\urine\rd\df_rd_4.pkl' )

df_serum_chem_ucr_value_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\ucr\df_serum_chem_ucr_value_3.pkl' )

df_bg_8_3 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\BG\df_bg_8_3.pkl' )


# %%
# rename back to the original names.

# %%

rename_dict = {
                'SCS-HTK' : 'DBD-HTK' ,
                'SCS-Omnisol' : 'DBD-Ecosol' ,
                'NMP-Omnisol' : 'NMP' 
}

# %%


rename_dict = {
                'DBD-Omnisol' : 'DBD-Ecosol'
}

# %%

df_bg_8_3['treatment'].replace( to_replace=rename_dict , inplace=True )


# %%' yjt

# Yeo-Johnson transformation , separate for each metric.
# from sklearn.preprocessing import PowerTransformer

df = df_bg_8_3.copy()

df["value_yjt"] = np.nan  # initialize column

for met in df["metric"].unique():
    idx = df["metric"] == met   #  masking index
    values = df.loc[idx, "value"].values.reshape(-1, 1)

    pt = PowerTransformer(method="yeo-johnson", standardize=False)
    transformed = pt.fit_transform(values)

    df.loc[idx, "value_yjt"] = transformed.flatten()

# %%

df.dropna(subset=["value_yjt", "value"], inplace=True)

# %%

