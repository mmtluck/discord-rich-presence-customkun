import flet as ft  # https://flet.dev/
import presence_info as prIn
import drp
import config as conf
import const
import webbrowser
from urllib.parse import urlparse


def check_clientid(pr, page):
    # クライアントIDが入力されている場合のみラジオボタン活性化
    if pr.client_id.current.value:
        pr.connect_radio.current.disabled = False
    else:
        pr.connect_radio.current.disabled = True
    page.update()


# 更新ボタン押下時 PresenceInfoオブジェクトに値を入れてプレゼンス更新
def update_presence(pr, page):
    presence_info = prIn.PresenceInfo()
    presence_info.client_id = pr.client_id.current.value
    presence_info.l_image_url = pr.l_image_url.current.value
    presence_info.l_image_txt = pr.l_image_txt.current.value
    presence_info.s_image_url = pr.s_image_url.current.value
    presence_info.s_image_txt = pr.s_image_txt.current.value
    presence_info.detail = pr.detail.current.value
    presence_info.status = pr.status.current.value
    # ボタン情報が入力されてる場合はボタンリストに追加
    if pr.button1_name.current.value:
        presence_info.button1_name = pr.button1_name.current.value
        presence_info.button1_url = pr.button1_url.current.value
    if pr.button2_name.current.value:
        presence_info.button2_name = pr.button2_name.current.value
        presence_info.button2_url = pr.button2_url.current.value

    # プレゼンス更新処理
    drp.drpUpdate(presence_info)
    pr.connection_status_message.current.value = const.RUNNING
    pr.connection_status_message.current.color = ft.colors.BLUE
    conf.save_presence_info(presence_info)
    page.update()


# ヘルプボタン押下時ReadMeページを開く
def on_click_popup():
    webbrowser.open(const.REPOSITORY)


# ラジオボタン切替時の処理 接続切り替えと各パーツのDisabled切り替え
def connect_process(pr, page):
    # Connect切り替え時に接続失敗した場合エラーメッセージを表示しDisconnectに切り替え
    if pr.connect_radio.current.value == const.RADIO_CHOICE[0]:
        pr.connection_status_message.current.value = const.CONNECTED
        pr.connection_status_message.current.color = ft.colors.WHITE
        # プレゼンス接続
        if not drp.drpConnect(pr.client_id.current.value):
            pr.connection_status_message.current.value = const.CONNECT_ERROR
            pr.connection_status_message.current.color = ft.colors.RED
        else:
            print("Connected")
            pr.connection_status_message.current.value = const.CONNECTED
            pr.connection_status_message.current.color = ft.colors.GREEN
            main_form_toggle_active_state(pr, True)
            update_button_active_decision(pr, page)

            # 切替時に必須項目入力済みの場合そのままカスタムプレゼンスを起動
            if (
                input_check_clientform(pr, page)
                and input_check_imageform(pr, page)
                and input_check_statusform(pr, page)
                and input_check_buttonform(pr, page)
            ):
                print("auto start")
                update_presence(pr, page)

    else:
        drp.drpDisconnect()
        pr.connection_status_message.current.value = const.DISCONNEDTED
        pr.connection_status_message.current.color = ft.colors.WHITE
        main_form_toggle_active_state(pr, False)
        update_button_active_decision(pr, page)

    page.update(page)


# client id  入力チェック
def input_check_clientform(pr, page):
    flag = True
    if all(char.isdigit() for char in pr.client_id.current.value) and check_len(
        pr.client_id.current.value, 1, 128
    ):
        pr.client_id.current.error_text = const.EMPTY
        pr.connect_radio.current.disabled = False

    else:
        pr.client_id.current.error_text = const.ERROR_INVALID_ID
        flag = False

    page.update()
    return flag


