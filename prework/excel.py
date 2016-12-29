import xlrd
import pickle
# -*- coding:utf8 -*- # 
data = xlrd.open_workbook('word.xlsx')
table = data.sheets()[0]
wordlist = {}
nrows = table.nrows
for i in range(nrows):
	word = table.cell(i,1).value
	word = word.encode('utf8')
	paraphrase = table.cell(i,2).value
	paraphrase = paraphrase.encode('utf8') 
	wordlist[word] = paraphrase
wordfile = open("wordlist.pkl",'wb')
pickle.dump(wordlist, wordfile)
wordfile.close()
