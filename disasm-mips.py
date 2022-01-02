import os
import sys
import subprocess


OBJDUMP = "mipsel-linux-gnu-objdump"
TMPFILE = "disasm.bin"
def disasm_one(instr):
    with open(TMPFILE,"wb") as file:
        file.write(instr.to_bytes(4,byteorder='little'))
    sp = subprocess.Popen("{} -b binary -m mips -D {}".format(OBJDUMP,TMPFILE), shell=True, stdout=subprocess.PIPE)
    out = sp.stdout.readlines()[-1].decode("ascii")
    os.unlink(TMPFILE)
    pos = out.find(":")
    if pos == -1:
        return ""
    out = out[pos+1:]
    pos2 = out.find(" ")
    out = out[pos2+1:].strip()
    return out

def disasm_coe(path):
    with open(path,"r") as file:
        txt = file.read()
    pos = txt.find("memory_initialization_vector")
    if pos == -1:
        return ""
    txt = txt[pos+1:]
    pos = txt.find("=")
    instr_list = txt[pos+1:].strip().split(",")
    buf = bytes()
    for instr in instr_list:
        cur = instr.strip()
        if len(cur) == 8:
            cur = int(cur,base=16)
            buf += cur.to_bytes(4,byteorder='little')
    with open(TMPFILE,"wb") as file:
        file.write(buf)
    sp = subprocess.Popen("{} -b binary -m mips -D {}".format(OBJDUMP,TMPFILE), shell=True, stdout=subprocess.PIPE)
    result = sp.stdout.read().decode("ascii")
    os.unlink(TMPFILE)
    return result

def interactive():
    while True:
        print(">>> ",end="")
        input_str = input().strip()
        try:
            instr = int(input_str,base=16)
            if instr.bit_length() <= 32:
                print(disasm_one(instr))
        except:
            print("ERROR! Please input instrution in HEX.")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        interactive()
    else:
        print(disasm_coe(sys.argv[1]))