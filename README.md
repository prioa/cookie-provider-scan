
# Cookie Provider Bulk Scaner

The Python Selenium script checks a list of URLs for their cookie consent provider by automating browser actions, extracting data from web pages, and storing the provider names in a list. The list is then printed to the console.




## Add custom Providers

Simply add an entry in the providers.json file. Also feel free to send a Pull Request to make the provider list bigger!

```json
    {
       "name": "DISPLAY NAME",
       "attribute": "id OR class",
       "value": "id OR classname"
    },
```
    
## Sample Output



```bash
  pages scanned / provider found:  148  /  46  ( 31.08108108108108 )
  OneTrust :  6.756756756756757 % ( 10 )
  Didomi :  1.3513513513513513 % ( 2 )
  CookieYes :  0.0 % ( 0 )
  Osano :  0.0 % ( 0 )
  Quantcast :  0.0 % ( 0 )
  SecurePrivacy :  0.0 % ( 0 )
  CookieBot :  4.72972972972973 % ( 7 )
  TrustArc :  0.0 % ( 0 )
  usercentrics :  6.081081081081081 % ( 9 )
  consentmanager :  2.027027027027027 % ( 3 )
  React Consent :  0.6756756756756757 % ( 1 )
  Cookie First :  0.0 % ( 0 )
  Cookie Notice & Compliance for GDPR / CCPA (WP) :  3.3783783783783785 % ( 5 )
  Cookiebar extension for Contao Open Source CMS :  2.027027027027027 % ( 3 )
  Borlabs Cookies :  2.7027027027027026 % ( 4 )
  DP Cookie Consent (TYPO3) :  0.6756756756756757 % ( 1 )
  Complianz - GDPR/CCPA Cookie Consent (WP) :  0.6756756756756757 % ( 1 )
```
