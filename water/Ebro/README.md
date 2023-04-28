If more data is needed it can be requested here https://saica.chebro.es/sugerencias.php

## How to download data quickly

Copy and paste the following url in the browser:

https://saica.chebro.es/exportrun.php?tag=11113&fini=01-01-2011&ffin=31-12-2016

Notice that it has three parameters:
	tag: each variable of each station has a unique tag. Get from tags.txt
	fini: desired starting date in format mm/dd/yyyy (>= 01/01/1997).
	finf: desired end date in format mm/dd/yyyy (<= today).

OJO porque no parece que estén todas las estaciones. No fiable.

Lo que habría que hacer sería ir a la página de descarga:

https://saica.chebro.es/export.php

Seleccionar la variable deseada (con un intervalo grande para que nos de tiempo a copiar el url) y darle a generar el txt. 
De esa forma se abrirá la pantalla de descarga y se nos mostrará su url, por ejemplo:

https://saica.chebro.es/exportrun.php?tag=7022&fini=28-01-2018&ffin=28-02-2023

De esta forma ya sabemos la tag adecuada y nos ahorramos hacer 4 intervalos de 5 años con simplemente cambiar los parámetros fini y ffin.

## How txt_joiner.py works

1. Starts from the original files downloaded, for example:
	ammonium 9904.txt, ammonium 0510.txt, ammonium 1116.txt, ammonium 1722.txt.

	The parameter 'folderNames' defines the station to process and the parameter 'fileNames' the variables in the station.

	Each file contains data from the 5 years defined in the name. It had to be done this way because 5 years in the maximum range the website allows.

2. Delete the first 10 rows of each file. These rows contain information on the station and the variables, but they are not time series data.

3. Concatenate the data from the 4 files of each variable.

4. Check if the first row is 01-01-1999 00:00:00 and if not, add it.

5. Check if the last row is 31-12-2022 23:45:00 and if not, add it.

6. The output for the example given aboved would be: ammonium_{station numer}


