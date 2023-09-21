import configparser
import os
import presence_info as prIn

config = configparser.ConfigParser()

config_file_path = "config.ini"


# コンフィグファイル初期設定
def init_config():
    # コンフィグファイルがなければ新規作成
    if not os.path.exists(config_file_path):
        config.add_section("ID")
        config.add_section("IMAGE")
        config.add_section("DETAIL")
        config.add_section("STATUS")
        config.add_section("BUTTON")
        with open(config_file_path, "w") as config_file:
            config.write(config_file)

        return False

    # 存在する場合は読み込み
    else:
        config.read(config_file_path)
        return True


# プレゼンス情報を取得
def get_config() -> prIn.PresenceInfo:
    info = prIn.PresenceInfo()
    info.client_id = config.get("ID", "client_id")
    info.l_image_url = config.get("IMAGE", "l_image_url")
    info.l_image_txt = config.get("IMAGE", "l_image_txt")
    info.s_image_url = config.get("IMAGE", "s_image_url")
    info.s_image_txt = config.get("IMAGE", "s_image_txt")
    info.detail = config.get("DETAIL", "detail")
    info.status = config.get("STATUS", "status")
    info.button1_name = config.get("BUTTON", "button1_name")
    info.button1_url = config.get("BUTTON", "button1_url")
    info.button2_name = config.get("BUTTON", "button2_name")
    info.button2_url = config.get("BUTTON", "button2_url")
    return info


# 入力したプレゼンス情報を保存
def save_presence_info(info: prIn.PresenceInfo):
    init_config()
    config.set("ID", "client_id", info.client_id)
    config.set(
        "IMAGE",
        "l_image_url",
        info.l_image_url if info.l_image_url else "",
    )
    config.set(
        "IMAGE",
        "l_image_txt",
        info.l_image_txt if info.l_image_txt else "",
    )
    config.set(
        "IMAGE",
        "s_image_url",
        info.s_image_url if info.s_image_url else "",
    )
    config.set(
        "IMAGE",
        "s_image_txt",
        info.s_image_txt if info.s_image_txt else "",
    )
    config.set("DETAIL", "detail", info.detail)
    config.set("STATUS", "status", info.status)
    config.set(
        "BUTTON",
        "button1_name",
        info.button1_name if info.button1_name else "",
    )
    config.set(
        "BUTTON",
        "button1_url",
        info.button1_url if info.button1_url else "",
    )
    config.set(
        "BUTTON",
        "button2_name",
        info.button2_name if info.button2_name else "",
    )
    config.set(
        "BUTTON",
        "button2_url",
        info.button2_url if info.button2_url else "",
    )

    with open(config_file_path, "w") as config_file:
        config.write(config_file)
