import requests
import json


if __name__ == '__main__':
    # 指定されたURL
    url = 'https://script.googleusercontent.com/macros/echo?user_content_key=PhvMg2JKOqux5QZYM3KSzEUa-FY5nMzY9-oY0TYULcbyvvyh6gK9KDAyLx-8lMmRGlvoFHClV2bqCb0kSLK3zpkUwVGM22F-m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnPxulySh2GtSKCBuTie7tvIGsvOkys3hz804skdAKb5Ah10vheb2fQbPfRPSUxAhoi7DLCMoUwEz-3nkyUpHwIKOEDEYMrI5Wtz9Jw9Md8uu&lib=MLoMIN9FtTpFMSP_bVTuP0D8rQg-QTqZL'  # *** に実際のURLを入れてください
    # URLからデータを取得する
    response = requests.get(url)

    # 正常な応答であるか確認する
    response.raise_for_status()

    # JSONデータを取得する
    data = response.json()

    # JSONデータをファイルに保存する
    with open('docs/sample.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("JSONデータをsample.jsonに保存しました。")
