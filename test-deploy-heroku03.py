from line_notify import LineNotify
import os
Line_Notify = "RDUnfnGrcnb81X9wpZUjWGf8GdtHNgCkMP76i9ANCKj"
notify = LineNotify(Line_Notify)

notify.send("TestDeploy", sticker_id=17851, package_id=1070)

