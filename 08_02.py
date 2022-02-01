import re
with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
    for line in logs.readlines():
        pattern = re.compile(r'(?P<r_ip>^\d{1,3}(?:\.\d{1,3}){3})'
                             r'.{6}(?P<r_date>\d{2}/\w{3}/\d{4}(?:\:\d{2}){3}\s.{5})'
                             r'.{3}(?P<r_type>\w+)\s'
                             r'(?P<r_resours>(?:/\w+)+)'
                             r'.{11}(?P<r_code>\d{3})\s'
                             r'(?P<r_size>\d{1,4})\s'
                             )
        for el in pattern.finditer(line):
            temp_dictory = el.groupdict()
            print(list(temp_dictory.values()))
