
def get_vin(text):
    import re
    m=re.findall('(?=.*\d|=.*[A-Z])(?=.*[A-Z])[A-Z0-9]{17}', text)
    return m
    






















