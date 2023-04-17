# XA3E
🦴 XOR Aligned 3 Encryption

## Encryption steps
- Loads all the characters
- Pack them all to 3 characters
- Align if necessary
- Encrypt using XOR key
- If progressive key is activated, current index will have a changed

## Usage
```
usage: run.py [-h] -f FILE [-k KEY] [-ks KEY_SIZE] [-p]

options:
  -h, --help            show this help message and exit

required:
  -f FILE, --file FILE  File to encrypt

optionnal:
  -k KEY, --key KEY     Use a custom encryption key.
  -ks KEY_SIZE, --key-size KEY_SIZE
                        Use a custom encryption key length.
  -p, --progressive-key
                        Use progressive key. The key will evoluate during the encryption.
```

### Examples
#### Progressive key
- Command: `python3 .\run.py -f .\test\0.txt -k random_key -p`
- Source (bytes):
```HEX
30 31 32 33 34 35 36 37 38 39 0A 30
31 32 33 34 35 36 37 38 39 0A 30 31
32 33 34 35 36 37 38 39 0A 30 31 32
33 34 35 36 37 38 39 0A 30 31 32 33
34 35 36 37 38 39 0A 30 31 32 33 34
35 36 37 38 39 0A 30 31 32 33 34 35
36 37 38 39 0A 30 31 32 33 34 35 36
37 38 39 0A 30 31 32 33 34 35 36 37
38 39 0A 30 31 32 33 34 35 36 37 38
39 0A
```
- Output (bytes):
```HEX
42 50 5C 03 1A 05 06 07 16 09 3A 00
01 02 03 04 05 06 07 08 09 3A 00 01
02 03 04 05 06 07 08 09 3A 00 01 02
03 04 05 06 07 08 09 3A 00 01 02 03
04 05 06 07 08 09 3A 00 01 02 03 04
05 06 07 08 09 3A 00 01 02 03 04 05
06 07 08 09 3A 00 01 02 03 04 05 06
07 08 09 3A 00 01 02 03 04 05 06 07
08 09 3A 00 01 02 03 04 05 06 07 08
09 3A
```

#### Static key
- Command: `python3 .\run.py -f .\test\0.txt -k random_key`
- Source (bytes):
```HEX
30 31 32 33 34 35 36 37 38 39 0A 30
31 32 33 34 35 36 37 38 39 0A 30 31
32 33 34 35 36 37 38 39 0A 30 31 32
33 34 35 36 37 38 39 0A 30 31 32 33
34 35 36 37 38 39 0A 30 31 32 33 34
35 36 37 38 39 0A 30 31 32 33 34 35
36 37 38 39 0A 30 31 32 33 34 35 36
37 38 39 0A 30 31 32 33 34 35 36 37
38 39 0A 30 31 32 33 34 35 36 37 38
39 0A
```
- Output (bytes):
```HEX
42 50 5C 41 55 5B 44 56 56 4B 6B 5E
43 53 5D 46 54 58 45 59 57 78 51 5F
40 52 5A 47 57 59 4A 58 64 42 50 5C
41 55 5B 44 56 56 4B 6B 5E 43 53 5D
46 54 58 45 59 57 78 51 5F 40 52 5A
47 57 59 4A 58 64 42 50 5C 41 55 5B
44 56 56 4B 6B 5E 43 53 5D 46 54 58
45 59 57 78 51 5F 40 52 5A 47 57 59
4A 58 64 42 50 5C 41 55 5B 44 56 56
4B 6B
```
