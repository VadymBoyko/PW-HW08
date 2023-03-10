from models import Author, Quote


def beatify_result(quotes):
    result = '*****\n'
    for i in quotes:
        result += f'Author: {i.author.fullname}\nQuote: {i.quote}\nTags:{i.tags}\n*****\n'
    return result


def find_quotes_by_author(author_name):
    auth = Author.objects(fullname=author_name)
    if auth.count() == 0:
        return f'Author {author_name} was not found'
    return beatify_result(Quote.objects(author=auth[0]))


def find_quotes_by_tag(tag_name):
    quotes_result = Quote.objects(tags__in=tag_name.split(','))
    return beatify_result(quotes_result)


def find_quotes(searchstring):
    param, value = searchstring.split(':')
    if param == 'name':
        return find_quotes_by_author(value)
    elif param == 'tag':
        return find_quotes_by_tag(value)
    else:
        return 'Search string should start with "name:" or "tag:" only'


if __name__ == '__main__':
    while True:
        input_str = input('Input search mask or exit: ')
        if input_str == 'exit':
            break
        else:
            print(find_quotes(input_str))
