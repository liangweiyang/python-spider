import threading
import requests
import json
import queue
import time

url = "http://www.hetianlab.com/knowInfo!queryCouExp.action"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"}


class hetian_spider(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            page_num = self.queue.get_nowait()
            self.spider(page_num)

    def spider(self, pageNum):
        response = requests.post(url=url, headers=header, data={"pageNum": pageNum})
        data = json.loads(response.text)
        long = len(data['message'])
        print("****************************************输出第{0}页信息*********************************".format(pageNum))
        for j in range(0, long):
            print(data['message'][j]['name'])


def main():
    q = queue.Queue()
    for i in range(1, 10):
        q.put(i)
    threads = []
    # 定义线程数量
    thread_counter = 2
    for i in range(thread_counter):
        t = hetian_spider(q)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("5线程爬取用时{0}秒".format(time.time() - start_time))