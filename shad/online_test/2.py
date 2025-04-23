import pandas as pd
import numpy as np

def process(customers: pd.DataFrame, transactions: pd.DataFrame):

    #===========create datamart=================
    #display('===========create datamart================')

    df = pd.merge(customers, transactions, left_on='id', right_on='customer_id')
    df = df[df['success_flg'] == True]
    df.sort_values(['name', 'transaction_dttm'], inplace=True)

    #display(df)
    


    #============process payments================
    #display('============process payments================')

    rur = df['amount_rur']
    #display(rur)

    dif = np.diff(rur)
    #display('dif is', dif)
    #display('previous', dif[:-1])

    #display('next', dif[1:])

    print('so result is', (dif[:-1] > 0) * (dif[1:] > 0))

    bool_diff = np.array([False, *((dif[:-1] > 0) * (dif[1:] > 0)), False])
    #display(bool_diff)



    #=========process names====================
    #display('=========process names====================')

    names = np.array(df['name'])

    bool_names = (names[:-2] == names[1:-1]) * (names[2:] == names[1:-1])
    #display(bool_names)

    bool_names = np.array([False, *bool_names, False])
    #display(bool_names)


    #apply masks to dataframe
    #display('====================result=======================')
    return df[bool_diff & bool_names]
