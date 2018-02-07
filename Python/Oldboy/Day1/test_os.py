import os

cmd_res = os.system("dir")
cmd_res = os.popen("dir").read()
print("->",cmd_res)
os.mkdir("new_dir")