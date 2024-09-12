def is_real_domen(mail:str) -> bool:
    domens = [".com", ".ru", ".kz", ".uk"]
    for domen in domens:
        if mail.find(domen) != -1:
            return True
    return False

def send_email(message: str, recipient: str, sender: str = "me@gmail.com"):
    if not is_real_domen(recipient) and not is_real_domen(sender):
        raise Exception(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if recipient.find("@") == -1 or sender.find("@") == -1:
        raise Exception(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if recipient == sender:
        raise Exception("Нельзя отправить письмо самому себе!")
    if sender == "me@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

data = [
    ['Это сообщение для проверки связи', 'vasyok1337@gmail.com'],
    ['Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com'],
    ['Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk'],
    ['Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru']
]

for query in data:
    try:
        send_email(*query)
    except Exception as e:
        print(e)
