import requests
from bs4 import BeautifulSoup
import pandas

#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.google.co.in/search?q=Kellton Tech Inc",headers=headers)

content = response.content
soup = BeautifulSoup(content,"html.parser")

rating_data_block = soup.find_all("div",attrs={"class": "Ob2kfd"})

print(rating_data_block)
