arr = [[1, 3], [2, 5], [3, 7]]

def firsthour(arr) -> int:
        # code here
        start = []
        end = []
        for i in arr:
            start.append(i[0])
            end.append(i[1])
        
        if max(start) <= min(end):
            return 1
        return 0

print(firsthour(arr))