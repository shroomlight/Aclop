#本文件是主文件

#导入模块
import isnt_space

#给变量赋值
script = vars.scripts.splitlines()
in_class = False

#遍历每一行代码
for i in script :
    if isnt_space.fun(i) or i[:1] == '//':    
        #判断是否在解释一个类的声明
        if in_class :
            pass    #这里暂时先不写 （：3 」∠）
        else :
            pass    #这里也暂时先不写 ∠( ᐛ 」∠)_
