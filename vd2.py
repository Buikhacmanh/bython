import pandas as pd

series_ex = {"a":[1, 4, 6, 7, 8], "b":[9, 10, 11, 12, 13], "c":[14, 15, 16, 17, 18]}

series_data = pd.DataFrame(series_ex)

print(series_data)
print("Xuat ra cot dau cua series")
print(series_data.iloc[:, 0])