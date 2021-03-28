import pexpect
import time



child = pexpect.spawn("sudo gatttool -b BE:89:30:01:6F:FA -I")
child.sendline("connect")

child.expect("Connection succ", timeout=7)

child.sendline("char-write-req 0x000e 7e00040000000000ef")
time.sleep(3)
child.sendline("char-write-req 0x000e 7e00040000000000ef")

print("connect")

print("DONE")
