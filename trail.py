import os,sys,subprocess,datetime

direct_output = subprocess.check_output('dir', shell=True)
x = datetime.datetime.now().date()
y = datetime.datetime.now().time()

"""f = open(f"logs/{str(x)}.log","a")
f.write(f'{x}  {y}\n{direct_output.decode("utf-8")}' )
f.close()
"""
print(x,y )
os.system("echo 'hello'")