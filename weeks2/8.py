#程序控制时间 测量时间 

import time

start = time.perf_counter()

time.sleep(3.3)

end = time.perf_counter()

print('{}'.format(end-start))