import urllib.request, re
import lxml
import os
from lxml import html
import datetime
from bs4 import BeautifulSoup
from dateutil import relativedelta

URL = 'https://nplus1.ru'

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

    print(daily_url)
    daily_news_page = download_page(daily_url)
    soup = BeautifulSoup(daily_news_page, features="lxml")

    all_anchor_nodes = soup.find(id="main").find_all('a', href=re.compile(path))

    all_links = list(set(map(lambda node: node.get('href'), all_anchor_nodes))) # сет можно убрать, ибо набор ссылок в ноде main не повторяется

    return all_links



def parse_article_page(article_path):
    article_page = download_page(URL + article_path)

    article_html = BeautifulSoup(article_page, features="lxml")

    paragraphs = article_html.find(class_="body").findAll('p', attrs={'class': ''})

    author = None
    # Убрать из последнего параграфа i, потому что это может быть автор
    if (paragraphs[-1].i):
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
    for n in range(int ((end_date - start_date).days + 1)):
        array.append(start_date + datetime.timedelta(n))
    return array

def do_staff():
    start_date = datetime.date(2015, 7, 1)
    end_date = datetime.date(2015, 7, 1)

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
            # article_path_set = set()
            # if article_path in article_path_set:
            #     continue
            # article_path_set.add(article_path)
            data = parse_article_page(article_path)
            article_name = article_path.split('/')[-1]
            article_text = data['article_text']



            # тут получать отмайстемленный текст и сохранять его так же, как и текст статьи, но в markup_corpus_path


            write_in_file(corpus_path + os.sep + article_name + '.txt', article_text)
            metadatas.append(data['article_metadata'])

    write_in_file('metadata.csv', '\n'.join([', '.join([str(el) for el in metadata]) for metadata in metadatas]))



do_staff()