lines = []

while True:
    try:
        lines.append(input())   
    except:
        break                  

for s in lines:
    result = ""
    for ch in s:
        if ch.isalpha():
            result += ch.upper()
    print(result)
