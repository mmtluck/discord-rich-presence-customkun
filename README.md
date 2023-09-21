# DRPカスタム君
Discord Rich Presenceをカスタムするためのアプリ


何のゲームモードをやってるか表示したり、ゲームにJoinしたり<br>パーティの人数を表示したり、ゲームの経過時間を表示したり<br>
<br>
…つまり「XXXをプレイ中」と表示されてるアレ


![2023-09-21_164812](https://github.com/mmtluck/discord-rich-presence-customkun/assets/87876753/c0399328-afe8-44c5-be19-2c1a92bcb2df)
<br>
これを自分で設定出来る

## 使い方

### 初期設定
・[Discord Developer Portal](https://discord.com/developers/applications/)にログイン<br>
・右上の「New application」をクリック<br>
・Applicationの名前を入力してアプリ作成<br>
　この時入力した名前がXXXをプレイ中のXXXの部分になる(後から変更可能)<br>
・作成したアプリをクリックして設定画面に入る<br>
　General InfomationのAPPLICATION IDを控えておく<br>

 ### 初回起動
 ・DRPカスタムくんを起動<br>
 1.Client ID入力欄に先ほど控えておいたAPPLICATION IDを貼り付け<br>
 2.上のラジオボタンが押せるようになるのでConnectをクリック<br>
 3.Details TextとStatus Text入力欄に好きな文言を入力※この欄は必須<br>
 4.画像を表示したい場合はLarge Image/Small Image入力欄に入力<br>
 5.ボタンを表示したい場合はButton Label/Button URL入力欄に入力<br>
 6.プレゼンス更新ボタンをクリックでカスタムプレゼンス起動！<br>
 
 ![2023-09-21_170838](https://github.com/mmtluck/discord-rich-presence-customkun/assets/87876753/c6d44f92-ff29-44fb-a584-fe7cbc5a9d1d)<br>
 ![2023-09-21_171945](https://github.com/mmtluck/discord-rich-presence-customkun/assets/87876753/2182048e-3e9a-4574-b204-58a0e62f25f2)<br>
<br>
<br>

 ### 2回目以降の起動
 config.iniに入力した情報が保存されている<br>
 アプリを起動してラジオボタンConnectをクリックするとそのままカスタムプレゼンスが起動する
