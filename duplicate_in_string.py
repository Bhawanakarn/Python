#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Write a code to remove duplicates from an unsorted linked list.
def dupli(list):
    new_list = []
    count = 0
    for i in list:
        if i not in new_list:
            new_list.append(i)
            count = len(list) - len(new_list)
        else: 
            pass
    print("The total number of duplicates are:", count)
    print("The new list is:", (new_list))
#driver
#dupli([1,2,2,3,5])
dupli([1, 3, 5, 6, 3, 5])
dupli([1,2,3,3,5,8])


# In[ ]:




