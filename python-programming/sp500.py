import pandas as pd
import statistics
from scipy.stats import pearsonr

sp500=pd.read_csv("sp21.csv",index_col="Date")
print(sp500["Close"].mean())
print(sp500["Close"].std())
print(sp500["Close"].skew())
type(sp500.ix["2001-01-02"])
pearsonr(sp500["Volume"],sp500["Close"])

