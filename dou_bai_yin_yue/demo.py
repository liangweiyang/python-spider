# 利用方法选择器

# 存储到数据库
import requests
from bs4 import BeautifulSoup
import pymysql
url = 'https://music.douban.com/chart'
html = requests.get(url=url).text
soup = BeautifulSoup(html, 'lxml')
ul = soup.find(attrs={'class': 'col5'})     # 找到存放排行榜音乐的ul标签
lis = ul.find_all(name='li')                # 获取每一首音乐对应的标签
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
print('数据库连接成功')
sql = 'CREATE TABLE IF NOT EXISTS music (paiming INT NOT NULL, name VARCHAR(255) NOT NULL, lianjie VARCHAR(255) NOT NULL, PRIMARY KEY (paiming))'
cursor.execute(sql)
print('数据表创建完成！')
for li in lis:
    paiming = li.find(name='span').string
    name = li.find(name='a', attrs={'href': 'javascript:;'}).string
    a = li.find(name='a', attrs={'class': 'face'})      # 获取存存放连接的a标签,再在a标签里获取连接
    if a != None:
        img = a.find(name='img')    # 获取连接的img标签
        lianjie = img.attrs['src']      # 获取到连接
    else:
        lianjie = '没有链接'
    print(paiming, name, lianjie)
    sql = 'INSERT INTO music(paiming, name, lianjie) values(%s, %s, %s)'
    try:
        cursor.execute(sql, (paiming, name, lianjie))
        db.commit()
        print('数据插入完成！！')
    except:
        print('插入失败')
        db.rollback()
db.close()


# 写入到csv
import requests
from bs4 import BeautifulSoup
import csv
url = 'https://music.douban.com/chart'
html = requests.get(url=url).text
soup = BeautifulSoup(html, 'lxml')
ul = soup.find(attrs={'class': 'col5'})     # 找到存放排行榜音乐的ul标签
lis = ul.find_all(name='li')                # 获取每一首音乐对应的标签
with open('doubai.csv', 'a', newline='', encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerow(['排名', '歌名', '链接'])
for li in lis:
    paiming = li.find(name='span').string
    name = li.find(name='a', attrs={'href': 'javascript:;'}).string
    a = li.find(name='a', attrs={'class': 'face'})      # 获取存存放连接的a标签,再在a标签里获取连接
    if a != None:
        img = a.find(name='img')    # 获取连接的img标签
        lianjie = img.attrs['src']      # 获取到连接
    else:
        lianjie = '没有链接'
    print(paiming, name, lianjie)
    with open('doubai.csv', 'a', newline='', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow([paiming, name, lianjie])


# 写入到txt
import requests
from bs4 import BeautifulSoup
url = 'https://music.douban.com/chart'
html = requests.get(url=url).text
soup = BeautifulSoup(html, 'lxml')
ul = soup.find(attrs={'class': 'col5'})     # 找到存放排行榜音乐的ul标签
lis = ul.find_all(name='li')                # 获取每一首音乐对应的标签
for li in lis:
    paiming = li.find(name='span').string
    name = li.find(name='a', attrs={'href': 'javascript:;'}).string
    a = li.find(name='a', attrs={'class': 'face'})      # 获取存存放连接的a标签,再在a标签里获取连接
    if a != None:
        img = a.find(name='img')    # 获取连接的img标签
        lianjie = img.attrs['src']      # 获取到连接
    else:
        lianjie = '没有链接'
    print(paiming, name, lianjie)

    with open('dou_bai_music.txt', 'a', encoding='utf-8') as f:
        f.write(paiming+'\t'+name+'\t'+lianjie+'\n')
        f.close()













