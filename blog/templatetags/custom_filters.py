# custom_filters.py
from django import template
from bs4 import BeautifulSoup
import markdown2

register = template.Library()

@register.filter
def markdown_to_html(markdown_text):
    # Parse HTML to find img tags and add img-fluid class
    html_content = markdown2.markdown(markdown_text)
    soup = BeautifulSoup(html_content, 'html.parser')
    for img in soup.find_all('img'):
        img['class'] = 'img-fluid'
        img['onclick'] = f"window.open('{img['src']}', '_blank');"

    return str(soup)
