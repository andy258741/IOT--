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
### LINE Developer
#### 1.點擊下列網址(line developer官網)https://developers.line.biz/zh-hant/  
#### 2.點擊右上角的Log in，點擊使用line帳號登入  
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/line%E7%99%BB%E5%85%A5%E7%95%AB%E9%9D%A2.png' width="700px">

#### 3.畫面移到下方點擊Provider旁邊的create  
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E5%89%B5%E5%BB%BAprovider.png' width="700px">

#### 4.點擊剛建立的Provider接著點擊create a new channel
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E6%96%B0%E5%BB%BAchannel.png' width="700px">

#### 5.點擊Messaging API，輸入channel的基本資料(下方為四個必填選項)
<img src='https://github.com/andy258741/IOT--Pet-Feeding-Machine/blob/main/image/%E8%A8%AD%E5%AE%9Achannel.png' width="700px">  
<em>備註：name, description及上方未截圖的icon都在之後可做更換，category和subcategory不影響後續操作</em>

#### 6.創建完成

----
### Python 程式碼  
#### 1.在開始編寫程式碼之前，請至terminal輸入以下指令(安裝linebot sdk)
    sudo apt-get line-bot-sdk
#### 2.在開始編寫程式碼之前，請至terminal輸入以下指令(安裝ssmtp和mailutils)
    sudo apt-get install ssmtp mailutils  
#### 接著請按照下列網址設定ssmtp和gmail https://ithelp.ithome.com.tw/articles/10196110
<em>若按照網址中測試指令( echo "這是信件內容。" | ssmtp recipient@your.domain.com) 得到回應為ssmtp:(raspberrypi) 是正常的，因為ssmtp無法在buster底下使用，若要測試請使用以下網址</em>
