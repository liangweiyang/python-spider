html = """
<div class="panel">
    <div class="panel-heading">
        <h3>hello</h3>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""
from bs4 import  BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
#标准选择器
#print(soup.find_all('ul'))      #返回所有ul标签
#for ul in soup.find_all('ul'):     #嵌套遍历查找
#    print(ul.find_all("li"))
#print(soup.find_all(attrs={'id':'list-1'}))     #  #查找所有标签里面含有id的值为list-1的标签
#print(soup.find_all(attrs={'class':'panel-heading'}))   #查找所有标签里面含有class的值为panel-heading的标签
#print(soup.find_all(text='Foo'))                #以文本方式查找，直接返回内容

#print(soup.find('ul'))  #返回第一个查找到的ul标签
#print(soup.find('li'))  #返回第一个查找到的li标签
#print(soup.find('li').string)   #返回第一个li标签的内容
#print(soup.find('li')['class'])#返回第一个li标签的class属性值

#css选择器
#print(soup.select('.panel .panel-heading'))     #找到panel 里面的panel-heading
#print(soup.select('ul'))        #选择所有ul标签
#print(soup.select('ul')[0])     #打印第一个ul标签里的内容
#print(soup.select('ul li'))     #先选择ul标签，次选择ul抱歉里面的li标签，打印出li标签里面的内容,以列表返回
#print(soup.select('ul li')[0].get_text())#获得ul标签中第1个li标签的文本

#for l in soup.select('ul'): #获得属性
 #   print(l['id'])

#for m in soup.select('li'): #获得文本
 #   print(m.get_text())




