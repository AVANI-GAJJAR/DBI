
from datetime import date
# import Name_ex as name
import credit_card as cred
import Dl_Ext as dl
import dob as date_birth
import email_ext as em
import ip_ext as ip
import mac_address as mac
import Phone_Tele as phn
import snn_ext as snn
import vin_ext as vin
def extract_PII_pipeline(textt):
    names=[]
    credit_cards=[]
    dl_num=[]
    date_of_birth=[]
    emails=[]
    ip_address=[]
    phone_number=[]
    snn_numbers=[]
    vin_number=[]
    mac_address=[]
    for text in textt.splitlines():
        # names.append(name.get_name(text))
        if(len(cred.credit_ext(text))):
            credit_cards.append(cred.credit_ext(text))
        if(len(dl.get_dl(text))):
            dl_num.append(dl.get_dl(text))
        if(len(date_birth.dob(text))):
            date_of_birth.append(date_birth.dob(text))
        if(len(em.email_add(text))):
            emails.append(em.email_add(text))
        if(len(ip.get_ip(text))):
            ip_address.append(ip.get_ip(text))
        if(len(mac.get_mac(text))):
            mac_address.append(mac.get_mac(text))
        if(len(phn.get_num(text))):
            phone_number.append(phn.get_num(text))
        if(len(snn.get_ssn(text))):
            snn_numbers.append(snn.get_ssn(text))
        if(len(vin.get_vin(text))):
            vin_number.append(vin.get_vin(text))
    return(credit_cards,dl_num,date_of_birth,emails,ip_address,mac_address,phone_number,snn_numbers,vin_number)
    
