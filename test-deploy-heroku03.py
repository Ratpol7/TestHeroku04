from line_notify import LineNotify
import os
Line_Notify = "RDUnfnGrcnb81X9wpZUjWGf8GdtHNgCkMP76i9ANCKj"
notify = LineNotify(Line_Notify)
t = 1
if t == 1:
    notify.send("TestDeploy", sticker_id=17851, package_id=1070)
    t = 0
