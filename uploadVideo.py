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
#Profile 2
options.add_argument('profile-directory=Default')
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

bot = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
bot.get("https://www.tiktok.com/@thouthou_vanila")
#bot.get("https://www.tiktok.com/search?q=hot%20dance%20viet%20nam")

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

def downloadVideo(link):
     print("Downloading video from: {link}")
     cookies = {
        
        }

     headers = {
        
        }

     params = {
        'url': 'dl',
        }

     data = {
        
        }
     print("post video")
     response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
     downloadSoup = BeautifulSoup(response.text, "html.parser")
     downloadLink = downloadSoup.a["href"]
     videoTitle = downloadSoup.p.getText().strip()
     videoTitle = remove_emoji(videoTitle)
     if os.path.exists("videos/video.mp4"):
         os.remove("videos/video.mp4")
         time.sleep(5)

     print("STEP 5: Saving the video :)")
     mp4File = urlopen(downloadLink)
     # Feel free to change the download directory
     with open(f"videos/video.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break
     return videoTitle


soup = BeautifulSoup(bot.page_source, "html.parser")
# this class may change, so make sure to inspect the page and find the correct class
video = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})
print(len(video))
print(len(video[0]))
videoTitle = downloadVideo(video[0].a["href"])
print(videoTitle)
time.sleep(5)

#YouTube part
print("UpLoad video")
bot.get("https://studio.youtube.com")
time.sleep(3)
upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
upload_button.click()
time.sleep(1)

file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
simp_path = 'videos/video.mp4'
abs_path = os.path.abspath(simp_path)

file_input.send_keys(abs_path)

time.sleep(7)

title = bot.find_element(By.CLASS_NAME, 'style-scope ytcp-social-suggestions-textbox')

if videoTitle:
   if len(videoTitle) > 98:
      videoTitle = videoTitle[0:98]
   videoTitle += " "   
   title.send_keys(videoTitle)
else:
    title.send_keys("Best Tiktok Dance all the time")

time.sleep(5)
next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
for i in range(3):
   next_button.click()
   time.sleep(1)

done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
done_button.click()

if os.path.exists("videos/video.mp4"):
   os.remove("videos/video.mp4")
   time.sleep(5)

bot.quit


