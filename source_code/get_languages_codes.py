import pandas as pd
from get_filepath import *
import re
df = pd.read_pickle(get_file_path(r'SPRACHENWAEHLEN_DF.PKL')[0])
def get_language(eingabe):
    try:
        if len(eingabe) == 2 and not eingabe.isnumeric():
            dfa = df.loc[df.iso_6391.str.contains(rf'^{eingabe}$', regex=True)].iloc[0].to_list()
            return dfa
        elif len(eingabe) == 3 and not eingabe.isnumeric():
            try:
                dfa = df.loc[df.iso_6392.str.contains(rf'^{eingabe}$', regex=True)].iloc[0].to_list()
                return dfa
            except:
                dfa = df.loc[df.iso_6393.str.contains(rf'^{eingabe}$', regex=True)].iloc[0].to_list()
                return dfa
        try:
            dfa = df.loc[eingabe].to_list()
            return dfa
        except:
            dfa = df.loc[df.language.str.contains(rf'^{eingabe}$', regex=True, flags=re.IGNORECASE)].iloc[0].to_list()
    except Exception as Fehler:
        return eingabe
# xx = get_language(eingabe='ger')
# print(xx)