import re


def email_parse(e_mail):
    msg = f'wrong e-mail {e_mail}'
    e_mail = e_mail.lower()
    pattern = re.compile(r'(?P<username>^[a-z,0-9,_]+)[@](?P<domain>\w+\.[a-z]{2,4}$)')
    if pattern.search(e_mail) is None:
        raise ValueError(msg)
    else:
        result = pattern.finditer(e_mail)
        for el in result:
            print(el.groupdict())


email_parse(input('input e-mail'))
