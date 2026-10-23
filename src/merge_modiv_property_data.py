"""Merge NJ MOD-IV property data with abstract and tax-list files.

Part of the NJ municipal fiscal analysis workflow: MOD-IV (MODIV22) is
New Jersey's statewide property record file. This step merges the main
MOD-IV extract with the abstract and taxes files on the parcel `key`.

Input files (NJ MOD-IV public property data, not included in this repo):
    MODIV22.CSV, 22abstract, 22taxes
Output:
    abstract_df.csv
"""
import pandas as pd

MERGED_DATA = pd.read_csv('MODIV22.CSV')

abstract = pd.read_excel('22abstract')
taxes = pd.read_excel('22taxes')

df_abstract = pd.merge(MERGED_DATA, abstract, on='key', how='left')
df_abstract.to_csv('abstract_df.csv', index=False)
