


def get_num(text):
    import re
    m=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    return m

