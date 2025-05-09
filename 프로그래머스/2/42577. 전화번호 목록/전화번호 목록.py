def solution(phone_book):
    unique_phone_book = set(phone_book)
    for phone in phone_book:
        temp = ''
        for num in phone[:-1]:
            temp += num
            if temp in unique_phone_book:
                return False
    return True