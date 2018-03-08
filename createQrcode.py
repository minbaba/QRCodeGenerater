# -*- coding: utf-8 -*-

import sys
import os
from workflow import Workflow3


def main(wf):
    
    if len(wf.args):
         query = wf.args[0]
    else:
         query = None

    path = "/Users/zhengmin/Pictures/qr.png"
    if query:
        url = "http://qr.liantu.com/api.php?text=" + query
        command = 'curl ' + url + ' -o ' + path
        os.system(command)
    
    subtitle = '回车放大二维码'
    wf.add_item(title=query, 
                subtitle=subtitle,
                icon=path,
                type="png",
                valid=True,
                arg=path)

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))