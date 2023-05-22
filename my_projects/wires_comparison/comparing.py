from reader import reader_func, create_unequal



def list_creator(df) -> dict:
    pass



new_df = create_unequal(reader_func('IRM_wires.csv'))
old_df = create_unequal(reader_func('IRM_wires.csv'))

for row in new_df.itertuples():
    print(row.KSID)
    for row_old in old_df.itertuples():
        if row.KSID in row_old.KSID:
            # print(row.KSID, row_old.KSID)
            if row.LTGNR == row_old.LTGNR:
                if row.LAENG == row_old.LAENG:
                    print('same length')  # TODO: same Lid and length -> write to file
                else:
                    print(f'{row.LTGNR} new length {row.LAENG} change length from {row_old.LAENG}')
                    continue



