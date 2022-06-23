import re
def dob(text):
    import re
    m=re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}', text)
    return m


