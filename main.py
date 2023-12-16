def solution(s):
    text = ''
    for i in s:
        if i == i.upper():
            text+= ' ' + i
        else:
            text += i
    return text