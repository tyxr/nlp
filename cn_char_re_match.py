import re
sstr=u"【心理箴言】现实是污浊的河流，要想接受污浊的河流而自身不被污染，我们必须成为大海。 ​​=-=4845/.?'​"

# pattern =re.compile(u'[\u4e00-\u9fa5]')

pattern =re.compile(u"[\u4e00-\u9fa5]+")

result=re.findall(pattern,sstr)



c = "河流"
if c in sstr:
    pass


xor = bool(len(sstr)) != bool(len(c))
print(xor)
