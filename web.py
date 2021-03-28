from flask import Flask, request
import pexpect
import time

app = Flask(__name__)

scan = pexpect.spawn("sudo hcitool lescan") 	#Skenovanie okolitých bluethoot zariadení
time.sleep(5)
print(scan.terminate())


@app.route("/", methods=['POST'])
def hello_world():
	print (request.is_json)
	content = request.get_json()		#Requesting JSON_APP
	print (content)
	if content["status"] == "On":

		child = pexpect.spawn("sudo gatttool -b BE:89:30:01:6F:FA -I")		# Bluethoot adresa

		child.sendline("connect")
		child.expect("Connection succ", timeout=7)

		child.sendline("char-write-req 0x000e 7e00040100000000ef")		# Command na zapnutie
		time.sleep(2)

		print("connect")
		print("DONE")

		child.sendline("disconnect")

		return "Hello"
	if content["status"] == "Off":

		child = pexpect.spawn("sudo gatttool -b BE:89:30:01:6F:FA -I")

		child.sendline("connect")
		time.sleep(2)
		child.sendline("char-write-req 0x000e 7e00040000000000ef")
		time.sleep(1)

		child.sendline("disconnect")

		print("connect")
		print("DONE")

		return "Bye"

	if content["status"] == "Red":

		child = pexpect.spawn("sudo gatttool -b BE:89:30:01:6F:FA -I")

		child.sendline("connect")
		time.sleep(2)
		#RED
		child.sendline("char-write-req 0x000e 7e000503ff000000ef")
		time.sleep(1)

		child.sendline("disconnect")

		print("connect")
		print("DONE")

		return "Red Light"

	if content["status"] == "WarmOrange":

		child = pexpect.spawn("sudo gatttool -b BE:89:30:01:6F:FA -I")

		child.sendline("connect")
		time.sleep(2)
		#RED
		child.sendline("char-write-req 0x000e 7e000503ff5D0000ef")		#Command na zmenu farby
		time.sleep(1)

		child.sendline("disconnect")

		print("connect")
		print("DONE")

		return "WarmOrange"
