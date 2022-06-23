from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
bert_tokenizer = AutoTokenizer.from_pretrained('dslim/bert-large-NER')
bert_model = AutoModelForTokenClassification.from_pretrained('dslim/bert-large-NER')
def get_name(text):
    

    nlp = pipeline('ner', model=bert_model, tokenizer=bert_tokenizer)
    ner_list = nlp(text)
    this_name = []
    all_names_list_tmp = []

    for ner_dict in ner_list:
        if ner_dict['entity'] == 'B-PER':
            if len(this_name) == 0:
                this_name.append(ner_dict['word'])
            else:
                all_names_list_tmp.append([this_name])
                this_name = []
                this_name.append(ner_dict['word'])
        elif ner_dict['entity'] == 'I-PER':
            this_name.append(ner_dict['word'])

    all_names_list_tmp.append([this_name])

    final_name_list = []
    for name_list in all_names_list_tmp:
        full_name = ' '.join(name_list[0]).replace('##', '').replace(' .', '.')
        final_name_list.append([full_name])
    ans=[]
    for i in final_name_list:
        str1 = "" 
    for ele in i: 
        str1 += ele 
    ans.append(str1)
    return ans
