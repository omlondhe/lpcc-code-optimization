with open('unreachableCodeInput.txt', 'r') as file:
    expression = file.read()
    ans = ""
    lines = expression.split('\n')
    add = True

    for line in lines:
        if add:
            ans += line + '\n'
        if line.__contains__('return'):
            add = False
    
    ans += '}'
    print(ans)
