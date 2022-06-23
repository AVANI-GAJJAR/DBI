from re import A
import pip_line as pl
import pandas as pd
import fitz 
import pathlib


def main_pipeline(input_dir,output_dir):
    num_comp=0
    num_non_comp=0
    for path in pathlib.Path(input_dir).iterdir():
        data={'File Name':[],
        'Names':[],
        'Credit Card':[],
        'Dl Nums':[],
        'DOB':[],
        'Emails':[],          
        'Ip_add':[],
        'Mac Address':[],
        'Phone Number':[],
        'SSN Nums':[],
        'VIN Nums':[],
        'Non Compliance Elemets':[],
        }
        if path.is_file():
            with fitz.open(path) as doc: 
                count=0
                data['File Name'].append(path.name) 
                text =''
                for page in doc:
                    text += page.get_text()
                names,credit_cards,dl_num,date_of_birth,emails,ip_address,mac_address,phone_number,snn_numbers,vin_number=pl.extract_PII_pipeline(text)
                if(names[0]!=''):
                    count=count+1
                    for i in names:
                        # alphanumeric = [character for character in i if character.isalnum()]
                        data['Names'].append(i)
                if(len(credit_cards)):
                    count=count+1
                    for i in credit_cards:
                        data['Credit Card'].append(i)
                if(len(dl_num)):
                    count=count+1
                    for i in dl_num:
                        data['Dl Nums'].append(i)

                if(len(date_of_birth)):
                    count=count+1
                    for i in date_of_birth:
                        data['DOB'].append(i)

                if(len(emails)):
                    count=count+1
                    for i in emails:
                        data['Emails'].append(i)

                if(len(ip_address)):
                    count=count+1
                    for i in ip_address:
                        data['Ip_add'].append(i)
                if(len(mac_address)):
                    count=count+1
                    for i in mac_address:
                        data['Mac Address'].append(i)

                if(len(phone_number)):
                    count=count+1
                    for i in phone_number:
                        data['Phone Number'].append(i)

                if(len(snn_numbers)):   
                    count=count+1
                    for i in snn_numbers:    
                        data['SSN Nums'].append(i)

                if(len(vin_number)):
                    count=count+1
                    for i in vin_number:
                        data['VIN Nums'].append(i)
                data['Non Compliance Elemets'].append(count)
                fname=path.name[:-4]+'.csv'
                temp=output_dir
                temp1=temp+"\ "
                fname=temp1[0:-1]+fname
                if(count > 0):
                    num_non_comp=num_comp+1
                else:
                    num_comp=num_non_comp+1

                (pd.DataFrame.from_dict(data=data, orient='index').to_csv(fname, header=False))
                pd.read_csv(fname, header=None).T.to_csv(fname, header=False, index=False)
    return num_comp, num_non_comp
                
                


