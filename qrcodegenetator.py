import pyqrcode
import pandas as pd    
data = pd.read_excel('C:/Users/DELL/OneDrive/Desktop/New programs/example1.xlsx')  
for i in range(0,len(data)):
    s=''
    for j in range(0,len(data.columns)):
        s=s+str(data.columns[j])+':'+str(data.loc[i][j])+(f",\n" if j<len(data.columns)-1 else ' ')
    print(s)
    url = pyqrcode.create(s)
    url.png(f'{data.loc[i][0]}_QRcode.png', scale = 6)
  
