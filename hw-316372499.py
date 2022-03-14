#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverse(sentence, word):
    if type(sentence)==str and type(word)==str:
        text=sentence.split()    
        if word in text:
            place=text.index(word)
            return(sentence.replace(text[place],word[::-1],1))
        elif word not in text:
            return("no match word found")
    else:
         return("invalid input")

        
       
           
    
print(reverse('how are you? are','are'))

