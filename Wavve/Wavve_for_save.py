dfs = []

for genre in genres:
    print(genres[genre], end=" ")
    for page in range(1,11):
        offset = (page-1) * 20
        print(page, end=" ")

        df = wavve(genre, offset, page)
        dfs.append(df)

wavve_dataset = pd.concat(dfs, ignore_index=True)
wavve_dataset.to_csv('./0312_wavve_dataset')