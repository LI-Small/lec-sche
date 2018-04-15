# -*- coding:utf-8  -*-

import sys, requests, bs4, pandas, html5lib, re, csv

"""https://syllabus.naist.jp/subjects/preview_detail/[番号]"""
oriUrl = 'https://syllabus.naist.jp/subjects/preview_detail/'

table = [['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time']]

"""[番号]:名前の対応"""
dict = {19:"JohoRikogaku", 20:"JohoSeimei", 25:"DataScience", 26:"KeishikiGengo", 33:"KouseinouKeisanKiban",
		34:"SoftwareSekkeiron"}

args = sys.argv

for i in range(1,len(args)):

	url = oriUrl + args[i]

	data = pandas.io.html.read_html(url)

	print(url)

	for j in range(1,9):

		if (data[4][1][j].find('B:')) != -1:
			p = data[4][1][j].find('B:')
			data[4][1][j] = data[4][1][j][2:p]

		elem = re.findall(r'\d+', data[4][1][j])

		month = elem[0].zfill(2)
		day = elem[1].zfill(2)
		year = '2018'

		startDate = month + '/' + day + '/' + year
		endDate = startDate

		#print(elem)

		if elem[2] == '1':
			startTime = '9:20 AM'
			endTime = '10:50 AM'
		elif elem[2] == '2':
			startTime = '11:00 AM'
			endTime = '12:30 PM'
		elif elem[2] == '3':
			startTime = '1:30 PM'
			endTime = '3:00 PM'
		elif elem[2] == '4':
			startTime = '3:10 PM'
			endTime = '4:40 PM'
		elif elem[2] == '5':
			startTime = '4:50 PM'
			endTime = '6:20 PM'
		elif elem[2] == '6':
			startTime = '6:30 PM'
			endTime = '8:00 PM'
		else:
			startTime = ' '
			endTime = ' '

		subject = dict[int(args[i])]

		sche = [subject, startDate, startTime, endDate, endTime]

		table.append(sche)

		#print(table)

#print(table)

"""出力するcsvのファイル名"""
f = open('schedule.csv', 'ab')
dataWriter = csv.writer(f)
dataWriter.writerows(table)

