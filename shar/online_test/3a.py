#=====================done==============================

import pandas as pd



def get_sample(df: pd.DataFrame) -> pd.DataFrame:
    df['verdict_int'] = (df['verdict'] == 'Yes').apply(int)


    best_people = df.groupby('uid')
    best_people = best_people.agg({'verdict':'count', 'verdict_int':'sum'})

    best_people['success_per_cent'] = best_people['verdict_int'] / best_people['verdict']
    best_people.sort_values('success_per_cent', inplace=True, ascending=False)
    best_people.reset_index(inplace=True)



    def find_all_rejected(df: pd.DataFrame, sender_id: int):
        return df[(df['verdict'] == 'No') & (df['uid'] == sender_id)]['banner_id']

    prob_normal = pd.Series()
    for index, row in best_people.iterrows():
        prob_normal = pd.concat([prob_normal, find_all_rejected(df, int(row['uid']))])

        if len(prob_normal) > 100:
            break


    return pd.DataFrame(prob_normal[:100], columns=['banner_id'])


