# Supporting data and tools for "Toward automating post processing of aquatic sensor data"

The files contained here are inputs, outputs, and processing scripts that support the analysis and visualization in the paper "Toward automating post processing of aquatic sensor data". The following files and directories are included and described in greater detail:

- **LRO_data:** Raw sensor observations that were used as inputs. Also include technician labels and corrections.
- **DetectionResults:** Results of anomaly detection are in the directory. 
- **CorrectionResults:** Results of anomaly correction. 
- **ConfusionMatrixPlots.py, DetectionPlots.py, CorrectionPlots.py:** Scripts to generate plots in the manuscript
- **detect_script.py, correct_script.py:** Scripts used to perform anomaly detection or correction that generated the output.

To reproduce figures shown in the paper, refer to the scripts ConfusionMatrixPlots.py, DetectionPlots.py, and CorrectionPlots.py.

The code provided in this resource was developed using Python 3.70. The following Python packages are required for running the scripts:
pandas 1.1.5, matplotlib 3.4.2, pyhydroqc 0.0.4, numpy 1.19.5.

## File Organization and Description

### LRO_data
This directory contains csv files with time series for each monitoring location. Each file corresponds to a single year of data. The files are named according to monitoring site (FranklinBasin, TonyGrove, WaterLab, MainStreet, Mendon, BlackSmithFork) and year. The files were sourced by querying the Logan River Observatory relational database, and equaivalent data could be obtained from the [LRO website](http://lrodata.usu.edu/tsa/) or on [HydroShare](https://www.hydroshare.org/search/?q=logan%20river%20observatory). Additional information on sites, variables, and methods can be found on the LRO website or HydroShare. Each file has the same structure indexed with a datetime column (mountain standard time) with three columns corresponding to each variable. Variable abbreviations and units are:

- **temp:** water temperature, degrees C 
- **cond:** specific conductance, μS/cm 
- **ph:** pH, standard units 
- **do:** dissolved oxygen, mg/L
- **turb:** turbidity, NTU
- **stage:** stage height, cm

For each variable, there are 3 columns:

1. Raw data value measured by the sensor (column header is the variable abbreviation).
2. Technician quality controlled (corrected) value (column header is the variable abbreviation appended with '\_cor').
3. Technician labels/qualifiers (column header is the variable abbreviation appended with '\_qual').

The directory also contains files with lists of dates for sensor calibrations at the MainStret site (MainStreet_cond_calib_dates.csv, MainStreet_ph_calib_dates.csv, MainStreet_do_calib_dates.csv). The dates were determined from technicians records and field notes. There is a separate file for each calibrated sensor (specific conductance (cond), pH (ph), dissolved oxygen (do)). Each file contains the following columns: 

- **start:** Start date for the period of drift. This is the first point to be corrected by linear dirft correction. 
- **end:** End date for the period of drift corresponding to a calibration event. 
- **gap:** When correction was performed by technicians, the data were shifted by this value. 


### DetectionResults
This directory contains the results of anomaly detection using the pyhydroqc functions and workflow. Results are organized by monitoring site with a zipped directory for each site (FranklinBasin, TonyGrove, WaterLab, MainStreet, Mendon, BlackSmithFork). Each zipped directory contains separate files organized by model, variable, and result type. File names include abbreviations for model, variable, and result type.

####Models: designated by the following abbreviations in the file name.

- **ARIMA:** autoregressive integrated moving average
- **LSTM_univar:** long short term memory univariate vanilla
- **LSTM_univar_bidir:** long short term memory univariate bidirectional
- **LSTM_multivar:** long short term memory multivariate
- **LSTM_Multivar_bidir:** long short term memory multivariate bidirectional

####Variables: designated by the variable abbreviation appended to the file name.

- **temp:** water temperature, degrees C
- **ph:** pH, standard units
- **cond:** specific conductance, μS/cm
- **do:** dissolved oxygen, mg/L

####Result types: There are several files containing results. Each result type corresponds to a combination of model and variable with the following abbreviations in the file name.

- **df or df_anomalies:** a table of inputs and outputs to the pyhydroqc workflow containing the following columns:
	- **datetime:** date time index
	- **raw:** sensor measured value
	- **cor:** technician corrected value
	- **labeled_anomaly:** boolean indicating technician labeled anomaly
	- **anomaly:** boolean indicating anomaly detected by rules based detection
	- **observed:** sensor measured values after passing through rules based detection and correction
	- **obs_scaled:** observed values scaled by the scikitlearn standard scaler
	- **raw_scaled:** raw values scaled by the scikitlearn standard scaler
	- **labeled_event:** numbering of technician labeled anomalies grouped into events
	- **detected_anomaly:** boolearn indicating anomaly detected by model based detection
	- **all_anomalies:** boolean combining rules based and model based detection
	- **detected_event:** numbering of combined rules based and model based detection grouped into events
	- **grp:** numbering of anomalies and non-anomalous groups
	- **conf_mtx:** identification of each point as true negative (tn), true positive (tp), false negative (fn), false positive (fp)


- **threshold:** a table of dynamic threshold values for each point containing the following columns:
	- **datetime:** date time index
	- **low:** the lower bound of the threshold
	- **high:** the upper bound of the threshold


- **detections:** a table with model predictions, residuals, and anomalies detected by the pyhydroqc workflow containing the following columns:
	- **datetime:** date time index
	- **observed:** sensor measured values after passing through rules based detection and correction
	- **prediction:** values predicted by the model
	- **residual:** difference between the observed and prediction
	- **anomaly:** boolean indicating anomaly detected by model based deteection


- **aggregate:** a table compiling anomaly detections from all models and comparing to technician labels containing the following columns:
	- **datetime:** date time index
	- **ARIMA:** boolean indiating anomaly detected by the ARIMA model workflow
	- **LSTM_van_uni:** boolean indicating anomaly detected by LSTM vanilla univariate model workflow
	- **LSTM_bidir_uni:** boolean indicating anomaly detected by LSTM bidirectional univariate model workflow
	- **LSTM_van_multi:** boolean indicating anomaly detected by LSTM vanilla multivariate model workflow
	- **LSTM_bidir_multi:** boolean indicating anomaly detected by LSTM bidirectional multivariate model workflow
	- **detected_event:** boolean indicating anomaly detected by any of the models (the previous 5 columns) grouped into events
	- **labeled_anomaly:** boolean indicating technician labeled anomaly
	- **labeled_event:** numbering of technician labeled anomalies grouped into events
	- **grp:** numbering of anomalies and non-anomalous groups
	- **conf_mtx:** identification of each point as true negative (tn), true positive (tp), false negative (fn), false positive (fp)


- **metrics:** pickled python object that contains the metrics determined by the pyhydroqc 'metrics' function (true positives, false positives, true negatives, false negatives, positive predictive value, negative predictive value, accuracy, recall, F1, F2)


### CorrectionResults
This directory contains the results of anomaly correction using the pyhydroqc functions and workflow. Results are organized into files corresponding to each monitoring site (FranklinBasin, TonyGrove, WaterLab, MainStreet, Mendon, BlackSmithFork) and variable (temp: water temperature (degrees C), ph: pH (standard units), cond: specific conductance (μS/cm), do: dissolved oxygen (mg/L)). Each file contatins the following columns:

- **datetime:** date time index
- **ARIMA:** boolean indiating anomaly detected by the ARIMA model workflow
- **detected_event:** boolean indicating anomaly detected by any of the models grouped into events
- **observed:** sensor measured values after passing through rules based detection and correction
- **det_cor:** correction estimate determined by the pyhydroqc correction workflow
- **corrected:** boolean indicating whether the correction was performed
- **forecasts:** for corrected points, the foreward looking estimates used in the correction algorithm
- **backcasts:** for corrected points, the backward looking estimates used in the correction algorithm


### ConfusionMatrixPlots.py
This script contains commands to generate Figures 6 and 7 in the manuscript. The script contains the data, which were generated from a run of the pyhydroqc workflow for all sites and all variables. These figures illustrate the confusion matrix for each series by showing the portion of true positives, false negatives, and false positives for both the rules based and model based anomaly detection. Figure 6 shows these for all model types and Figure 7 shows an aggregate for each series.

### DetectionPlots.py
This script contains commands to generate Figures 3, 4, 5, C1, C2, C3, C4 focuesed on anomaly detection. Many of the plots use consistent symbology and show observed data, model predictions, technician labeled anomalies, and algorithm detected anomalies for specific date ranges identified in data series of interest. Some of the figures are generated from importing raw data and running pyhydroqc commands while others are generated by importing pyhydroqc results. The necessary files are found in the folders 'LROData' and 'Plotting/SelectedResults'.

### CorrectionPlots.py
This script contains commands to generate Figures 8 and C5 focused on anomaly correction. These plots use consistent symbology and show observed data, model corrected data, and technician corrected data (where appropriate) along with the forecasts and backcasts used to generate the model corrections for specific date ranges identified in data series of interest. The figures are generated by importing PyHdydroQC results. The necessary files are found in the folder 'Plotting/SelectedResults'.

### SelectedResults
This directory contains files with detection and correction results used for plotting in the scripts DetectionPlots.py and CorrectionPlots.py. The files are a subset of the detection and correction results for data series selected for illustration in the figures. The structure of each file is as described under DetectionResults and CorrectionResults sections of this file.

### detect_script.py
This is the script used to generate the results in the DetectionResults directory. It runs the pyhydroqc anomaly detection workflow for all LRO monitoring sites and variables. It runs the workflows for all model types, calculates metrics, aggregates the results, and saves the results as csv files and as pickled object.  This script used raw data with the necessary files found in the folder 'LROData'. Note that this script was created with a previous version of pyhydroqc and continuing compatibility has not been verified. This script is time and resource demanding as is mostly provided as a reference. 

### correct_script.py
This is the script used to generate the results in the CorrectionResults directory. It runs the pyhydroqc ARIMA anomaly detection workflow all LRO monitoring sites and variables and then performs anomaly correction on identified anomalies. It saves the corrections as csv files. This script used raw data with the necessary files found in the folder 'LROData'. This script is time and resource demanding as is mostly provided as a reference. 
