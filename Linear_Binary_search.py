#!/usr/bin/env python
# coding: utf-8

# # Linear Search

# In[2]:


def locate(cards, ele):
    pos = 0
    while pos < len(cards):
        if ele == cards[pos]:
            return pos
        pos+=1
    return -1


# In[3]:


cards = []
ele = 3
locate(cards, ele)


# In[4]:


cards = [2, 6, 7, 3, 5, 8]
ele = 7
locate(cards, ele)


# In[5]:


cards = [2, 6, 7, 3, 5, 8]
ele = 2
locate(cards, ele)


# In[6]:


cards = [2, 6, 7, 3, 5, 8]
ele = 8
locate(cards, ele)


# # Binary Search

# In[11]:


def location(cards, ele, mid):
    mid_num = cards[mid]
    if mid_num == ele:
        if mid-1 >= 0 and cards[mid-1] == ele:
            return 'left'
        else:
            return 'found'
    elif mid_num < ele:
        return 'left'
    else:
        return 'right'


def locate_card(cards, ele):
    lo, hi = 0, len(cards)-1
    while lo <= hi:
        print(f'lo-{lo}, hi-{hi}')
        mid = (lo+hi)//2
        result = location(cards, ele, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1


# In[12]:


input_ele = {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}
locate_card(input_ele['cards'], input_ele['query'])


# In[13]:


input_ele = {'cards': [8, 8, 6, 3, 2, 2, 2, 0, 0], 'query': 8}
locate_card(input_ele['cards'], input_ele['query'])


# In[14]:


input_ele = {'cards': [8, 8, 6, 3, 2, 2, 2, 0, 0], 'query': 0}
locate_card(input_ele['cards'], input_ele['query'])


# In[ ]:




