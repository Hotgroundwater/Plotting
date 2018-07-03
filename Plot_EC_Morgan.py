import numpy as np
import pandas as pd
from pandas import read_csv,Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns



directory = "D:\\"##"C:\\Users\\xxxx\\Documents\\Python_test\\inputfiles\\"
outfile = "D:\\"##"C:\\Users\\xxxx\\Documents\\Python_test\\Out_files\\"
obsfile = "HistoricalAverageEC_Morgan.csv" ###### change file name

sns.set(style="darkgrid")


##
df = pd.read_csv(directory+obsfile, sep = ',', delimiter = ',')###need to specify header otherwise it will give 1 column
df = pd.DataFrame(df, columns = ['Year','EC','Target'])
df1 = df['Year'].astype(int)
df2 = df['EC']
df3 = df['Target']
no_rows, no_cols = df.shape 
print (no_rows, no_cols)

xmin,xmax, xinterval = min(df1), max(df1)+3 ,10
##ymax = 160 ###
##ymin = 0

fig = plt.figure( figsize=(15,15) )
ax = df.plot(x = 'Year',y = 'EC',color='blue',linewidth=0.75,label= 'Historical Salinity', fontsize =20)##,linestyle='dashed'
df.plot(x = 'Year',y = 'Target',ax= ax,color ='orange',linestyle='solid',label= 'Basin Salinity Target', linewidth = 2,fontsize =20)

ax.set_xlim(xmin,xmax, xinterval)
ax.set_ylim(0, 2000, 500)
plt.rc("font", size = 20)## font size for all labels
plt.xlabel('Year', fontsize =20 )
plt.ylabel('EC',fontsize =20)
plt.title('Salinity at Morgan',weight = 'bold', fontsize=24)
plt.legend(loc='best', fontsize = 20)
plt.show()

##plt.savefig(directory + filename +'out.png')##dpi=600  
##plt.clf()
##plt.close()
##print ("completed")
