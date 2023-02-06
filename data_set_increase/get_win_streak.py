def get_win_streak(df):
    df['win_streak'] = 0
    win_streak = 0
    last_winner = None
    for i, row in df.iterrows():
        if row['champion_name'] == last_winner:
            win_streak += 1
        else:
            win_streak = 1
        df.at[i, 'win_streak'] = win_streak
        last_winner = row['champion_name']
    return df