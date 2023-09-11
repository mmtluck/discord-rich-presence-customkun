import flet as ft  # https://flet.dev/
from urllib.parse import urlparse
import drp
import presence_info as prIn

CONNECT_SETTING = "アプリ接続状態:"
CLIENT_ID = "クライアントIDを入力※ポータルサイトのアプリID"
LARGE_URL_MESSAGE = "large_imageのURLを入力※注意：URLは画像の「直リンク」を指定してください"
LARGE_TEXT_MESSAGE = "large_imageマウスオーバー時のメッセージを入力"
SMALL_URL_MESSAGE = "small_imageのURLを入力※注意：URLは画像の「直リンク」を指定してください"
SMALL_TEXT_MESSAGE = "small_imageマウスオーバー時のメッセージを入力"
DETAIL_MESSAGE = "detailに表示されるメッセージを入力※２行目"
STATUS_MESSAGE = "statusに表示されるメッセージを入力※３行目"


# 設定ファイル読み込み
# config


# URL整合性チェック
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def main(page):
    # 各フォームのエラー状態チェック エラーなしなら更新ボタン活性化
    def error_check():
        if (
            l_image_url.current.error_text
            or l_image_txt.current.error_text
            or s_image_url.current.error_text
            or s_image_txt.current.error_text
            or detail.current.error_text
            or status.current.error_text
            or button1_url.current.error_text
            or button1_name.current.error_text
            or button2_url.current.error_text
            or button2_name.current.error_text
        ):
            update_button.current.disabled = True
        else:
            update_button.current.disabled = False
        page.update()

    # ラジオボタン切替時のEvent 接続切り替え
    def connect_radio_changed(e):
        # Connect切り替え時に接続失敗した場合エラーメッセージを表示しDisconnectに切り替え
        if connect_radio.current.value == radio[0]:
            # プレゼンス接続
            drp.drpConnect(client_id.current.value)
            print("Connected")
            l_image_url.current.disabled = False
            l_image_txt.current.disabled = False
            s_image_url.current.disabled = False
            s_image_txt.current.disabled = False
            detail.current.disabled = False
            status.current.disabled = False
            button1_name.current.disabled = False
            button1_url.current.disabled = False
            button2_url.current.disabled = False
            button2_name.current.disabled = False
            client_id.current.disabled = True

            # 必須項目入力済みならそのままプレゼンス情報更新
        else:
            drp.drpDisconnect()
            l_image_url.current.disabled = True
            l_image_txt.current.disabled = True
            s_image_url.current.disabled = True
            s_image_txt.current.disabled = True
            detail.current.disabled = True
            status.current.disabled = True
            button1_name.current.disabled = True
            button1_url.current.disabled = True
            button2_url.current.disabled = True
            button2_name.current.disabled = True
            client_id.current.disabled = False
            update_button.current.disabled = True

        page.update()

    # フォーム入力時のEvent 必須フォームが入力されているか、
    def on_change_form(e):
        # 大画像URL入力チェック
        if l_image_url.current.value:
            if is_valid_url(l_image_url.current.value):
                l_image_url.current.error_text = ""
            else:
                l_image_url.current.error_text = "Invalid URL"
        elif l_image_txt.current.value:
            l_image_url.current.error_text = "Required URL"
        else:
            l_image_url.current.error_text = ""
        # 大画像テキスト入力チェック
        if l_image_txt.current.value:
            if len(l_image_txt.current.value) > 1:
                l_image_txt.current.error_text = ""
            else:
                l_image_txt.current.error_text = "At least 2 characters must be entered"
        elif l_image_url.current.value:
            l_image_txt.current.error_text = "At least 2 characters must be entered"
        else:
            l_image_txt.current.error_text = ""

        # 小画像URL入力チェック
        if s_image_url.current.value:
            if is_valid_url(s_image_url.current.value):
                s_image_url.current.error_text = ""
            else:
                s_image_url.current.error_text = "Invalid URL"
        elif s_image_txt.current.value:
            s_image_url.current.error_text = "Required URL"
        else:
            s_image_url.current.error_text = ""
        # 小画像テキスト入力チェック
        if s_image_txt.current.value:
            if len(s_image_txt.current.value) > 1:
                s_image_txt.current.error_text = ""
            else:
                s_image_txt.current.error_text = "At least 2 characters must be entered"
        elif s_image_url.current.value:
            s_image_txt.current.error_text = "At least 2 characters must be entered"
        else:
            s_image_txt.current.error_text = ""

        # details入力チェック
        if len(detail.current.value) > 1:
            detail.current.error_text = ""
        else:
            detail.current.error_text = "At least 2 characters must be entered"

        # status入力チェック
        if len(status.current.value) > 1:
            status.current.error_text = ""
        else:
            status.current.error_text = "At least 2 characters must be entered"

        # １ボタンURL入力チェック
        if button1_url.current.value:
            if is_valid_url(button1_url.current.value):
                button1_url.current.error_text = ""
            else:
                button1_url.current.error_text = "Invalid URL"
        elif button1_name.current.value:
            button1_url.current.error_text = "Required URL"
        else:
            button1_url.current.error_text = ""
        # １ボタン名前入力チェック
        if button1_name.current.value:
            if len(button1_name.current.value) > 1:
                button1_name.current.error_text = ""
            else:
                button1_name.current.error_text = (
                    "At least 2 characters must be entered"
                )
        elif button1_url.current.value:
            button1_name.current.error_text = "At least 2 characters must be entered"
        else:
            button1_name.current.error_text = ""

        # ２ボタンURL入力チェック
        if button2_url.current.value:
            if is_valid_url(button2_url.current.value):
                button2_url.current.error_text = ""
            else:
                button2_url.current.error_text = "Invalid URL"
        elif button2_name.current.value:
            button2_url.current.error_text = "Required URL"
        else:
            button2_url.current.error_text = ""
        # ２ボタン名前入力チェック
        if button2_name.current.value:
            if len(button2_name.current.value) > 1:
                button2_name.current.error_text = ""
            else:
                button2_name.current.error_text = (
                    "At least 2 characters must be entered"
                )
        elif button2_url.current.value:
            button2_name.current.error_text = "At least 2 characters must be entered"
        else:
            button2_name.current.error_text = ""

        error_check()
        page.update()

    def on_change_client(e):
        # クライアントIDが入力されている場合のみラジオボタン活性化
        if client_id.current.value:
            connect_radio.current.disabled = False
        else:
            connect_radio.current.disabled = True
        page.update()

    def on_change_button_forme(e):
        page.update()

    # 更新ボタン押下時のEvent PresenceInfoオブジェクトに値を入れてプレゼンス更新
    def button_click_update_presence(e):
        presence_info = prIn.PresenceInfo()
        presence_info.l_image_url = l_image_url.current.value
        presence_info.l_image_txt = l_image_txt.current.value
        presence_info.s_image_url = s_image_url.current.value
        presence_info.s_image_txt = s_image_txt.current.value
        presence_info.detail = detail.current.value
        presence_info.status = status.current.value
        # ボタン情報が入力されてる場合はボタンリストに追加
        if button1_name.current.value:
            presence_info.append_button_list(
                button1_name.current.value, button1_url.current.value
            )
        if button2_name.current.value:
            presence_info.append_button_list(
                button2_name.current.value, button2_url.current.value
            )

        # プレゼンス更新処理
        drp.drpUpdate(presence_info)
        page.update()

    # フォーカスアウト時のURLチェック
    def on_blur_check_url(e):
        page.update()

    # ヘルプボタン押下時の操作説明
    def on_click_popup(e):
        page.update()

    # Windowの設定と各フォーム部分
    page.title = "DRPカスタムくん"
    page.window_width = 700
    page.window_height = 1100
    radio = ["Connect", "Disconnect"]
    connection_status_message = ft.Ref[ft.Text]()
    help_button = ft.Ref[ft.IconButton]()
    client_id = ft.Ref[ft.TextField]()
    connect_radio = ft.Ref[ft.RadioGroup]()
    l_image_url = ft.Ref[ft.TextField]()
    l_image_txt = ft.Ref[ft.TextField]()
    s_image_url = ft.Ref[ft.TextField]()
    s_image_txt = ft.Ref[ft.TextField]()
    detail = ft.Ref[ft.TextField]()
    status = ft.Ref[ft.TextField]()
    button1_name = ft.Ref[ft.TextField]()
    button1_url = ft.Ref[ft.TextField]()
    button2_name = ft.Ref[ft.TextField]()
    button2_url = ft.Ref[ft.TextField]()
    update_button = ft.Ref[ft.ElevatedButton]()

    # ページの部品表示はここ
    page.add(
        ft.IconButton(
            ref=help_button,
            icon=ft.icons.HELP_ROUNDED,
            icon_color="pink600",
            on_click=on_click_popup,
        ),
        ft.Row(
            [
                ft.Text(CONNECT_SETTING),
                ft.Text(
                    ref=connection_status_message,
                    value="未接続",
                ),
            ]
        ),
        ft.RadioGroup(
            ref=connect_radio,
            content=ft.Row(
                [
                    ft.Radio(value=connect, label=connect.capitalize())
                    for connect in radio
                ],
            ),
            on_change=connect_radio_changed,
            value="Disconnect",
            disabled=True,
        ),
        ft.Text(CLIENT_ID),
        ft.TextField(ref=client_id, label="client id", on_change=on_change_client),
        ft.Text(LARGE_URL_MESSAGE),
        ft.TextField(
            ref=l_image_url,
            label="large image URL",
            on_change=on_change_form,
            disabled=True,
        ),
        ft.Text(LARGE_TEXT_MESSAGE),
        ft.TextField(
            ref=l_image_txt,
            label="large image TEXT",
            on_change=on_change_form,
            max_length=128,
            disabled=True,
        ),
        ft.Text(LARGE_URL_MESSAGE),
        ft.TextField(
            ref=s_image_url,
            label="small image URL",
            on_change=on_change_form,
            disabled=True,
        ),
        ft.Text(LARGE_TEXT_MESSAGE),
        ft.TextField(
            ref=s_image_txt,
            label="small image TEXT",
            on_change=on_change_form,
            max_length=128,
            disabled=True,
        ),
        ft.Text(DETAIL_MESSAGE),
        ft.TextField(
            ref=detail,
            label="detail",
            on_change=on_change_form,
            max_length=128,
            disabled=True,
        ),
        ft.Text(STATUS_MESSAGE),
        ft.TextField(
            ref=status,
            label="status",
            on_change=on_change_form,
            max_length=128,
            disabled=True,
        ),
        ft.Text("ボタン設定(任意/最大２個)"),
        ft.Row(
            [
                ft.Column(
                    [
                        ft.TextField(
                            ref=button1_name,
                            label="button1 name",
                            on_change=on_change_form,
                            max_length=32,
                            disabled=True,
                        ),
                        ft.TextField(
                            ref=button1_url,
                            label="button1 url",
                            on_change=on_change_form,
                            disabled=True,
                        ),
                    ],
                ),
                ft.Column(
                    [
                        ft.TextField(
                            ref=button2_name,
                            label="button2 name",
                            on_change=on_change_form,
                            max_length=32,
                            disabled=True,
                        ),
                        ft.TextField(
                            ref=button2_url,
                            label="button2 url",
                            on_change=on_change_form,
                            disabled=True,
                        ),
                    ],
                ),
            ],
        ),
        ft.ElevatedButton(
            ref=update_button,
            text="プレゼンスを更新",
            on_click=button_click_update_presence,
            disabled=True,
        ),
    )


# 起動
ft.app(target=main)
