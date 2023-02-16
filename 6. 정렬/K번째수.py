def solution(array, commands):
    answer = []
    
    for l in range(len(commands)):
        i,j,k = commands[l]
        #print(i,j,k)
        
        if i == j:
            answer.append(array[i-1])
        else:
            temp_list = array[i-1 : j] #.sort(reverse=False)
            temp_list.sort(reverse=False)
            #print(temp_list)
            answer.append(temp_list[k-1])
        #print("temp:",temp_list)
    return answer
