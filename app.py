from line_notify import LineNotify
from flask import Flask, jsonify
# LINE_TOKEN=str(os.environ['Line_Notify_Token'])
Line_Notify = "RDUnfnGrcnb81X9wpZUjWGf8GdtHNgCkMP76i9ANCKj"
notify = LineNotify(Line_Notify)

app = Flask(__name__)

@app.route('/')
def hello_view():
    # notify.send("TestDeploy", sticker_id=17851, package_id=1070)
    return "<h1>Hello World!<h1>"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)

