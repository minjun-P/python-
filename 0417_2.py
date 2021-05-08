import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
from scipy import stats
import matplotlib.pyplot as plt

tlt = pdr.get_data_yahoo('TLT','2002-07-30')
kospi = pdr.get_data_yahoo('^KS11','2002-07-30')

df = pd.DataFrame({'X':tlt.Close,'Y':kospi.Close})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

regr = stats.linregress(df.X,df.Y)
regr_line = f'Y = {regr.slope:.2f}*X + {regr.intercept:.2f}'
print(regr)
plt.figure(figsize=(7,7))
plt.plot(df.X,df.Y,'.')
plt.plot(df.X, regr.slope*df.X+regr.intercept, 'r')
plt.legend(['DOW x KOSPI', regr_line])
plt.title(f'DOW x KOSPI ( R = {regr.rvalue:.2f})')
plt.xlabel('TLT')
plt.ylabel('KOSPI')
plt.show()
