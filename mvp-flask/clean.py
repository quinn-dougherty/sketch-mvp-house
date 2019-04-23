#!/usr/bin/env python

''' '''
import pandas as pd
import numpy as np
import re
PTHURL = '3rdpartyExport.csv'
from utils import Spinner
spin = Spinner()

class Data:
    ''' from a raw csv, clean it, and pick out regressands and target. train_test_split will happen in notebook as will the rest of it.

    based entirely on the excel sheet Anthony shared on day one 04-22-2019.
        here https://docs.google.com/spreadsheets/d/1T1SD2SD_Rc_AVLREZk5TaZSHVUwzw_z_zLwMJDlklak/edit?usp=sharing
    '''
    def __init__(self, csv_string):
        spin.start()
        self.dat = self.clean(pd.read_csv(csv_string))
        self.regressands = ['price_per_sq_ft', 'beds_total', 'baths.lavs',
                            'original_list_price', 'year_built',
                            'sqft-est_tot_fin', 'sqft-est_fin_abv_grd', 'acreage']
        self.X = self.dat[self.regressands]
        self.y = self.dat['sale_price']
        spin.stop()

    def clean(self, dat: pd.DataFrame) -> pd.DataFrame:
        ''''''
        def try_lower(x):
            ''''''
            try:
                return x.lower()
            except AttributeError:
                return x

        def try_float_cash(x):
            ''''''
            try:
                return float('.'.join(re.findall(r'\d+', x)))
            except TypeError:
                return x
            except ValueError:
                return x


        return (dat.assign(**{feat: dat[feat].apply(try_lower).apply(try_float_cash)
                              for feat in dat.select_dtypes(exclude=[np.number]).columns})
                .drop([x for x in dat.columns if dat[x].isna().sum()>0], axis=1)
                .rename(columns={' $/ sq ft ': 'price_per_sq_ft',
                                   '$ / sq ft for keywords': 'price_per_sq_ft_by_keyword',
                                   ' $/ sq ft .1': 'price_per_sq_ft_.1',
                                'baths.lavs': 'baths_total'})
                .rename(columns=lambda s: s.replace(' ', '_').lower().replace(':', ''))
               )
