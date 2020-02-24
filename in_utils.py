# Module to create influence folder given artistic parameters

import pandas as pd
import shutil
import os.path

def gather_influence(artist=False, start_date=False, end_date=False, genre=False, style=False):
    df_info = pd.read_csv('all_data_info.csv')
    df_info['include'] = False
    if (artist != False):
        mask = df_info.artist == artist
        df_info.loc[mask, 'include'] = True
    if (genre != False):
        mask = df_info.genre == genre
        df_info.loc[mask, 'include'] = True
    if (style != False):
        mask = df_info.style == style
        df_info.loc[mask, 'include'] = True
    if ((start_date != False) & (end_date != False)):
        mask = df_info.date >= int(start_date)
        mask = mask & (df_info.date <= int(end_date))
        df_info.loc[mask, 'include'] = True
    elif (end_date != False):
        mask = df_info.date <= int(end_date)
        df_info.loc[mask, 'include'] = True
    elif (start_date != False):
        mask = df_info.date >= int(start_date)
        df_info.loc[mask, 'include'] = True   
    display(df_info[df_info['include']])
    filenames = df_info.loc[df_info['include'], 'new_filename']
    for ff in filenames:
        if os.path.exists('original_paintings/'+ff):
            shutil.copyfile('original_paintings/'+ff, 'influence/'+ff)
            ff 
    return 