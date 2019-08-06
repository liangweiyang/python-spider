import requests
from bs4 import BeautifulSoup

# response请求页面的响应，all_url_lis用于存放所有页面的utl，all_title_list用于存放所有页面的title，
# i用来显示当前爬取到第几个页面


def parse(response, all_url_list, all_title_list, i):
    html = response.content  # 先获取二进制形式的内容，下面再进行转换，否则会出现中文乱码
    html = str(html, encoding='utf-8')
    soup = BeautifulSoup(html, 'lxml')  # 利用Beautifulsoup解析库
    f = open('title_and_url.txt', 'a', encoding='utf-8')    # 打开文件，存储所有页面的title和url

    # 获取正文
    # content = soup.find(name='div', attrs={'class': 'main_article'})
    # p_list = content.find_all(name='p')
    # for p in p_list:
    #     print(p.string)

    flag = 0    # 用来标志当前页面的url有多少已经存储过了，后面可以作为结束循环的条件

    # 获取下方社会新闻
    Sociology_list = soup.find_all(name='div', attrs={'class': 'r'})
    sociology_a_list = Sociology_list[0].find_all(name='a')
    for a in sociology_a_list:
        sociology_title = a.string
        sociology_url = a.attrs.get('href')
        # print(sociology_title, sociology_url)
        # 判断列表中是否已经存在这个页面的url或title，实现去重
        if sociology_url not in all_url_list and sociology_title not in all_title_list:
            all_url_list.append(sociology_url)
            all_title_list.append(sociology_title)
            f.write(sociology_title + '   ' + sociology_url + '\n')
        else:
            flag += 1

    # 获取排行榜
    Ranking_list = soup.find_all(name='ul', attrs={'class': 'tt', 'id': 'tt'})
    rank_a_list = Ranking_list[0].find_all(name='a')
    for a in rank_a_list:
        rank_title = a.string
        rank_url = a.attrs.get('href')
        # print(rank_title, rank_url)
        if rank_url not in all_url_list and rank_title not in all_title_list:
            all_url_list.append(rank_url)
            all_title_list.append(rank_title)
            f.write(rank_title + '   ' + rank_url + '\n')
        else:
            flag += 1

    # 热点推荐
    hot_list = soup.find_all(name='ul', attrs={'class': 'ducheng_list'})
    hot_a_list = hot_list[0].find_all(name='a')
    for a in hot_a_list:
        hot_title = a.string
        hot_url = a.attrs.get('href')
        # print(hot_title, hot_url)
        if hot_url not in all_url_list and hot_title not in all_title_list:
            all_url_list.append(hot_url)
            all_title_list.append(hot_title)
            f.write(hot_title + '   ' + hot_url + '\n')
        else:
            flag += 1

    # 热点视频
    video_list = soup.find_all(name='ul', attrs={'class': 'tuku_list'})
    video_a_list = video_list[0].find_all(name='a')
    for a in video_a_list:
        video_title = a.string
        video_url = a.attrs.get('href')
        # print(video_title, video_url)
        if video_url not in all_url_list and video_title not in all_title_list:
            all_url_list.append(video_url)
            all_title_list.append(video_title)
            f.write(video_title + '   ' + video_url + '\n')
        else:
            flag += 1

    # 要闻
    yaowen_list = soup.find_all(name='ul', attrs={'class': 'yaowen_list'})
    yaowen_a_list = yaowen_list[0].find_all(name='a')
    for a in yaowen_a_list:
        yaowen_title = a.string
        yaowen_url = a.attrs.get('href')
        # print(yaowen_title, yaowen_url)
        if yaowen_url not in all_url_list and yaowen_title not in all_title_list:
            all_url_list.append(yaowen_url)
            all_title_list.append(yaowen_title)
            f.write(yaowen_title + '   ' + yaowen_url + '\n')
        else:
            flag += 1

    f.close()
    print('第{0}个页面存储完成'.format(i), flag)
    # 一个页面中有44条新闻。如果改页面中的所有url都已经被存储过了，则可以大致认为已经获取到了所有的url
    # 实际少了十三条
    if flag == 44:
        return flag
    else:
        return


if __name__ == '__main__':
    all_url_list = []
    all_title_list = []
    url = 'http://www.cymodel.net/deaafc/13143.html'
    all_url_list.append(url)
    i = 0
    while (True):
        # 如果想要把all_url_list里面的每个页面的url全部爬取一遍，则可以用这个条件作为循环结束
        # 把下面的内嵌if和函数里面的if else注释掉即可
        if( i < len(all_url_list) ):
            response = requests.get(url=all_url_list[i])
            flag = parse(response, all_url_list, all_title_list, i+1)
            i += 1
            if flag == 44:
                print('已爬取大部分的url！！！！！')
                break
        else:
            print('已爬取到所有的url！！！！！')
            break
