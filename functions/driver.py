def process_driver(exte):
    from functions.extension import ALLOWED_EXTENSIONS
    if exte in ALLOWED_EXTENSIONS[:3]:
        from modes.modeA import modeA
        print('Mode = A')
        modeA(file)
    else:
        pass
