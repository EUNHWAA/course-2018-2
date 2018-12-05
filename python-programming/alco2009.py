import pandas as pd
alco2009=pd.read_csv("niaa-report2009.csv", index_col="State")

print(alco2009.max())
print(alco2009.min(axis=1))
print(alco2009.sum())

alco=pd.read_csv("niaaa-report.csv", index_col=["State","Year"])
alco["Total"]=alco.Wine+alco.Spirits+alco.Beer
print(alco.head())

cats=pd.cut(alco2009["Wine"],3).lables
print(cats)
wine_state=alco2009["Wine"]>alco2009["Wine"].mean()
beer_state=alco2009["Beer"]>alco2009["Beer"].mean()
pd.crosstab(wine_state,beer_state)
