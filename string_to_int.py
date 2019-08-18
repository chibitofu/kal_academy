#Covnert an string of numbers into an int value.
#"123" -> 123

def string_to_int(input:str):
    int_dic = { "1" : 1,
                "2" : 2,
                "3" : 3,
                "4" : 4,
                "5" : 5,
                "6" : 6,
                "7" : 7,
                "8" : 8,
                "9" : 9,
                "0" : 0
    }

    answer = []

    for i in range(0, len(input)):
        if input[i] is in int_dic:
            answer.append(int_dic[input[i]])
            for i, d in enumerate(arr[::-1]):
                print(i,d)
                print(d * 10**i )
        else:
            return "Not a number string"
    
    return answer
    