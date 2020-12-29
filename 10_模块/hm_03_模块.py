# import hm_01_测试模块1 as modular1
# import hm_02_测试模块2 as modular2

from hm_01_测试模块1 import Dog
from hm_01_测试模块1 import say_hello as say1
from hm_02_测试模块2 import say_hello as say2
import random
print(random.__file__)
print(Dog())
say1()
say2()

# print(modular1.Dog())
# modular1.say_hello()
# print(modular1.title)
#
# print(modular2.Cat())
# modular2.say_hello()
# print(modular2.title)