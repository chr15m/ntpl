import sys
if sys.version_info[0] == 2:
    from io import open
    string_type = basestring
else:
    string_type = str
from bs4 import BeautifulSoup as bs
from pyhiccup.core import convert as render

def _idempotent_bs(html):
    "Idempotent conversion function for str or BeautifulSoup to BeautifulSoup object."
    return bs(html, 'html.parser') if isinstance(html, string_type) else html

def replace(html, selector, new):
    "Replace innerHTML of html elements that match selector with new."
    html = _idempotent_bs(html)
    new = bs(str(new), 'html.parser')
    for s in html.select(selector):
        s.clear()
        s.insert(0, new)
    return str(html)

def replaceWith(html, selector, new):
    "Replace outerHTML of html elements that match selector with new."
    html = _idempotent_bs(html)
    new = bs(str(new), 'html.parser')
    for s in html.select(selector):
        s.insert_after(new)
        s.decompose()
    return str(html)

def remove(html, selector):
    "Remove html elements that match selector."
    html = _idempotent_bs(html)
    [s.decompose() for s in html.select(selector)]
    return str(html)

def attr(html, selector, key, value=None):
    "Get or set value on attribute called key, in html elements that match selector."
    html = _idempotent_bs(html)
    selected = html.select(selector)
    if value == None:
        return selected[0].get(key)
    else:
        for s in selected:
            s[key] = value
        return str(html)

def attrs(html, selector, key):
    "Get a list of values of attribute called key in html elements that match selector."
    html = _idempotent_bs(html)
    selected = html.select(selector)
    return [s.get(key) for s in selected]

def slurp(path):
    "Load a file as a string."
    with open(path, encoding="utf-8") as f:
        return f.read()

