import pip_line as pl
import pandas as pd
import fitz
import pathlib
import os
import textract
from pathlib import Path
def main_pipeline(input_dir,output_dir):
    num_comp=0
    num_non_comp=0

    for root, dirs, files in os.walk(input_dir):
        for name in files:
            count=0
            data={'File Name':[],
            #'Names':[],
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
            text=''
            data['File Name'].append(name)
            path=os.path.join(root,name)
            try:
                text = textract.process(path)
                text=text.decode('UTF-8')
            except Exception:
                pass
            if(name[-3:]=='txt' or name[-3:] == 'csv' or name[-3:]=='zip'):
                pass
            else:
                print(name)
                credit_cards,dl_num,date_of_birth,emails,ip_address,mac_address,phone_number,snn_numbers,vin_number=pl.extract_PII_pipeline(text)
                # if(len(names)):
                    #     count=count+1
                    #     for i in names:
                    #         data['Names'].append(i)

                if(len(credit_cards)):
                        count=count+1
                        for i in credit_cards:
                            for j in i:
                                data['Credit Card'].append(j)

                if(len(dl_num)):
                        count=count+1
                        for i in dl_num:
                            for j in i:
                                data['Dl Nums'].append(j)

                if(len(date_of_birth)):
                        count=count+1
                        for i in date_of_birth:
                            for j in i:
                                data['DOB'].append(j)

                if(len(emails)):
                        count=count+1
                        for i in emails:
                            for j in i:
                                data['Emails'].append(j)

                if(len(ip_address)):
                        count=count+1
                        for i in ip_address:
                            for j in i:
                                data['Ip_add'].append(j)

                if(len(mac_address)):
                        count=count+1
                        for i in mac_address:
                            for j in i:
                                data['Mac Address'].append(j)

                if(len(phone_number)):
                        count=count+1
                        for i in phone_number:
                            for j in i:
                                data['Phone Number'].append(j)

                if(len(snn_numbers)):
                        count=count+1
                        for i in snn_numbers:
                            for j in i:
                                data['SSN Nums'].append(j)

                if(len(vin_number)):
                        count=count+1
                        for i in vin_number:
                            for j in i:
                                data['VIN Nums'].append(j)

                data['Non Compliance Elemets'].append(count)
                fname =Path(name).stem
                fname=fname+'.csv'
                temp=output_dir
                temp1=temp+"/ "
                fname=temp1[0:-1]+fname
                if(count > 0):
                    num_non_comp=num_non_comp+1
                else:
                    num_comp=num_comp+1
                (pd.DataFrame.from_dict(data=data, orient='index').to_csv(fname, header=False))
                pd.read_csv(fname, header=None).T.to_csv(fname, header=False, index=False)
    return num_comp, num_non_comp
