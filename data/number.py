#本文件提供解析数字的类

#定义类
class number() :
    def __init__(self) :
        #给变量赋值
        self.char = ''    #当前字符
        self.num = ''    #数字内容
        self.times = -1    #循环次数（之所以要设为-1，是因为如果设为0，那么返回times时times就会是数字后面的那个空格的索引）
        self.returns = ''    #要返回的数字
        
    def get(self,number) :
        for i in number :
            #判断下个字符是否是 （表明数字结束）
            if i == ' ' :
                #返回数字，函数结束
                if '.' in self.num :
                    self.returns = float(self.num)
                else :
                    self.returns = int(self.num)
                return { 'num':self.returns , 'times':self.times }
            #判断当前字符是否是_（借鉴python语法糖）
            elif i == '_' :
                self.char = ''
            #那么当前字符只可能是普通的字符了
            else :
                self.char = i
            
            self.num = self.num + self.char
            self.times += 1
