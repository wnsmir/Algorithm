def solution(array, commands):
    answer = []
    for command in commands:
        i_array = array[command[0]-1: command[1]]
        i_array.sort()
        num = i_array[command[2]-1]
        answer.append(num)
    
    return answer