def date_cell(cell):
    import re
    from support.definitions import date_patterns

    if re.search(r'^\d+\.\d+$', cell):
        return False
    return any(re.search(pattern, cell, re.IGNORECASE) for pattern in date_patterns)

def extract_periods(df):
    for _, row in df.iterrows():
        periods = [str(cell) for cell in row if date_cell(str(cell))]
        if periods:
            return periods
    return ['No Periods Found']
