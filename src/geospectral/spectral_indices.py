import pandas as pd
import numpy as np


def brightness_index(red: pd.Series, green: pd.Series) -> pd.Series:
    return np.sqrt((red ** 2 + green ** 2) / 2)

def second_brightness_index(red: pd.Series, green: pd.Series, nir: pd.Series) -> pd.Series:
    return np.sqrt((red ** 2 + green ** 2 + nir ** 2) / 3)

def redness_index(red: pd.Series, green: pd.Series) -> pd.Series:
    return red / green ** (1/3)

def color_index(red: pd.Series, green: pd.Series) -> pd.Series:
    return (red - green) / (red + green)

def hue_index(red: pd.Series, green: pd.Series, blue: pd.Series) -> pd.Series:
    return (2 * red - green - blue) / (green - blue)

def saturation_index(red: pd.Series, blue: pd.Series) -> pd.Series:
    return (red - blue) / (red + blue)

# DataFrame function for spectral indices
def spectral_indices_df(red: pd.Series, green: pd.Series, blue: pd.Series, nir: pd.Series = None) -> pd.DataFrame:
    data = {
        'BI': brightness_index(red, green),
        'RI': redness_index(red, green),
        'CI': color_index(red, green),
        'HI': hue_index(red, green, blue),
        'SI': saturation_index(red, blue)
    }
    if nir is not None:
        data['BI2'] = second_brightness_index(red, green, nir)
    
    return pd.DataFrame(data)