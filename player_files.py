import numpy as np
import pandas as pd

class files:
    def get_files(year, position):
        if (position is None):
            df = pd.read_csv('./StatFiles/qb_stats.csv')
        if (position == 'QB'):
            df = pd.read_csv('./StatFiles/qb_stats.csv')
        elif (position == 'RB'):
            df = pd.read_csv('./StatFiles/rb_stats.csv')
        elif (position == 'WR'):
            df = pd.read_csv('./StatFiles/wr_stats.csv')
        elif (position == 'TE'):
            df = pd.read_csv('./StatFiles/te_stats.csv')

        if (year is None):
            df = df[df.Year == 2022]
        else:
            df = df[df.Year == year]
        return df

    def get_player_stats(player_name):
        qb_df = pd.read_csv('./StatFiles/qb_stats.csv')
        rb_df = pd.read_csv('./StatFiles/rb_stats.csv')
        wr_df = pd.read_csv('./StatFiles/wr_stats.csv')
        te_df = pd.read_csv('./StatFiles/te_stats.csv')

        player_df = pd.DataFrame()
        isPlayer = False

        for df in [qb_df, rb_df, wr_df, te_df]:
            df.PLAYER = df.PLAYER.str.strip()
            df['Name'] = df.PLAYER.apply(lambda x: x.split()[0] + ' ' + x.split()[1])
            df['Team'] = df.PLAYER.apply(lambda x: x.split()[-1].replace('(', '').replace(')', ''))
            df.Name = df.Name.str.replace('.', '')
            if (player_name in df.Name.values):
                isPlayer = True
                df = df.copy()
                player_df = df[df.Name == player_name]
                player_df = player_df.drop(labels=['PLAYER', 'Name'], axis=1)
                player_df = files.clean_data(player_df)

                return player_df, isPlayer

        return player_df, isPlayer

    def clean_data(df):
        df = df.copy()

        for col in df.columns:
            try:
                df[col] = df[col].str.replace(',', '')
                df[col] = df[col].astype(np.float64)

            except Exception as e:
                print(e)

        df.rename(columns={'RANK': 'id'}, inplace=True)

        return df