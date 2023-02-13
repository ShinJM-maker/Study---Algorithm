from collections import deque


"""
def solution(maps):
    answer = 0
    i_len = len(maps)
    j_len = len(maps[0])
    answer_list = []
    
    
    def dfs(idx,jdx,maps,answer,visited=[]):
        #print(visited)
        if (idx == i_len-1) & (jdx == j_len-1):
            answer+=1
            #print(answer)
            answer_list.append(answer)
            return visited
        else: 
            if (idx+1 < i_len):
                if (maps[idx+1][jdx]==1) & ((idx+1,jdx) not in visited):
                    print(idx+1,jdx)
                    visited.append((idx+1,jdx))
                    answer+=1
                    dfs(idx+1,jdx,maps,answer,visited)
            if (jdx+1 < j_len):
                if (maps[idx][jdx+1]==1) & ((idx,jdx+1) not in visited):
                    print(idx,jdx+1)
                    visited.append((idx,jdx+1))
                    answer+=1
                    dfs(idx,jdx+1,maps,answer,visited)
            if (idx-1 >= 0):
                if (maps[idx-1][jdx]==1) & ((idx-1,jdx) not in visited):
                    print(idx-1,jdx)
                    visited.append((idx-1,jdx))
                    answer+=1
                    dfs(idx-1,jdx,maps,answer,visited)
            if (jdx-1 >= 0):
                if (maps[idx][jdx-1]==1) & ((idx,jdx-1) not in visited):
                    print(idx,jdx-1)
                    visited.append((idx,jdx-1))
                    answer+=1
                    dfs(idx,jdx,maps,answer,visited)
        return visited
    
    dfs(0,0,maps,0)
    #print("answer:",answer_list)
    print(answer_list)
    if len(answer_list)>0:
        answer = min(answer_list)
    else:
        answer = -1
    #answer = min(answer_list)
    return answer
    """


def solution(maps):
    answer = 1
    j_len = len(maps)
    i_len = len(maps[0])
    dx,dy = [0,1,-1,0],[1,0,0,-1]
    Q = deque()
    Q.append((0,0,answer))
    while Q:
        y,x,answer = Q.popleft()
        maps[y][x] = 0
        for i in range(len(dx)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny == j_len-1 and nx == i_len-1:
                return answer + 1
            elif 0<= ny < j_len and 0<= nx < i_len and maps[ny][nx]: #and (y+j,x+i) not in visited:
                #visited.append((y+j,x+i))
                Q.append((ny,nx,answer+1))
                maps[ny][nx] = 0
    return -1
    

"""
from collections import deque
def solution(maps):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    n = len(maps)
    m = len(maps[0])
    answer= 1
    Q = deque()
    Q.append((0,0,answer))
    while Q:
        y,x,answer = Q.popleft()
        maps[y][x] = 0
        for i in range(len(dx)):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx == m-1 and ny == n-1:
                return answer + 1
            elif 0 <= nx < m and 0 <= ny < n and maps[ny][nx]:
                Q.append((ny,nx,answer+1))
                maps[ny][nx] = 0

    
    return -1
    """
