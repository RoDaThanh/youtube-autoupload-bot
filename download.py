import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen
import re



options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--no-sandbox')
options.add_argument("user-data-dir=C:\\Users\\tg\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('profile-directory=Profile 2')
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

bot = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
#bot.get("https://www.tiktok.com/search?q=dance%20trend%20tiktok")
bot.get("https://www.tiktok.com/@vnkafaz_hn")
#bot.get("https://www.tiktok.com/search?q=hot%20dance%20viet%20nam")
#https://www.tiktok.com/@vnkafaz_hn


# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
# to 60 seconds, just enough time for you to complete the captcha yourself.
time.sleep(2)
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def downloadVideo(link, id):
     print("Downloading video from: {link}")
     cookies = {
        
        }

     headers = {
        
        }

     params = {
       
        }

     data = {
        'id': link,
        'locale': 'vi',
        'tt': 'a3Y5VzVk',
        }
     print("STEP 4: Getting the download link")
     response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
     downloadSoup = BeautifulSoup(response.text, "html.parser")
     downloadLink = downloadSoup.a["href"]
     videoTitle = downloadSoup.p.getText().strip()
     videoTitle = remove_emoji(videoTitle).replace(" ", "_")


     print("STEP 5: Saving the video :)")
     mp4File = urlopen(downloadLink)
     # Feel free to change the download directory
     with open(f"videos/video{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break
     return videoTitle



scroll_pause_time = 1
screen_height = bot.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    bot.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = bot.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

soup = BeautifulSoup(bot.page_source, "html.parser")
# this class may change, so make sure to inspect the page and find the correct class
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})
print(f"before STEP 3: Time to download {len(videos)} videos")
if len(videos) > 20:
    videos = videos[:50]

print(f"STEP 3: Time to download {len(videos)} videos")
for index, video in enumerate(videos):
    print(f"Downloading video: {index}")
    downloadVideo(video.a["href"], index)
    time.sleep(10)


bot.quit


