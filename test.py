from flask import Flask, render_template # render_template는 템플릿 파일을 렌더링할 떄 사용

app = Flask(__name__) #플라스크 객체 실행

@app.route("/") #라우팅 설정
def main():
    #return "Welcome"
    return render_template('index_jeju.html')

@app.route("/logging")
def logging_test():
    test = 1
    app.logger.debug('디버깅 필요')
    app.logger.warning(str(test) + " 라인")
    app.logger.error('에러발생')
    return "로깅 "

if __name__ == "__main__":
    app.run(port=4555, debug=True)


