import pandas as pd
alco2009=pd.read_csv("niaa-report2009.csv", index_col="State")

print(alco2009.max())
print(alco2009.min(axis=1))
print(alco2009.sum())

alco=pd.read.csv("niaaa-report2009.csv", index_col=["State","Year"])
