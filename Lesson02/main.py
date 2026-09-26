x = 12
print(x)
# Variable (Biến): Là tên của vùng nhớ dùng để lưu trữ giá trị và giá trị đó có thể thay đổi được khi thực hiện chương trình.
a, b, c = "hello", 3, 3.14
print(a, b, c)

# Data types (Kiểu dữ liệu): 
    # int (integer)kiểu số nguyên ví dụ: -33, 0, 12,...
    # float: Kiểu số thực ví dụ: -12.3, 0.0, 11.0, 2.3,...
    # bool (Boolean) True / False
    # str (string) kiểu chuỗi ví dụ: "0", "23ab", 'Hello World',...
var = "123"
number = -3.0

# Quy tắc đặt tên biến trong python
# Rule 1: Tên biến phải bao gồm chữ in hoa, chữ in thường, số và dấu underscore (_)
    # Practice: Liệt kê ra các tên biến hợp lệ trong các tên biến sau
        # a4b, q%3, _abc, a_123, <abc
        # => các tên biến hợp lệ: a4b, _abc, a_123
# Rule 2: Tên biến không được bắt đầu bằng số
        # 1abc, 123, 0hi: không hợp lệ
# Rule 3: Tên biến phân biệt in hoa và in thường
        # a12C khác với A12C và khác với a12c
# Rule 4: Tên biến không được trùng với từ khoá
        # Các từ khoá: if, else, pass, elif, True, False,...
        # If, true, false, Pass, iF: là các tên biến hợp lệ
# Nếu đặt tên biến trùng với từ khoá thì dẫn đến lỗi cú pháp: SyntaxError: Invalid Syntax
# Cú pháp nhận biết kiểu dữ liệu
my_name = "Bùi Trường Vũ"
print(type(my_name))
age = 24
print(type(age))
number = 12.0
print(type(number))
is_student = True
print(type(is_student))
print(2.0)
print(int(2.0))
str1 = '12.3' 
print(type(str1))
new_var = float(str1)
print(type(new_var))

# Practice:

# Đầu vào của input() là kiểu str

age = int(input("Xin hãy nhập tuổi của bạn: "))
future_age = age + 10
print("Trong 10 năm nữa, bạn sẽ", future_age, "tuổi.")






