# Python-based Instruction Disassembly
# Marcus Botacin

from capstone import *  # Disasm Framework
import sys              # Input Argument
import pefile           # Parse PE File

# Parse PE File
pe = pefile.PE(sys.argv[1])
# Enumerate All Binary Sections
for sec in pe.sections:
    # Get Characteristics
    characteristics = getattr(sec, 'Characteristics')
    # Check if Section is Executable
    if characteristics & 0x00000020 > 0 or characteristics & 0x20000000 > 0:
        # Get All Section Bytes
        data = sec.get_data()
        # interpret as 32-bit data
        md = Cs(CS_ARCH_X86, CS_MODE_32)
        # For each instruction
        for i in md.disasm(data, 0x1000):
            # Represent Instruction
            instruction_rep = "%s\t%s" % (i.mnemonic, i.op_str)
            # Print Instruction
            print(instruction_rep)
