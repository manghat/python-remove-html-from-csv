
# coding: utf-8

# # Dependancies

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import re
import html

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&.{4};')
    cleantext = re.sub(cleanr, '', str(raw_html))
#     replacing the special characters
#     cleanr = re.compile ('\\n')
#     cleantext = re.sub(cleanr, ' ', cleantext)
    clean = re.sub('\s+',' ',cleantext)
    return html.unescape(clean) # replaces the special characters


#same using beautifulsoup

def remove_html_escape(html):
    return BeautifulSoup(str(html), "lxml").text


# In[9]:


file = input("Enter CSV File name (without '.csv' at the end): ")


# In[10]:


# reading the file
try:
    d = pd.read_csv("%s.csv" % file )
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("File read successfully")
    


# In[11]:


a = pd.DataFrame(d)
print("File preview: \n",a.head(5))


# In[15]:



col = input("Enter column name: ")

try: 
    a[col][0:5]
except:
    print("Error in fetching column. Please check the name '%s' from the table preview above" %col)
else:
    print("Column read successfully: \n", a[col][0:5])


# In[16]:


a['clean'] = a[col].apply(cleanhtml)


# In[17]:


a['clean_bs'] = a['question'].apply(remove_html_escape)


# In[18]:


# a.head(5)


# In[19]:


a['parity'] = a[col].str.len() - a['clean'].str.len() #using regex
a['parity_bs'] = a[col].str.len() - a['clean_bs'].str.len() #using beautifulsoup


# In[24]:


# a.tail(5)

print ("------------------------------------------------- \n HTML has been removed from your column contents \n------------------------------------------------- \n ")
print ("column 'clean' contins regex replacement of anything in between < > or &; or \\* \nin otherwords, it removes any html with the space character, no conversion of special characters to respective ASCII values.")
print ("column 'clean_bs' contains html removed with special characters replaced with their respective ASCII characters.")
print ("Parity columns show the difference in number of characters from the original html")

print ("Output table: \n %s" %a.head(5))


# In[13]:


a.to_csv("%shtml_cleaned_output.csv"%file)
print("New file '%shtml_cleaned_output.csv' generated with cleaned columns. Check in the same direcotry"%file)

