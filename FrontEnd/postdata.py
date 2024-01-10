
import requests

from jokesExtract import final_result
jokes=final_result



for i in range(len(jokes)):
    r=requests.post(data={"desc":jokes[i]},url="http://localhost:8000/create-joke/")