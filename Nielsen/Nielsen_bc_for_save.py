dfs_01 = []

for tv_channel in range(5):
    for days_ in days_range:
        if tv_channel == 1:
            df_01 = program_percentage(tv_channel,days_)
            dfs_01.append(df_01)
            df_01['category'] = tv_channels['1']
            df_01['date'] = days_

nielsen_df_01 = pd.concat(dfs_01)
nielsen_df_01.to_csv('./nielsen/0313_지상파_시청률.csv', index=False, encoding='utf-8-sig')