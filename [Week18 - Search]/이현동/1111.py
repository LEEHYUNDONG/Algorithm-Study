import sys
input = sys.stdin.readline

"""

등차수열을 계산하여 공차와 초항을 찾는다.
다음 수를 계산하는 문제

1 2 3 4 _

만약 다음칸에 여러개 수가 존재하면 A 출력, 존재하지 않으면 B출력

"""
N = int(input())
lst = list(map(int, input().split()))