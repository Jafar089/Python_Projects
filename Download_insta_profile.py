# This is for download instagram profile picture

import instaloader
bot1=instaloader.Instaloader()
username = "your username"
print(bot1.download_profile(username,profile_pic_only=True))