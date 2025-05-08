import sys
import math
from itertools import combinations
input = sys.stdin.readline

def vector_matching():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    total_x = sum(x for x, y in points)
    total_y = sum(y for x, y in points)
    min_length = math.inf
    
    # 절반 선택 조합 생성
    for selected in combinations(points, n//2):
        sum_x = sum(x for x, y in selected)
        sum_y = sum(y for x, y in selected)
        residual_x = total_x - 2*sum_x
        residual_y = total_y - 2*sum_y
        current = math.hypot(residual_x, residual_y)
        min_length = min(min_length, current)
    
    print(f"{min_length:.12f}")

for _ in range(int(input())):
    vector_matching()
