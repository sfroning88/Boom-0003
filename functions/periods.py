def date_cell(cell):
    import re
    from support.definitions import date_patterns

    if re.search(r'^\d+\.\d+$', cell):
        return False
    return any(re.search(pattern, cell, re.IGNORECASE) for pattern in date_patterns)

def strip_timestamp(period):
    import re
    return re.sub(r'\s+\d{1,2}:\d{2}(:\d{2})?$', '', period)

def extract_periods(df):
    for _, row in df.iterrows():
        periods = [strip_timestamp(str(cell)) for cell in row if date_cell(str(cell))]
        periods = list(dict.fromkeys(periods)) # remove duplicates
        if periods:
            return periods
    return ['No Periods Found']
