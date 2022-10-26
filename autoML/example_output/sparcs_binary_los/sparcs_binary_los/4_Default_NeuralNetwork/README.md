# Summary of 4_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

9.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.376986 | nan           |
| auc       | 0.926112 | nan           |
| f1        | 0.872605 |   0.448384    |
| accuracy  | 0.857983 |   0.45332     |
| precision | 0.982405 |   0.983634    |
| recall    | 1        |   5.15408e-18 |
| mcc       | 0.713556 |   0.486738    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.376986 |   nan       |
| auc       | 0.926112 |   nan       |
| f1        | 0.871153 |     0.45332 |
| accuracy  | 0.857983 |     0.45332 |
| precision | 0.871869 |     0.45332 |
| recall    | 0.870439 |     0.45332 |
| mcc       | 0.712968 |     0.45332 |


## Confusion matrix (at threshold=0.45332)
|                  |   Predicted as long |   Predicted as short |
|:-----------------|--------------------:|---------------------:|
| Labeled as long  |                1671 |                  312 |
| Labeled as short |                 316 |                 2123 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
