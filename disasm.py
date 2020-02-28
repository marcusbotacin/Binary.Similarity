from capstone import *
import sys
import os
import pefile
import hashlib

itf = dict()

for filename in os.listdir(sys.argv[1]):
    filepath=sys.argv[1]+'/'+filename
    digest = hashlib.sha256(open(filepath,'r').read()).hexdigest()
    try:
        pe = pefile.PE(filepath)
        for sec in pe.sections:
            characteristics = getattr(sec, 'Characteristics')
            if characteristics & 0x00000020 > 0 or characteristics & 0x20000000 > 0:
                data = sec.get_data()
                md = Cs(CS_ARCH_X86, CS_MODE_64)
                for (address, size, mnemonic, op_str) in md.disasm_lite(data, 0x1000):
                    instruction_rep = "%s\t%s" % (mnemonic, op_str)
                    try:
                        x = itf[instruction_rep]
                    except:
                        itf[instruction_rep]=set()
                    itf[instruction_rep].add(digest)
    except:
        continue

for instruction in itf:
    try:
        print("%f\t%s" % (1/float(len(itf[instruction])),instruction))
    except:
        pass
