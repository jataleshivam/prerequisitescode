import sys
def decode_mad_man():
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    
    for line in sys.stdin:
        line = line.lower()
        result = []
        
        for char in line:
            if char == ' ' or char == '\n':
                result.append(char)
            else:
                idx = keyboard.find(char)
                if idx != -1:
                    result.append(keyboard[idx - 2])
                else:
                    result.append(char)
        
        print("".join(result), end="")
if __name__ == "__main__":
    decode_mad_man()