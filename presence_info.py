# プレゼンス情報を格納するクラス
class PresenceInfo:
    def __init__(
        self,
        client_id=None,
        l_image_url=None,
        l_image_txt=None,
        s_image_url=None,
        s_image_txt=None,
        detail=None,
        status=None,
        button1_name=None,
        button1_url=None,
        button2_name=None,
        button2_url=None,
    ):
        self.client_id = client_id
        self.l_image_url = l_image_url
        self.l_image_txt = l_image_txt
        self.s_image_url = s_image_url
        self.s_image_txt = s_image_txt
        self.detail = detail
        self.status = status
        self.button1_name = button1_name
        self.button1_url = button1_url
        self.button2_name = button2_name
        self.button2_url = button2_url

    # ボタン情報のリスト追加
    def append_button_list(self, button_name, button_url):
        button_info = {"label": button_name, "url": button_url}
        self.button_list.append(button_info)


# 各部品のラベル情報を格納するクラス
class LabelInfo:
    def __init__(
        self,
        l_image_url_label=None,
        l_image_txt_label=None,
        s_image_url_label=None,
        s_image_txt_label=None,
        detail_label=None,
        status_label=None,
        button1_name_label=None,
        button1_url_label=None,
        button2_name_label=None,
        button2_url_label=None,
    ):
        self.l_image_url_label = l_image_url_label
        self.l_image_txt_label = l_image_txt_label
        self.s_image_url_label = s_image_url_label
        self.s_image_txt_label = s_image_txt_label
        self.detail_label = detail_label
        self.status_label = status_label
        self.button1_name_label = button1_name_label
        self.button1_url_label = button1_url_label
        self.button2_name_label = button2_name_label
        self.button2_url_label = button2_url_label


# 各部品のref情報を格納するクラス
class PresenceRef:
    def __init__(
        self,
        connection_status_message,
        load_button,
        help_button,
        client_id,
        connect_radio,
        l_image_url,
        l_image_txt,
        s_image_url,
        s_image_txt,
        detail,
        status,
        button1_name,
        button1_url,
        button2_name,
        button2_url,
        update_button,
    ):
        self.connection_status_message = connection_status_message
        self.load_button = load_button
        self.help_button = help_button
        self.client_id = client_id
        self.connect_radio = connect_radio
        self.l_image_url = l_image_url
        self.l_image_txt = l_image_txt
        self.s_image_url = s_image_url
        self.s_image_txt = s_image_txt
        self.detail = detail
        self.status = status
        self.button1_name = button1_name
        self.button1_url = button1_url
        self.button2_name = button2_name
        self.button2_url = button2_url
        self.update_button = update_button
