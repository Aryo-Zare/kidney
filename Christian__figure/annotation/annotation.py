

# %%



# %% manual annotation with function !

# this does not work since I had removed the x ticks before : 
        # g.set(xticks=[])
        # :
            # # test
            # xticks = {label.get_text(): pos for pos, label in enumerate(ax.get_xticklabels())}

            # xticks
            #     # Out[63]: {}



def add_sig_bar(ax, group1, group2, y_offset=0.05, text="*"):
    # Get the x positions of the categories
    xticks = {label.get_text(): pos for pos, label in enumerate(ax.get_xticklabels())}
    x1, x2 = xticks[group1], xticks[group2]
    y = ax.get_ylim()[1] * (1 - y_offset)
    h = (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.02
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c='k')
    ax.text((x1+x2)/2, y+h, text, ha='center', va='bottom', fontsize=16)

# Usage
ax = g.axes.flatten()[3]
add_sig_bar(ax, "SCS-Omnisol", "NMP-Omnisol", text="**")


# %%

# Get the correct axis (subplot-D is index 3 if 0-based)
ax = g.axes.flatten()[3]

# Define the pairs you want to annotate
pairs = [("SCS-HTK", "SCS-Omnisol")]

# Subset the dataframe to only the biomarker shown in subplot-D
df_subset = multiplex_13[multiplex_13["biomarker"] == "Zo-1+_%"]

# Create the annotator
annotator = Annotator(
    ax,
    pairs,
    data=df_subset,
    x="treatment",
    y="cnp",
    order=["SCS-HTK", "SCS-Omnisol", "NMP-Omnisol"],  # ensure consistent order
    hue=None  # hue not needed since x encodes treatment
)

# Configure how the annotation should look
annotator.configure(
    test=None,              # you already know it's significant, so skip test
    text_format="star",     # show stars instead of p-values
    loc="outside",          # place bar outside the plot area
    fontsize=16
)

# Apply the annotation
annotator.set_pvalues([0.03])  # or whatever your actual p-value is
annotator.annotate()


# %%'
# %%'

# %%'  info

# multiplex_13['biomarker'].value_counts()
#     # Out[26]: 
#     # biomarker
#     # HMGB1+_%       18
#     # NGAL+_%        18
#     # Casp3+_%       18
#     # Zo-1+_%        18
#     # Syndecan+_%    18
#     # Name: count, dtype: int64

# multiplex_13[:4]
#     # Out[27]: 
#     #    sample_ID    treatment biomarker      cnp
#     # 8       ZC05  SCS-Omnisol  HMGB1+_% 0.529383
#     # 9       ZC07  SCS-Omnisol  HMGB1+_% 0.165114
#     # 10      ZC09  SCS-Omnisol  HMGB1+_% 0.227194
#     # 11      ZC11  SCS-Omnisol  HMGB1+_% 0.062555

# multiplex_13.dtypes
#     # Out[28]: 
#     # sample_ID      object
#     # treatment    category
#     # biomarker    category
#     # cnp           float64
#     # dtype: object

# df_subset
#     # Out[43]: 
#     #     sample_ID    treatment biomarker       cnp
#     # 179      ZC05  SCS-Omnisol   Zo-1+_%  1.755413
#     # 180      ZC07  SCS-Omnisol   Zo-1+_%  2.043836
#     # 181      ZC09  SCS-Omnisol   Zo-1+_%  2.534376
#     # 182      ZC11  SCS-Omnisol   Zo-1+_%  0.440731
#     # 183      ZC14  SCS-Omnisol   Zo-1+_%  0.475583
#     # 184      ZC15  SCS-Omnisol   Zo-1+_%  0.267382
#     # 186      ZC04      SCS-HTK   Zo-1+_% 28.733793
#     # 187      ZC08      SCS-HTK   Zo-1+_%  5.382421
#     # 188      ZC10      SCS-HTK   Zo-1+_%  0.305836
#     # 189      ZC23      SCS-HTK   Zo-1+_%  0.000669
#     # 190      ZC35      SCS-HTK   Zo-1+_% 11.633191
#     # 191      ZC37      SCS-HTK   Zo-1+_%  4.824107
#     # 192      ZC38      SCS-HTK   Zo-1+_%  0.250362
#     # 207      ZC61  NMP-Omnisol   Zo-1+_% 14.205230
#     # 209      ZC63  NMP-Omnisol   Zo-1+_%  0.026254
#     # 211      ZC66  NMP-Omnisol   Zo-1+_%  0.047061
#     # 212      ZC67  NMP-Omnisol   Zo-1+_%  1.836251
#     # 213      ZC68  NMP-Omnisol   Zo-1+_%  0.051995


# g.axes
#     # Out[48]: 
#     # array([<Axes: title={'center': 'HMGB1'}, ylabel='cell count(%)'>,
#     #        <Axes: title={'center': 'NGAL'}>,
#     #        <Axes: title={'center': 'Casp3'}>,
#     #        <Axes: title={'center': 'Zo-1'}, ylabel='cell count(%)'>,
#     #        <Axes: title={'center': 'Syndecan'}>], dtype=object)

# %%'

# Grab subplot-D (Zo-1 biomarker)
ax = g.axes.flatten()[3]

# Subset the dataframe to Zo-1 only
df_subset = multiplex_13[multiplex_13["biomarker"] == "Zo-1+_%"]

# Define the order of categories on the x-axis
order = ["SCS-HTK", "SCS-Omnisol", "NMP-Omnisol"]

# Define the pair you want to annotate
# pairs = [("SCS-HTK", "SCS-Omnisol")]
# pairs = [("SCS-HTK", "NMP-Omnisol")]
pairs = [("SCS-Omnisol", "NMP-Omnisol")]

# Create the annotator
annotator = Annotator(ax, pairs, data=df_subset, x="treatment", y="cnp" ,  order=order)

# Configure appearance
annotator.configure(text_format="star", loc="outside", fontsize=16)

# Supply your p-value (or use a test if you want statannotations to compute it)
annotator.set_pvalues([0.01])  # replace with your actual p-value
annotator.annotate()

# ValueError: Missing x value(s) `"NMP-Omnisol", "SCS-HTK", "SCS-Omnisol"` in None (specified in `order`)

# %%

df_subset = multiplex_13[multiplex_13["biomarker"] == "Zo-1+_%"].copy()
df_subset["treatment"] = df_subset["treatment"].astype(str)  # drop categorical dtype

order = ["SCS-HTK", "SCS-Omnisol", "NMP-Omnisol"]
pairs = [("SCS-Omnisol", "NMP-Omnisol")]

annotator = Annotator(ax, pairs, data=df_subset, x="treatment", y="cnp", order=order)
annotator.configure(text_format="star", loc="outside", fontsize=16)
annotator.set_pvalues([0.01])
annotator.annotate()


# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\kidney\manuscript\Christian__figure\annotation\test_annotation_4.pdf' )

# %%
