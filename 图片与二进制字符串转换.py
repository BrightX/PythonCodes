import base64


image = input("输入图片名：")

# 将图片encode为二进制字符串_方法一
with open(image, 'rb') as f:
    f_str = base64.b64encode(f.read())
print(type(f_str))


# 将图片encode为二进制字符串_方法二
f = open(image, 'rb')
f_str = base64.b64encode(f.read())
f.close()
print(type(f_str))


# 将二进制字符串(图片)decode为图片
str = f_str
file_str = open(image, 'wb')
file_str.write(base.b64decode(str))
file_str.close
