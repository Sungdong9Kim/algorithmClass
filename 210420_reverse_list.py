# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
# 코드를 입력하세요.
    if len(some_list) == 1 or len(some_list) == 0:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
#some_list = [9, 8, 7 ,6 ,5 ,4 ,3 ,2 ,1]
print(some_list)