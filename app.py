import requests
news_Source = ["BBC", "CNN", "News24", "Fox News"]
for x in news_Source:
    print(x)


def we(e):
    news_dict = {'new_source': {1: {'BBC': 'bbc-news'}, 2: {'CNN': 'cnn'}, 3:     {'News24': 'news24'}, 4:
                                {'Fox News': 'fox'}}}
    for k, v in news_dict.items():
        if type(v) == dict:
            for k, v in v.items():
                for k, v in v.items():
                    if k == e:
                        return v


user_choice = we(input("Please Enter Your Prefered News Source: "))
url = ('https://newsapi.org/v2/top-headlines?'
       f'sources={user_choice}&'
       'apiKey=71559e9f96b449998b48d3fba79eaecc')
response = requests.get(url)
print(response.json())
