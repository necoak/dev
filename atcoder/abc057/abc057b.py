#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc057/tasks/abc057_b

N, M = list(map(int, input().split()))

students = []
for i in range(N):
    students.append(list(map(int, input().split())))

checkpoints =  []
for j in range(M):
    checkpoints.append(list(map(int, input().split())))

def calc_manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

for i in range(N):
    min_distance = 10**16
    mins_j = 50
    student_x, student_y = students[i]
    for j in range(M):
        checkpoint_x, checkpoint_y = checkpoints[j]
        ij_distance = calc_manhattan_distance(student_x,  student_y, checkpoint_x, checkpoint_y)
        if ij_distance < min_distance:
            min_distance = ij_distance
            mins_j = j
    print(mins_j+1)
