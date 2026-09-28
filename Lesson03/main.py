# Toán tử số học: 
# Toán tử cộng (add) +
print(12 + 23.4) # Output: 35.4
print("Hello" + "World")
# Toán tử trừ -
print(12.5 - 0.7) # Output: 11.8
# Toán tử nhân *
print(2 * 3) # Output: 6
print("hi" * 5)
st = "4" * 0
print(">>>", st)
print(type(st))
# Toán tử chia /
print(12 / 3) # Output: 4.0
# Chia lấy phần nguyên //
print(13 // 2) # Output: 6
# Chia lấy phần dư %
print(17 % 3) # Output: 2
# Mũ **
print(2 ** 3) # Output: 8
# => Thứ tự ưu tiên: ** -> *, /, //, % -> +, -
# Nếu các phép toán chỉ có *, /, //, % hoặc chỉ có +, - thì thực hiện từ trái qua phải 
print(12 - 11 + 4) # Output: 5
print(12 % 3 * 256) # Output: 0
# Nếu các phép toán chỉ có ** thì thực hiện từ phải qua trái
print(2 ** 2 ** 3) # Output: 256

# Toán tử quan hệ (Trả về kiểu bool hay Boolean: True, False )
# So sánh bằng (==) Dùng để kiểm tra hai giá trị có bằng nhau hay không
a, b, c, d, e, f = 12, 12.0, 12, 13.3, 13.3, "12"
print(a == c)
print(a == b)
print(a is b)
print(d == e)
print(d is e)
print(a == f)
# So sánh khác (!=) Dùng để kiểm tra hai giá trị có khác nhau hay không
a, b, c, d, e, f = 12, 12.0, 12, 13.3, 13.3, "12"
print(a != f) #Output: True
print(a != c) #Output: False

# Lớn hơn (>), lớn hơn hoặc bằng (>=): Kiểm tra giá trị bên trái có lớn hơn hay lớn hơn hoặc bằng giá trị bên phải hay không
num1, num2, num3 = 0.0, -23, 12.5
print(num1 > num2) # Output: True
print(num2 >= num3) # Output: False
# Bé hơn (<), bé hơn hoặc bằng (<=): Kiểm tra giá trị bên trái có bé hơn hay bé hơn hoặc bằng giá trị bên phải hay không
num1, num2, num3 = 0.0, -23, 12.5
print(num1 < num2) # Output: False
print(num2 <= num3) # Output: True
print("-" * 30)
# Toán tử logic
# Falsy: Là những giá trị khi ép thành kiểu bool thì nhận giá trị False
      # False, 0, 0.0, "", [], {}, set(), range(0), '' 
print("*" * 30)
lst = [False, 0, 0.0, "", [], {}, set(), range(0), '']
for element in lst:
  print(bool(element))
print("*" * 30)

# Truthy: Là những giá trị khi ép thành kiểu bool thì nhận giá trị True
      # Các giá trị còn lại là Truthy
print(">>>", bool("hi"))
print(">>>", bool(10))
print(">>>", bool(-245))
print(">>>", bool(2.4))

# and (và)
tr = True
fal = False
print(tr and tr) # Output: True
print(tr and fal) # Output: False
print(fal and fal) # Output: False

# Nếu tất cả phần tử ngoài phần tử cuối đều là giá trị Truthy thì trả về giá trị cuối cùng
print("abc" and 123 and True and "MindX-PTB43-MK")
# Trả về giá trị Falsy đầu tiền từ trái qua phải
print("abc" and 0 and True and "MindX-PTB43-MK")

# or (hoặc)
tr = True
fal = False
print(tr or tr) # Output: True
print(tr or fal) # Output: True
print(fal or fal) # Output: False

# not (phủ định)
print(not True) # output: False
print(not False) # output: True
