import pyqrcode
import pandas as pd    
data = pd.read_excel('C:/Users/DELL/OneDrive/Desktop/New programs/example1.xlsx')  
def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]
for i in range(0,len(data)):
    a=str(data.loc[i])
    url = pyqrcode.create(remove_last_line_from_string(a)) 
    url.png(f'./Qrcodes/{data.loc[i][0]}.png', scale = 6)
  
