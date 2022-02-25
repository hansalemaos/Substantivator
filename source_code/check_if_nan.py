import numpy as np
import pandas as pd
import math
import regex
def isnan(wert, nan_back=False, debug=False):
    allenanvalues = ['<NA>', '<NAN>', '<nan>', 'np.nan', 'NoneType', 'None', '-1.#IND', '1.#QNAN', '1.#IND', '-1.#QNAN',
                     '#N/A N/A', '#N/A', 'N/A', 'n/a', 'NA', '', '#NA', 'NULL', 'null', 'NaN', '-NaN', 'nan', '-nan']
    try:
        if pd.isna(wert) is True:
            if nan_back is True: return np.nan
            return True
    except Exception as Fehler:
        if debug is True: print(Fehler)

    try:
        if pd.isnull(wert) is True:
            if nan_back is True: return np.nan
            return True
    except Exception as Fehler:
        if debug is True: print(Fehler)

    try:
        if math.isnan(wert) is True:
            if nan_back is True: return np.nan
            return True
    except Exception as Fehler:
        if debug is True: print(Fehler)

    try:
        if wert is None:
            return True
    except Exception as Fehler:
        if debug is True: print(Fehler)

    for allaaa in allenanvalues:
        try:
            nanda = regex.findall(str(fr'^\s*{wert}\s*$'), allaaa)
            if any(nanda):
                return True
        except Exception as Fehler:
            if debug is True: print(Fehler)
            return False
    return False