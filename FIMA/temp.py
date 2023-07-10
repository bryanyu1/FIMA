import pandas as pd

df = pd.read_csv("FIMA/FimaNfipClaimsV1.csv")

df1 = df[:len(df)//3]
df2 = df[len(df)//3: 2*len(df)//3]
df3 = df[2*len(df)//3:]

df1.to_csv("FIMA/FimaNfipClaimsV1_1.csv")
df2.to_csv("FIMA/FimaNfipClaimsV1_2.csv")
df3.to_csv("FIMA/FimaNfipClaimsV1_3.csv")
