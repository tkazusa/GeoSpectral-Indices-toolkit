import pandas as pd
import numpy as np

def ssi1(blue: pd.Series, red: pd.Series, green: pd.Series) -> pd.Series:
    return (blue * red) / green

def ssi2(green: pd.Series, red: pd.Series) -> pd.Series:
    return (green + red) / 2

def ssi3(blue: pd.Series, red: pd.Series) -> pd.Series:
    return np.sqrt(blue * red)

# DataFrame function for soil salinity indices
def soil_salinity_indices_df(blue: pd.Series, red: pd.Series, green: pd.Series) -> pd.DataFrame:
    return pd.DataFrame({
        'SSI1': ssi1(blue, red, green),
        'SSI2': ssi2(green, red),
        'SSI3': ssi3(blue, red)
    })