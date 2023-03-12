
# Cookie Provider Bulk Scaner

The Python Selenium script checks a list of URLs for their cookie consent provider by automating browser actions, extracting data from web pages, and storing the provider names in a list. The list is then printed to the 
console.




## Add custom Providers

Simply add an entry in the providers.json file. Also feel free to send a Pull Request to make the provider list bigger!

```json
    {
       "name": "DISPLAY NAME",
       "attribute": "id OR class",
       "value": "id OR classname"
    },
```
    
