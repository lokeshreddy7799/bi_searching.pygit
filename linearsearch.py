pos = -1

def search(list,n):
    i = 0
    while i< len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False


list = [3,4,5,6,7]
n = 5
if search(list,n):
    print("Found at ",pos)
else:
    print("not Found")
