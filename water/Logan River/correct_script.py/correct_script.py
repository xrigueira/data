#####################################################
### SINGLE SITE ANOMALY DETECTION AND CORRECTION
#####################################################

#### Import Libraries and Functions
from pyhydroqc import anomaly_utilities
from pyhydroqc import model_workflow
from pyhydroqc import rules_detect
from pyhydroqc import arima_correct
from pyhydroqc.parameters import site_params

#####################################################
### FRANKLIN BASIN
#####################################################

#### Retrieve data
#########################################
site = 'FranklinBasin'
sensors = ['temp', 'cond', 'ph', 'do']
years = [2014, 2015, 2016, 2017, 2018, 2019]
sensor_array = anomaly_utilities.get_data(sensors=sensors, site=site, years=years, path="./LRO_data/")

#### Rules Based Anomaly Detection
#########################################
range_count = dict()
persist_count = dict()
rules_metrics = dict()
for snsr in sensor_array:
    sensor_array[snsr], range_count[snsr] = rules_detect.range_check(df=sensor_array[snsr],
                                                                     maximum=site_params[site][snsr].max_range,
                                                                     minimum=site_params[site][snsr].min_range)
    sensor_array[snsr], persist_count[snsr] = rules_detect.persistence(df=sensor_array[snsr],
                                                                       length=site_params[site][snsr].persist,
                                                                       output_grp=True)
    sensor_array[snsr] = rules_detect.interpolate(df=sensor_array[snsr])

#### Model Based Anomaly Detection
#########################################

##### ARIMA Detection
#########################################
ARIMA = dict()
for snsr in sensors:
    ARIMA[snsr] = model_workflow.arima_detect(
            df=sensor_array[snsr], sensor=snsr, params=site_params[site][snsr],
            rules=False, plots=False, summary=False, compare=False)
print('ARIMA detection complete.\n')

##### Aggregate Detections for All Models
#########################################
results_all = dict()
metrics_all = dict()
for snsr in sensors:
    models = dict()
    models['ARIMA'] = ARIMA[snsr].df
    results_all[snsr] = anomaly_utilities.aggregate_results(df=sensor_array[snsr],
                                                            models=models,
                                                            verbose=True,
                                                            compare=False)

#### Correction
#########################################
corrections = dict()
for snsr in sensors:
    corrections[snsr] = arima_correct.generate_corrections(df=results_all[snsr],
                                                           observed='observed',
                                                           anomalies='detected_event',
                                                           savecasts=True)
    print(snsr + 'correction complete')

# Saving corrections
for snsr in sensors:
    corrections[snsr].to_csv(r'Examples/' + site + '_' + snsr + '_corrections.csv')



#####################################################
### TONY GROVE
#####################################################

#### Retrieve data
#########################################
site = 'TonyGrove'
sensors = ['temp', 'cond', 'ph', 'do']
years = [2014, 2015, 2016, 2017, 2018, 2019]
sensor_array = anomaly_utilities.get_data(sensors=sensors, site=site, years=years, path="./LRO_data/")

#### Rules Based Anomaly Detection
#########################################
range_count = dict()
persist_count = dict()
rules_metrics = dict()
for snsr in sensor_array:
    sensor_array[snsr], range_count[snsr] = rules_detect.range_check(df=sensor_array[snsr],
                                                                     maximum=site_params[site][snsr].max_range,
                                                                     minimum=site_params[site][snsr].min_range)
    sensor_array[snsr], persist_count[snsr] = rules_detect.persistence(df=sensor_array[snsr],
                                                                       length=site_params[site][snsr].persist,
                                                                       output_grp=True)
    sensor_array[snsr] = rules_detect.interpolate(df=sensor_array[snsr])

#### Model Based Anomaly Detection
#########################################

##### ARIMA Detection
#########################################
ARIMA = dict()
for snsr in sensors:
    ARIMA[snsr] = model_workflow.arima_detect(
            df=sensor_array[snsr], sensor=snsr, params=site_params[site][snsr],
            rules=False, plots=False, summary=False, compare=False)
print('ARIMA detection complete.\n')

##### Aggregate Detections for All Models
#########################################
results_all = dict()
metrics_all = dict()
for snsr in sensors:
    models = dict()
    models['ARIMA'] = ARIMA[snsr].df
    results_all[snsr] = anomaly_utilities.aggregate_results(df=sensor_array[snsr],
                                                            models=models,
                                                            verbose=True,
                                                            compare=False)

#### Correction
#########################################
corrections = dict()
for snsr in sensors:
    corrections[snsr] = arima_correct.generate_corrections(df=results_all[snsr],
                                                           observed='observed',
                                                           anomalies='detected_event',
                                                           savecasts=True)
    print(snsr + 'correction complete')

