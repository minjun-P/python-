from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT',start='2018-05-04')

def make_dpc(stock):
    dpc = (stock['Close']/stock['Close'].shift(1)-1)*100
    dpc[0]=0
    dpc_cs = dpc.cumsum()
    return dpc,dpc_cs

sec_dpc,sec_dpc_cs = make_dpc(sec)
msft_dpc,msft_dpc_cs = make_dpc(msft)

import matplotlib.pyplot as plt

plt.plot(sec.index,sec_dpc_cs,'b',label='Samsung Electronic')
plt.plot(msft.index,msft_dpc_cs,'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()

