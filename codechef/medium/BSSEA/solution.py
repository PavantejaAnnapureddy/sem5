# cook your dish here
n = int(input())
seats = list(map(int, input().split()))

min_seat = min(seats)
max_seat = max(seats)
center_sum = min_seat + max_seat  # This is 2 * center

best_seat = seats[0]
best_dist = abs(2 * seats[0] - center_sum)

for seat in seats:
    dist = abs(2 * seat - center_sum)
    if dist < best_dist or (dist == best_dist and seat < best_seat):
        best_dist = dist
        best_seat = seat

print(best_seat)