
from matplotlib.pyplot import get
from pyrsistent import l


def get_mac(text):
    import re
    list=[]
    m=re.findall(r'(([a-zA-z0-9]{2}[-:]){5}[a-zA-z0-9][a-zA-z0-9])', text)

    for i in m:
        list.append(i[0])

    return list





