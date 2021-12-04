import sys
from passwordManager import base

pwdwrong = ["Sorry that's not correct!",
            "Not even close!",
            "Nice Try!",
            "Hold on and give the correct password!"
            ]

DASH = """
------------------Help-------------------------

python main.py update facebook

python main.py add

python main.py -u username -a appname

python main.py showall -sort ascend / date

python main.py backup

------------0000000000000----------------------
//
------------000000000000-----------------------
--copytoclip
--hint
------------------------------------------------
"""
action = sys.argv[1]
if action == "help":
    print(DASH)
elif action == "add":
    base.insert("shoaibislam")
elif action == "-a":
    act_name = sys.argv[2]
    print(act_name)
    base.viewdb_by_appname("shoaibislam", act_name)
elif action == "-u":
    act_name = sys.argv[2]
    base.viewdb_by_username("shoaibislam", act_name)

elif action == "showall":
    base.viewall("shoaibislam")

else:
    print(action)
