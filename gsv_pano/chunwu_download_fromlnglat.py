import pano
import pandas as pd
import os
import json

df = pd.read_excel(r"C:\Local Storage\Code\StreetView\gsv_pano\chunwu\Calveston_Lat_lon.xlsx")

l = len(df)

path = r'C:\Local Storage\Code\StreetView\gsv_pano\chunwu\json'

k = pano.GSV_pano()

for i in range(0,l):
    x,p = k.getPanoJsonfrmLonat_chunwu(str(df.loc[i]['Longitude']),str(df.loc[i]['Latitude']))
    
    try:
        with open(os.path.join(path, str(p) + '.json'), 'w') as f:
            json.dump(x, f)
    except Exception as e:
        print(e)
    input()
