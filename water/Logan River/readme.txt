This repo contains the data from this paper: https://www.sciencedirect.com/science/article/pii/S1364815222000706?via%3Dihub

And its resources are here: https://www.hydroshare.org/resource/a6ea89ae20354e39b3c9f1228997e27a/

The labeled data are in the folder LRO_data. More specifically in the <var name>_qual columns for each variable.
Anomalies are marked with number. So all that is not NULL in those columns.

HOWEVER, this study aimed to detect anomalies from sensors, such as
wrong measurements, calibrations or gaps. (It fills the gaps smartly).
Once the data is corrected, they perform anomaly detection witth ARIMA and
several types or LSTM. Therefore I should use the data contained in the folder DetectionResults
In particular, those file that have 'df' in their name. 

There is one for each model used for anomaly detector. I would have to chose the results of best model according 
to the paper, which is ARIMA if I am not wrong, or include the results of
all models to get the actual anomalies. On top of that we have a column telling
if each sample was labeled by the experts. So the goal would be to train my model
on the corrected data to see if it finds both the anomalies of the experts and the
models used in the paper.

The columns in the 'df' files are:

df or df_anomalies: a table of inputs and outputs to the pyhydroqc workflow containing the following columns:

    datetime: date time index
    raw: sensor measured value
    cor: technician corrected value
    labeled_anomaly: boolean indicating technician labeled anomaly
    anomaly: boolean indicating anomaly detected by rules based detection
    observed: sensor measured values after passing through rules based detection and correction
    obs_scaled: observed values scaled by the scikitlearn standard scaler
    raw_scaled: raw values scaled by the scikitlearn standard scaler
    labeled_event: numbering of technician labeled anomalies grouped into events
    detected_anomaly: boolearn indicating anomaly detected by model based detection
    all_anomalies: boolean combining rules based and model based detection
    detected_event: numbering of combined rules based and model based detection grouped into events
    grp: numbering of anomalies and non-anomalous groups
    conf_mtx: identification of each point as true negative (tn), true positive (tp), false negative (fn), false positive (fp)