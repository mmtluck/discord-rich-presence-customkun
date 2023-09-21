import flet as ft
import const


# 縦並びの汎用テキストフィールド(説明文とテキストフィールド)コンテナ作成
def flet_text_column(**general_form) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(general_form["text"], size=11),
                ft.TextField(
                    ref=general_form["ref"],
                    label=general_form["label"],
                    disabled=general_form["disabled"],
                    on_change=general_form["event"],
                    content_padding=5,
                ),
            ],
        )
    )
    return container


# 横並びの汎用テキストフィールド(説明文とテキストフィールド)コンテナ作成
def flet_text_row(**general_form) -> ft.Container:
    container = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(general_form["text"]),
                ft.TextField(
                    ref=general_form["ref"],
                    label=general_form["label"],
                    disabled=general_form["disabled"],
                    on_change=general_form["event"],
                ),
            ]
        )
    )
    return container


# アイコンボタンコンテナ作成
def flet_icon_button(**button) -> ft.Container:
    container = ft.Container(
        content=ft.IconButton(
            ref=button["ref"],
            icon=button["icon"],
            on_click=button["event"],
            icon_color="white100",
        )
    )
    return container


# 汎用ボタンコンテナ作成
def flet_elevated_button(**button) -> ft.Container:
    container = ft.Container(
        content=ft.ElevatedButton(
            ref=button["ref"],
            text=button["text"],
            disabled=button["disabled"],
            on_click=button["event"],
            icon=ft.icons.UPDATE,
        )
    )
    return container


# ラジオボタンコンテナ作成
def flet_radio_button(**button) -> ft.Container:
    container = ft.Container(
        content=ft.RadioGroup(
            ref=button["ref"],
            value=const.RADIO_CHOICE[1],
            disabled=button["disabled"],
            on_change=button["event"],
            content=ft.Row(
                controls=[
                    ft.Radio(value=connect, label=connect.capitalize())
                    for connect in button["choice"]
                ],
            ),
        )
    )
    return container


# ２つの縦並びテキストフィールドのコンテナ作成
def flet_textfield_column(**textfield) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.TextField(
                    ref=textfield["textfield1_ref"],
                    label=textfield["textfield1_label"],
                    disabled=textfield["textfield1_disabled"],
                    on_change=textfield["textfield1_event"],
                    width=200,
                ),
                ft.TextField(
                    ref=textfield["textfield2_ref"],
                    label=textfield["textfield2_label"],
                    disabled=textfield["textfield2_disabled"],
                    on_change=textfield["textfield2_event"],
                    width=200,
                ),
            ],
        ),
    )
    return container


# ２つの横並びテキストフィールドのコンテナ作成
def flet_textfield_row(**textfield) -> ft.Container:
    container = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextField(
                    ref=textfield["textfield1_ref"],
                    label=textfield["textfield1_label"],
                    disabled=textfield["textfield1_disabled"],
                    on_change=textfield["textfield1_event"],
                    width=200,
                ),
                ft.TextField(
                    ref=textfield["textfield2_ref"],
                    label=textfield["textfield2_label"],
                    disabled=textfield["textfield2_disabled"],
                    on_change=textfield["textfield2_event"],
                    width=200,
                ),
            ],
        ),
    )
    return container


# 設定ロードボタン/ヘルプボタン部分作成
def create_load_help_button(**icon) -> ft.Container:
    container = ft.Container(
        margin=-10,
        content=ft.Row(
            spacing=-60,
            controls=[
                flet_icon_button(
                    ref=icon["help_ref"],
                    icon=icon["help_icon"],
                    event=icon["help_event"],
                ),
                ft.Text("←つかいかた", size=11),
            ],
        ),
    )
    return container


