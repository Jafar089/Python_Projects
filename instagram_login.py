# This is for download instagram profile picture

# import instaloader
# bot1=instaloader.Instaloader()
# username = "your username"
# print(bot1.download_profile(username,profile_pic_only=True))



# THis is for checking correct email

# from verify_email import verify_email
# email_id = input("Enter your email id ")
# if(verify_email(email_id)):
#     print("This is a valid email address")
# else:
#     print("This is an invalid email address")




# THis is for uploading photo on instagram

from instabot import Botana
bot=Bot()
bot.login(username="put your username",password="put your password here")
bot.upload_photo("aa.jpeg")




#Facobook login using python program

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# email_id=input("Enter your email id! ")
# password=input("Enter your password! ")
# server=webdriver.Chrome(ChromeDriverManager().install())
# server.get('https://www.facebook.com/syed.sherazi.79462')
# username=server.find_element_by_id('pass')
# passw.send_keys(password)
# login=server.find_element_by_id('loginbutton')
# login.click()
# server.quit()




#Print all wifi passwords which you enter in your pc

# import subprocess
# data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
# connections=[i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# for i in connections:
#     results=subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('\n')
#     results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print("{:<30}| {:<}".format(i,results[0]))
#     except IndexError:
#         print("{:<30}| {:<}".format(i,""))




# Voice Recorder

# #import required libraries
# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv

# #sampling frequency
# freq = 44100
# #Recording Duration
# duration = 30

# #Start Recoder With The Given Values of duration and sample frequency
# recording = sd.rec(int(duration * freq), samplerate = freq, channels = 2)

# #Recode audio for the given number of seconds
# sd.wait()

# #this will convert the Numpy array to an Audio
# #File with The Given Sampling Frequency
# write("recording0.wav", freq, recording)

# #Convert the Numpy Array To Audio File
# wv.write("recording1.way", recording, freq, sampwidth = 2)

# if duration == 30:
#     print("Your voice has been recorded!")




# Python Quiz App

# import json
# import random
# import getpass

# user = []

# def play():
# 	print("\n==========QUIZ START==========")
# 	score = 0
# 	with open("assets/questions.json", 'r+') as f:
# 		j = json.load(f)
# 		for i in range(10):
# 			no_of_questions = len(j)
# 			ch = random.randint(0, no_of_questions-1)
# 			print(f'\nQ{i+1} {j[ch]["question"]}\n')
# 			for option in j[ch]["options"]:
# 				print(option)
# 			answer = input("\nEnter your answer: ")
# 			if j[ch]["answer"][0] == answer[0].upper():
# 				print("\nYou are correct")
# 				score+=1
# 			else:
# 				print("\nYou are incorrect")
# 			del j[ch]
# 		print(f'\nFINAL SCORE: {score}')

# def quizQuestions():
# 	if len(user) == 0:
# 		print("You must first login before adding questions.")
# 	elif len(user) == 2:
# 		if user[1] == "ADMIN":
# 			print('\n==========ADD QUESTIONS==========\n')
# 			ques = input("Enter the question that you want to add:\n")
# 			opt = []
# 			print("Enter the 4 options with character initials (A, B, C, D)")
# 			for _ in range(4):
# 				opt.append(input())
# 			ans = input("Enter the answer:\n")
# 			with open("assets/questions.json", 'r+') as f:
# 				questions = json.load(f)
# 				dic = {"question": ques, "options": opt, "answer": ans}
# 				questions.append(dic)
# 				f.seek(0)
# 				json.dump(questions, f)
# 				f.truncate()
# 				print("Question successfully added.")		
# 		else:
# 			print("You don't have access to adding questions. Only admins are allowed to add questions.")


# def createAccount():
# 	print("\n==========CREATE ACCOUNT==========")
# 	username = input("Enter your USERNAME: ")
# 	password = getpass.getpass(prompt= 'Enter your PASSWORD: ')
# 	with open('assets/user_accounts.json', 'r+') as user_accounts:
# 		users = json.load(user_accounts)
# 		if username in users.keys():
# 			print("An account of this Username already exists.\nPlease enter the login panel.")
# 		else:
# 			users[username] = [password, "PLAYER"]
# 			user_accounts.seek(0)
# 			json.dump(users, user_accounts)
# 			user_accounts.truncate()
# 			print("Account created successfully!")

# def loginAccount():
# 	print('\n==========LOGIN PANEL==========')
# 	username = input("USERNAME: ")
# 	password = getpass.getpass(prompt= 'PASSWORD: ')
# 	with open('assets/user_accounts.json', 'r') as user_accounts:
# 		users = json.load(user_accounts)
# 	if username not in users.keys():
# 		print("An account of that name doesn't exist.\nPlease create an account first.")
# 	elif username in users.keys():
# 		if users[username][0] != password:
# 			print("Your password is incorrect.\nPlease enter the correct password and try again.")
# 		elif users[username][0] == password:
# 			print("You have successfully logged in.\n")
# 			user.append(username)
# 			user.append(users[username][1])

# def logout():
# 	global user
# 	if len(user) == 0:
# 		print("You are already logged out.")
# 	else:
# 		user = []
# 		print("You have been logged out successfully.")

# def rules():
# 	print('''\n==========RULES==========
# 1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
# Your final score will be given at the end.
# 2. Each question consists of 1 point. There's no negative point for wrong answers.
# 3. You can create an account from ACCOUNT CREATION panel.
# 4. You can login using the LOGIN PANEL. Currently, the program can only login and not do anything more.
# 	''')

# def about():
# 	print('''\n==========ABOUT US==========
# This project has been created by Danish Ali.''')

# if __name__ == "__main__":
# 	choice = 1
# 	while choice != 7:
# 		print('\n=========WELCOME TO QUIZ MASTER==========')
# 		print('-----------------------------------------')
# 		print('1. PLAY QUIZ')
# 		print('2. ADD QUIZ QUESTIONS')
# 		print('3. CREATE AN ACCOUNT')
# 		print('4. LOGIN PANEL')
# 		print('5. LOGOUT PANEL')
# 		print('6. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
# 		print('7. EXIT')
# 		print('8. ABOUT US')
# 		choice = int(input('ENTER YOUR CHOICE: '))
# 		if choice == 1:
# 			play()
# 		elif choice == 2:
# 			quizQuestions()
# 		elif choice == 3:
# 			createAccount()
# 		elif choice == 4:
# 			loginAccount()
# 		elif choice == 5:
# 			logout()
# 		elif choice == 6:
# 			rules()
# 		elif choice == 7:
# 			break
# 		elif choice == 8:
# 			about()
# 		else:
# 			print('WRONG INPUT. ENTER THE CHOICE AGAIN')