import requests
from decimal import Decimal
from datetime import datetime


def currency_rates(kod):
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    if r.status_code == 200:
        contents = r.content.decode(encoding=r.encoding)
        date_content = contents[(contents.index('Date="')+6):(contents.index('" name'))]
        form_date = datetime.date(datetime.strptime(date_content, "%d.%m.%Y"))
        dict_course = {}
        for el in contents.split('<NumCode>')[1:]:
            course = Decimal(el[(el.index('<Value>') + 7):(el.index('</Value>'))].replace(",", "."))
            value = el[(el.index('<Nominal>') + 9):(el.index('</Nominal>'))]
            dict_course[el[(el.index('<CharCode>') + 10):(el.index('</CharCode>'))]] = course/int(value)

        answer = str(f'{dict_course.get(kod.upper())}  {form_date}')
        """
        Для ответа 'None' без даты при ошибке ввода кода валюты
         раскоментировать следующий блок, и закомментировать строку № 18:
         
        if dict is not None:
            answer = str(f'{dict.get(kod.upper())}  {form_date}')
        else:
            answer = str(dict)
        """
    else:
        answer = str("no connection to server")
    return print(answer)


currency_rates('USD')
currency_rates('eur')
