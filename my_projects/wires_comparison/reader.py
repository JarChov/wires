from pathlib import Path
import pandas as pd
import numpy as np


def reader(filename: Path):
    df = pd.read_csv(filename)
    return df


def create_unequal(df):

    for row in df.itertuples():
        if pd.isna(row.BG_LIDENT) and pd.isna(row.SL_LIDENT):
            df.at[row.Index, 'lid_uneque'] = row.LIDENT
        elif not pd.isna(row.BG_LIDENT):
            df.at[row.Index, 'lid_uneque'] = row.BG_LIDENT
        elif not pd.isna(row.SL_LIDENT):
            df.at[row.Index, 'lid_uneque'] = row.SL_LIDENT

    return df



if __name__ == '__main__':
    file = Path('IRM_wires.csv')
    lines = reader(file)
    # print(lines)
    check = (str(lines.SLNR[1]))
    # print(type(check))
    lines_new = create_unequal(lines)
    print(lines_new)
    lines_new.to_excel('data.xlsx')

    print(type(np.nan))




