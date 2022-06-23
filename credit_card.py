


def credit_ext(text):
    import re
    m=re.findall("((?:(?:\\d{4}[- ]){3}\\d{4}|\\d{16}))(?![\\d])",text)
    return m