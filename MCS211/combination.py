# target                : 949
# list of numbers desc  : [500,200,100,50,20,10,5,2,1]

def combination(target, *args):
    arr = []
    while target > 0:
        for i in range(len(args)):
            if args[i] <= target:
                target = target - args[i]
                arr.append(args[i])
                break
            else:
                continue
    return arr

# print(combination(949, 500, 200, 100, 50, 20, 10, 5, 2, 1))

def combinationMod(target, *args):
    arr = [list(args), [0] * len(args)]
    for i in range(len(args)):
        if target<=0:
            return
        arr[1][i] = target//arr[0][i]
        target = target%arr[0][i]
        if arr[1][i] != 0:
            print(f"no. of {arr[0][i]} is {arr[1][i]}")
            
# combinationMod(949, 500, 200, 100, 50, 20, 10, 5, 2, 1)


def combinationModRec(target, i, *args):
    if target<=0:
        return
    res = target//args[i]
    if res>0:
        mod = target%args[i]
        print(f"nor. of {args[i]} is {res}")
        combinationModRec(mod,i+1, *args )
    else:
        combinationModRec(target,i+1, *args )
        
combinationModRec(949, 0, 500, 200, 100, 50, 20, 10, 5, 2, 1)