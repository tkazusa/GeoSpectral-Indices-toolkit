import pandas as pd
import numpy as np

def radar_vegetation_index(VH: pd.Series, VV: pd.Series) -> pd.Series:
    return (4 * VH) / (VV + VH)

def cross_ratio(VH: pd.Series, VV: pd.Series) -> pd.Series:
    return VH / VV

# DataFrame function for radar indices
def radar_indices_df(VH: pd.Series, VV: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({
        'RVI': radar_vegetation_index(VH, VV),
        'CR': cross_ratio(VH, VV)
    })