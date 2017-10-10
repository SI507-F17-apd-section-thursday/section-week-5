import requests
from bs4 import BeautifulSoup

try:
    # with open("nyt_today.html", "r") as f:
    #     html = f.read()

    html = open("nyt_today.html", "r").read()

except:
    response = requests.get("http://www.nytimes.com/pages/todayspaper/index.html")
    html = response.text

    # or requests.get("http://www.nytimes.com/pages/todayspaper/index.html").text

    with open("nyt_today.html", 'w') as f:
        f.write(html)

# soup object
soup = BeautifulSoup(html, "html.parser")

# specific div
div = soup.find("div", {"class": "aColumn"})

# all stories in that specific div
stories = div.find_all("div", {"class": "story"})
# print(type(stories))

stories_data = {}
for story in stories:
    # extract
    title = story.find("h3").text
    url = story.find('h3').a['href']

    file_name = title.split()[0] + '.html'

    try:
        # with open("nyt_today.html", "r") as f:
        #     html = f.read()

        html = open(file_name, "r").read()

    except:
        response = requests.get("http://www.nytimes.com/pages/todayspaper/index.html")
        html = response.text

        # or requests.get("http://www.nytimes.com/pages/todayspaper/index.html").text

        with open(file_name, 'w') as f:
            f.write(html)

    sub_page_soup = BeautifulSoup(html, 'html.parser')
    

    # print(html)

    authors = story.find("h6").text[4:]
    authors = authors.replace(' and ', ', ')
    authors = authors.split(', ')
    authors[-1] = authors[-1].strip()
    # print(authors)

    summary = story.find('p', {"class": "summary"}).text

    thumbnail = story.find('img')['src']
    # print(thumbnail['src'])
    # print(thumbnail.get('src', 'some default value'))

    stories_data[title] = {
        'title': title,
        'authors': authors,
        'summary': summary,
        'thumbnail': thumbnail
    }


    # Article(title, authors, summary, thumbnail)

    # print(story_dict)
    # stories_data.append(story_dict)

# import json
# print(json.dumps(stories_data, indent=4))
