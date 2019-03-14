
import requests
news_dict = {'new_source': {1: {'BBC':'bbc-news'}, 2: {'CNN':'cnn'}, 3: {'News24':'news24'}, 4: {'Fox News':'fox'}}}
print('Here is a list of News Sources you can choose from!')
def news_api(d):
    
    for k,v in d.items():        
     if isinstance(v, dict):
         news_api(v)
     else:            
          print(k)

news_api(news_dict) 
user_Choice = input("Enter your prefered News Source: ")
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=71559e9f96b449998b48d3fba79eaecc')
response = requests.get(url)
print (response.json())







