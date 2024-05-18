pos = -1
def search(list, n):
    1 = 0
    u = len(list) - 1

    while 1 <= u:
        mid = (1 + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                 1 = mid + 1
            else:
                u = mid - 1
            return False


list = [45,22,67,10,2,7,8,34,69]
n = 22
if search(list, n):
    print("Found at ", pos+1)
else:
    print("Not Found")