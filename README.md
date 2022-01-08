# IOT--Pet-Feeding-Machine
## 寵物餵食機 
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%81%B4%E9%9D%A2.jpg' width="400px">

#### 這個作品利用rasbperry pi和簡單的電子零件，搭配上linebot，可以選擇時間與餵食的量，在手機上就能輕鬆地幫家中的寵物餵食
## 硬體
> #### 樹梅派3(Raspberry pi 3)  
> #### 紅外線感測器(pir motion sensor)  
> #### 相機模組(camera module)  
> #### 減速馬達(GA12-N20)
> #### 厚紙板(cardboard)
### 電路圖
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/circuit.png' width="500px">

### 作品圖片  
#### 上方
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E4%B8%8A%E6%96%B9.jpg' width="400px">

#### 正面
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E6%AD%A3%E9%9D%A2.jpg' width="400px">

#### 內部箱子底部
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%85%A7%E7%AE%B1%E5%AD%90%E5%BA%95.jpg' width="400px">

#### 檔板
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E6%AA%94%E6%9D%BF.jpg' width="400px">

## 軟體
### LINE Developers(可在主機上操作)
#### 1.點擊下列網址(line developers官網)https://developers.line.biz/zh-hant/  
#### 2.點擊右上角的Log in，點擊使用line帳號登入  
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/line%E7%99%BB%E5%85%A5%E7%95%AB%E9%9D%A2.png' width="600px">

#### 3.畫面移到下方點擊Provider旁邊的create  
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%89%B5%E5%BB%BAprovider.png' width="600px">

#### 4.點擊剛建立的Provider接著點擊create a new channel
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E6%96%B0%E5%BB%BAchannel.png' width="600px">

#### 5.點擊Messaging API，輸入channel的基本資料(下方為四個必填選項)
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%AD%E5%AE%9Achannel.png' width="600px">  
<em>備註：name, description及上方未截圖的icon都在之後可做更換，category和subcategory不影響後續操作</em>

#### 6.勾選下方兩個閱讀選項，點擊下方create創建完成  
#### 7.點選新創建的channel，點擊Messaging API，按下Auto-reply messages
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%8A%E6%81%AF%E8%A8%AD%E5%AE%9A.png' width="600px">

#### 8.將自動回應訊息關閉，並把webhook啟用，如下圖所示
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%8A%E6%81%AF%E8%A8%AD%E5%AE%9A2.png' width="600px">

#### 9.回到line developers點擊Basic settings最下方會有channel專屬的secret(紅色方框區域)，python程式碼需要使用
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E9%A0%BB%E9%81%93%E5%AF%86%E7%A2%BC.png' width="600px">

#### 10.點擊Messaging API，按下最下方Channel access token內的issue，就會出現channel專屬的access token(紅色方框區域)，python程式碼需要使用
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E9%A0%BB%E9%81%93access.png' width="600px">

----
### Line official account  
#### 1.點擊下列網址(line official account官網)https://tw.linebiz.com/
#### 2.點擊右上方的登入管理頁面，再點擊下圖的管理頁面進行登入(流程與line developers相同)
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E7%99%BB%E5%85%A5line%E5%AE%98%E6%96%B9%E5%B8%B3%E8%99%9F.png' width="600px">

#### 3.在下方畫面點選剛才創立的channel
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E9%81%B8%E6%93%87channel.png' width="600px">

#### 4.在左側點選聊天室相關的圖文選單，接著點擊右上角的建立
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%BB%BA%E7%AB%8B%E5%9C%96%E6%96%87%E9%81%B8%E5%96%AE.png' width="600px">

#### 5.設定圖文選單，輸入標題及使用時間後，選擇想要的版型，並輸入相對應的關鍵字。範例為：A-setting B-feed C-check
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%9C%96%E6%96%87%E9%81%B8%E5%96%AE%E8%A8%AD%E5%AE%9A.png' width="600px">

#### 6.點選最下方的儲存即建立完成

----
### Ngrok(需在Raspberrypi上操作)
#### 1.點擊下列網址(ngrok官網)https://ngrok.com/  
#### 2.點擊右上角Log，可使用github或是google帳號登入
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/ngrok%E7%99%BB%E5%85%A5.png' width="600px">

#### 3.下載ngrok(請選擇Linux(ARM)版本)
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/nrgok%E4%B8%8B%E8%BC%89.png' width="600px">

#### 4.解壓縮tgz檔
    tar zxvf FileName.tgz
#### 5.在Downloads的目錄底下輸入以下指令(以port=5000開啟ngrok)
    ngrok http 5000
#### 如果成功就會出現以下畫面
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/ngrok%E6%88%90%E5%8A%9F.png' width="600px">
<em>備註：白色遮擋部分為英數夾雜的字串</em>

#### 6.完成ngrok設定
----
### Python 程式碼(需在Raspberrypi上操作) 
### 所有程式碼都在以下網址(即上方linebot資料夾)https://github.com/andy258741/IOT--Pet-Feeding-Machine/tree/main/line_bot 
#### 1.在開始編寫程式碼之前，請至terminal輸入以下指令(安裝linebot sdk)
    sudo apt-get line-bot-sdk
