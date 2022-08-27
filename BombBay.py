from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import wikipediaapi
import keyboard

input = input('ENTER WORD: ').lower()
rhymes = []
rhymeListLength = []
wiki_wiki = wikipediaapi.Wikipedia('en')

rhyme_zone = 'https://www.rhymezone.com'

# PATH was depicated
s = Service('C:\Program Files (x86)\chromedriver.exe')


o = webdriver.ChromeOptions()
# so that chrome doesnt pop up every time i run this
# o.add_argument("headless")
# removes warning messages for some reason id, not going to mess with it lol
o.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=s, options=o)

driver.get(rhyme_zone)

driver.find_element('xpath', "//select/option[@value='adv']").click()

search = driver.find_element('id', 'rzinput')
search.send_keys(input)
search.send_keys(Keys.RETURN)


get_list = driver.find_elements(
    'xpath', "//a[@aria-controls='rzadv_table']")
for listThing in get_list:
    rhymeListLength.append(listThing.text)

rhymeListLength = rhymeListLength[1:-1]


# makes array for every rhyming word of inputed word but looping until it gets through every page
# have to initaliase the elements each loop so it doesnt become 'stale' :(
for i in rhymeListLength:
    next = driver.find_element('xpath', "//a[@id='rzadv_table_next']")
    get_classes = driver.find_elements('xpath', "//a[@class='reslink']")
    for thing in get_classes:
        rhymes.append(thing.text.lower())
    try:
        next.click()

    except:
        pass

input.lower().split()


out1 = []
# thanks !!!!!!!
for string in rhymes:
    splitString = string.split(' ')
    inArray1 = False
    for sect in splitString:
        if sect in input:
            inArray1 = True

    if inArray1 == False:
        out1.append(string)

out2 = []

for j in range(len(out1)):
    page = wiki_wiki.page(out1[j])
    if page.exists() == True:
        out2.append('https://en.wikipedia.org/wiki/' + out1[j])


index = 0
rhymes = out2
o2 = webdriver.ChromeOptions()
o2.add_experimental_option('excludeSwitches', ['enable-logging'])
driver2 = webdriver.Chrome(service=s, options=o2)

if not rhymes:
    print('NO RHYMING WORDS IN WIKI!!!! :((((')
    exit()
driver2.get(rhymes[index])

print(out1)

while True:
    if keyboard.is_pressed("right arrow"):
        index = index + 1
        time.sleep(0.17)
        if index > len(rhymes) - 1:
            index = index - 1
        driver2.get(rhymes[index])
    if keyboard.is_pressed("left arrow"):
        index = index - 1
        time.sleep(0.17)
        if index < 0:
            index = 0
        driver2.get(rhymes[index])
