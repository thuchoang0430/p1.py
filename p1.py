lines = []

while True:
    try:
        lines.append(input())   # store each line
    except:
        break                  # stop at EOF

for s in lines:
    result = ""
    for ch in s:
        if ch.isalpha():
            result += ch.upper()
    print(result)
