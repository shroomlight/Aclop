#本文件提供解析数字的函数

#定义函数
def fun(par) :
    #给变量赋值
    char = ''    #当前字符
    num = ''    #数字内容
    times = -1    #循环次数（之所以要设为-1，是因为如果设为0，那么返回times时times就会是数字后面的那个空格的索引）
    returns = ''    #要返回的数字

    for i in par :
        #判断下个字符是否是 （表明数字结束）
        if i == ' ' :
            #返回数字，函数结束
            if '.' in num :
                returns = float(num)
            else :
                returns = int(num)
            return { 'num':returns , 'times':times }
        #判断当前字符是否是_（借鉴python语法糖）
        elif i == '_' :
            char = ''
        #那么当前字符只可能是普通的字符了
        else :
            char = i
        
        num = num + char
        times += 1