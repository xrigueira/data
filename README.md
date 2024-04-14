# data
 Contains several time series databases for research purposes.

## Algorithms and datasets
 [This](https://github.com/rob-med/awesome-TS-anomaly-detection) is a very nice collection of anomaly detection algorithms and several anomaly-labeled databases at the end of the webside: NAB, Yahoo's, and SKAB.

## Numenta/NAB
One of the most widely used labeled databases for the validation of **univariate** anomaly detection methods. [Kaggle - NAB](https://www.kaggle.com/datasets/boltzmannbrain/nab). [GitHub - NAB](https://github.com/numenta/NAB). The NAB corpus of 58 timeseries data files is designed to provide data for research in streaming anomaly detection. It is comprised of both real-world and artifical timeseries data containing labeled anomalous periods of behavior. The majority of the data is real-world from a variety of sources such as AWS server metrics, Twitter volume, advertisement clicking metrics, traffic data, and more.

## Yahoo's Webscope S5
Another one of the most widely labeled **univariate** databases for the same purposes. [website - Webscope S5](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70). The dataset consists of real and synthetic time-series with tagged anomaly points. The dataset tests the detection accuracy of various anomaly-types including outliers and change-points. The synthetic dataset consists of time-series with varying trend, noise and seasonality. The real dataset consists of time-series representing the metrics of various Yahoo services.

## SKAB
Skoltech Anomaly Benchmark (SKAB) is designed for evaluating **multivariate** anomaly detection algorithms. [Kaggle - SKAB](https://www.kaggle.com/datasets/yuriykatser/skoltech-anomaly-benchmark-skab). [GitHub - SKAB](https://github.com/waico/SkAB) It allows working with two main problems: outlier detection and changepoint detection. It is composed of (i) datasets, (ii) leaderboard (scoreboard), (iii) python modules for algorithms’ evaluation, and (iv) notebooks: python notebooks with anomaly detection algorithms.

## scarlat database
 It contains **11 variables** with more than 509k data points each plus their labels which account for a total of 443 rows.
 [Kaggle -scarlat database](https://www.kaggle.com/code/drscarlat/anomaly-detection-in-multivariate-time-series/notebook)

## TSB-UAD benchmark
 The TSB-UAD benchmark is presented in [this research paper](https://dl.acm.org/doi/10.14778/3529337.3529354). It contains 18 public databases with labeled anomalies (including NAB and Yahoo's) and some artificially generated data. The downside is that it is for univariate methods. The public datasets can be downloaded [here](http://chaos.cs.uchicago.edu/tsb-uad/public.zip)
 [GitHub - TSB-UAD database](https://github.com/TheDatumOrg/TSB-UAD).

## TODS System
 TODS is a full-stack automated machine learning system for outlier detection on multivariate time-series data. It includes labeled databases such as NAB, KPI and Yahoo's. [Here](https://github.com/datamllab/tods/tree/benchmark/benchmark/realworld_data) is how to download the data.

## Exathlon benchmark
The dataset of this benchmark, characterized by its high dimensionality, was constructed based on real data traces collected from around 100 repeated executions of 10 distributed streaming jobs on a Spark cluster over 2.5 months. The traces were obtained by disturbing more than 30 job executions with nearly 100 instances of 6 different classes of anomalous events (e.g., misbehaving inputs, resource contention, process failures). For each of these anomalies, ground truth labels are provided for both the root cause interval and the corresponding effect interval, enabling the use of our dataset in a wide range of AD and ED tasks. Overall, both the normal (undisturbed) and anomalous (disturbed) traces contain enough variety (including some noise due to Spark’s inherent behavior) to capture real-world data characteristics in this domain. [Here is the original research paper](https://arxiv.org/pdf/2010.05073.pdf).
The dataset, code, and documentation for Exathlon are publicly available [here](https://github.com/exathlonbenchmark/exathlon).

## Coventry database
 It includes several models for data generation presented *Section III. Benchmark Results and Analysis* of [this research paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7388055&tag=1).


