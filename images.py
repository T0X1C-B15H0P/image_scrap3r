from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def scrap():
    search = input("Enter what you want to search for: ")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()
    print("Now searchin for " + search + "and saving it in " + dir_name)
    try:
        r = requests.get("https://www.bing.com/images/search", params=params)

        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)

        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.findAll("a", {"class": "thumb"})

        for images in links:
            try:
                img_obj = requests.get(images.attrs["href"])
                title = images.attrs["href"].split("/")[-1]
                try:
                    img = Image.open(BytesIO(img_obj.content))
                    print("Getting", title)
                    img.save("./" + dir_name + "/" + title, img.format)
                except:
                    print("Could not save image!!!! Moving on to the next \n")
            except:
                print("Could not request image")

        scrap()
    except:
        print("Could not connect this time. Please check your connection and try again")


print("\n===============================================================")
print("STARTING TOXIC IMAGE SCRAPPER")
print("Searches are made through bing.com".capitalize())
print("===============================================================\n\n")
scrap()
