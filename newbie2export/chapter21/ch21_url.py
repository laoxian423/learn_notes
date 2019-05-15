# LOOK 爬虫-普通网页
import urllib.request

url = 'http://q.stock.sohu.com/cn/600992/cjmx.shtml'
req = urllib.request.Request(url)
# req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1')


with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode('gbk')
    print(htmlstr)
    with open('f:\\temp\\1.txt', 'w+') as f:
        f.write(htmlstr)


