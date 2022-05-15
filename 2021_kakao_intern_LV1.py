def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(len(words)):
        # nums 리스트 따로 가져가지 않는 경우
        s = s.replace(words[i], str(i))
        #s = s.replace(words[i], nums[i])

    answer = int(s)
    return answer