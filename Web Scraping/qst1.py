# 1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
print('Webbrowser :It opens a browser to specific path')
print('requests : It downloads the files and web pages from the net')
print('bs4:It parses the format of web pages that are in written')
print('selenium : It launches and control the web browser.Its able to fill in forms and similate mouse clicks in the browser')


import webbrowser
import requests
# webbrowser.open('https://www.analyticsvidhya.com/')
# res =requests.get('https://courses.analyticsvidhya.com/pages/nlp-program-brochure/download brochure')
res =requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code==requests.codes.ok
print(res.text[:300])