# Saving corrections
for snsr in sensors:
    corrections[snsr].to_csv(r'Examples/' + site + '_' + snsr + '_corrections.csv')


#####################################################
### WATER LAB
#####################################################

#### Retrieve data
#########################################
site = 'Waterlab'
sensors = ['temp', 'cond', 'ph', 'do']
years = [2014, 2015, 2016, 2017, 2018, 2019]
sensor_array = anomaly_utilities.get_data(sensors=sensors, site=site, years=years, path="./LRO_data/")

#### Rules Based Anomaly Detection
#########################################
range_count = dict()
persist_count = dict()
rules_metrics = dict()
for snsr in sensor_array:
    sensor_array[snsr], range_count[snsr] = rules_detect.range_check(df=sensor_array[snsr],
                                                                     maximum=site_params[site][snsr].max_range,
                                                                     minimum=site_params[site][snsr].min_range)
    sensor_array[snsr], persist_count[snsr] = rules_detect.persistence(df=sensor_array[snsr],
                                                                       length=site_params[site][snsr].persist,
                                                                       output_grp=True)
    sensor_array[snsr] = rules_detect.interpolate(df=sensor_array[snsr])

#### Model Based Anomaly Detection
#########################################

##### ARIMA Detection
#########################################
ARIMA = dict()
for snsr in sensors:
    ARIMA[snsr] = model_workflow.arima_detect(
            df=sensor_array[snsr], sensor=snsr, params=site_params[site][snsr],
            rules=False, plots=False, summary=False, compare=False)
print('ARIMA detection complete.\n')

##### Aggregate Detections for All Models
#########################################
results_all = dict()
metrics_all = dict()
for snsr in sensors:
    models = dict()
    models['ARIMA'] = ARIMA[snsr].df
    results_all[snsr] = anomaly_utilities.aggregate_results(df=sensor_array[snsr],
                                                            models=models,
                                                            verbose=True,
                                                            compare=False)

#### Correction
#########################################
corrections = dict()
for snsr in sensors:
    corrections[snsr] = arima_correct.generate_corrections(df=results_all[snsr],
                                                           observed='observed',
                                                           anomalies='detected_event',
                                                           savecasts=True)
    print(snsr + 'correction complete')

# Saving corrections
for snsr in sensors:
    corrections[snsr].to_csv(r'Examples/' + site + '_' + snsr + '_corrections.csv')


#####################################################
### MAIN STREET
#####################################################

#### Retrieve data
#########################################
site = 'MainStreet'
sensors = ['temp', 'cond', 'ph', 'do']
years = [2014, 2015, 2016, 2017, 2018, 2019]
sensor_array = anomaly_utilities.get_data(sensors=sensors, site=site, years=years, path="./LRO_data/")

#### Rules Based Anomaly Detection
#########################################
range_count = dict()
persist_count = dict()
rules_metrics = dict()
for snsr in sensor_array:
    sensor_array[snsr], range_count[snsr] = rules_detect.range_check(df=sensor_array[snsr],
                                                                     maximum=site_params[site][snsr].max_range,
                                                                     minimum=site_params[site][snsr].min_range)
    sensor_array[snsr], persist_count[snsr] = rules_detect.persistence(df=sensor_array[snsr],
                                                                       length=site_params[site][snsr].persist,
                                                                       output_grp=True)
    sensor_array[snsr] = rules_detect.interpolate(df=sensor_array[snsr])

#### Model Based Anomaly Detection
#########################################

##### ARIMA Detection
#########################################
ARIMA = dict()
for snsr in sensors:
    ARIMA[snsr] = model_workflow.arima_detect(
            df=sensor_array[snsr], sensor=snsr, params=site_params[site][snsr],
            rules=False, plots=False, summary=False, compare=False)
print('ARIMA detection complete.\n')

##### Aggregate Detections for All Models
#########################################
results_all = dict()
metrics_all = dict()
for snsr in sensors:
    models = dict()
    models['ARIMA'] = ARIMA[snsr].df
    results_all[snsr] = anomaly_utilities.aggregate_results(df=sensor_array[snsr],
                                                            models=models,
                                                            verbose=True,
                                                            compare=False)

#### Correction
#########################################
corrections = dict()
for snsr in sensors:
    corrections[snsr] = arima_correct.generate_corrections(df=results_all[snsr],
                                                           observed='observed',
                                                           anomalies='detected_event',
                                                           savecasts=True)
    print(snsr + 'correction complete')

