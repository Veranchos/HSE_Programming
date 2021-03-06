import urllib.request, re
import os
import datetime
from bs4 import BeautifulSoup
from pymystem3 import Mystem
import json


URL = 'https://nplus1.ru'   #источник текстов


def download_page(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.read()

    return page


def write_in_file(filename, text):
    f = open(filename, 'w+', encoding='UTF-8')
    f.write(text)
    f.close()


def get_links_from_daily_page(date_string):
    path = "/news/" + date_string
    daily_url = URL + path
    daily_news_page = download_page(daily_url)
    soup = BeautifulSoup(daily_news_page, features="lxml")

    all_anchor_nodes = soup.find(id="main").find_all('a', href=re.compile(path))

    all_links = list(set(map(lambda node: node.get('href'), all_anchor_nodes)))

    return all_links


def parse_article_page(article_path):
    article_page = download_page(URL + article_path)

    article_html = BeautifulSoup(article_page, features="lxml")

    paragraphs = article_html.find(class_="body").findChildren('p', recursive=False)

    author = None
    # Убрать из последнего параграфа <i>, потому что это может быть автор. Где-то автор не указан.
    if (len(paragraphs) > 0 and paragraphs[-1].i):
        author = paragraphs[-1].i.extract().text

    article_text = ' '.join([p.text for p in paragraphs])

    title = article_html.h1.text
    source = URL + article_path
    wordcount = len(article_text.split(' '))
    [date] = article_html.time.get_attribute_list('content')

    article_metadata = [article_path, author, date, URL, title, source, wordcount]

    return {
        'article_text': article_text,
        'article_metadata': article_metadata
    }


def daterange(start_date, end_date):
    array = []
    for n in range(int((end_date - start_date).days + 1)):
        array.append(start_date + datetime.timedelta(n))
    return array


def main():
    start_date = datetime.date(2017, 1, 1)
    end_date = datetime.date(2018, 12, 31)

    dates = daterange(start_date, end_date)
    metadatas = [['path', 'author', 'date', 'source', 'title', 'url', 'wordcount']]

    for date in dates:
        [year, month, day] = str(date).split('-')
        path = year + os.sep + month
        corpus_path = 'corpus_path' + os.sep + path
        markup_corpus_path = 'markup_corpus_path' + os.sep + path

        if not(os.path.exists(corpus_path)):
            os.makedirs(corpus_path)

        if not(os.path.exists(markup_corpus_path)):
            os.makedirs(markup_corpus_path)

        date_string = '/'.join([year, month, day])

        article_paths = get_links_from_daily_page(date_string)

        for article_path in article_paths:
            #парсим страницы
            data = parse_article_page(article_path)
            article_name = article_path.split('/')[-1]
            article_text = data['article_text']

            #mystem-обработка
            analyzed_text = Mystem().analyze(article_text)
            beautified_json = json.dumps(analyzed_text, indent=4, ensure_ascii=False)

            #записываем всё в файлы
            write_in_file(markup_corpus_path + os.sep + article_name + '.json', beautified_json)
            write_in_file(corpus_path + os.sep + article_name + '.txt', article_text)
            metadatas.append(data['article_metadata'])

    #собираем мета-дату
    write_in_file('metadata.csv', '\n'.join(['\t'.join([str(el) for el in metadata]) for metadata in metadatas]))

    return


if __name__ == '__main__':
    main()