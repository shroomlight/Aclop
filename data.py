#本文件提供解析字符串的类

#导入模块
import consts

#字符串
def string() :
    #给变量赋值
    text = ''    #字符串中的文本
    raec = False    #当前字符是否是转义字符
    char = ''    #当前字符
    times = 0    #循环次数

    #遍历每个字符
    for i in string :
        #判断当前字符是否是转义字符
        if raec :
            char = consts.Ec[i]
            raec = False
        #判断当前字符是否是\（表明下个字符是转义字符）
        elif i == '\\' :
            raec = True
        #判断当前字符是否是'（表明字符串结束）
        elif i == "'" :
            return { 'text':text , 'times':times }    #返回字符串的内容，函数结束
        #那么当前字符只可能是普通的字符了
        else :
            char = i
            
        text = text + char
        times += 1

#数字
def number() :
    #给变量赋值
    char = ''    #当前字符
    num = ''    #数字内容
    times = -1    #循环次数（之所以要设为-1，是因为如果设为0，那么返回times时times就会是数字后面的那个空格的索引）
    returns = ''    #要返回的数字
        
    #遍历每个字符
    for i in number :
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