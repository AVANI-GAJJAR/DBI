
def get_ssn(text):
    import re
    m=re.findall('[0-9]{3}[ -]?[0-9]{2}[ -]?[0-9]{4}', text)
    return m
    

