# 接続状態表示部分作成
def create_connect_detail(**connect) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            spacing=-50,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(connect["message"]),
                        ft.Text(
                            ref=connect["status_ref"],
                            value=connect["value"],
                        ),
                    ]
                ),
                flet_radio_button(
                    ref=connect["radio_ref"],
                    choice=connect["choice"],
                    disabled=connect["disabled"],
                    event=connect["event"],
                ),
            ],
        ),
    )
    return container


# クライアントID入力フォーム作成
def create_clientid_form(**client) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            controls=[
                flet_text_column(
                    text=client["text"],
                    ref=client["ref"],
                    label=client["label"],
                    disabled=client["disabled"],
                    event=client["event"],
                ),
            ]
        )
    )
    return container


# 大画像/小画像入力フォーム作成
def create_image_form(**image) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(const.IMAGE_MESSAGE, size=11),
                ft.Row(
                    controls=[
                        flet_textfield_column(
                            textfield1_ref=image["l_image_txt_ref"],
                            textfield1_label=image["l_image_txt_label"],
                            textfield2_ref=image["l_image_url_ref"],
                            textfield2_label=image["l_image_url_label"],
                            textfield1_disabled=image["l_image_txt_disabled"],
                            textfield2_disabled=image["l_image_url_disabled"],
                            textfield1_event=image["l_image_txt_event"],
                            textfield2_event=image["l_image_url_event"],
                        ),
                        flet_textfield_column(
                            textfield1_ref=image["s_image_txt_ref"],
                            textfield1_label=image["s_image_txt_label"],
                            textfield2_ref=image["s_image_url_ref"],
                            textfield2_label=image["s_image_url_label"],
                            textfield1_disabled=image["s_image_txt_disabled"],
                            textfield2_disabled=image["s_image_url_disabled"],
                            textfield1_event=image["s_image_txt_event"],
                            textfield2_event=image["s_image_url_event"],
                        ),
                    ],
                ),
            ],
        )
    )
    return container


# Details/Status入力フォーム作成
def create_status_form(**status) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            controls=[
                flet_text_column(
                    text=status["details_text"],
                    ref=status["details_ref"],
                    label=status["details_label"],
                    disabled=status["details_disabled"],
                    event=status["details_event"],
                ),
                flet_text_column(
                    text=status["status_text"],
                    ref=status["status_ref"],
                    label=status["status_label"],
                    disabled=status["status_disabled"],
                    event=status["status_event"],
                ),
            ]
        )
    )
    return container


# ボタン入力フォーム作成
def create_button_form(**buttons) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(const.BUTTON_MESSAGE, size=11),
                ft.Row(
                    controls=[
                        flet_textfield_column(
                            textfield1_ref=buttons["button1_name_ref"],
                            textfield1_label=buttons["button1_name_label"],
                            textfield2_ref=buttons["button1_url_ref"],
                            textfield2_label=buttons["button1_url_label"],
                            textfield1_disabled=buttons["button1_name_disabled"],
                            textfield2_disabled=buttons["button1_url_disabled"],
                            textfield1_event=buttons["button1_name_event"],
                            textfield2_event=buttons["button1_url_event"],
                        ),
                        flet_textfield_column(
                            textfield1_ref=buttons["button2_name_ref"],
                            textfield1_label=buttons["button2_name_label"],
                            textfield2_ref=buttons["button2_url_ref"],
                            textfield2_label=buttons["button2_url_label"],
                            textfield1_disabled=buttons["button2_name_disabled"],
                            textfield2_disabled=buttons["button2_url_disabled"],
                            textfield1_event=buttons["button2_name_event"],
                            textfield2_event=buttons["button2_url_event"],
                        ),
                    ],
                ),
            ],
        ),
    )
    return container


# プレゼンス更新ボタン表示部分作成
def create_update_presence_button(**button) -> ft.Container:
    container = ft.Container(
        content=ft.Column(
            controls=[
                flet_elevated_button(
                    ref=button["ref"],
                    text=button["text"],
                    disabled=button["disabled"],
                    event=button["event"],
                ),
            ]
        ),
    )
    return container
