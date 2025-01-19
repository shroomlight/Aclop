'''#本文件提供解析数组的类

#导入库
import string_ , number
import objects


#定义类
class array() :
    def __init__( self , array ) :
        self.times = 0    #循环次数
        self.char = array[self.times]    #当前字符
        self.array = []    #数组的内容
        self.get_ = None    #得到的数据信息
        self.data = None    #得到的数据内容
    def get(self) :
        while True :
            #判断当前字符是否是]（代表数组结束）
            if self.char == ']' :
                return { 'array':self.array , 'times':self.times }    #返回数据，函数结束
            #判断当前字符是否是空格
            elif self.char == ' ' :
                pass    #不必管他~（玉帝音）
            #判断当前字符是否是代表接下来是某种数据的字符
            elif self.char in ( "'" , '1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'-' ,'[' , ) :
                #判断是否是代表接下来是字符串的字符
                if self.char == "'" :
                    self.get_ = objects.string.get( self.array[ self.times + 1 : -1 ] )
                    self.data = self.get_['text']
                    self.times = self.times + 1 + self.get_['times']
                #判断是否是代表接下来是数字的字符
                elif self.char in ( '1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' , '-' ) :
                    self.get_ = objects.number.get( self.array[ self.times + 1 : -1 ] )
                    self.data = self.get_['num']
                    self.times = self.times + 1 + self.get_['times']
                #判断是否是代表接下来是数组的字符
                elif self.char == '[' :
                    n = array( self.datas[ self.times + 1 : -1 ] )
                    self.get_ = n.get()
                    self.data = self.get_['array']
                    self.times = self.times + 1 + self.get_['times']
            
            self.array.append(self.data)
            self.times += 1

test = array(" 114514 'Hello,world!' ] ")
print(test.get()['array'])'''