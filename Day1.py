# input
# name = input()
# age = input("Please enter your age: ")
# # control, process
# message = "Hello" + " "+ name+" "+ age
# # output
# print(message)
#print("Hello dat ngoc nghech")

#input

# if a<b: print("a < b")
# elif a>b: print("a > b")
# else: print("a=b")


# input: nhập a, nhập b và nhập phép toán. Trả về kết quả dưới dạng: a + b = ...
a = int(input("nhập số thứ nhất:"))
c = input("nhập phép tính(+,-,x,:):")
b = int(input("nhập số thứ hai:"))
if c=="+": rs = a+b
if c=="-": rs = a-b
if c=="x": rs = a*b
if c==":": rs = a/b

print("a "+c +" b" + " = " + str(rs))



# viết chương trình input: chiều dài, chiều rộng. Output: trả về hình chữ nhật * với số 
# tương ứng chiều dài, chiều rộng
# Ví dụ: chiều dài 3, chiều rộng 4
#  ****
#  ****
#  ****
