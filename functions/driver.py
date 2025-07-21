def process_driver(exte):
    from functions.extension import ALLOWED_EXTENSIONS
    if exte in ALLOWED_EXTENSIONS[:3]:
        print('Mode = A')
    else:
        pass
