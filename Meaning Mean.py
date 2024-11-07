
test_cases = int(input())
for i in range(test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    while len(arr) > 1:
        floor_mean = 0
        floor_mean = (arr[0]+arr[1])//2
        arr.pop(1)
        arr.pop(0)
        arr.insert(0, floor_mean)
    print(arr[0])