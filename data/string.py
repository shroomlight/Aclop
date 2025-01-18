#本文件提供解析字符串的类

#定义类
class string() :
    def __init__(self) :
        self.text = ''    #字符串中的文本
        self.Ec = { "'":"'" , '{':'{' , '}':'}' , '\\':'\\' , 'n':'\n' }    #转义字符
        self.raec = False    #当前字符是否是转义字符
        self.char = ''    #当前字符
        self.times = 0    #循环次数

    def get(self,string) :
        #遍历每个字符
        for i in string :
            #判断当前字符是否是转义字符
            if self.raec :
                self.char = self.Ec[i]
                self.raec = False
            #判断当前字符是否是\（表明下个字符是转义字符）
            elif i == '\\' :
                self.raec = True
            #判断当前字符是否是'（表明字符串结束）
            elif i == "'" :
                return { 'text':self.text , 'times':self.times }    #返回字符串的内容，函数结束
            #那么当前字符只可能是普通的字符了
            else :
                self.char = i
            
            self.text = self.text + self.char
            self.times += 1
