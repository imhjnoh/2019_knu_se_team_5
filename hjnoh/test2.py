from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/gamza', methods=['POST'])
def order():

    # 카카오톡 서버에서 json 형식의 메시지 받기
    req = request.get_json()
    # 메시지에서 데이터 받기
    gamza_type = req["action"]["detailParams"]["감자종류"]["value"]
    address = req["action"]["detailParams"]["sys_location"]["value"]
    # answer에 보낼 메시지 할당
    if len(gamza_type) <= 0 or len(address) <= 0:
        answer = "ERROR"
    else:
        answer = gamza_type + "라는 감자가 아직은 없더라도 '" + address + "'주변에서 연구하고 있는 연구자가 있을지도 모르는 일입니다."

    # 카카오톡 서버로 보낼 메시지
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        # line 14-17 에서 정의했던 메시지 answer
                        "description": answer,
                        "buttons": [
                            {
                                "action": "weblink",
                                "label": "LINK",
                                "webLinkUrl": "https://www.provin.gangwon.kr/gw/portal/sub03_06?mode=listForm&searchGroup=83"

                            }

                        ]
                    }
                }
            ]
        }
    }
    # 보낼 데이터를 json으로 변환하여 전송
    return jsonify(res)


# 메인 함수
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
