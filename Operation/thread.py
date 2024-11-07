import concurrent
from concurrent.futures import ThreadPoolExecutor

import requests

# with ThreadPoolExecutor(max_workers =1 )as executor:
#     future = executor.submit(pow,2,10)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
def request_douban(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f'!!爬取了{url},数据量：{len(response.content)}')
            return response.content
    except requests.RequestException:
        return None

def done(fn):
    if fn.done():
        print("调用完成")

if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start=' + str(i + 25) + '&filter=' for i in range(0,10)]
    task = []


    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for url in urls:
            future = executor.submit(request_douban, url)
            future.add_done_callback(done)
            task.append(future)

    for future in task:
        try:
            data = future.result()
            print(data)
        except Exception as ex:
            print('产生异常。。。')


