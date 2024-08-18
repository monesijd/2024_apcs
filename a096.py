time1 = list(map(int, input().split(":")))
time2 = list(map(int, input().split(":")))

sum1 = 3600 * time1[0] + 60 * time1[1] + time1[2]
sum2 = 3600 * time2[0] + 60 * time2[1] + time2[2]

if sum1 > sum2:
    gap = sum2 + 86400 - sum1
else:
    gap = sum2 - sum1

print(f"{gap//3600:02d}:{(gap%3600)//60:02d}:{(gap%3600)%60:02d}")
