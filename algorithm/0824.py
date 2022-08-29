# 슬라이딩 윈도우
def minSlidingWindow(nums, k):
    min_sum = 9999
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        if end >= k - 1:
            # 0~k-1 까지 더한 값이 최소값보다 작다면, 최소값을 갱신
            if window_sum <= min_sum:
                min_sum = window_sum

            # 윈도우에 포함된 맨 앞자리 수를 제거
            window_sum -= nums[start]
            # 윈도우 시작 인덱스를 하나 증가
            start += 1
    return min_sum
nums = [7, 2, 4, 3, 2, 1, 1, 9, 2]

result = minSlidingWindow(nums, 3)
print(result)

# #투포인터 알고리즘
nums = [7, 2, 4, 3, 2, 1, 1, 9, 2]
N, M = map(int, input().split())
def two_pointer(nums):
    global count
    count = 0
    start, end = 0, 0

    window_sum = nums[start]
    while start < N:
        if window_sum == M:
            count += 1
            window_sum -= nums[start]
            start += 1
        elif window_sum < M:
            end += 1
            if end >= N:
                break
            window_sum += nums[end]
        else:
            window_sum -= nums[start]
            start += 1
        print(f'start = {start} / end = {end}')

two_pointer(nums)
print(count)