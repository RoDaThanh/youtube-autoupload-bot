# youtube-autoupload-bot
upload video to youtube with selenium



Before to start:

* Python installed
* Selenium-4.8.3 installed
* Take an eyses on imports library in script
* chrome version 11

There is 2 script
- one is download.py
- second is uploadVideo.py

``` download.py ``` is for dowload videos from tiktok that you defind in script. 
For example: 

`bot.get("https://www.tiktok.com/search?q=dance%20trend%20tiktok")`

Set up to download: 

- add chrome agrument: 
* options.add_argument("user-data-dir=C:\\Users\\tg\\AppData\\Local\\Google\\Chrome\\User Data")
* options.add_argument('profile-directory=Profile 2') 
* options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
 
 Go to your chrome and type `chrome://version/` then coppy like pic beloww:
 ![image](https://user-images.githubusercontent.com/117510172/232280629-e3f545c2-0858-4839-ba30-333da1eb50a8.png)
 
 * add tiktok link: `bot.get("https://www.tiktok.com/search?q=dance%20trend%20tiktok")`
 * add cookies, headers, params, data when call rest to `https://ssstik.io/abc` -- in oder to download video. Res: https://www.youtube.com/watch?v=UsT11sOD1JA&t=960s
 
 Run cmd : `python download.py`
 
 **Remember close all chromes before run srcript.**

 
 ``` uploadVideo.py ``` is for dowload a video from tiktok that you defind in script and then upload that video to your youtube channel. 
 
 Set up:
 The same with dowload script. Make sure to sig in to youtube channel before.
 
  Run cmd : `python uploadvideo.py`
  
  **Remember close all chromes before run srcript.**

 
 # Bottom line is sometimes you will face to captcha then the script will fail =)), try to do the captcha manually and then run script again.
 
 **I am not a root author of these scipt, I jsut enhace and refactor some code that do for my needs.**
 
 **Res:**
 https://github.com/codewithvincent1/tiktokVideoScraper/blob/main/scrape_video.py
 
 https://github.com/redianmarku/youtube-autoupload-bot

 
 
