# encoding: utf-8

import sys
import os
from workflow import Workflow, ICON_WEB


def main(wf):
    
    if len(wf.args):
         query = wf.args[0]
    else:
         query = None

    
    if query:
        url = "http://qr.liantu.com/api.php?text=" + query
        command = 'curl ' + url + ' -o /Users/zhengmin/Pictures/qr.png'
        os.system(command)

    path = "/Users/zhengmin/Pictures/qr.png"
    wf.add_item(title=query, 
                subtitle=query,
                icon=path,
                type="png",
                valid=True,
                arg=path)

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))