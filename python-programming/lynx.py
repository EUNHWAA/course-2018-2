import pandas as pd

lynx1=pd.read_csv("lynx.csv")
lynx1
lynx1["time"]=round(lynx1["time"]/10)
sum_lynx1=lynx1.groupby("time").sum()
sum_lynx1.sort_values("time",ascending=False)
