dfs_02 = []
for tv_channel in range(2,4):
    for days_ in days_range:
        if tv_channel == 2:
            df = program_percentage_another(tv_channel,days_)
            dfs_02.append(df)
            df['category'] = tv_channels['2']
            df['date'] = days_
        else:
            df_ = program_percentage_another(tv_channel,days_)
            dfs_02.append(df_)
            df_['category'] = tv_channels['3']
            df_['date'] = days_

nielsen_df_02 = pd.concat(dfs_02)
nielsen_df_02.to_csv('./nielsen/0313_종편_케이블_시청률.csv', index=False, encoding='utf-8-sig')