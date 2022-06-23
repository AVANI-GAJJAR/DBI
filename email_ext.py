def email_add(text):
    import re  
    lst = re.findall('\S+@\S+',text)     
    return lst



