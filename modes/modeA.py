def modeA(exte, file):
    accounts = {}
    
    import pandas as pd
    if exte == 'csv':
        df = pd.read_csv(file)
    elif exte == 'xlsx':
        df = pd.read_excel(file)

    from functions.periods import extract_periods
    periods = extract_periods(df)
    accounts['periods'] = periods

    from functions.extraction import extract_revenue
    rev = extract_revenue(df, len(periods))
    accounts['revenue'] = rev

    from functions.extraction import extract_account
    ar = extract_account(df, 'ar', len(periods))
    accounts['accounts receivable'] = ar

    ap = extract_account(df, 'ap', len(periods))
    accounts['accounts payable'] = ap

    inv = extract_account(df, 'inv', len(periods))
    accounts['inventory'] = inv

    return accounts
