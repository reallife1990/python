d_ip = {}
with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    length = len(f.readlines())
    f.seek(0)
    for i in range(0, length):
        data = f.readline()
        ip = data.split(' ')[0]
        if d_ip.get(ip) is None:
            d_ip[ip] = 1
        else:
            d_ip[ip] = (d_ip.get(ip)+1)


for k, v in d_ip.items():
    if v == max(d_ip.values()):
        print(f"ip спамера: {k},количество запросов: {v}")
        break
