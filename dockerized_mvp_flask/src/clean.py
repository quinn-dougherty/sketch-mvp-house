# -*- coding: utf-8 -*-

''' '''
import pandas as pd
import numpy as np
import re

# './3rdpartyExport.csv'
PTHURL = "https://raw.githubusercontent.com/quinn-dougherty/sketch-mvp-house/master/MVPFlask/src/3rdpartyExport.csv"


class Data:
    ''' from a raw csv, clean it, and pick out regressands and target. train_test_split will happen in notebook as will the rest of it.

    based entirely on the excel sheet Anthony shared on day one 04-22-2019.
        here https://docs.google.com/spreadsheets/d/1T1SD2SD_Rc_AVLREZk5TaZSHVUwzw_z_zLwMJDlklak/edit?usp=sharing
    '''

    def __init__(self, csv_string):
        self.dat = self.clean(pd.read_csv(csv_string))
        self.regressands = [
            'home_size', # selected for MVP. 
            'beds_total', # compromising between what we want and what Anthony's datacleaning made available
            'baths_total'] 
        self.X = self.dat[self.regressands] 
        self.y = self.dat['sale_price']

    def clean(self, dat: pd.DataFrame) -> pd.DataFrame:
        ''''''
        def try_lower(x):
            '''using try to make string features all lower case. '''
            try:
                return x.lower()
            except AttributeError:
                return x

        def try_float_cash(x):
            ''' get a `$` out of what's supposed to be a number 
            
            TODO: fix incorrect behavior: e.g. `assert try_float_cash("$1,345.29")==1345.29` '''
            try:
                return float('.'.join(re.findall(r'\d+', x)))
            except TypeError:
                return x
            except ValueError:
                return x
        
        return (dat.assign(**{feat: dat[feat].apply(try_lower).apply(try_float_cash)
                              # cast all non-numeric features to number (stripping out dollar sign) or to all lower case (if the features are supposed to be string) 
                              for feat in dat.select_dtypes(exclude=[np.number]).columns})
                # drop anything wiht more than zero nulls. (just for MVP) 
                .drop([x for x in dat.columns if dat[x].isna().sum() > 0], axis=1)
                .rename(columns={' $/ sq ft ': 'price_per_sq_ft', # self explanatory, i guess. 
                                 '$ / sq ft for keywords': 'price_per_sq_ft_by_keyword',
                                 ' $/ sq ft .1': 'price_per_sq_ft_.1',
                                 'Baths.Lavs': 'baths_total',
                                 'SqFt-Est Tot Fin': 'home_size'
                                 })
                # we want our column names to be valid python names, etc. 
                .rename(columns=lambda s: s.replace(' ', '_').lower().replace(':', ''))
                )
