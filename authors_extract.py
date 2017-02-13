__author__ = 'shepherd'

import io
import urllib
from bs4 import BeautifulSoup

f = io.open('/home/hank/Documents/codes/aditya/docTest.tsv','w', encoding='utf-8')

alp1 = 492
alp2 = 63303
for i in range(26):
	alp1 += 1
	alp2 += 1
	url = 'http://www.nndb.com/lists/'+str(alp1)+"/0000"+str(alp2)+"/"
	print url
	response = urllib.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	Author_links = []

	data = soup.findAll("td", {"valign": "middle"})
	for t in data:
		if t.text == 'Author':
			Author_links.append(t.find_previous_sibling().a['href'])

	for auth in Author_links:
		author_details = {}

		author_details['Name'] = ""
		author_details['AKA'] = ""
		author_details['Born'] = ""
		author_details['Birthplace'] = ""
		author_details['Died'] = ""
		author_details['Location of death'] = ""
		author_details['Cause of death'] = ""
		author_details['Remains'] = ""
		author_details['Gender'] = ""
		author_details['Religion'] = ""
		author_details['Race'] = ""
		author_details['Sexual orientation'] = ""
		author_details['Occupation'] = ""
		author_details['Official Website'] = ""
		author_details['Nationality'] = ""
		author_details['Executive summary'] = ""
		#author_details['Relations'] = ""
		author_details['Author of books'] = ""

		url_p = auth
		response_p = urllib.urlopen(url_p)
		html_p = response_p.read()
		soup_p = BeautifulSoup(html_p)


		data_p = soup_p.findAll("b")

		name = data_p[2].text
		author_details['Name'] = name

		for i in range(3,len(data_p)):
			tg = data_p[i]
			tg_key = str(tg.text.strip(":"))
			if tg_key == '':
				continue

			elif tg_key == 'Official Website':
				tg_val = tg.next.next.a.text

			elif tg_key == 'Author of books':
				books_i = tg.next.next.findAll('i')
				books = '|'.join([book.text for book in books_i]).replace("\n","")
				tg_val = books
				author_details[tg_key] = tg_val
				break


			else:
				tg_val = tg.next.next
				if tg_val == u' ':
					tg_val = tg.find_next_sibling().text

			author_details[tg_key] = tg_val
		
		f.write(author_details['Name'] + "\t" + author_details['AKA'] + "\t" + author_details['Born'] + "\t" + author_details['Birthplace'] + "\t" + author_details['Died'] + "\t" + author_details['Location of death'] + "\t" + author_details['Cause of death'] + "\t" + author_details['Remains'] + "\t" + author_details['Gender'] + "\t" + author_details['Religion'] + "\t" +author_details['Race'] + "\t" +author_details['Sexual orientation'] + "\t" + author_details['Occupation'] + "\t" + author_details['Official Website'] + "\t" + author_details['Nationality'] + "\t" + author_details['Executive summary'] + "\t" + author_details['Author of books'] + "\n".encode('utf-8'))

f.close()