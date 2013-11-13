#Trailblaze
from types import *
parenthesis = raw_input()
stack = ['*']
isNormalParenthesis = True
for i in range(len(parenthesis)):
    sum = 0
    if parenthesis[i] == '(' or parenthesis[i] == '[':
        stack.append(parenthesis[i])
    elif parenthesis[i] == ')' :
        while stack[len(stack) - 1] != '(':
            if type(stack[len(stack) - 1]) is IntType:
                sum += stack[len(stack) - 1]
                stack.pop()
            else :
                print '0'
                exit()
        if sum == 0:
            sum = 1
        sum = sum * 2
        stack.pop()
        stack.append(sum)

    elif parenthesis[i] == ']' :
        while stack[len(stack) - 1] != '[':
            if type(stack[len(stack) - 1]) is IntType:
                sum += stack[len(stack) - 1]
                stack.pop()
            else :
                print '0'
                exit()
        if sum == 0:
            sum = 1
        sum = sum * 3
        stack.pop()
        stack.append(sum)

answer = 0
for i in range(1, len(stack)):
    if type(stack[i]) is IntType:
        answer = answer + stack[i]
    else :
        print '0'
        exit()

print answer