# Python-based Objdump Parser
# Marcus Botacin

import sys          # Input File
import struct       # Represent Byte Array
import subprocess   # Run Objdump Command

# Build command string
cmd = "objdump -d %s" % sys.argv[1]
# Run the command
p = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
# Get Output (may break if too large)
output = p.stdout.read()
# Instruction Bytes Representation
ibytes_array = bytearray()
# For each line
for line in output.split("\n"):
    # Consider only the instruction lines
    splitted = line.split(":")
    try:
        # Address is the first field
        addr = int(splitted[0].strip())
        # Get bytes as string
        ibytes = splitted[1].split("\t")[1].strip().split(" ")
        # Convert ascii to actual bytes
        for b in ibytes:
            ibytes_array=ibytes_array+struct.pack("B", int(b,16))
        # Instruction Opcode is the last field
        irepr = splitted[1].split("\t")[2].split("#")[0].strip()
        # Print
        print(addr,ibytes,irepr)
    # Ignore the non-instruction lines
    except:
        continue
