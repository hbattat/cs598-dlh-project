# CS598-DL4H-Project

This project is a reproduction of [StageNet](https://github.com/v1xerunt/StageNet), and the data preprocessing stage applies the [MIMIC-III Benchmarks](https://github.com/YerevaNN/mimic3-benchmarks/) workflow.

The model.py and train.py files are modified versions of StageNet files used for abalation test, as well as hidden_dim and chunk_size test.

# [The video demo]

# Result

| Model | AUPRC | AUROC | min(Re, P+)
|------------------|------------------|------------------|------------------|
| Original | 0.323  | 0.903  | 0.372 |
| Pre-Trained Model  | 0.337  | 0.903  | 0.372 |
| Reproduced  | 0.320  | 0.907  | 0.348 |
| Reduced Model  | Row 3, Column 2  | Row 3, Column 3  |
|Ablation Model | 0.193  | 0.873  | 0.274 |

Error between reproduced result and the original Paper: AUPRC 0.9%, AUROC 0.4%, min(Re,P+) 6%

# Running the code
## Preprocessing (MIMIC-III Benchmark)
```python
import os
from sh import gunzip
```

## Data Preperation
To prepare the data for StageNet, we need to download the data an process it using MIMIC-III Benchmark to procduce the decompensation data.

### Download
To obtain the full MIMIC-III dataset, download the files from physionet.org using your credentialed account. First set an environment variable for the username and password.


```python
!wget -r -N -c -np --user <username> --password <password> https://physionet.org/files/mimiciii/1.4/
```

### Extract Files
Once the file as are obtained, extact all the files.


```python
MIMIC3_DIR = './physionet.org/files/mimiciii/1.4/'
for filename in os.listdir(MIMIC3_DIR):
    f = os.path.join(MIMIC3_DIR, filename)
    if os.path.isfile(f):
        gunzip(f)
```

## Data Processing

### Clone the repo
Copy the original benchmark code to run the steps on the extracted CSV files


```python
!git clone https://github.com/YerevaNN/mimic3-benchmarks.git
%cd mimic3-benchmarks
```

### Install dependencies
The code uses python 3.7. The following steps run using python3.7, assuming it is installed properly and the executable is present the user bin directory.


```python
!pip3.7 install -r requirements.txt
```

### Step 1: Generate subject directories
This step generates one directory per SUBJECT_ID and writes ICU stay information to data/{SUBJECT_ID}/stays.csv, diagnoses to data/{SUBJECT_ID}/diagnoses.csv, and events to data/{SUBJECT_ID}/events.csv.


```python
!python3.7 -m mimic3benchmark.scripts.extract_subjects ../physionet.org/files/mimiciii/1.4/ data/root/
```

### Step 2: Data cleaning
This step attempts to fix some issues with each subject ID data. Some of the fixes:
- Remove all events for which HADM_ID is missing.
- Remove all events for which HADM_ID is not present in stays.csv.
- If ICUSTAY_ID is missing in an event and HADM_ID is not missing, then we look at stays.csv and try to recover ICUSTAY_ID.
- Remove all events for which we cannot recover ICUSTAY_ID.
- Remove all events for which ICUSTAY_ID is not present in stays.csv.


```python
!python3.7 -m mimic3benchmark.scripts.validate_events data/root/
```

### Step 3: Generate episodes time series
This step breaks up each subject ICU stays into individual time seriese. Time series of events are stored in {SUBJECT_ID}/episode{#}_timeseries.csv (where # counts distinct episodes) while episode-level information (patient age, gender, ethnicity, height, weight) and outcomes (mortality, length of stay, diagnoses) are stores in {SUBJECT_ID}/episode{#}.csv


```python
!python3.7 -m mimic3benchmark.scripts.extract_episodes_from_subjects data/root/
```

### Step 4: Split traning/testing data
This step splits the whole dataset into training and testing datasets.


```python
 !python3.7 -m mimic3benchmark.scripts.split_train_and_test data/root/
```

### Step 5: Generate decompensation data
This step generates the decompensation data needed for StageNet


```python
!python3.7 -m mimic3benchmark.scripts.create_in_hospital_mortality data/root/ data/in-hospital-mortality/
!python3.7 -m mimic3benchmark.scripts.create_decompensation data/root/ data/decompensation/
```


# References
Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas M. Glass, Jimeng Sun. 2020. 
StageNet: Stage-Aware Neural Networks for Health Risk Prediction. 
In Proceedings of The Web Conference 2020 (WWW ’20), April 20–24, 2020, Taipei, Taiwan. ACM, New York, NY, USA, 11 pages. 
https://doi.org/10.1145/3366423.3380136

[StageNet](https://github.com/v1xerunt/StageNet)

[MIMIC-III Benchmarks](https://github.com/YerevaNN/mimic3-benchmarks/)