# large_image/small_image入力チェック
def input_check_imageform(pr, page):
    flag = True
    # large_image_url入力チェック
    if pr.l_image_url.current.value:
        if check_url(pr.l_image_url.current.value):
            pr.l_image_url.current.error_text = const.EMPTY
        else:
            pr.l_image_url.current.error_text = const.ERROR_INVALID_URL
            flag = False
    # l_image_textが入力されている場合の相関チェック
    elif pr.l_image_txt.current.value:
        pr.l_image_url.current.error_text = const.ERROR_REQUIRED_URL
        flag = False
    else:
        pr.l_image_url.current.error_text = const.EMPTY

    # large_image_text入力チェック
    if pr.l_image_txt.current.value:
        if check_len(pr.l_image_txt.current.value, 2, 128):
            pr.l_image_txt.current.error_text = const.EMPTY
        else:
            pr.l_image_txt.current.error_text = const.errmsg_invalid_length(2, 128)
            flag = False
    # large_image_urlが入力されている場合の相関チェック
    elif pr.l_image_url.current.value:
        pr.l_image_txt.current.error_text = const.errmsg_invalid_length(2, 128)
        flag = False
    else:
        pr.l_image_txt.current.error_text = const.EMPTY

    # small_image_url入力チェック
    if pr.s_image_url.current.value:
        if check_url(pr.s_image_url.current.value):
            pr.s_image_url.current.error_text = const.EMPTY
        else:
            pr.s_image_url.current.error_text = const.ERROR_INVALID_URL
            flag = False
    # small_image_textが入力されている場合の相関チェック
    elif pr.s_image_txt.current.value:
        pr.s_image_url.current.error_text = const.ERROR_REQUIRED_URL
        flag = False
    else:
        pr.s_image_url.current.error_text = const.EMPTY

    # small_image_text入力チェック
    if pr.s_image_txt.current.value:
        if check_len(pr.s_image_txt.current.value, 2, 128):
            pr.s_image_txt.current.error_text = const.EMPTY
        else:
            pr.s_image_txt.current.error_text = const.errmsg_invalid_length(2, 128)
            flag = False
    # small_image_urlが入力されている場合の相関チェック
    elif pr.s_image_url.current.value:
        pr.s_image_txt.current.error_text = const.errmsg_invalid_length(2, 128)
        flag = False
    else:
        pr.s_image_txt.current.error_text = const.EMPTY

    update_button_active_decision(pr, page)
    page.update()
    return flag


#
def input_check_statusform(pr, page):
    flag = True
    # Details入力チェック
    if check_len(pr.detail.current.value, 2, 128):
        pr.detail.current.error_text = const.EMPTY
    else:
        pr.detail.current.error_text = const.errmsg_invalid_length(2, 128)
        flag = False

    # Status入力チェック
    if check_len(pr.status.current.value, 2, 128):
        pr.status.current.error_text = const.EMPTY
    else:
        pr.status.current.error_text = const.errmsg_invalid_length(2, 128)
        flag = False

    update_button_active_decision(pr, page)
    page.update()
    return flag


