#!/usr/bin/env python
# coding: utf-8

# In[26]:

import os
def extracting_e_words_from_tsv(filename) : 
    with open(os.getenv("HOME")+'/Domain_Specific_Alignment_Dictionary/'+filename,"r") as tsv:
        data = tsv.read().strip("\n").split("\n")
        data = data[1:]
        eng_words =[]
        for i in data :
            i=i.split("\t")
            eng=i[2].split(": ")[1]
            #print(eng)
            if int(i[3]) >= 10 :
                eng_words.append(eng)
    return(eng_words)

def creating_no_of_words_based_dict(all_eng) :
    
    single_word_dict = []
    multi_word_dict = []
    for word in all_eng :
        temp=word.split(" ")
        if len(temp) == 1 :
            single_word_dict.append(word)
        else :
            multi_word_dict.append(word)
    return single_word_dict,multi_word_dict
#all_words=extracting_e_words_from_tsv(filename)
#s,m=creating_no_of_words_based_dict(all_words)
#print(s)

# In[ ]:




