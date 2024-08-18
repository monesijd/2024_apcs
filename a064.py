def notpass(students):
    notpass_list = []
    for _ in students:
        if _ < 60:
            notpass_list.append(_)
    if len(notpass_list) == 0:
        return "best case"
    return max(notpass_list)

def ispass(students):
    pass_list = []
    for _ in students:
        if _ >= 60:
            pass_list.append(_)
    if len(pass_list) == 0:
        return "worst case"
    return min(pass_list)


number = int(input())
students = sorted(list(map(int, input().split())))
print(' '.join(list(map(str, students))))
print(notpass(students))
print(ispass(students))
