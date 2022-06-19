import pandas as pd


def load_names(filename):
    dataframe = pd.read_csv(filename)
    return dataframe


print(load_names("names.csv").head(20))
