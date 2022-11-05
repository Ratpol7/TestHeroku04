from line_notify import LineNotify
from flask import Flask
# LINE_TOKEN=str(os.environ['Line_Notify_Token'])
Line_Notify = "RDUnfnGrcnb81X9wpZUjWGf8GdtHNgCkMP76i9ANCKj"
notify = LineNotify(Line_Notify)

app = Flask(__name__)

app.callback
if __name__ == "__main__":
    print("/n/ntesttttttt/n/n")
    notify.send("TestDeploy", sticker_id=17851, package_id=1070)

