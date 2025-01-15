#本文件提供解析字符串的函数

#定义函数
def fun(par) :
    #给变量赋值
    text = ''    #字符串中的文本
    Ec = { "'":"'" , '{':'{' , '}':'}' , '\\':'\\' , 'n':'\n' }    #转义字符
    raec = False    #当前字符是否是转义字符
    char = ''    #当前字符
    times = 0    #循环次数

    #遍历每个字符
    for i in par :
        #判断当前字符是否是转义字符
        if raec :
            char = Ec[i]
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