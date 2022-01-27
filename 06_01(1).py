import requests
r = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")

contents = r.content.decode(encoding=r.encoding).split('\n')
length = len(r.content.decode(encoding=r.encoding).splitlines())
result = []
for i in range(0, length):
    data = contents[i]
    elem_t = (data.split(' ')[0], data.split(' ')[5][1:], data.split(' ')[6])
    result.append(elem_t)

print(result)
