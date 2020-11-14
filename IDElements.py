

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from PetangoScrape import pet_links
headings = []
values = []
ShelterInfo = []
ShelterInfoWebsite = []
ShelterInfoEmail = []
ShelterInfoPhone = []
ShelterInfoAddress = []
PetName = []
Breed = []
Age = []
Color = []
SpayedNeutered = []
Size = []
Declawed = []
AdoptionDate = []
ShelterNameTest =[]
PetID = []
DateAdded = []
#there are options to use a cached html while I was working on identifying the elements
# to access sites, change url list to pet_links (break out as needed) and change if false to true.  false looks to the html file
#url_list = (pet_links[1], pet_links[30], pet_links[40])
#url_list = ("Petango.html", "Petango.html", "Petango.html")
#for link in url_list:
for link in pet_links:
    page_source = None
    if True:
        #pet page = link should populate links from above, hard code link was for 1 detail page, =to hemtl was for cached site
        PetPage = link
        #PetPage = 'https://www.petango.com/Adopt/Dog-Terrier-American-Pit-Bull-45569732'
        #PetPage = Petango.html
        PetDriver = webdriver.Chrome(executable_path='/Users/paulcarson/Downloads/chromedriver')
        PetDriver.implicitly_wait(30)
        PetDriver.get(link)
        page_source = PetDriver.page_source
        PetDriver.close()
    else:
        with open("Petango.html",'r') as f:
            page_source = f.read()
    PetSoup = BeautifulSoup(page_source, 'html.parser')

    #get the details about the shelter and add to lists
    ShelterInfo.append(PetSoup.find('div', class_ = "DNNModuleContent ModPethealthPetangoDnnModulesShelterShortInfoC").find('h4').text)

    ShelterInfoParagraphs = PetSoup.find('div', class_ = "DNNModuleContent ModPethealthPetangoDnnModulesShelterShortInfoC").find_all('p')
    First_Paragraph = ShelterInfoParagraphs[0]
    if "Website" not in First_Paragraph.text:
        raise AssertionError("first paragraph is not about site")
    ShelterInfoWebsite.append(First_Paragraph.find('a').text)

    Second_Paragraph = ShelterInfoParagraphs[1]
    ShelterInfoEmail.append(Second_Paragraph.find('a')['href'])

    Third_Paragraph = ShelterInfoParagraphs[2]
    ShelterInfoPhone.append(Third_Paragraph.find('span').text)

    Fourth_Paragraph = ShelterInfoParagraphs[3]
    ShelterInfoAddress.append(Fourth_Paragraph.find('span').text)

    #get the details about the pet
    if PetSoup.select_one("[data-bind='text: name']") is None:
        PetName.append('None')
    else:
        PetName.append(PetSoup.select_one("[data-bind='text: name']").text)
    if PetSoup.select_one("[data-bind='text: id']") is None:
        PetID.append('None')
    else:
        PetID.append(PetSoup.select_one("[data-bind='text: id']").text)
    if PetSoup.select_one("[data-bind='text: color']") is None:
        Color.append('None')
    else:
        Color.append(PetSoup.select_one("[data-bind='text: color']").text)
    if PetSoup.select_one("[data-bind='text: breed']") is None:
        Breed.append('None')
    else:
        Breed.append(PetSoup.select_one("[data-bind='text: breed']").text)
    if PetSoup.select_one("[data-bind='text: age']") is None:
        Age.append('None')
    else:
        Age.append(PetSoup.select_one("[data-bind='text: age']").text)
    if PetSoup.select_one("[data-bind='text: spayedNeutered']") is None:
        SpayedNeutered.append('None')
    else:
        SpayedNeutered.append(PetSoup.select_one("[data-bind='text: spayedNeutered']").text)
    if PetSoup.select_one("[data-bind='text: size']") is None:
        Size.append('None')
    else:
        Size.append(PetSoup.select_one("[data-bind='text: size']").text)
    if PetSoup.select_one("[data-bind='visible: declawedVisible']") is None:
        Declawed.append('None')
    else:
        Declawed.append(PetSoup.select_one("[data-bind='visible: declawedVisible']").text)
    if PetSoup.select_one("[data-bind='text: visible: adoptionDateVisible']") is None:
        AdoptionDate.append('None')
    else:
        AdoptionDate.append(PetSoup.select_one("[data-bind='text: color']").text)
    DateAdded.append(pd.to_datetime('today').date())


CombinedShelterPetDF = pd.DataFrame(
    {'PetName': PetName,
     'PetID': PetID,
     'Breed': Breed,
     'Age': Age,
     'Color': Color,
     'Spayed/Neutered': SpayedNeutered,
     'Size': Size,
     'Declawed': Declawed,
     'Adoption Date': AdoptionDate,
     'Shelter': ShelterInfo,
      'Shelter Website': ShelterInfoWebsite,
      'Shelter Email': ShelterInfoEmail,
      'Shelter Phone Number': ShelterInfoPhone,
      'Shelter Address': ShelterInfoAddress,
     'Date Added': DateAdded
    })

# eppend to a csv.  will eventually migrate to a better process, this is mvp1

with open('/Users/paulcarson/Documents/DogData.csv', 'a') as f:
    CombinedShelterPetDF.to_csv(f, header=False)














