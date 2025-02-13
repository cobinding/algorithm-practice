def solution(arr, query):
    for i in range(len(query)):
        idx = query[i]
        # idx가 짝수면 [:idx+1]번까지만 남긴다.
        if i%2 == 0:
            arr = arr[:idx+1]
        # idx가 홀수면 [idx:]까지만 남긴다.
        else:
            arr = arr[idx:]
    return arr