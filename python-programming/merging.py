import pandas as pd

population=pd.read_csv("population.csv",index_col="State")

df=pd.merge(alco2009.reset_index(),population.reset_index()).set_index("State")

