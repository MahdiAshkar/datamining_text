import pandas as pd

file_path = "tabnak_news.csv"
df = pd.read_csv(file_path, usecols=[1, 2, 3, 4])
column = 2

for i in range(len(df)):
    if (df.iloc[i, column] in ['هنری', 'عکس', 'دفاع مقدس']):
        df.iloc[i, column] = 'فرهنگی'
    elif (df.iloc[i, column] in ['حقوقی', 'بین\u200cالملل', 'سياست خارجی']):
        df.iloc[i, column] = 'سیاسی'

rows_to_drop = df[df.iloc[:, column] == 'علمی -آموزشی'].index
df.drop(rows_to_drop, inplace=True)
df.to_csv('edit_'+file_path, index=False)

df = pd.read_csv('edit_'+file_path)
category_set = set(df.iloc[:, 2])
print(category_set)
