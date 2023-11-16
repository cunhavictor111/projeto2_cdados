import pandas as pd

df1 = pd.read_csv(r"C:\Users\Victor Cunha\Downloads\Projeto2.csv")
df1.to_excel(r"C:\Users\Victor Cunha\Downloads\Projeto2.xlsx", index=False)
