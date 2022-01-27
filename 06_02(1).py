import requests

d_ip = {}
r = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
contents = r.content.decode(encoding=r.encoding).split('\n')
length = len(r.content.decode(encoding=r.encoding).splitlines())

for i in range(0, length):
    ip = contents[i].split(' ')[0]
    if d_ip.get(ip) is None:
        d_ip[ip] = 1
    else:
        d_ip[ip] = (d_ip.get(ip) + 1)

for k, v in d_ip.items():
    if v == max(d_ip.values()):
        print(f"ip спамера: {k},количество запросов: {v}")
        break
