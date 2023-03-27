# Write a program that extracts data from a HTML file.
#
# Using BeautifulSoup is not required.
# Make sure you extract the company's name, the date registered in this element, the short description,
# and the link to "More information".

from bs4 import BeautifulSoup
soup = BeautifulSoup(open('src/keurmerk.info.html', 'r').read(), features='html.parser')
