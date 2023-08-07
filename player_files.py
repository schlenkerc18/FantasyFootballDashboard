import numpy as np
import pandas as pd

class files:
    def clean_df(df):
        new_df = df.copy()

        new_df.columns = new_df.columns.str.lower()
        new_df['player'] = new_df['player'].apply(lambda x: ' '.join(x.split()[:-1]))
        new_df['firstName'] = new_df.player.str.split().str[0]
        new_df['lastName'] = new_df.player.str.split().str[1]
        new_df.yds = pd.to_numeric(new_df.yds.str.replace(',', ''))

        return new_df
    def clean_text_df(df, year, position):
        new_df = df.copy()
        new_df.Player = new_df.Player.str.replace('[*+]', '', regex = True)
        new_df['firstName'] = new_df.Player.str.split().str[0]
        new_df['lastName'] = new_df.Player.str.split().str[1]
        new_df['year'] = year

        if position == 'wr':
            new_df = new_df[['Tm', 'Age', 'Ctch%', 'firstName', 'lastName', 'year']]
        else:
            new_df = new_df[['Tm', 'Age', 'firstName', 'lastName', 'year']]

        return new_df
    def get_files(year, position):
        if (position == 'QB' or position is None):
            df = pd.read_csv('./StatFiles/qb_stats.csv')
            df = files.clean_df(df)

            df_18 = pd.read_csv('./StatFiles/qb_2018.txt')
            df_clean_18 = files.clean_text_df(df_18, 2018, 'qb')

            df_19 = pd.read_csv('./StatFiles/qb_2019.txt')
            df_clean_19 = files.clean_text_df(df_19, 2019, 'qb')

            df_20 = pd.read_csv('./StatFiles/qb_2020.txt')
            df_clean_20 = files.clean_text_df(df_20, 2020, 'rqb')

            df_21 = pd.read_csv('./StatFiles/qb_2021.txt')
            df_clean_21 = files.clean_text_df(df_21, 2021, 'qb')

            df_22 = pd.read_csv('./StatFiles/qb_2022.txt')
            df_clean_22 = files.clean_text_df(df_22, 2022, 'qb')

            df_combined = pd.concat([df_clean_18, df_clean_19, df_clean_20, df_clean_21, df_clean_22],
                                    ignore_index=True)
            df_merged = pd.merge(df, df_combined, on=['firstName', 'lastName', 'year'], how='inner')

            df = df_merged[['rank', 'player', 'Age', 'Tm', 'cmp', 'att', 'pct', 'yds', 'y/a', 'td', 'int', 'sacks', 'att.1', 'yds.1', 'td.1', 'fl', 'g', 'fpts', 'fpts/g', 'year']]
        elif (position == 'RB'):
            df = pd.read_csv('./StatFiles/rb_stats.csv')
            df = files.clean_df(df)

            df_18 = pd.read_csv('./StatFiles/rb_2018.txt')
            df_clean_18 = files.clean_text_df(df_18, 2018, 'rb')

            df_19 = pd.read_csv('./StatFiles/rb_2019.txt')
            df_clean_19 = files.clean_text_df(df_19, 2019, 'rb')

            df_20 = pd.read_csv('./StatFiles/rb_2020.txt')
            df_clean_20 = files.clean_text_df(df_20, 2020, 'rb')

            df_21 = pd.read_csv('./StatFiles/rb_2021.txt')
            df_clean_21 = files.clean_text_df(df_21, 2021, 'rb')

            df_22 = pd.read_csv('./StatFiles/rb_2022.txt')
            df_clean_22 = files.clean_text_df(df_22, 2022, 'rb')

            df_combined = pd.concat([df_clean_18, df_clean_19, df_clean_20, df_clean_21, df_clean_22],
                                    ignore_index=True)
            df_merged = pd.merge(df, df_combined, on=['firstName', 'lastName', 'year'], how='inner')

            df = df_merged[['rank', 'player', 'Age', 'Tm', 'att', 'yds', 'y/a', 'lg', '20+', 'td', 'rec', 'tgt', 'yds.1', 'y/r', 'td.1', 'fl', 'fpts', 'fpts/g', 'year']]
        elif (position == 'WR'):
            df = pd.read_csv('./StatFiles/wr_stats.csv')
            df = files.clean_df(df)

            df_18 = pd.read_csv('./StatFiles/receiver_2018.txt')
            df_clean_18 = files.clean_text_df(df_18, 2018, 'wr')

            df_19 = pd.read_csv('./StatFiles/receiver_2019.txt')
            df_clean_19 = files.clean_text_df(df_19, 2019, 'wr')

            df_20 = pd.read_csv('./StatFiles/receiver_2020.txt')
            df_clean_20 = files.clean_text_df(df_20, 2020, 'wr')

            df_21 = pd.read_csv('./StatFiles/receiver_2021.txt')
            df_clean_21 = files.clean_text_df(df_21, 2021, 'wr')

            df_22 = pd.read_csv('./StatFiles/receiver_2022.txt')
            df_clean_22 = files.clean_text_df(df_22, 2022, 'wr')

            df_combined = pd.concat([df_clean_18, df_clean_19, df_clean_20, df_clean_21, df_clean_22],
                                    ignore_index=True)
            df_merged = pd.merge(df, df_combined, on=['firstName', 'lastName', 'year'], how='inner')

            df = df_merged[['rank', 'player', 'Age', 'Tm', 'rec', 'tgt', 'Ctch%', 'yds', 'y/r', 'lg', 'td', 'att', 'yds.1', 'td.1', 'fl', 'g', 'fpts', 'fpts/g', 'year']]
        elif (position == 'TE'):
            df = pd.read_csv('./StatFiles/te_stats.csv')
            df = files.clean_df(df)

            df_18 = pd.read_csv('./StatFiles/receiver_2018.txt')
            df_clean_18 = files.clean_text_df(df_18, 2018, 'wr')

            df_19 = pd.read_csv('./StatFiles/receiver_2019.txt')
            df_clean_19 = files.clean_text_df(df_19, 2019, 'wr')

            df_20 = pd.read_csv('./StatFiles/receiver_2020.txt')
            df_clean_20 = files.clean_text_df(df_20, 2020, 'wr')

            df_21 = pd.read_csv('./StatFiles/receiver_2021.txt')
            df_clean_21 = files.clean_text_df(df_21, 2021, 'wr')

            df_22 = pd.read_csv('./StatFiles/receiver_2022.txt')
            df_clean_22 = files.clean_text_df(df_22, 2022, 'wr')

            df_combined = pd.concat([df_clean_18, df_clean_19, df_clean_20, df_clean_21, df_clean_22],
                                    ignore_index=True)
            df_merged = pd.merge(df, df_combined, on=['firstName', 'lastName', 'year'], how='inner')

            df = df_merged[['rank', 'player', 'Age', 'Tm', 'rec', 'tgt', 'Ctch%', 'yds', 'y/r', 'lg', 'td', 'att', 'yds.1', 'td.1', 'fl', 'g', 'fpts', 'fpts/g', 'year']]

        if (year is None):
            df = df[df.year == 2022]
        elif (year == 'all'):
            return df
        else:
            df = df[df.year == year]


        return df

    def get_player_stats(player_name):
        qb_df = files.get_files('all', 'QB')
        rb_df = files.get_files('all', 'RB')
        wr_df = files.get_files('all', 'WR')
        te_df = files.get_files('all', 'TE')

        player_df = pd.DataFrame()
        # for search, false means name match has not been found
        isPlayer = False

        print(qb_df)

        for df in [qb_df, rb_df, wr_df, te_df]:
            df.player = df.player.str.strip()
            df['Name'] = df.player.apply(lambda x: x.split()[0] + ' ' + x.split()[1])
            df.Name = df.Name.str.replace('.', '')
            if (player_name in df.Name.values):
                # match has been found in player search
                isPlayer = True
                df = df.copy()
                player_df = df[df.Name == player_name]
                player_df = player_df.drop(labels=['player', 'Name'], axis=1)
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