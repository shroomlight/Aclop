#本文件提供检测字符串是否空白的函数

#定义函数
def fun(str):
    if str == '' :
        return True
    else:
        #判断字符串是否全是空格
        for i in str :
            if i != ' ' :
                return True
            return False
        
#测试函数
if __name__ == '__main__' :
    if fun('') :
        print(1)
    if fun('         ') :
        print(1)