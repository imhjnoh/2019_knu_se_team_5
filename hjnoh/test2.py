# 다음 코드의 테스트용 복사수정본
# https://github.com/deepseasw/kakao_i_pizza_chatbot/blob/master/alphago_pizza.py

from flask import Flask, request, jsonify


ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해주세요.'


app = Flask(__name__)


# 피자 주문 스킬
@app.route('/order', methods=['POST'])
def order():

    # 메시지 받기
    req = request.get_json()

    gamza_type = req["action"]["detailParams"]["감자종류"]["value"]
    address = req["action"]["detailParams"]["sys_text"]["value"]

    if len(gamza_type) <= 0 or len(address) <= 0:
        answer = ERROR_MESSAGE
    else:
        answer = gamza_type + "라는 감자가 아직은 없더라도 '" + address + "'주변에서 연구하고 있는 연구자가 있을지도 모르는 일입니다."

    # 메시지 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "description": answer
                        "buttons" : [
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

    return jsonify(res)


# 메인 함수
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
