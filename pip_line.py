
from datetime import date
import Name_ex as name
import credit_card as cred
import Dl_Ext as dl
import dob as date_birth
import email_ext as em
import ip_ext as ip
import mac_address as mac
import Phone_Tele as phn
import snn_ext as snn
import vin_ext as vin
def extract_PII_pipeline(text):
    names=name.get_name(text)
    credit_cards=cred.credit_ext(text)
    dl_num=dl.get_dl(text)
    date_of_birth=date_birth.dob(text)
    emails=em.email_add(text)
    ip_address=ip.get_ip(text)
    mac_address=mac.get_mac(text)
    phone_number=phn.get_num(text)
    snn_numbers=snn.get_ssn(text)
    vin_number=vin.get_vin(text)
    return(names,credit_cards,dl_num,date_of_birth,emails,ip_address,mac_address,phone_number,snn_numbers,vin_number)




