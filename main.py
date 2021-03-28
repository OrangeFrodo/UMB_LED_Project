import pexpect
import time



scan = pexpect.spawn("sudo hcitool lescan")
time.sleep(5)
print(scan.terminate())

child = pexpect.spawn("sudo gatttool -b BE:89:30:01:6F:FA -I")
child.sendline("connect")

child.sendline("char-write-req 0x000e 7e00040100000000ef")
child.expect("Connection succ", timeout=7)

child.sendline("char-write-req 0x000e 7e0005030000ff00ef")
time.sleep(2)
child.sendline("char-write-req 0x000e 7e0005030000ff00ef")

print("connect")

print("DONE")