def input_check_buttonform(pr, page):
    flag = True
    # button1_url入力チェック
    if pr.button1_url.current.value:
        if check_url(pr.button1_url.current.value):
            pr.button1_url.current.error_text = const.EMPTY
        else:
            pr.button1_url.current.error_text = const.ERROR_INVALID_URL
            flag = False
    # button1_labelが入力されている場合の相関チェック
    elif pr.button1_name.current.value:
        pr.button1_url.current.error_text = const.ERROR_REQUIRED_URL
        flag = False
    else:
        pr.button1_url.current.error_text = const.EMPTY
    # button1_label入力チェック
    if pr.button1_name.current.value:
        if check_len(pr.button1_name.current.value, 2, 32):
            pr.button1_name.current.error_text = const.EMPTY
        else:
            pr.button1_name.current.error_text = const.errmsg_invalid_length(2, 32)
            flag = False
    # button1_urlが入力されている場合の相関チェック
    elif pr.button1_url.current.value:
        pr.button1_name.current.error_text = const.errmsg_invalid_length(2, 32)
        flag = False
    else:
        pr.button1_name.current.error_text = const.EMPTY

    # button2_url入力チェック
    if pr.button2_url.current.value:
        if check_url(pr.button2_url.current.value):
            pr.button2_url.current.error_text = const.EMPTY
        else:
            pr.button2_url.current.error_text = const.ERROR_INVALID_URL
            flag = False
    # button2_labelが入力されている場合の相関チェック
    elif pr.button2_name.current.value:
        pr.button2_url.current.error_text = const.ERROR_REQUIRED_URL
        flag = False
    else:
        pr.button2_url.current.error_text = const.EMPTY
    # button2_label入力チェック
    if pr.button2_name.current.value:
        if check_len(pr.button2_name.current.value, 2, 32):
            pr.button2_name.current.error_text = const.EMPTY
        else:
            pr.button2_name.current.error_text = const.errmsg_invalid_length(2, 32)
            flag = False
    # button2_urlが入力されている場合の相関チェック
    elif pr.button2_url.current.value:
        pr.button2_name.current.error_text = const.errmsg_invalid_length(2, 32)
        flag = False
    else:
        pr.button2_name.current.error_text = const.EMPTY

    update_button_active_decision(pr, page)
    page.update()
    return flag


# 各フォームのエラーチェック エラーがなければ更新ボタン活性化
def update_button_active_decision(pr, page):
    if pr.connect_radio.current.value == const.RADIO_CHOICE[0] and (
        pr.l_image_url.current.error_text
        or pr.l_image_txt.current.error_text
        or pr.s_image_url.current.error_text
        or pr.s_image_txt.current.error_text
        or pr.detail.current.error_text
        or pr.status.current.error_text
        or pr.button1_url.current.error_text
        or pr.button1_name.current.error_text
        or pr.button2_url.current.error_text
        or pr.button2_name.current.error_text
    ):
        pr.update_button.current.disabled = True
    else:
        pr.update_button.current.disabled = False
    page.update()


# 保存されている状態を呼び出す
def load_info(pr):
    if conf.init_config():
        conf_info = conf.get_config()
        pr.client_id.current.value = conf_info.client_id
        pr.l_image_url.current.value = conf_info.l_image_url
        pr.l_image_txt.current.value = conf_info.l_image_txt
        pr.s_image_url.current.value = conf_info.s_image_url
        pr.s_image_txt.current.value = conf_info.s_image_txt
        pr.detail.current.value = conf_info.detail
        pr.status.current.value = conf_info.status
        pr.button1_name.current.value = conf_info.button1_name
        pr.button1_url.current.value = conf_info.button1_url
        pr.button2_name.current.value = conf_info.button2_name
        pr.button2_url.current.value = conf_info.button2_url
        pr.connect_radio.current.disabled = False


# フォームの活性状態切り替え
def main_form_toggle_active_state(pr, connect_state: bool):
    pr.l_image_url.current.disabled = not connect_state
    pr.l_image_txt.current.disabled = not connect_state
    pr.s_image_url.current.disabled = not connect_state
    pr.s_image_txt.current.disabled = not connect_state
    pr.detail.current.disabled = not connect_state
    pr.status.current.disabled = not connect_state
    pr.button1_name.current.disabled = not connect_state
    pr.button1_url.current.disabled = not connect_state
    pr.button2_url.current.disabled = not connect_state
    pr.button2_name.current.disabled = not connect_state
    pr.client_id.current.disabled = connect_state


# 最小/最大文字数チェック チェック通過でTrue
def check_len(str, min, max):
    if len(str) >= min and len(str) <= max:
        return True
    else:
        return False


# URL整合性チェック チェック通過でTrue
def check_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


# 起動時にiniファイルがあればフォームに情報セット
def load_ini(pr):
    load_info(pr)
