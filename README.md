# Kappa
This project will demonstrate applications of machine learning models to estimate and predict performance of an index fund. Initially, the index fund of interest is SP500 which 
tracks the stock performance of 500 large companies listed on exchanges in the U.S. To model the performance of this index, the set of features will include technical indicators.
Additional features will be created using data from other sources.

The dataset for the index fund was obtained from Yahoo Finance. The features created as of now are included in the table:

| Variable | Definition                                                                           |
|----------|--------------------------------------------------------------------------------------|
| mavg_5   | 5-day moving average                                                                 |
| mstd_5   | 5-day moving standard deviation                                                      |
| lbb_5    | lower bound of the bollinger band with period=5                                      |
| ubb_5    | upper bound of the bollinger band with period=5                                      |
| mavg_10  | 10-day moving average                                                                |
| mstd_10  | 10-day moving standard deviation                                                     |
| lbb_10   | lower bound of the bollinger band with period=10                                     |
| ubb_10   | upper bound of the bollinger band with period=10                                     |
| mavg_200 | 200-day moving average                                                               |


## Blog 
My blog on this project can be accessed at TO BE POSTED


## Cross Validation
TBD

## Hyperparameter Optimization
TBD

## Model Results and Feature Importance
TBD

## Model Persistence
TBD
