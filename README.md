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
