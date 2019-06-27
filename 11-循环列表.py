# for: 遍历对象依次获取对象中的每一个元素

my_list = ["小明", "小红"]

for value in my_list:
    print(value)

print("--------")

index = 0
# 获取列表长度 len函数获取（字符串，列表）的长度
# my_str = "hello"
# print(len(my_str))
my_list_len = len(my_list)
print(my_list_len)
# 获取列表的最大下标
max_index = my_list_len - 1

while index <= max_index:
    # 根据下标获取对应的元素
    value = my_list[index]
    print(value)
    index += 1