import subprocess, sys, pwd

def getgroups(user):
	out = subprocess.getoutput("Groups " + str(user))
	return out[len(user)+2:]

if len(sys.argv) == 1:
	raise AssertionError("No arguments were given")

if not sys.argv[1] in ["list", "listsudo"]:
	raise AssertionError("Invalid arguments given")

for user in pwd.getpwall():
	userid = user[2]
	if userid >= 1000 and userid != 65534:
		groups = getgroups(user[0])
		if sys.argv[1] == "list":
			print("User %s with ID %s\nGroups %s\n\n" % (user[0], userid, groups))
		elif sys.argv[1] == "listsudo":
			if "sudo" in groups:
				print("User %s (%s) has admin rights" % (user[0], userid))
