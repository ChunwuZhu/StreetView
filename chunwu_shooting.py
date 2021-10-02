from GPano_chunwu import GPano
import pandas as pd
import os
import json

df = pd.read_excel(r"C:\Local Storage\Code\StreetView\gsv_pano\chunwu\Calveston_Lat_lon.xlsx")

l = len(df)

path = r'C:\Local Storage\Code\StreetView\gsv_pano\chunwu\shoot'

k = GPano()
for i in range(0,l):
    k.shootLonlat(str(df.loc[i]['Longitude']),str(df.loc[i]['Latitude']),saved_path=path)
    
