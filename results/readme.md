1.ablation_test.txt contains the test result of the model without the convolutional module.

2.reproduced.txt contains the result of using the same original paper hyperparameter, except using 1440 batch size instead of 128 to speed up the training.

3.small_sample_result.txt contains the test results of using 400 random generated samples with different parameter set.

4.trained_model is trained weights by using full MIMIC-III decompensation train set. 

5.parameter_tuning_results.txt contains the test result of the model with hidden dimention of 72 and chunk size of 36

# Summary Of The Key Results

| Model | AUPRC | AUROC | min(Re, P+)
|------------------|------------------|------------------|------------------|
| Original | 0.323  | 0.903  | 0.372 |
| Pre-Trained Model  | 0.337  | 0.903  | 0.372 |
| Reproduced  | 0.320  | 0.907  | 0.348 |
| Parameter Tunning  | 0.261  | 0.885  | 0.296 |
|Ablation Model | 0.193  | 0.873  | 0.274 |

Error between reproduced result and the original Paper: AUPRC 0.9%, AUROC 0.4%, min(Re,P+) 6%
