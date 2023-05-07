1.ablation_test.txt contains the test result of the model without the convolutional module.

2.reproduced.txt contains the result of using the same original paper hyperparameter, except using 1440 batch size instead of 128 to speed up the training.

3.small_sample_result.txt contains the test results of using 400 random generated samples with different parameter set.

4.trained_model is trained weights by using full MIMIC-III decompensation train set. 

5.parameter_tuning_results.txt contains the test result of the model with hidden dimention of 72 and chunk size of 36
