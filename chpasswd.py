import os, sys, pwd

print("What is the new password:")
newpswd = input()

if sys.argv[1] == "set":
	for user in pwd.getpwall():
		username = user[0]
		if username == sys.argv[2]: continue
		
		userid = user[2]
		if userid >= 1000 and userid != 65534:
			os.system("echo \"%s\\n%s\" | sudo passwd %s" % (newpswd, newpswd, user[0]))
