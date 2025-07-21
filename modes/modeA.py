import pandas as pd

def modeA(exte, file):
    print(file.filename)

    if exte == 'csv':
        df = pd.read_csv(file)
    elif exte == 'xlsx':
        df = pd.read_excel(file)

    print(df)
