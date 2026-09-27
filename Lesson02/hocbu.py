print(5 + 5)

x = 10
print(x)

str, number1, number2, number3 = "Thien Nhan", 9.0, 12, 9
print(number1)
print(number3)

# Data types (Kiểu dữ liệu):
    # int (Integer: Số nguyên) 5, -10, 12, 0,...
    # float (Số thực) 1.2, -1.5, 2.0, 0.0,...
    # str (String: Chuỗi) "Hello", "a", '23', "0",...
    # bool (Boolean): True, False

# Quy tắc đặt tên biến:
    # Rule 1: Tên biến phải bao gồm chữ thường, chữ in hoa, số và dấu underscore (_)
          # Một số tên biến không hợp lệ: *abc, a12&b, >123,..
          # Một số tên biến hợp lệ: _abc, a123B_, A_B_C,...
    # Rule 2: Tên biến không được bắt đầu bằng chữ số:
          # Một số tên biến không hợp lệ: 1a123, 1__, 0ab12,...
          # Một số tên biến hợp lệ: _abc, A123,...
    # Rule 3: Biến phân biệt chữ in hoa, in thường
          # _Abc và _abc là 2 biến khác nhau
    # Rule 4: Tên biến không được trùng với từ khoá (Keyword)
          # Các từ khoá: or, if, else, elif, def, True, False...
          # If, false, Or là các tên biến hợp lệ
# Lưu ý: Khi dùng từ khoá làm tên biến thì sẽ sinh ra lỗi SyntaxError: invalid syntax

true = False
print(type(true))
a, b, c = "0", 12.0, 33
print(type(a))
print(type(b))
print(type(c))

age = int(input("Please, enter your age: "))
future_age = age + 10
print(f"In 10 years, you will be {future_age} years old.")

print(int(12.0))
print(int(12.4))
print(int(12.9))

print(int('123'))
print(float('123.2'))

