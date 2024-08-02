import webbrowser
import os
import json
import time

def user_options():
     user_input = input('>>> Type \"1\" if you want to replace links. Type  \"2\" if you want to open links. Type  \"3\" if you want to replace links and open them: ')
     return user_input

def user_links(): 
    
    links_list = []

    for name in ['Link to google doc: ','Link to traslation - web: ','Link to tranlation - local:']:
        user_input = input(f'{name}')
        links_list.append(user_input)
    
    return links_list

def windows_arise(some_links):
        os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/firefox")
        time.sleep(0.5)
        for url in some_links:
            
            if url.startswith('https'):
                webbrowser.open(url)
            else:
                os.startfile(url)

get_option = user_options()

if get_option == str(1):    
    get_links = user_links()
    with open('links.json', 'w') as file:
         json.dump(get_links, file)
elif get_option == str(2):
    with open('links.json', 'r') as file:
         get_links = json.load(file)
    windows_arise(get_links)
else: 
    get_links = user_links()
    with open('links.json', 'w') as file:
         json.dump(get_links, file)

    with open('links.json', 'r') as file:
         get_links = json.load(file)
    windows_arise(get_links)