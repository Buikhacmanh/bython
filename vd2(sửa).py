import pandas as pd

dataframe_ex = {"a":[1, 4, 6, 7, 8], "b":[23, 12, 56, 8, 22], "c":[87, 65, 43, 11, 34]}

dataFrame_data = pd.DataFrame(dataframe_ex)

print(dataFrame_data)

print("Xuat ra cot dau cua series")

print(dataFrame_data.iloc[:, 0])