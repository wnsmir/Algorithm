def solution(lottos, win_nums):
    count = 0
    zero = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1

    for lotto in lottos:
        if lotto in win_nums:
            # win_nums에서 당첨번호 제거, lotto에서 제거
            win_nums.remove(lotto)
            count += 1
    
    max_value = count + zero
    min_value = count
    
    answer_sheet = {}
    answer_sheet[0] = 6
    answer_sheet[1] = 6
    answer_sheet[2] = 5
    answer_sheet[3] = 4
    answer_sheet[4] = 3
    answer_sheet[5] = 2
    answer_sheet[6] = 1
    answer = []
    answer.append(answer_sheet[max_value])
    answer.append(answer_sheet[min_value])

    return answer