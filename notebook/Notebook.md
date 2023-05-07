
# Reproducibility Summary

We have successfully replicated the results of the StageNet model on the MIMIC-III decompensation risk prediction task, with only minor deviations from the original paper: AUPRC by 0.9%, AUROC by 0.4%, and min(Re, P+) by 6%. 

Furthermore, we conducted an ablation test by removing the convolution module from the model. Our findings indicate that the convolution module significantly impacts the StageNet's performance. Additionally, we tuned the model's hyperparameters, including hidden dimension and chunk size, and observed a decrease in model performance with reduced hyperparameter values. However, the effect on AUROC was minimal. We also generated a small sample dataset to validate different parameter settings.

To ensure reproducibility, we followed the MIMIC-III benchmark preprocessing steps. We utilized the Google Colab premium platform for training and testing purposes.


# Overview of the data 

The StageNet utilized two datasets, namely, ESRD
and MIMIC III. However, due to the private nature
of the former, access to it was unavailable to us. In
contrast, the MIMIC III (Medical Information Mart
for Intensive Care III) dataset is a publicly accessi-
ble dataset that features de-identified health-related
information of over 40,000 patients admitted to the
Beth Israel Deaconess Medical Center in Boston,
Massachusetts, USA, from 2001 to 2012 [2]. You can
obtained access to this dataset through an applica-
tion submitted to physionet.org. Some statistics is
shown in table below  [1][2]
| -| Number | 
|------------------|------------------|
| #patients| Over 40,000 | 
| #ICU stays  | 53,423 | 
| #visit with positive label  | 45,364|
| #visit with negative label  | 2,156,750  | 


# Overview of the methodology and experiments run

The input data is first preprocessed and split into
different stages based on the disease progression
extracting information about ICU stays and other
events from the MIMIC-III dataset for a patient.
The output dataset has a time series of each patient
based on ICU stays. The model is then trained
to predict the health risk for each stage separately,
using the corresponding input data. During infer-
ence, the model predicts the risk for each stage and
aggregates the predictions to obtain the final risk
estimate.
Specifically, the model has two types of modules
as Figure 1 shows. At time-step t, the stage-aware
LSTM module uses the elapsed time and patient’s
current visit information to calculate the current
hidden state and the current variation in disease
stage. These hidden states are then inputted into a
“stage-adaptive” convolutional module. This con-
volutional module extracts progression patterns at
the current disease stage and adjusts these patterns
using the so-called progression theme. Finally, the
adjusted patterns are used to predict the patient’s
health risk.

Please check the executable code examples [stagenet_train.ipynb](https://github.com/hbattat/cs598-dlh-project/blob/main/notebook/stagenet_train.ipynb), for the preprocessing, please refer to [preprocessing.ipynb](https://github.com/hbattat/cs598-dlh-project/blob/main/notebook/preprocessing.ipynb) please note that you need to have access to MIMIC-III dataset.

# Summary of the key results.

| Model | AUPRC | AUROC | min(Re, P+)
|------------------|------------------|------------------|------------------|
| Original | 0.323  | 0.903  | 0.372 |
| Pre-Trained Model  | 0.337  | 0.903  | 0.372 |
| Reproduced*  | 0.320  | 0.907  | 0.348 |
| Parameter Tunning**  | 0.261  | 0.885  | 0.296 |
|Ablation Model | 0.193  | 0.873  | 0.274 |


* Same setup with the original paper with different batch size 1440 vs 128
** Use hidden dimention of 72 and chunk size 36 VS Original paper 384 and 128
Error between reproduced result and the original Paper: AUPRC 0.9%, AUROC 0.4%, min(Re,P+) 6%


# References 

[1]Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas M. Glass, Jimeng Sun. 2020. 
StageNet: Stage-Aware Neural Networks for Health Risk Prediction. 
In Proceedings of The Web Conference 2020 (WWW ’20), April 20–24, 2020, Taipei, Taiwan. ACM, New York, NY, USA, 11 pages. 
https://doi.org/10.1145/3366423.3380136
[2] https://physionet.org/content/mimiciii/1.4/

[3][StageNet](https://github.com/v1xerunt/StageNet)

[4][MIMIC-III Benchmarks](https://github.com/YerevaNN/mimic3-benchmarks/)

