#bijavix Q4-2020 - (you'll need to have a dir called rawBook in the working directory)
import requests #pip install requests
bookName = input("book name: ")
fExt = input("File Extension to save (Probably jpg): ")
unit = 1
page = 1
def newUrl(): 
    url = (f"https://example.com/book/{unit:02d}/{page}.jpg") #Only download what you are autorized to. I'm not responsible for any of your actions.
    return url #Change to your book url on the previous line. Use {unit} and {page} as variables and :0Xd to add X leading zeros if needed.
url = newUrl()
print(url)
r = requests.get(url)
print(r.status_code)
if(r.status_code != 200):
    print(f"Check your settings or if the webpage is up. HTTP Error: {print(r.status_code)}")
    exit()
while(True): 
    url = newUrl()
    print(f"Downloading: {url}")
    r = requests.get(url)
    print(r.status_code)
    if (r.status_code == 200):
        try:
            open(f'rawBook/{bookName}_{unit:02d}-{page:02d}.{fExt}', 'wb').write(r.content) #the :02d will add leading zeros to the number, change as needed.
        except FileNotFoundError:
            print("You need a folder called RawBook on your working direcory, please make it and try again.")
            exit()
        page = page+1
        unitCheck = 0
    else:
        print("no pages left, next unit.") #If you haven't set the unit parameter on the URL, you'll need to stop the script manually or it will run until your drive is full!
        unit = unit+1
        page = 1 #change to 0 if your book starts from page 0
        unitCheck = unitCheck+1
        if(unitCheck > 5):
            print("Done downloading!")
            exit()
