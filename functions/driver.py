def process_driver(exte, file):
    from functions.extension import ALLOWED_EXTENSIONS
    if exte in ALLOWED_EXTENSIONS[:3]:
        from modes.modeA import modeA
        print('Mode = A')
        modeA(exte, file)
    else:
        pass
