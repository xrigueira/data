"""This program can be used to download data from meteorological stations from AEMET (Spanish Meteorological Agency).

1. First, identify the station you are interested in. You can do this by using the following URL:https://www.aemet.es/es/eltiempo/observacion/ultimosdatos_3129_datos-horarios.csv

2. Second, you need to get the ID of the station you are interested in. To do this, run the second step (first cell) and go to "datos" in the output

3. Finally, you can download the data of the station you are interested in by running the third step (second cell). To get the URL needed go to https://opendata.aemet.es/dist/index.html?
Then "valores-climatoloficos and use the first option "climatologías diarias" where we need the start and end dates and the ID of the desired station. Lastly, go to "datos" in the output
and convert the JSON file to a CSV file using an online converter.

I also found two helpful YouTube videos that explain how to get the data from AEMET:

1. https://www.youtube.com/watch?v=wGNYqLOq4fE&ab_channel=AEMET

2. https://www.youtube.com/watch?v=gntHivOmT_U&ab_channel=AEMET

The second explains this process, while the frist one explains how to get the data using the more user-friendly interface of AEMET.
"""

import requests

#%% Second step
# To get the ID of all stations, which is needed in the next step.
# url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

# querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4dXJ4by5yaWd1ZWlyYUB1dmlnby5nYWwiLCJqdGkiOiJhNjJhN2RlOC00ZTgzLTRjMTgtODFhNS0xMmRlMjNmYTBlYzgiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcxMjg0MzM5OCwidXNlcklkIjoiYTYyYTdkZTgtNGU4My00YzE4LTgxYTUtMTJkZTIzZmEwZWM4Iiwicm9sZSI6IiJ9.BuITNWV5ZeAf02nnOaCDz8YR6fqve7JaPB1u1bg27D8"}

# headers = {
#     'cache-control': "no-cache"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

#%% Third step
# To download the data of a specific station.
url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2019-01-01T00%3A00%3A00UTC/fechafin/2023-12-31T00%3A00%3A00UTC/estacion/9501X"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4dXJ4by5yaWd1ZWlyYUB1dmlnby5nYWwiLCJqdGkiOiJhNjJhN2RlOC00ZTgzLTRjMTgtODFhNS0xMmRlMjNmYTBlYzgiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcxMjg0MzM5OCwidXNlcklkIjoiYTYyYTdkZTgtNGU4My00YzE4LTgxYTUtMTJkZTIzZmEwZWM4Iiwicm9sZSI6IiJ9.BuITNWV5ZeAf02nnOaCDz8YR6fqve7JaPB1u1bg27D8"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