# Saving corrections
for snsr in sensors:
    corrections[snsr].to_csv(r'Examples/' + site + '_' + snsr + '_corrections.csv')


#####################################################
### MENDON
#####################################################

#### Retrieve data
#########################################
site = 'Mendon'
sensors = ['temp', 'cond', 'ph', 'do']
years = [2014, 2015, 2016, 2017, 2018, 2019]
sensor_array = anomaly_utilities.get_data(sensors=sensors, site=site, years=years, path="./LRO_data/")

#### Rules Based Anomaly Detection
#########################################
range_count = dict()
persist_count = dict()
rules_metrics = dict()
for snsr in sensor_array:
    sensor_array[snsr], range_count[snsr] = rules_detect.range_check(df=sensor_array[snsr],
                                                                     maximum=site_params[site][snsr].max_range,
                                                                     minimum=site_params[site][snsr].min_range)
    sensor_array[snsr], persist_count[snsr] = rules_detect.persistence(df=sensor_array[snsr],
                                                                       length=site_params[site][snsr].persist,
                                                                       output_grp=True)
    sensor_array[snsr] = rules_detect.interpolate(df=sensor_array[snsr])

#### Model Based Anomaly Detection
#########################################

##### ARIMA Detection
#########################################
ARIMA = dict()
for snsr in sensors:
    ARIMA[snsr] = model_workflow.arima_detect(
            df=sensor_array[snsr], sensor=snsr, params=site_params[site][snsr],
            rules=False, plots=False, summary=False, compare=False)
print('ARIMA detection complete.\n')

##### Aggregate Detections for All Models
#########################################
results_all = dict()
metrics_all = dict()
for snsr in sensors:
    models = dict()
    models['ARIMA'] = ARIMA[snsr].df
    results_all[snsr] = anomaly_utilities.aggregate_results(df=sensor_array[snsr],
                                                            models=models,
                                                            verbose=True,
                                                            compare=False)

#### Correction
#########################################
corrections = dict()
for snsr in sensors:
    corrections[snsr] = arima_correct.generate_corrections(df=results_all[snsr],
                                                           observed='observed',
                                                           anomalies='detected_event',
                                                           savecasts=True)
    print(snsr + 'correction complete')

# Saving corrections
for snsr in sensors:
    corrections[snsr].to_csv(r'Examples/' + site + '_' + snsr + '_corrections.csv')


#####################################################
### BLACKSMITH FORK
#####################################################

#### Retrieve data
#########################################
site = 'BlackSmithFork'
sensors = ['temp', 'cond', 'ph', 'do']
years = [2015, 2016, 2017, 2018, 2019]
sensor_array = anomaly_utilities.get_data(sensors=sensors, site=site, years=years, path="./LRO_data/")

#### Rules Based Anomaly Detection
#########################################
range_count = dict()
persist_count = dict()
rules_metrics = dict()
for snsr in sensor_array:
    sensor_array[snsr], range_count[snsr] = rules_detect.range_check(df=sensor_array[snsr],
                                                                     maximum=site_params[site][snsr].max_range,
                                                                     minimum=site_params[site][snsr].min_range)
    sensor_array[snsr], persist_count[snsr] = rules_detect.persistence(df=sensor_array[snsr],
                                                                       length=site_params[site][snsr].persist,
                                                                       output_grp=True)
    sensor_array[snsr] = rules_detect.interpolate(df=sensor_array[snsr])

#### Model Based Anomaly Detection
#########################################

##### ARIMA Detection
#########################################
ARIMA = dict()
for snsr in sensors:
    ARIMA[snsr] = model_workflow.arima_detect(
            df=sensor_array[snsr], sensor=snsr, params=site_params[site][snsr],
            rules=False, plots=False, summary=False, compare=False)
print('ARIMA detection complete.\n')

##### Aggregate Detections for All Models
#########################################
results_all = dict()
metrics_all = dict()
for snsr in sensors:
    models = dict()
    models['ARIMA'] = ARIMA[snsr].df
    results_all[snsr] = anomaly_utilities.aggregate_results(df=sensor_array[snsr],
                                                            models=models,
                                                            verbose=True,
                                                            compare=False)

#### Correction
#########################################
corrections = dict()
for snsr in sensors:
    corrections[snsr] = arima_correct.generate_corrections(df=results_all[snsr],
                                                           observed='observed',
                                                           anomalies='detected_event',
                                                           savecasts=True)
    print(snsr + 'correction complete')

# Saving corrections
for snsr in sensors:
    corrections[snsr].to_csv(r'Examples/' + site + '_' + snsr + '_corrections.csv')

##################################################################################
