
# copying the data corresponding to each figure in the 'Vivalyx' folder.

# %%

df_serum_chem_6_od_or_yjt_2.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\df_serum_chem_6_od_or_yjt_2.csv' )

df_bg_8_2.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\df_bg_8_2.csv' )

df_urine_8_2.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\df_urine_8_2.csv' )

df_rd_3.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\df_rd_3.csv' )

df_NGAL_2.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\df_NGAL_2.csv' )

df_hist_7.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\df_hist_7.csv' )

multiplex_11.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\multiplex_11.csv' )

# %%

df_serum_chem_6_od_or_yjt_2_dropped = df_serum_chem_6_od_or_yjt_2.drop( columns=
                                                                               [
                                                                                'baseline_value',
                                                                                'value_bc',
                                                                                'value_yjt',
                                                                                'value_bc_yjt'
                                                                                ]
)

# %%

df_bg_8_2_dropped = df_bg_8_2.drop( columns=
                                            [
                                             'baseline_value',
                                             'value_bc',
                                             'value_yjt',
                                             'value_bc_yjt'
                                             ]
)


# %%

df_urine_8_2_dropped = df_urine_8_2.drop( columns=
                                            [
                                             'baseline_value',
                                             'value_bc',
                                             'value_yjt',
                                             'value_bc_yjt'
                                             ]
)

# %%

df_rd_3_dropped = df_rd_3.drop( columns=
                                            [
                                             'baseline_value',
                                             'value_bc',
                                             'value_yjt',
                                             'value_bc_yjt'
                                             ]
)


# %%


df_NGAL_2_dropped = df_NGAL_2.drop( columns=
                                            [
                                             'baseline_value',
                                             'value_bc',
                                             'value_yjt',
                                             'value_bc_yjt'
                                             ]
)


# %%

df_hist_7_dropped = df_hist_7.drop( columns= [ 'value_yjt' ])


# %%

multiplex_11[:4]
    # Out[44]: 
    #    sample_ID   treatment biomarker      cnp
    # 8       ZC05  DBD-Ecosol  HMGB1+_% 0.529383
    # 9       ZC07  DBD-Ecosol  HMGB1+_% 0.165114
    # 10      ZC09  DBD-Ecosol  HMGB1+_% 0.227194
    # 11      ZC11  DBD-Ecosol  HMGB1+_% 0.062555

# %%
# %%

df_serum_chem_6_od_or_yjt_2_dropped.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\dropped\df_serum_chem_6_od_or_yjt_2_dropped.csv' )

df_bg_8_2_dropped.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\dropped\df_bg_8_2_dropped.csv' )

df_urine_8_2_dropped.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\dropped\df_urine_8_2_dropped.csv' )

df_rd_3_dropped.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\dropped\df_rd_3_dropped.csv' )

df_NGAL_2_dropped.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\dropped\df_NGAL_2_dropped.csv' )

df_hist_7_dropped.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\dropped\df_hist_7_dropped.csv' )

multiplex_11.to_csv( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\Vivalyx\dropped\multiplex_11.csv' )


# %%


