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




# References
Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas M. Glass, Jimeng Sun. 2020. 
StageNet: Stage-Aware Neural Networks for Health Risk Prediction. 
In Proceedings of The Web Conference 2020 (WWW ’20), April 20–24, 2020, Taipei, Taiwan. ACM, New York, NY, USA, 11 pages. 
https://doi.org/10.1145/3366423.3380136
