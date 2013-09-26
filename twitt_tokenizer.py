# -*- coding: utf-8 -*- 
#twitt_tokenizer removes 'rt :' from retwitts, replaces links with the 
#word 'httplink' and removes all punctuation signs except the '@' and 
#'#' symbols.
#Author: Andrés Babino

import nltk

def twitt_tokenizer(twitt):
  twitt_lower=twitt.lower() 
  twitt_lower.replace(' rt:',' ')
  splited_twitt=[w for w in twitt_lower.split()]
  splited_twitt_out=[]
  for i,w in enumerate(splited_twitt):
    if 'http' in w:
      splited_twitt_out.append('httplink')
      continue
    elif '@' in w or '#' in w:
      if ':' in w:
        splited_twitt_out.append(w.replace(':','').replace(u'“','').replace(u'¿','').replace(u'¿','').replace('?',''))
      else:
        splited_twitt_out.append(w)
      continue
    elif w.replace('.','').replace(',','').isdigit():
      splited_twitt_out.append(w)
      continue
    elif w=='rt':
      continue
    elif not w.isalpha():
      w_split=[tok for tok in nltk.tokenize.wordpunct_tokenize(w) if tok.isalnum()]
      for j,new_w in enumerate(w_split):
	splited_twitt_out.append(new_w)
    else:
      splited_twitt_out.append(w)
  return ' '.join(splited_twitt_out)

