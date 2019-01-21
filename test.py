
import readConfig
import random
rd = readConfig.ReadConfig()
li = [chr(i) for i in range(ord("A"),ord("Z")+1)]
li1 = [chr(i) for i in range(ord("a"),ord("z")+1)]
li2 = [str(i) for i in range(0,10)]
print(li)


# for i in range(100):
#     # print(random.sample(li, 3) )

#     print(''.join(random.sample(li+li1+li2, 3)))
print(rd.suiji())