import re

#kanonikes ekfraseis gia ta zitoumena

rexp1 = re.compile(r'<title>(.+?)</title>') #zitoumeno1 eksagwgi titlou sto rexp1

rexp2 = re.compile(r'<!--.*?-->',re.DOTALL) #zitoumeno2 eksagwgi sxoliwn sto rexp2

rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL) #zitoumeno3 eksagwgi script/style tags mazi me to periexomeno

rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) #zitoumeno4 eksagwgi sindesmou 

rexp5a = re.compile(r'<.+?>|</.+?>',re.DOTALL) #zitoumeno5a eksagwgi tags me dipli morfi 
rexp5b = re.compile(r'<.+?/>',re.DOTALL) #zitoumeno5b eksagwgi tags me moni morfi 

rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') #zitoumeno6 eksagwgi twn html entries

rexp7 = re.compile(r'\s+') #zitoumeno7 eksagwgi sinexomenwn whitespaces


#sinartisi i opoia metatrepei ta html entries opws mas perigrafei o pinakas

def cb(m):
  if(m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  elif (m.group(0)=='&lt;'):
    return '<'
  elif (m.group(0)=='&nbsp;'):
    return ' '


with open('testpage.txt','r',encoding='utf-8') as fp: #anoigma arxeiwn (apo windows)
  text = fp.read()
  m = rexp1.search(text)
  print(m.group(1)) #ektipwsi titlwn
  
  text = rexp2.sub(' ',text) #apaloifi sxoliwn
  
  text = rexp3.sub(' ',text) #apaloifi script kai style tags
  
  for m in rexp4.finditer(text): 
    print('{} {}'.format(m.group(1),m.group(2)))#ektipwsi links
    
  text = rexp5a.sub(' ',text) 
  text = rexp5b.sub(' ',text) #apaloifi tags

  text = rexp6.sub(cb,text) #metatropi html entries

  text = rexp7.sub(' ',text) #metatropi sinexomenwn kenwn se ena keno

  print(text)
