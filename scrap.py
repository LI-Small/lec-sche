# -*- coding:utf-8  -*-

import os
import sys
import requests
import bs4
import pandas
import html5lib
import re
import csv

"""https://syllabus.naist.jp/subjects/preview_detail/[番号]"""
oriUrl = 'https://syllabus.naist.jp/subjects/preview_detail/'

table = [['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time']]

"""[番号]:名前の対応"""
dict = {
		2:"KagakuTetsugaku",
		19:"JohoRikogakuJoron",
		20:"JohoSeimeiJoron",
		21:"BioScienceJoron",
		22:"BionanoRikogakuJoron",
		23:"BussituRikogakuJoron",
		24:"ChonouSyakaiSouseiJoron",
		25:"DataScienceJoron",
		26:"KeishikiGengo",
		27:"PurogrammingEnsyu",
		28:"SingouSyori",
		29:"OuyouKaisekigaku",
		30:"DataKougakuKiso",
		31:"KikaiGakusyuGairon",
		32:"Kougaku",
		33:"KouseinouKeisanKiban",
		34:"SoftwareSekkeiron",
		35:"JinkouChinou",
		56:"BunsanComputingron",
		57:"AlgorithmSekkeiron",
		58:"UbiquitousSystem",
		59:"MobileComputingron",
		60:"KasoukaSystemKiban",
		61:"SoftwareKougaku",
		62:"InternetKougaku",
		63:"ComputerNetwork",
		64:"KankyouChinou",
		65:"SizenGengoSyori",
		66:"VirtualReality",
		67:"ComputerVision",
		68:"ComputerGraphics",
		69:"MediaJohoSyori",
		70:"MusenTsushinSystem",
		71:"ShingouKensyutsuRiron",
		72:"HumanComputerInteraction",
		73:"PatternNinshiki",
		74:"SyakaiSystemRiron",
		75:"KikaigakusyuToChinouseigyo",
		76:"ModelBaseSeigyo",
		77:"NingenRobotJohogaku",
		78:"SuriModelRon",
		80:"DataMining",
		81:"SeitaiIyouGazouKaiseki",
		82:"SeitaiIyouMediaJohogaku",
		#83:"DataScienceRon",
		88:"OtoJohoSyori",
		89:"KeiretsuDataModelling",
		90:"Robotics",
		91:"GendaiJohoSecurityRon",
		92:"JohoRiron",
		93:"HardwareSecurity",
		94:"FugoRiron",
		95:"KakuritsuKateiron",
		96:"KeisanShinkeiKagaku",
		97:"JohoSecurityUnyouLiteracy1",
		98:"JohoSecurityUnyouLiteracy2",
		102:"SaitekikaSugaku",
		103:"DataKaiseki"
		}

"""出力するcsvのファイル名"""
filename = 'schedule.csv'

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

		if 1 <= int(elem[0]) and int(elem[0]) <= 3:
			year = '2019'
		else:
			year = '2018'

		startDate = month + '/' + day + '/' + year
		endDate = startDate

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
			startTime = 'unknown'
			endTime = 'unknown'

		subject = dict[int(args[i])]

		sche = [subject, startDate, startTime, endDate, endTime]

		table.append(sche)

f = open(filename, 'ab')
dataWriter = csv.writer(f)
dataWriter.writerows(table)

print('output:' + os.path.dirname(os.path.abspath(__file__)) + '/' + filename)

