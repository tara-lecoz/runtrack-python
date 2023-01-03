def calcule(num1,operator,num2):
    match operator:
        case '+':
            result=num1+num2
        case '-':
            result=num1-num2
        case '*':
            result=num1*num2
        case '/':
            result=num1/num2
        case '%':
            result=num1%num2
    return result

print(calcule(1,'+',2))
print(calcule(2,'-',1))
print(calcule(2,'*',1))
print(calcule(4,'/',2))
print(calcule(6,'%',2))
