from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
import time
import json


def percent(part, whole):
    return 100 * float(part) / float(whole)


driver = webdriver.Chrome()

targetsFile = open('targets.txt', 'r')
targetLines = targetsFile.readlines()

with open('providers.json', 'r') as f:
    providers = json.load(f)

# setup counters for statistics
counterComplete = 0
counterFound = 0
for provider in providers:
    globals()[provider['name']] = 0

# Strips the newline character
for target in targetLines:
    if not target.lstrip().startswith('http'):
        target = "https://" + target
    try:
        driver.get(target)
    except WebDriverException:
        print("page down")
    counterComplete += 1
    time.sleep(1)
    for provider in providers:
        attribute = provider['attribute']
        value = provider['value']
        by = getattr(By, attribute.upper())

        try:
            element = driver.find_element(by, value)
            print(f"Found {target} uses: {provider['name']}")
            globals()[provider['name']] += 1
            counterFound += 1
        except (NoSuchElementException, WebDriverException):
            pass

driver.quit()
res_f = percent(counterFound, counterComplete)
print("################################\npages scanned / provider found: ", counterComplete, " / ", counterFound, " (", res_f, ")")
for provider in providers:
    res = percent(globals()[provider['name']], counterComplete)
    print(provider['name'], ": ", res, "% (", globals()[provider['name']], ")")
