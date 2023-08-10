import requests
import json


if __name__ == '__main__':
    # 指定されたURL
    url = 'https://script.google.com/macros/s/AKfycbz4SfH1mb3mMECNLrHtOmKti7dGHq1Rr5GYrbRVCEDvDLVGq_1eYC9d8qYZ-55a-BwzZQ/exec'  # *** に実際のURLを入れてください

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
