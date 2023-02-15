def solution(phone_book):
    answer = True
    phone_dict = dict()
    #phone_dict = collections.Counter(phone_book)
    phone_book.sort(reverse=False)
    #print(phone_book)
    for i in range(len(phone_book)-1):
        #for j in range(i+1,len(phone_book)):
        #if i<len(phone_book[i]):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                #print(phone_book[i],phone_book[j][0:len(phone_book[i])])
                return False
            #phone_dict[phone_book[i]] = len(phone_book[i])
    #print(phone_dict)
    #print(phone_book)
    #sorted_dic = sorted(phone_dict.items(), key = lambda item: item[1])
    #print(sorted_dic)
    """
    for number in range(len(phone_book)):
        for number2 in range(number+1,len(phone_book)):
            if phone_book[number] == phone_book[number2][0:len(phone_book[number])]:
                print(phone_book[number],phone_book[number2][0:len(phone_book[number])])
                return False
                """
    return answer
