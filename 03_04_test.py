import requests
from decimal import Decimal
from datetime import datetime
"""
r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")

if r.status_code ==200:
    print(r.content.decode(encoding=r.encoding))
    content = r.content.decode(encoding=r.encoding)
    lst = []
    for el in content.split('<NumCode>')[1:]:

        print(el[(el.index('<CharCode>')+10):(el.index('</CharCode>'))])
        a = Decimal(el[(el.index('<Value>') + 7):(el.index('</Value>'))].replace(",","."))
        print(a)
        print(el[(el.index('<Nominal>') + 9):(el.index('</Nominal>'))])
        val = el[(el.index('<Nominal>') + 9):(el.index('</Nominal>'))]
        name = el[(el.index('<Name>') + 6):(el.index('</Name>'))]
        print(el)
        print(f' за один {name} - {a/int(val)} российских рублей')
"""
def currency_rates(kod):
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")

    if r.status_code == 200:
        print(r.content.decode(encoding=r.encoding))
        contents = r.content.decode(encoding=r.encoding)
        date = contents[(contents.index('Date="')+6):(contents.index('" name'))]
        print(date)
        print(type(date))
        #am = datetime.strptime(date, "%d.%m.%Y")
        am = datetime.date(datetime.strptime(date, "%d.%m.%Y"))
        dict = {}
        for el in contents.split('<NumCode>')[1:]:

            # if kod == el[(el.index('<CharCode>') + 10):(el.index('</CharCode>'))]:
                #print(el[(el.index('<CharCode>') + 10):(el.index('</CharCode>'))])
            a = Decimal(el[(el.index('<Value>') + 7):(el.index('</Value>'))].replace(",", "."))
                #print(a)
                #print(el[(el.index('<Nominal>') + 9):(el.index('</Nominal>'))])
            val = el[(el.index('<Nominal>') + 9):(el.index('</Nominal>'))]
            name = el[(el.index('<Name>') + 6):(el.index('</Name>'))]
            dict[el[(el.index('<CharCode>') + 10):(el.index('</CharCode>'))]] = a/int(val)
                #print(el)
            # print(f'За один {name} - {a / int(val)} российских рублей')

        answer = str(f'{dict.get(kod)}  {am}')

        if dict is not None:
            answer = str(f'{dict.get(kod)}  {am}')
        else:
            answer = str(dict)

        return print(answer)

currency_rates('USD')
#currency_rates('EUR')
currency_rates('USD')
#print(currency_rates('eur'))