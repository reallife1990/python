import requests
from decimal import Decimal


def currency_rates(kod):
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    if r.status_code == 200:
        content = r.content.decode(encoding=r.encoding)
        dict_course = {}
        for el in content.split('<NumCode>')[1:]:
            course = Decimal(el[(el.index('<Value>') + 7):(el.index('</Value>'))].replace(",", "."))
            value = el[(el.index('<Nominal>') + 9):(el.index('</Nominal>'))]
            dict_course[el[(el.index('<CharCode>') + 10):(el.index('</CharCode>'))]] = course/int(value)
        return dict_course.get(kod.upper())
    else:
        return str("no connection to server")


print(currency_rates('eur'))
print(currency_rates('usd'))
