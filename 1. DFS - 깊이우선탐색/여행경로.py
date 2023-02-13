"""
def solution(tickets):
    answer = []
    node_level = 0
    start = "ICN"
    node_list = list(set(sum(tickets,[])))
    node_list.sort()
    #print(tickets2)
    visited = []
    node_list2 = list(sum(tickets,[]))
    #print(node_list)
    #print(node_list2)
    end = ""
    for i in range(len(node_list)):
        if node_list2.count(node_list[i]) == 1 and node_list[i] != start:
            end = node_list[i]
    #print(end)
    #print(len(tickets),len(node_list))
    #visited.append("ICN")
    def dfs(node, graph, node_level, visited):
        #print(graph)
        #visited[node]=True
        #visited.append("ICN")
        if node_level == len(tickets):
            return visited
        else:
            for i in range(len(node_list)):
                node2 = node_list[i]
                #print([node,node2])
                if [node,node2] in graph and [node,node2] not in visited and not node2 == end:
                    #print([node,node2])
                    node_level+=1
                    visited.append([node,node2])
                    #graph.remove([node,node2])
                    dfs(node2,graph,node_level,visited)
            return visited
    
    #visited.append(start)
    visited = dfs(start,tickets,node_level,visited)
    answer.append(start)
    for i in range(len(visited)):
        answer.append(visited[i][1])
    if end != "":
        answer.append(end)
    return answer
    """

from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 재귀 호출을 사용한 DFS
    def dfs(key, footprint):
        if len(footprint) == N + 1:
            return footprint

        for idx, country in enumerate(routes[key]):
            routes[key].pop(idx)

            fp = footprint[:] # deepcopy
            fp.append(country)

            ret = dfs(country, fp)
            if ret: return ret # 모든 티켓을 사용해 통과한 경우

            routes[key].insert(idx, country) # 통과 못했으면 티켓 반환

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    N = len(tickets)
    answer = dfs("ICN", ["ICN"])

    return answer
