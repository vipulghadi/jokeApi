
# import requests


from bs4 import BeautifulSoup

jokes=[]

#method to adextract jokes
def extract_blackquote_content(url):
    # Make a request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <blackquote> tags and extract their content
        blackquote_tags = soup.find_all('blockquote')
        for tag in blackquote_tags:
            # Print or process the content as needed
            jokes.append(tag.text)

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Replace 'your_webpage_url' with the actual URL of the webpage
webpage_url = 'https://befunky.in/hindi-jokes/'
extract_blackquote_content(webpage_url)
import re

def remove_escape_numbers_letters(input_string):
    # Remove escape characters
    cleaned_string = re.sub(r'\\.', '', input_string)

    # Remove numbers and English alphabets
    cleaned_string = re.sub(r'[0-9a-zA-Z]', '', cleaned_string)

    return cleaned_string

# Example usage:
new_jokes=[]
for j in jokes:
    new=remove_escape_numbers_letters(j)
   
    new_jokes.append(new)

final_result=[]
for j in new_jokes:
    new_str=[]
    for alpha in j:
         if alpha!='\n':new_str.append(alpha)
    new_str="".join(new_str)
    final_result.append(new_str)
    