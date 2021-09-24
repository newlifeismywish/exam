#!/usr/bin/env python
# coding: utf-8

# In[35]:


import urllib.parse
import urllib.request

url="https://cn.investing.com/instruments/HistoricalDataAjax"
header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
values={'curr_id': '6408',
'smlID': '1159963',
'header': 'AAPL历史数据',
'st_date': '2021/08/20',
'end_date': '2021/09/14',
'interval_sec': 'Daily',
'sort_col': 'date',
'sort_ord': 'DESC',
'action': 'historical_data'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data, headers=header)
response:=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))





