import flet as ft  # https://flet.dev/
import presence_info as prIn
import contents
import const
import event as ev


def main(page):
    # Windowの設定と各フォーム部分
    page.title = const.PAGE_TITLE
    page.window_width = 450
    page.window_height = 750
    page.window_top = 300
    page.window_left = 600
    page.window_resizable = False
    page.bgcolor = "#222222"
    pr_ref = prIn.PresenceRef(
        ft.Ref[ft.Text](),
        ft.Ref[ft.IconButton](),
        ft.Ref[ft.IconButton](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.RadioGroup](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.TextField](),
        ft.Ref[ft.ElevatedButton](),
    )

    # 各種フォームEvent呼び出し

    # HelpボタンonClick
    def onClick_help_button(e):
        ev.on_click_popup()

    # 接続状態onChange
    def onChange_radio(e):
        ev.connect_process(pr_ref, page)

    # クライアントIDフォームonChange
    def onChange_client_form(e):
        ev.input_check_clientform(pr_ref, page)

    # 大画像,小画像フォームonChange
    def onChange_image_form(e):
        ev.input_check_imageform(pr_ref, page)

    # Details,StatusフォームonChange
    def onChange_status_form(e):
        ev.input_check_statusform(pr_ref, page)

    # ボタンフォームonChange
    def onChange_button_form(e):
        ev.input_check_buttonform(pr_ref, page)

    # プレゼンス更新ボタンonClick
    def onClick_update_button(e):
        ev.update_presence(pr_ref, page)

    # コンテナ1:ロードボタン/ヘルプボタン
    c1 = contents.create_load_help_button(
        load_ref=pr_ref.load_button,
        load_icon=ft.icons.PRESENT_TO_ALL_OUTLINED,
        help_ref=pr_ref.help_button,
        help_icon=ft.icons.HELP_OUTLINED,
        help_event=onClick_help_button,
    )

    # コンテナ2:プレゼンス接続
    c2 = contents.create_connect_detail(
        message=const.CONNECT_DETAIL_MESSAGE,
        status_ref=pr_ref.connection_status_message,
        value=const.STARTUP,
        radio_ref=pr_ref.connect_radio,
        choice=const.RADIO_CHOICE,
        disabled=True,
        event=onChange_radio,
    )

    # コンテナ:クライアントID設定
    c3 = contents.create_clientid_form(
        text=const.CLIENT_ID_TIPS,
        ref=pr_ref.client_id,
        label=const.LABEL_CLIEND_ID,
        disabled=False,
        event=onChange_client_form,
    )

    # コンテナ3:大画像/小画像設定
    c4 = contents.create_image_form(
        l_image_txt_ref=pr_ref.l_image_txt,
        l_image_txt_label=const.LABEL_LIMAGE_TXT,
        l_image_url_ref=pr_ref.l_image_url,
        l_image_url_label=const.LABEL_LIMAGE_URL,
        s_image_txt_ref=pr_ref.s_image_txt,
        s_image_txt_label=const.LABEL_SIMAGE_TXT,
        s_image_url_ref=pr_ref.s_image_url,
        s_image_url_label=const.LABEL_SIMAGE_URL,
        l_image_txt_disabled=True,
        l_image_url_disabled=True,
        s_image_txt_disabled=True,
        s_image_url_disabled=True,
        l_image_txt_event=onChange_image_form,
        l_image_url_event=onChange_image_form,
        s_image_txt_event=onChange_image_form,
        s_image_url_event=onChange_image_form,
    )
    # コンテナ4:Details/Status設定
    c5 = contents.create_status_form(
        details_text=const.DETAILS_MESSAGE,
        details_ref=pr_ref.detail,
        details_label=const.LABEL_DETAILS,
        status_text=const.STATUS_MESSAGE,
        status_ref=pr_ref.status,
        status_label=const.LABEL_STATUS,
        details_disabled=True,
        status_disabled=True,
        details_event=onChange_status_form,
        status_event=onChange_status_form,
    )

    # コンテナ5:ボタン設定
    c6 = contents.create_button_form(
        button1_name_ref=pr_ref.button1_name,
        button1_name_label=const.LABEL_BUTTON1_NAME,
        button1_url_ref=pr_ref.button1_url,
        button1_url_label=const.LABEL_BUTTON1_URL,
        button2_name_ref=pr_ref.button2_name,
        button2_name_label=const.LABEL_BUTTON2_NAME,
        button2_url_ref=pr_ref.button2_url,
        button2_url_label=const.LABEL_BUTTON2_URL,
        button1_name_disabled=True,
        button1_url_disabled=True,
        button2_name_disabled=True,
        button2_url_disabled=True,
        button1_name_event=onChange_button_form,
        button1_url_event=onChange_button_form,
        button2_name_event=onChange_button_form,
        button2_url_event=onChange_button_form,
    )

    # コンテナ6:プレゼンス更新
    c7 = contents.create_update_presence_button(
        ref=pr_ref.update_button,
        text=const.UPDATE_PRESENCE,
        disabled=True,
        event=onClick_update_button,
    )

    # iniファイル読み込み
    ev.load_ini(pr_ref)

    # ページに部品追加
    page.add(c1, c2, c3, c4, c5, c6, c7)


# ページ起動
ft.app(target=main)
