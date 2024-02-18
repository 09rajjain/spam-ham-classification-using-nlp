import pandas as pd

try:
    data = pd.read_csv('spam.csv', encoding='utf-8', delimiter=',')
    print(data.head())
    if 'v1' in data.columns:
        x = data['v1']
    else:
        raise KeyError("Column 'v1' not found in DataFrame")
    if 'v2' in data.columns:
        y = data['v2']
    else:
        raise KeyError("Column 'v2' not found in DataFrame")
except KeyError as e:
    print("Error:", e)
