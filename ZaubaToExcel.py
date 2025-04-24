#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as req
from bs4 import BeautifulSoup
import re


# In[16]:


s=input("Enter company name:")
company=s.replace(" ","-")
company=company.lower()
print(company)
url="https://www.zaubacorp.com/companysearchresults/"+company
attr={"class":"container basic-cont"}
r=req.get(url)
soup=BeautifulSoup(r.content)


l=soup.find_all("div",attr)
child=list(l[0].children)
text=str(child[2])
if text[4:len(text)-4].startswith("We are unable to find"):
    print("Company not available in Zauba")
else:
    print("Company found")
    l=soup.find_all("h5")
    id=str(l[0])[4:len(l)-8]
    name=str(l[1])[4:len(l)-8]
    url="https://www.zaubacorp.com/company/"+company.upper()+"/"+id
    print(url)


# In[ ]:




