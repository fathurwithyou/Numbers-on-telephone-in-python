kamus = [" ", ",.!?", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
arr = list(map(str, input().split()))
for i in range(len(arr)):
    print(kamus[int(arr[i][0])][len(arr[i])-1], end="")

# 2 55 88 0 44 33 22 2 8
# 7 2 7 2 0 6 444 66 8 2 0 7 88 555 7777 2
