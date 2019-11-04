from loading import ft_progress
import time

listy = range(1000)
ret = 0
print(listy)
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)