# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model             |   Weight |
|:------------------|---------:|
| 3_Default_Xgboost |        5 |

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.244482 | nan           |
| auc       | 0.963344 | nan           |
| f1        | 0.912928 |   0.520228    |
| accuracy  | 0.90389  |   0.520228    |
| precision | 1        |   0.999119    |
| recall    | 1        |   5.80332e-05 |
| mcc       | 0.805687 |   0.520228    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.244482 |  nan        |
| auc       | 0.963344 |  nan        |
| f1        | 0.912928 |    0.520228 |
| accuracy  | 0.90389  |    0.520228 |
| precision | 0.912367 |    0.520228 |
| recall    | 0.913489 |    0.520228 |
| mcc       | 0.805687 |    0.520228 |


## Confusion matrix (at threshold=0.520228)
|                  |   Predicted as long |   Predicted as short |
|:-----------------|--------------------:|---------------------:|
| Labeled as long  |                1769 |                  214 |
| Labeled as short |                 211 |                 2228 |

## Learning curves
![Learning curves](learning_curves.png)
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
