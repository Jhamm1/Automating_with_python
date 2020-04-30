# Automating with python

This repo provides examples of using Python for Automation. Any repetitive online task can be optimized with a Python script.

## Dependencies

`pip3 install beautifulsoup4`

`pip3 install lxml`

`pip3 install requests`

`pip3 install selenium`

`pip install -U python-dotenv`

### API automated tests

`cd API_tests` navigate to the API test sub-dir

`python3 apiCall.py`

`python3 apiKey.py`

### Automate web browsing

`cd automate_web_browsing` 

`python3 dragAndDrop.py`

`python3 googleEarthBrowse.py`

`python3 webBrowse.py`

### Execute cmd

`cd execute_cmds`

`python3 example.py`

`python3 script.py`

### fileIO

`cd fileIO`

`python3 fileIO.py`

### Web scraping

`cd web_scraping`

`python3 scrapePages.py`

`python3 scrape.py`

### Issues and considerations

**Why to use Wait functions**

- Many websites use asynchronous techniques to load content
- Technique creates a problem when Selenium tries to locate an element that isn't loaded
- Avoid exceptions in scripts

**Explicit wait functions -** will wait until a condition is satisfied

**Implicit wait functions -** pull DOM for a certain amount of time, until the element becomes available

`python3 googleEarthBrowse.py` > example of explicit wait



