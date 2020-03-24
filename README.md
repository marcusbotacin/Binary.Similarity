# Binary.Similarity

Additional material for the binary similarity paper.

## Goal

Disassemble binary instructions for clustering experiments.

## Author

Marcus Botacin, under supervision of André Grégio.

## Disasm

Disassemble binaries using capstone.

Usage:

```python
python disasm.py <binary>
```

Sample Output:
```python
je	0x13ac
insb	byte ptr es:[edi], dx
inc	esp
imul	esi, dword ptr [edx + 0x65], 0x726f7463
jns	0x13cb
add	byte ptr [eax], al
```

## Objdump

An objdump parser to be used as alternative to the capstone disassembler.

Usage:

```python
python objdump.py <binary>
```

Sample Output:
```python
(411934, ['55'], 'push   %ebp')
(411946, ['8b', '0d', '5c', '86', '41', '00'], 'mov    0x41865c,%ecx')
(411953, ['e8', 'fc', 'ae', 'ff', 'ff'], 'call   0x40c854')
(411965, ['64', 'ff', '30'], 'pushl  %fs')
```
