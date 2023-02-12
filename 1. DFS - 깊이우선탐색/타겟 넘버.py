def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx,num_sum):
        if idx == n:
            if num_sum == target:
                nonlocal answer
                answer += 1
        if idx <n:
            dfs(idx+1,num_sum+numbers[idx])
            dfs(idx+1,num_sum-numbers[idx])

    dfs(0,0)
    return answer

#출처 : https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS
