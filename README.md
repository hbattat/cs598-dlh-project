# CS598-DL4H-Project

This project is a reproduction of [StageNet](https://github.com/v1xerunt/StageNet), and the data preprocessing stage applies the [MIMIC-III Benchmarks](https://github.com/YerevaNN/mimic3-benchmarks/) workflow.

The model.py and train.py files are modified versions of StageNet files used for abalation test, as well as hidden_dim and chunk_size test.

# Demo Video

[![Demo Video](https://github.com/hbattat/cs598-dlh-project/blob/main/yt.png?raw=true)](https://youtu.be/lQGDX9ScNbQ)



# Running the code
## Preprocessing (MIMIC-III Benchmark)
If you run this code in a Jupyter Notebook or Google Colab, see the ipynb files under notebook/, otherwise, follow the steps here:

### Clone the mimic3-benchmark repo

```bash
git clone https://github.com/YerevaNN/mimic3-benchmarks.git
cd mimic3-benchmarks
```

### Install dependencies
```bash
pip3 install sh
pip3 install -r requirements.txt
```
_requirements file in the mimic3-benchmark repo_

### Obtain the data
To obtain the full MIMIC-III dataset, download the files from physionet.org using your credentialed account. First set an environment variable for the username and password.


```bash
wget -r -N -c -np --user <username> --password <password> https://physionet.org/files/mimiciii/1.4/
```

You need to provide the username and passoword for your physionet account to access the data.

### Extract Files
Once the file as are obtained, extact all the files.


```bash
cd physionet.org/files/mimiciii/1.4/
for f in `ls *.gz`; do gunzip $f; done;
```

### Data Processing

#### Step 1: Generate subject directories
This step generates one directory per SUBJECT_ID and writes ICU stay information to data/{SUBJECT_ID}/stays.csv, diagnoses to data/{SUBJECT_ID}/diagnoses.csv, and events to data/{SUBJECT_ID}/events.csv.


```bash
python3 -m mimic3benchmark.scripts.extract_subjects ../physionet.org/files/mimiciii/1.4/ data/root/
```

### Step 2: Data cleaning
This step attempts to fix some issues with each subject ID data. Some of the fixes:
- Remove all events for which HADM_ID is missing.
- Remove all events for which HADM_ID is not present in stays.csv.
- If ICUSTAY_ID is missing in an event and HADM_ID is not missing, then we look at stays.csv and try to recover ICUSTAY_ID.
- Remove all events for which we cannot recover ICUSTAY_ID.
- Remove all events for which ICUSTAY_ID is not present in stays.csv.


```bash
python3 -m mimic3benchmark.scripts.validate_events data/root/
```

### Step 3: Generate episodes time series
This step breaks up each subject ICU stays into individual time seriese. Time series of events are stored in {SUBJECT_ID}/episode{#}_timeseries.csv (where # counts distinct episodes) while episode-level information (patient age, gender, ethnicity, height, weight) and outcomes (mortality, length of stay, diagnoses) are stores in {SUBJECT_ID}/episode{#}.csv


```bash
python3 -m mimic3benchmark.scripts.extract_episodes_from_subjects data/root/
```

### Step 4: Split traning/testing data
This step splits the whole dataset into training and testing datasets.


```bash
python3 -m mimic3benchmark.scripts.split_train_and_test data/root/
```

### Step 5: Generate decompensation data
This step generates the decompensation data needed for StageNet


```bash
python3 -m mimic3benchmark.scripts.create_in_hospital_mortality data/root/ data/in-hospital-mortality/
python3 -m mimic3benchmark.scripts.create_decompensation data/root/ data/decompensation/
```

## Training the model
### Install dependencies


```bash
pip3 install numpy matplotlib torch scipy scikit-learn
```

### Clone StageNet repo

```bash
git clone https://github.com/v1xerunt/StageNet.git
```

### Replace modified files (model.py and train.py)

```bash
cp model.py StageNet/model.py
cp train.py StageNet/train.py
```

### Download decompensation data

We also need the decompensation data from the preprocessing step. We download the result files and extract them into the data direcotory of StageNet


```bash
wget -o decompensation.tar.gz https://files.home.battat.us/api/public/dl/I0mJUD39
```

### Extract decompensation into StageNet data dir

```bash
tar -xkvf decompensation.tar.gz -C StageNet/data/
mv StageNet/data/train/listfile.csv StageNet/data/train_listfile.csv
mv StageNet/data/test/listfile.csv StageNet/data/test_listfile.csv
cd StageNet/
```

### Train the model with original paper specs

```bash
python3 train.py --batch_size 3600  --test_mode=0 --data_path='./data/' --file_name='original_model'
```

### Train the model with pre-trained weights

```bash
python3 train.py --batch_size 3600  --test_mode=1 --data_path='./data/' --file_name='test_model'
```

### Train the model with reduced architecture 
```bash
python3 train.py --batch_size 3600  --ablation=1 --test_mode=0 --data_path='./data/' --file_name='test_model'
```

# References
Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas M. Glass, Jimeng Sun. 2020. 
StageNet: Stage-Aware Neural Networks for Health Risk Prediction. 
In Proceedings of The Web Conference 2020 (WWW ’20), April 20–24, 2020, Taipei, Taiwan. ACM, New York, NY, USA, 11 pages. 
https://doi.org/10.1145/3366423.3380136

[StageNet](https://github.com/v1xerunt/StageNet)

[MIMIC-III Benchmarks](https://github.com/YerevaNN/mimic3-benchmarks/)
