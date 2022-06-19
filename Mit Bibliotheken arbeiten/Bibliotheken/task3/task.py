import pandas as pd


def create_dataframe():
    df = pd.DataFrame([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], ["A", "B", "C"], ["D", "E", "F"])

    return df


print(create_dataframe())
