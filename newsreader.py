from win32com.client import Dispatch
import requests
import json
def newsreading(string):

    speak =Dispatch("SAPI.SpVoice")

    speak.Speak(string)

if __name__ == '__main__':
    news=requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e96b3ad517e94fc8b8190c57a3f19bc8").text

    # print(url.text)
    news_dict=json.loads(news)
    print(news_dict)
    arts=news_dict["articles"]
    newsreading("News For today")
    for articles in arts:
        print(articles["title"])
        newsreading(articles["title"])
        print(articles["description"])
        newsreading(articles["description"])
        newsreading("Next News of today")

    newsreading("Thanks for listining")

