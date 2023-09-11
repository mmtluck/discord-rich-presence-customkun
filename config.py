import configparser
import os

config = configparser.ConfigParser()

config_file_path = "config.ini"


# コンフィグファイル初期設定
def init_config():
    # コンフィグファイルがなければ新規作成
    if not os.path.exists(config_file_path):
        with open(config_file_path, "w") as config_file:
            config.read(config_file)
        return False

    # 存在する場合は読み込み
    else:
        config.read(config_file_path)
        return True


# プレゼンス情報を取得
def read_presence_info():
    return config


# 入力したプレゼンス情報を保存
def save_presence_info():
    with open(config_file_path, "w") as config_file:
        config.read(config_file)
