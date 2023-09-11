# プレゼンス情報を格納するクラス
class PresenceInfo:
    def __init__(
        self,
        l_image_url=None,
        l_image_txt=None,
        s_image_url=None,
        s_image_txt=None,
        detail=None,
        status=None,
        button_list=None,
    ):
        self.l_image_url = l_image_url
        self.l_image_txt = l_image_txt
        self.s_image_url = s_image_url
        self.s_image_txt = s_image_txt
        self.detail = detail
        self.status = status
        if button_list is None:
            button_list = []
        self.button_list = button_list

    # ボタン情報のリスト追加
    def append_button_list(self, button_name, button_url):
        button_info = {"label": button_name, "url": button_url}
        self.button_list.append(button_info)
