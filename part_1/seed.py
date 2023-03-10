import json

from models import Author, Quote

authors = Author.objects()
quotes = Quote.objects()


def get_author(fullname):
    result = Author.objects(fullname=fullname)
    if result.count() == 0:
        return None
    return result[0]


def get_quote(text):
    result = Quote.objects(quote=text)
    if result.count() == 0:
        return None
    return result[0]


def load_authors():
    with open(r".\data\authors.json", "r", encoding="utf-8") as f:
        data = f.read()

    js = json.loads(data)

    for i in js:
        if not get_author(i['fullname']):  # зроблено для того, аби не задвоювати авторів при повторному запуску
            Author(fullname=i['fullname'], born_date=i['born_date'], born_location=i['born_location'], \
                   description=i['description']).save()


def load_quotes():
    with open(r".\data\qoutes.json", "r", encoding="utf-8") as f:
        data = f.read()

    js = json.loads(data)

    for i in js:
        if not get_quote((i['quote'])):  # зроблено для того, аби не задвоювати цитати при повторному запуску
            author = get_author(i['author'])
            Quote(quote=i['quote'], author=author, tags=i['tags']).save()


if __name__ == '__main__':
    load_authors()
    load_quotes()
