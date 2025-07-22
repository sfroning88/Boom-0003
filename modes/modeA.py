def modeA(exte, file):
    import pandas as pd
    if exte == 'csv':
        df = pd.read_csv(file)
    elif exte == 'xlsx':
        df = pd.read_excel(file)

    from functions.periods import extract_periods
    periods = extract_periods(df)

    accounts['periods'] = periods

    return accounts
