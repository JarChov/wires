from reader import reader_func, create_unequal
import time
import pandas as pd



def list_creator(df) -> dict:
    pass


start = time.time()
new_df = create_unequal(reader_func('new_wires.csv'))
old_df = create_unequal(reader_func('old_wires.csv'))


# Порівняння 2-х df
merged_df = new_df.merge(old_df, on=['KSID', 'LTGNR'], suffixes=('_new', '_old'))

# Порівняння довжин та LID
changed_df = merged_df[(merged_df['LAENG_new'] != merged_df['LAENG_old']) & (merged_df['lid_uneque_new'] != merged_df['lid_uneque_old'])]
changed_df = changed_df.assign(Comment='Зміна довжини та LID')

changed_length_df = merged_df[merged_df['LAENG_new'] != merged_df['LAENG_old']]
filtered_length_df = changed_length_df[~changed_length_df[['LTGNR', 'KSID']].isin(changed_df[['LTGNR', 'KSID']])]
filtered_length_df = filtered_length_df.assign(Comment='Зміна довжини')
changed_lid_df = merged_df[merged_df['lid_uneque_new'] != merged_df['lid_uneque_old']]
filtered_lid_df = changed_lid_df[~changed_lid_df[['LTGNR', 'KSID']].isin(changed_df[['LTGNR', 'KSID']])]
changed_lid_df = changed_lid_df.assign(Comment='Зміна LID')


filtered_lid_df.to_excel('changed_lid_df.xlsx', index=False)
filtered_length_df.to_excel('change_length.xlsx', index=False)
changed_df.to_excel('changed_length_lid.xlsx', index=False)
print(f'diff = {time.time() - start}')


