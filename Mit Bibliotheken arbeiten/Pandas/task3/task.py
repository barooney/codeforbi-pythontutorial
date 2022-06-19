import pandas as pd


def load_names(filename):
    df = pd.read_csv(filename)
    df.at[3, 'firstname'] = "Simon"
    df = df.drop(17)
    df["fullname"] = df["firstname"] + " " + df["lastname"]
    df["length"] = df["fullname"].str.len()
    return df


def filter_long_names(names):
    return names[(names["length"] >= 14)]


names = load_names("names.csv")

long_names = filter_long_names(names)

print(long_names.head(20))
