import pandas as pd
import numpy as np

def savi(nir: pd.Series, red: pd.Series, L: float = 0.5) -> pd.Series:
    return ((nir - red) * (1 + L)) / (nir + red + L)

def tsavi(nir: pd.Series, red: pd.Series, s: float, a: float, X: float = 0) -> pd.Series:
    return (s * (nir - s * red - a)) / (s * nir + red - a * s + X * (1 + s ** 2))

def msavi(nir: pd.Series, red: pd.Series, M: float = 2, L: float = 0.5) -> pd.Series:
    return ((1 + M) * (nir - red)) / (nir + red + L)

def msavi12(nir: pd.Series, red: pd.Series) -> pd.Series:
    return (2 * nir + 1 - np.sqrt((2 * nir + 1) ** 2 - 8 * (nir - red))) / 2

def dvi(nir: pd.Series, red: pd.Series) -> pd.Series:
    return nir - red

def rvi(nir: pd.Series, red: pd.Series) -> pd.Series:
    return nir / red

def pvi(nir: pd.Series, red: pd.Series, b: float) -> pd.Series:
    return np.sin(b) * nir - np.cos(b) * red

def wdvi(nir: pd.Series, red: pd.Series, S: float) -> pd.Series:
    return nir - S * red

def ipvi(nir: pd.Series, red: pd.Series) -> pd.Series:
    return nir / (nir + red)

def ndvi(nir: pd.Series, red: pd.Series) -> pd.Series:
    return (nir - red) / (nir + red)

def tndvi(nir: pd.Series, red: pd.Series) -> pd.Series:
    return np.sqrt((nir - red) / (nir + red) + 0.5)

def arvi(nir: pd.Series, red: pd.Series, rb: pd.Series) -> pd.Series:
    return (nir - rb) / (nir + rb)

def gemi(nir: pd.Series, red: pd.Series) -> pd.Series:
    eta = (2 * (nir ** 2 - red ** 2) + 1.5 * nir + 0.5 * red) / (nir + red + 0.5)
    return eta * (1 - 0.25 * eta) - (red - 0.125) / (1 - red)

# DataFrame function for vegetation indices
def vegetation_indices_df(nir: pd.Series, red: pd.Series, b: float = 1, S: float = 1, rb: pd.Series = None) -> pd.DataFrame:
    data = {
        'NDVI': ndvi(nir, red),
        'SAVI': savi(nir, red),
        'MSAVI': msavi(nir, red),
        'MSAVI12': msavi12(nir, red),
        'DVI': dvi(nir, red),
        'RVI': rvi(nir, red),
        'PVI': pvi(nir, red, b),
        'WDVI': wdvi(nir, red, S),
        'IPVI': ipvi(nir, red),
        'TNDVI': tndvi(nir, red),
    }
    if rb is not None:
        data['ARVI'] = arvi(nir, red, rb)
    
    return pd.DataFrame(data)
