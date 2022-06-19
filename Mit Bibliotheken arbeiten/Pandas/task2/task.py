import pandas as pd


def load_names(filename):
    df = pd.read_csv(filename)
    df.at[3, 'firstname'] = "Simon"
    df = df.drop(17)
    df["fullname"] = df["firstname"] + " " + df["lastname"]
    df["length"] = df["fullname"].str.len()
    return df


names = load_names("names.csv")

print(names.head(20))

