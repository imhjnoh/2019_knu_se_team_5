from flask import Flask, request, jsonify
import AcadInfo


ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해주세요.'

app = Flask(__name__)

#URL출력 스킬
@app.route('/info', methods=['POST'])
def order():

    # 메시지 받기
    req = request.get_json()

    academicInfo = req["action"]["detailParams"]["학사정보"]["value"]
    
    #URL크롤러
    c = AcadInfo.Crawler(academicInfo)
    infoURL = c.getMenuURL()[0]
    
    if len(academicInfo) <= 0:
        answer = ERROR_MESSAGE
    elif infoURL == 0:
        answer = academicInfo + "에 대한 정보를 찾을수 가 없네요"
    else:
        answer = academicInfo + "에 대한 정보는\n" + infoURL + " 에서 찾을수 가 있네요"

    # 메시지 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    return jsonify(res)


if __name__ == '__main__':

    app.run(host='0.0.0.0', threaded=True, debug = True)
