html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html.parser")

oup = BeautifulSoup(html_doc, "lxml")     #lxml网页解析库
print(soup.prettify())      #prettify()方法将html代码格式化，并且补齐代码
print(soup.title.string)    #获取标签内容
print(soup.title.name)      #获取标签名称

print(soup.title)           #内容和标签一起输出
print(soup.head)             #内容和标签一起输出
print(soup.a)                #内容和标签一起输出

print(soup.a['href'])
print(soup.a.attrs['href'])

print(soup.get_text())



#遍历结点
#print(soup.p.contents)
#print(soup.p)
#print(list(soup.p.children))    #寻找一个标签下的所有子标签
#print(soup.p.parent)            #打印父标签包含的所有内容
#print(list(enumerate(soup.a.parents)))      #寻找a的所有上级标签,以列表的形式返回
print(list(enumerate(soup.a.next_siblings)))    #a以下并列结点
print(list(enumerate(soup.a.previous_siblings)))    #a以上并列结点