#### 2.在開始編寫程式碼之前，請至terminal輸入以下指令(安裝ssmtp和mailutils)
    sudo apt-get install ssmtp mailutils  
#### 接著請按照下列網址設定ssmtp和gmail https://ithelp.ithome.com.tw/articles/10196110
<em>備註：若按照網址中測試指令( echo "這是信件內容。" | ssmtp recipient@your.domain.com) 得到回應為ssmtp:(raspberrypi) 是正常的，因為ssmtp無法在buster底下使用。  
    若要測試請使用以下網址的程式碼並在python環境底下進行測試https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/mail_test.py</em>
    
#### 3.程式碼  
> #### app.py:設定此python程式在(http://127.0.0.1:5000) 上運行
> #### line_chatbot_api.py:載入所需linebot_api，並設定channel secret和channel token
> #### line_chatbot_handle.py:處理由line客戶端傳回來的訊息，並控制raspberypi
> #### mail.py:利用smtp寄送郵件

#### 4.程式碼說明  
##### 4.1 app.py
##### 可在最下方程式碼更改運行的port號，其餘部分不須更動
    if __name__ == "__main__":
        app.run(host='127.0.0.1', port=你想要的port號, debug=True)
##### 4.2 line_bot_api.py  
> ##### channel access token設定
    line_bot_api = LineBotApi('your channel secret token')
> ##### channel secret設定
    handler = WebhookHandler('your channel secret')
##### 4.3 line_bot_handle.py  
> ##### function_handle_something(event)：用來處裡收到的字串，以做出相對應的處理，像是呼叫函式或是回傳訊息
> ##### setting(event)：回傳一個carouseltemplate讓使用者選擇設定的投餵時間和投餵份量
> ##### job():根據設定讓減速馬達轉動，並呼叫pir()
> ##### pir():感測寵物，若感測到則呼叫camera()拍照
> ##### camera():拍照並儲存於桌面，之後呼叫mail.py裡面的send_mail()
> ##### check(event):查看目前的設定(時間和量)
> ##### startnow(event):根據目前所設定的量立即啟動餵食
> ##### start(event):利用Timer讓餵食機在正確的時間啟動
##### 4.4 mail.py
> ##### send_mail():寄送寵物進食的照片，並告訴飼主成功餵食
<em>備註：這四個.py檔需存放在同個目錄底下，範例是放在Desktop資料夾</em>

----
## 實作(需在Raspberrypi上操作)  
### Step 1：在terminal輸入下列指令，進入app.py的所在目錄(範例為Desktop)並啟動app.py
    cd Desktop
    sudo python3 app.py
#### 成功後出現以下畫面：
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%95%9F%E5%8B%95app.py.png' width="600px">

#### Step 2：在terminal輸入下列指令啟用ngrok，並複製https
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A4%87%E8%A3%BDhttps.png' width="600px">

#### Step 3：到Line Delelopers開啟剛剛創建的channel，點擊Messaging API，找到Webhook settings併案下edit
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%AD%E5%AE%9Awebhook.png' width="600px">

#### Step 4：將剛才複製的網址貼上並在後面加上<em>/callback</em>，點擊update  
#### Step 5：開啟下方的Use Webhook並點擊vertify
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E9%BB%9E%E6%93%8Avertify.png' width="600px">

#### 若成功就會出現以下畫面
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E6%88%90%E5%8A%9F.png' width="600px">

#### Step 6：到Line Delelopers開啟channel，並點擊Messing API，用BOT basic ID或是QR code連接linebot
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E9%80%A3%E6%8E%A5linebot.png' width="600px">

#### Step 7：恭喜!可以開始操作了!

#### 實際運行影片
https://youtu.be/1DA6Vm8g91Y

----
### 改進、改善  
#### 1.可以將重物壓在底下將底盤加重，或是使用無痕貼緊貼牆邊，防止傾倒  
#### 2.減速馬達的優點是動力較大，且速度較慢，然而不能控制旋轉圈數，因此只能慢慢測試出轉動一圈所需要的時間，再將數值填入sleep函數當中，使用步進馬達可能是更好的選擇  
#### 3.定時工作使用threading.timer，不適合指定多次工作，使用apscheduler會是更好的選擇  
#### 4.因為沒有適合的加工器具，所以選擇使用紙箱，如果有適合的工具，使用壓克力或是其他堅固防水材質會是更好的選擇

----
### 參考網站
> timethreading:https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/693491/  
> Picamera:https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/0  
> 紅外線感測器:http://hophd.com/raspberry-pi-sensor-infrared/  
> ngrok:https://noob.tw/ngrok/  
> tgz解壓縮:http://note.drx.tw/2008/04/command.html  
> 時間加減:https://www.twblogs.net/a/5c9e9e3bbd9eee73ef4b66dc  
> smtp內容:https://forums.raspberrypi.com/viewtopic.php?t=263695  
> smtp設定:https://ithelp.ithome.com.tw/articles/10196110  
> 傳送照片:https://www.itread01.com/content/1548600499.html  
> ssmtp測試:https://forums.raspberrypi.com/viewtopic.php?t=263695  
