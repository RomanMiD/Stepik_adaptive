time_sec = int(input()) % (3600 * 24)
print(
    '%d:%.2d:%.2d' %(time_sec//3600, time_sec//60%60, time_sec%60)
)