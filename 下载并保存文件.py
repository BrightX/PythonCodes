import requests
import os
import sys


def over(i):
    """是否继续执行，或者终止程序"""
    while True:
        s = "  是否继续{}y/n?  ".format(i)
        n = input(s)
        if n in ['Y', 'y', 'N', 'n']:
            break
    if n == 'n'or n == 'N':
        input("\n  请按回车键退出……")
        return 0
    else:
        return 1

e = 1
while e:
    # 下载到内存
    while True:
        url = input("\n  请输入下载链接：")
        if url == '':
            continue
        try:
            print("OK，正在下载中.....")
            r = requests.get(url)
            break
        except requests.exceptions.MissingSchema:
            print("\n---------- 请正确输入下载链接 ----------")
        except requests.exceptions.InvalidSchema:
            print("\n---------- 请正确输入下载链接 ----------")
        except requests.exceptions.ConnectionError:
            print("\n--------- 网络异常，请重试 ---------")


    # 计算文件大小
    size = len(r.content)
    if size < 1024:
        print("文件大小为：", size, "Byte")
    elif size >= 1024 and size < 1048576:
        print("文件大小为：", size/1024, "KB")
    elif size >= 1048576 and size < 1073741824:
        print("文件大小为：", size/1048576, "MB")
    else:
        print("文件大小为：", size/1073741824, "GB")

    print("下载完成，正在保存")

    # 保存文件
    while True:
        filePath = input("\n请输入文件保存路径(选填)：")
        fileName = input("\n请输入文件名(包含扩展名)：")
        if fileName == ''or '.'not in fileName:
            print("\n---------- 请正确输入文件名 ----------")
        else:
            break
    print("OK")
    if filePath == '':
        Path = fileName
    else:
        Path = filePath + "\\" + fileName
    with open(Path, "wb") as f:
        f.write(r.content)
    f.close()

    print("保存成功    保存位置在 {}\n".format(os.path.abspath(Path)))
    
    e = over("下载其它文件")
sys.exit()

