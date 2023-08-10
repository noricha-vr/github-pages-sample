import requests
import json


if __name__ == '__main__':
    # 指定されたURL
    url = 'https://script.googleusercontent.com/macros/echo?user_content_key=bBwAnCjDmXbvp1oF4TWqrn9kSmNtdj_zUlG8_BRGJch_oBo_-iAqyHBu3BEXfQGlXLEMLHhDuNX9-K4BoDPxXa0px7g-NHqkm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnJdgNG2cQvZjSgoYy3SiiaVo1_sc_kd3moTIsaiIQK_BWhuoQM4-TmIwNOwUK3_lyWXu0pIj0wWr48a0p1bdH4dW0m2lyD18cNz9Jw9Md8uu&lib=MLoMIN9FtTpFMSP_bVTuP0D8rQg-QTqZL'  # *** に実際のURLを入れてください
    # URLからデータを取得する
    response = requests.get(url)

    # 正常な応答であるか確認する
    response.raise_for_status()

    # JSONデータを取得する
    data = response.json()

    # JSONデータをファイルに保存する
    with open('sample.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("JSONデータをsample.jsonに保存しました。")
