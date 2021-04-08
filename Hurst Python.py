# pip install pandas-datareader
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data
from hurst import compute_Hc, random_walk
series = data.get_data_yahoo('UL', start='2010-01-01', end='2020-01-01')['Adj Close']
# Evaluate Hurst equation
# pip install hurst
H, c, data = compute_Hc(series)

# Plot
f, ax = plt.subplots()
ax.plot(data[0], c*data[0]**H, color="black", label='H=0,5794 c=1,0766')
ax.scatter(data[0], data[1], color="blue")
ax.set_xscale('log')
ax.set_yscale('log')
ax.grid(False)
plt.legend(loc='lower right',title='Esponente di Hurst')
ax.set_xlabel('Log (n)')
ax.set_ylabel('Log (R/S)')
plt.title('Test R/S Allianz')
plt.savefig('AllianzRS.png', dpi=300)
plt.show()



print("Esponente di Hurst = {:.4f}, c={:.4f}".format(H,c))

# series = pd.read_csv('file')
