
# coding: utf-8

# In[16]:





# In[11]:


import subprocess,os, string, sys, re
from nltk import ngrams
#
# enginput = "state"
e_file = sys.argv[1]
h_file = sys.argv[2]
enginput = sys.argv[3]


# print(e_sent_path)
def data_cleaning(data) :
    cleaned_data = []
    for sent in data :
        sent=sent.strip("\n")
        remove=string.punctuation
        remove=remove.replace("-","")
        sent=sent.translate(sent.maketrans('', '', remove))
        cleaned_data.append(sent)
#     print(cleaned_data)
    return cleaned_data
                                                                                                                                                                                   
def count_occurence(e_file,word):
    e_sent_file = os.getenv("HOME")+'/Domain_Specific_Alignment_Dictionary/'+e_file  
    length=len(word.split(" "))
    e_data=open(e_sent_file,"r").read()
    e_data=e_data.lower()
    e_data=e_data.split("\n")
#     print(cmd)
#     print(e_data)
    sent_no = []
    e_data=data_cleaning(e_data)
#     print(e_data)
    occurence=0
    for sent in e_data :
        sentgrams = ngrams(sent.split(), length)
        nwords = []
        for i in sentgrams :
            i=" ".join(i)
            #print(i)
            if word == i :
                occurence=occurence+1
                sent_no.append(e_data.index(sent))
    return sent_no,occurence,length

sentences,o,length=count_occurence(e_file,enginput)
#print(sentences)
print(o)
def common_hindi_words(h_file,sentences,length):
    from collections import Counter
    from statistics import mode 
    h_sent_file =  os.getenv("HOME")+'/Domain_Specific_Alignment_Dictionary/'+h_file
    hindi_data = []
    hindi_ngrams = []
    stopList ={'BI','ho','','ne','howA','honA','cAhie','prApwa','bI','wo','nbsp','hE','meM','kI','ke','ko','se','Ora','kA','ki','hEM','eka','jo','para','kriyA','lie','kiyA','karawA','usake','karane','yA','nahIM','hama','kara','sakawe','yaha','jAwA','o','ke','C2','-','tI'}
    h_data = open(h_sent_file,"r").read().split("\n")
    h_data = data_cleaning(h_data)
#   
    for i in sentences :
        
        temp=[word for word in h_data[i].split(" ") if word not in stopList]
        temp= " ".join(temp)
        hindi_data.append(temp)
        
#         print(i+1)
#     print(hindi_data)
    for i in hindi_data :
        sentgrams = ngrams(i.split(), length)
        for i in sentgrams :
            hindi_ngrams.append(" ".join(i))
    
    c = Counter(hindi_ngrams)
    most_hin_occured = c.most_common(2)
    if most_hin_occured != [] :
        return most_hin_occured
    
#     most_freq=mode(hindi_ngrams)
#     occ=hindi_ngrams.count(most_freq)
#     print(most_freq," ",occ)
        
    #hindi_data_flat = [item for sublist in hindi_data for item in sublist]
    #print(hindi_data_flat)
#     hindi_data=[word for word in hindi_data if word not in stopList]
#     print(hindi_data)
    #Counter = Counter(hindi_data)
    #most_hin_occured = Counter.most_common(2)
    #if most_hin_occured != [] :
     #   return most_hin_occured
    #print("###############")
    #print(hindi_data)

x=common_hindi_words(h_file,sentences,length)  
print(x)

