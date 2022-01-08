# IOT--Pet-Feeding-Machine
## 寵物餵食機 
這個作品利用rasbperry pi和簡單的電子零件，搭配上linebot，可以選擇時間與餵食的量，在手機上就能輕鬆地幫家中的寵物餵食
## 硬體
> #### 樹梅派3(Raspberry pi 3)  
> #### 紅外線感測器(pir motion sensor)  
> #### 相機模組(camera module)  
> #### 減速馬達(GA12-N20)
> #### 厚紙板(cardboard)
## 軟體
### LINE Developers(可在主機上操作)
#### 1.點擊下列網址(line developers官網)https://developers.line.biz/zh-hant/  
#### 2.點擊右上角的Log in，點擊使用line帳號登入  
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/line%E7%99%BB%E5%85%A5%E7%95%AB%E9%9D%A2.png' width="700px">

#### 3.畫面移到下方點擊Provider旁邊的create  
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%89%B5%E5%BB%BAprovider.png' width="700px">

#### 4.點擊剛建立的Provider接著點擊create a new channel
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E6%96%B0%E5%BB%BAchannel.png' width="700px">

#### 5.點擊Messaging API，輸入channel的基本資料(下方為四個必填選項)
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%AD%E5%AE%9Achannel.png' width="700px">  
<em>備註：name, description及上方未截圖的icon都在之後可做更換，category和subcategory不影響後續操作</em>

#### 6.勾選下方兩個閱讀選項，點擊下方create創建完成  
#### 7.點選新創建的channel，點擊Messaging API，按下Auto-reply messages
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%8A%E6%81%AF%E8%A8%AD%E5%AE%9A.png' width="700px">

#### 8.將自動回應訊息關閉，並把webhook啟用，如下圖所示
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%8A%E6%81%AF%E8%A8%AD%E5%AE%9A2.png' width="700px">

#### 9.回到line developers點擊Basic settings最下方會有channel專屬的secret(紅色方框區域)，python程式碼需要使用
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E9%A0%BB%E9%81%93%E5%AF%86%E7%A2%BC.png' width="700px">

#### 10.點擊Messaging API，按下最下方Channel access token內的issue，就會出現channel專屬的access token(紅色方框區域)，python程式碼需要使用
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E9%A0%BB%E9%81%93access.png' width="700px">

----
### Ngrok(需在Raspberrypi上操作)
#### 1.點擊下列網址(ngrok官網)https://ngrok.com/  
#### 2.點擊右上角Log，可使用github或是google帳號登入
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/ngrok%E7%99%BB%E5%85%A5.png' width="700px">

#### 3.下載ngrok(請選擇Linux(ARM)版本)
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/nrgok%E4%B8%8B%E8%BC%89.png' width="700px">

#### 4.解壓縮tgz檔
    tar zxvf FileName.tgz
#### 5.在Downloads的目錄底下輸入以下指令(以port=5000開啟ngrok)
    ngrok http 5000
#### 如果成功就會出現以下畫面
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/ngrok%E6%88%90%E5%8A%9F.png' width="700px">
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
##### channel access token設定
    line_bot_api = LineBotApi('your channel secret token')
##### channel secret設定
    handler = WebhookHandler('your channel secret')
##### 4.3 line_bot_handle.py
##### 4.4 

