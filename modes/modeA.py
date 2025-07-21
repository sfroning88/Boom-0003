import pandas as pd

def modeA(exte, file):
    if exte == 'csv':
        df = pd.read_csv(file)
    elif exte == 'xlsx':
        df = pd.read_excel(file)

    from functions.periods import extract_periods
    extract_periods(df)
