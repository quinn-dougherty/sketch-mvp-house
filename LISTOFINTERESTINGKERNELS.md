# Kaggle had a zilllow contest w the valuation task 

from the list of top kernels  https://www.kaggle.com/c/zillow-prize-1/kernels?sortBy=scoreAscending&group=everyone&pageSize=20&competitionId=6649


1. https://www.kaggle.com/wangsg/ensemble-stacking-lb-0-6436 this one seems useful for feature-engineering stuff. Includes some rudimentary wisdoms like "bedroom / commonroom as two separate features doesn't gain information what it loses in parsimony, so engineer `total_rooms = bedrooms + commonrooms` and drop bedroom/commonroom", etc. 

- interaction and polynomial: 
```
    # Ratio of tax of property over parcel
    properties['N-ValueRatio'] = properties['taxvaluedollarcnt'] / properties['taxamount']

    # TotalTaxScore
    properties['N-TaxScore'] = properties['taxvaluedollarcnt'] * properties['taxamount']

    # polnomials of tax delinquency year
    properties["N-taxdelinquencyyear-2"] = properties["taxdelinquencyyear"] ** 2
    properties["N-taxdelinquencyyear-3"] = properties["taxdelinquencyyear"] ** 3


    # error in calculation of the finished living area of home
    properties['N-LivingAreaError'] = properties['calculatedfinishedsquarefeet'] / properties['finishedsquarefeet12']

    # proportion of living area
    properties['N-LivingAreaProp'] = properties['calculatedfinishedsquarefeet'] / properties['lotsizesquarefeet']
    properties['N-LivingAreaProp2'] = properties['finishedsquarefeet12'] / properties['finishedsquarefeet15']

```
- as well as variously using year like this `properties['N-life'] = 2018 - properties['yearbuilt']`

- see also their `LabelEncoder` on line 112

2. ...


Honeslty not a lot of these folks are doing a lot of feature engineering, the preprocessing is quite lackluster. I'm trying to ignore kernels that are just exhibiting hyperparams.  
