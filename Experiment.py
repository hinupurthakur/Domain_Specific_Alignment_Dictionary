#!/usr/bin/env python
# coding: utf-8

# In[2]:


import Dict_from_TSV as d
import sys
import Occurance_based_preprocessing as oc
# e_sent_file = '/home/nupur/13Task/Merged_eng.txt'
# h_sent_file = '/home/nupur/13Task/Merged_wx.txt'
unknown = []
single_word = []
probable_word = []
multi_word = []
tsv_file=sys.argv[1]
eng_file=sys.argv[2]
hin_file=sys.argv[3]
all_words=d.extracting_e_words_from_tsv(tsv_file)
single,multi=d.creating_no_of_words_based_dict(all_words)
def multi_word_handling() :
    for e_word in multi :
#         print(e_word)
        sentences,e_occurence,length=oc.count_occurence(eng_file,e_word)
        result=oc.common_hindi_words(hin_file,sentences,length)
#         print(result)
        if e_occurence != 0 :
        #print("####",i)
            h_word_with_occ = result[0]
            h_word = h_word_with_occ[0]
            h_occurence = h_word_with_occ[1]
            if h_occurence > 2 :
                multi_word.append(e_word+" <> "+h_word)
            else :
                #str1="Maybe "+h_word+" with h_occurence = "+str(h_occurence)+" for e_occurence = "+str(e_occurence)
                probable_word.append(e_word+" <> "+h_word)
            
        else :
            unknown.append(e_word)

def single_word_handling() :
#     print(single)
    for e_word in single :
#         print(e_word)
        sentences,e_occurence,length=oc.count_occurence(eng_file,e_word)
        #print(e_occurence)
        result=oc.common_hindi_words(hin_file,sentences,length)
        #print(result)
        if e_occurence != 0 :
        #print("####",i)
            h_word_with_occ = result[0]
            h_word = h_word_with_occ[0]
            h_occurence = h_word_with_occ[1]
            if h_occurence >= (e_occurence/2 -1) :
                str1=e_word+" <> "+h_word
#                 print(str1)
                single_word.append(str1)
            else :
                #str1="Maybe "+h_word+" with h_occurence = "+str(h_occurence)+" for e_occurence = "+str(e_occurence)
                probable_word.append(e_word+" <> "+h_word)
            
        else :
            unknown.append(e_word)
def dict_creation() :
    with open("Output/Multi_word.txt","w") as mul :
        print("CONFIRM MULTI-WORD MEANING")
        for i in multi_word :
            print(i)
            mul.write(i+"\n")
    with open("Output/Single_word.txt","w") as confirm :
        print("CONFIRM MEANING")
        for i in single_word :
            print(i)
            confirm.write(i+"\n")
    with open("Output/Probable_dict.txt","w") as probable :
        print("PROBABLE MEANING")
        for i in probable_word :
            print(i)
            probable.write(i+"\n")
    with open("Output/Unknown_word_list.txt","w") as un :
        print("UNKNOWN WORDS")
        for i in unknown :
            print(i)
            un.write(i+"\n")

# print(unknown)

multi_word_handling()
single_word_handling()
dict_creation()


# In[ ]:





# In[ ]:




