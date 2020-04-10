import requests
import os
import time

session = requests.Session()
for i in range(1,20) :#19个班
	stulist = session.get("http://115.239.202.76:8181/api/yw_sch.ashx?type=faceList&sch_Type=%E6%99%AE%E9%80%9A%E9%AB%98%E4%B8%AD&schName=%E6%B5%99%E6%B1%9F%E7%9C%81%E4%B9%89%E4%B9%8C%E4%B8%AD%E5%AD%A6&gradeName=%E9%AB%98%E4%B8%89&className=%E9%AB%98%E4%B8%89（"+str(i)+"）%E7%8F%AD").text
	pos=stulist.find("facePhoto\":\"")
	while(pos>0):
		en=stulist.find("\",\"creatTime",pos)
		url=stulist[pos+12:en]
		img=session.get(url).content
		filename=stulist[stulist.rfind("/",pos,en)+1:en]
		with open(filename,"wb") as f:
			f.write(img)
		pos=stulist.find("facePhoto\":\"",pos+5)
print("successful")

