from bs4 import BeautifulSoup
import urllib.request
import re
import random

message = "rip "
name = '@CNN‏Politics'
url = 'https://twitter.com/CNBC/status/861601079313739776'
theurl = urllib.request.urlopen(url)
soup = BeautifulSoup(theurl, "html.parser")


def get_id(url):
    # gets stream-item-tweet id
    theurl = urllib.request.urlopen(url)
    soup = BeautifulSoup(theurl, "html.parser")
    stream_item = soup.find_all('li', 'stream-item')
    for id in stream_item:
        num = re.sub(r'stream-item-tweet-', "", str(id.get('id')))
        return num


def get_user(url):
    su = re.sub(r'https://twitter.com/', "", url)
    name = re.sub(r'/status/.*', '', su)  # Remove everything after /status/
    theid = re.sub(r'.*status/', '', url)  # Remove everything before status/
    name = '@' + name
    return name


def tweet_clean(url, message):
    su = re.sub(r'https://twitter.com/', "", url)
    name = re.sub(r'/status/.*', '', su)  # Remove everything after /status/
    theid = re.sub(r'.*status/', '', url)  # Remove everything before status/
    name = '@' + name

    print(url)
    print(name)
    print(theid)

    # api.update_status(message + name, theid)


def get_text(url):
    theurl = urllib.request.urlopen(url)
    soup = BeautifulSoup(theurl, "html.parser")
    tweet_text = soup.find_all('p', 'js-tweet-text')
    for text in tweet_text:
        # print(text.text)
        print()

        return str(text.text)


def pick():
    url = get_url()
    list = []
    theurl = urllib.request.urlopen(url)
    soup = BeautifulSoup(theurl, "html.parser")
    links = soup.find_all("a")
    for link in links:
        line = link.get('href')
        if "status/" in str(line):
            list.append(line)
            max = len(list)
            # print(line)

    max = max - 1
    ra = random.randint(0, max)
    return list[ra]


def reply_count(url):
    urll = "https://twitter.com" + url
    theurl = urllib.request.urlopen(urll)
    soup = BeautifulSoup(theurl, "html.parser")
    href = []
    clean = []
    all = soup.find_all("a")

    for moo in all:
        href.append(moo.get('href'))

    for links in href:
        if 'status' in str(links):
            if 'http' not in str(links):
                if url not in str(links):
                    clean.append(links)

    for links in clean:
        print(links)
    count = len(clean)
    # count = count - 1
    print(count)

    return count


def get_time(url):
    theurl = urllib.request.urlopen(url)
    soup = BeautifulSoup(theurl, "html.parser")
    timestamp = soup.find_all('a', 'tweet-timestamp')
    for time in timestamp:
        # print("timestamp: " + time.get("title"))
        print()

    return time.get("title")


def get_url():
    list = []
    list.append("https://twitter.com/CNN")  # = 0
    list.append("https://twitter.com/CNNPolitics")
    list.append("https://twitter.com/CNNMoney")
    list.append("https://twitter.com/washingtonpost")
    list.append("https://twitter.com/WSJ")
    list.append("https://twitter.com/AP")
    list.append("https://twitter.com/CNBC")
    list.append("https://twitter.com/guardian")
    list.append("https://twitter.com/theintercept")
    list.append("https://twitter.com/nytimes")  # = 9
    list.append("https://twitter.com/qz")
    list.append("https://twitter.com/TheNextWeb")
    list.append("https://twitter.com/FoxNews")
    list.append("https://twitter.com/inquirerdotnet")
    list.append("https://twitter.com/politico")
    list.append("https://twitter.com/CBSNews")  # = 15
    list.append("https://twitter.com/ABC")

    max = len(list)
    max = max - 1
    ra = random.randint(0, max)

    return list[ra]





testUrl= "https://twitter.com/DEAcampaign/status/1199751061474553856"

print(get_id(testUrl))
print(get_text(testUrl))
print(get_time(testUrl))
print(get_user(testUrl))
