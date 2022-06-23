
def get_ip(text):
    import re
    m=re.findall('(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', text)
    return m
    
























