from pypresence import (
    Presence,
)  # https://qwertyquerty.github.io/pypresence/html/index.html
import time
import presence_info as prIn

# 経過時間表示用
elapsed_time = int(time.time())
# 現在時刻表示用
present_time = None

RPC = None


# Discord Rich Presenceに接続
def drpConnect(client_id):
    # オブジェクトの初期化
    global RPC
    RPC = Presence(client_id)
    try:
        RPC.connect()
        return True
    except Exception as e:
        print(e)
        return False


# Discord Rich Presenceから切断
def drpDisconnect():
    global RPC
    try:
        RPC.close()
        print("Disconnected")
    except Exception as e:
        print(e)


# Discord Rich Presenceの情報を更新
def drpUpdate(presence_info: prIn.PresenceInfo):
    button_list = []
    if presence_info.button1_name:
        button_list.append(
            {
                "label": presence_info.button1_name,
                "url": presence_info.button1_url,
            }
        )
    if presence_info.button2_name:
        button_list.append(
            {
                "label": presence_info.button2_name,
                "url": presence_info.button2_url,
            }
        )
    if not presence_info.l_image_url:
        presence_info.l_image_url = None
    if not presence_info.l_image_txt:
        presence_info.l_image_txt = None
    if not presence_info.s_image_url:
        presence_info.s_image_url = None
    if not presence_info.s_image_txt:
        presence_info.s_image_txt = None

    RPC.update(
        # 大画像とマウスオーバー時のテキスト
        large_image=presence_info.l_image_url,
        large_text=presence_info.l_image_txt,
        # 小画像とマウスオーバー時のテキスト
        small_image=presence_info.s_image_url,
        small_text=presence_info.s_image_txt,
        # ※１行目はポータルサイトでのみ設定可能
        # ２行目に表示される文章
        details=presence_info.detail,
        # ３行目に表示される文章
        state=presence_info.status,
        # プログラム起動からの経過時間
        start=elapsed_time,
        # ボタンとクリック時に遷移するURL
        buttons=button_list,
    )
