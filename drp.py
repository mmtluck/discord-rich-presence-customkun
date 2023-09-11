from pypresence import (
    Presence,
)  # https://qwertyquerty.github.io/pypresence/html/index.html
import time
import presence_info as prIn

# 経過時間表示用
elapsed_time = int(time.time())
# 現在時刻表示用
present_time = None
# 画像URLを指定(サンプル)
custom_image_url = "https://media.tenor.com/cgiP2AOrxaQAAAAj/yuumi-cat.gif"

RPC = None


# Discord Rich Presenceに接続
def drpConnect(client_id):
    # オブジェクトの初期化
    global RPC
    RPC = Presence(client_id)
    RPC.connect()


# Discord Rich Presenceから切断
def drpDisconnect():
    global RPC
    RPC.close()


# Discord Rich Presenceの情報を更新
def drpUpdate(presence_info: prIn.PresenceInfo):
    # buttonsは0件のリストだとエラーになるのでNoneで初期化
    if len(presence_info.button_list) == 0:
        presence_info.button_list = None
    RPC.update(
        # 大画像とマウスオーバー時のテキスト
        large_image=presence_info.l_image_url,
        large_text=presence_info.l_image_txt,
        # 小画像とマウスオーバー時のテキスト
        # ※１行目はポータルサイトでのみ設定可能
        # ２行目に表示される文章
        details=presence_info.detail,
        # ３行目に表示される文章
        state=presence_info.status,
        # プログラム起動からの経過時間
        start=elapsed_time,
        # ボタンとクリック時に遷移するURL
        buttons=presence_info.button_list,
    )
