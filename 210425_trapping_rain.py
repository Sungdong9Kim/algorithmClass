def trapping_rain(buildings):
# 코드를 작성하세요
    total_height = 0
    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        upper_bound = min(max_left, max_right)

        total_height += max(0, upper_bound - buildings[i])

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))