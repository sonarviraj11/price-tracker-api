import pandas as pd

def clean_data(raw_data):
    df = pd.DataFrame(raw_data)
    df['price'] = df['price'].str.replace('$','').astype(float, errors='ignore')
    df['price'] = df['price'].fillna(-1)
    df['name'] = df['name'].fillna("Unknown")
    return df
