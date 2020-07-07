A minimal Python library to manipulate and render HTML, without any templating language.

Un-template (`ntpl`) works with plain HTML documents. You use Python datastructures to build new document fragments. The declarative HTML manipulation works like front-end libraries like React and Mithril.

```python
from ntpl import slurp, replace, replaceWith, render

template = slurp("index.html")
faqs = markdown(slurp("FAQ.md"))

def faq(request):
    html = template
    html = replace(html, "#content-title", "FAQ")
    html = replace(html, "#content", faqs)
    html = replaceWith(html, "a#home", render(["a", {"href": "/"}, "home"]))
    return HttpResponse(html)
```

To modify an existing HTML document, you pass a string containing `html` into the functions `replace`, `remove`, `replaceWith`, and `attr` and then use a CSS-style `selector` to choose the HTML elements that you want to modify. You generate HTML components from scratch by passing Python datastructures to the declarative `render` function. You can combine the manipulation and rendering functions to update an existing HTML document with new content.

If you're writing a back end web service you can use this library to modify pure HTML files on the server side and then pass the result back to the browser directly in the HTTP response.

Inspired by Clojure's [Enlive](https://github.com/cgrand/enlive) and [Hiccup](https://github.com/weavejester/hiccup), this library uses [pyhiccup](https://github.com/nbessi/pyhiccup) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) to do its work.

This library works in Python 2.7 and higher.

# Documentation

Generated from `pydoc ntpl`.

### `attr(html, selector, key, value=None)`

Get or set value on attribute called key, in html elements that match selector.
    
### `attrs(html, selector, key)`

Get a list of values of attribute called key in html elements that match selector.
    
### `remove(html, selector)`

Remove html elements that match selector.

### `replace(html, selector, new)`

Replace innerHTML of html elements that match selector with new.
    
### `replaceWith(html, selector, new)`

Replace outerHTML of html elements that match selector with new.
    
### `slurp(path)`

Load a file as a string.

# Example

```python

import ntpl

# load an HTML file in as a string
t = ntpl.slurp("index.html")

# get the ids of all divs
ntpl.attrs(t, "div", "id")
# ['first', 'second']

# set the class of a div with id="frank"
ntpl.attrs(t, "div#frank", "class", "special")
# returns rendered HTML

# remove all <li> elements
ntpl.remove(t, "li")
# returns rendered HTML with <li> elements removed

# replace the innerHTML of a p element with id "description"
ntpl.replace(t, "p#description", "Some new stuff.")
# returns rendered HTML

# replace the entire outerHTML of a p element
ntpl.replaceWith(t, "p", "<h2>Barre.</h2>")
# returns rendered HTML with all <p> replaced with new tag

# render Python datastructure as HTML
ntpl.render(["div", {"class": "special"}, "Some text."])
# <div class="special">Some text.</div>
# see https://github.com/nbessi/pyhiccup for details

# combine HTML manipulation with rendering
ntpl.replace(t, "ul#users",
    ntpl.render([["li", "Bob"], ["li", "Alice"], ["li", "Satoshi"]]))
# returns render HTML document with user list items contents replaced
```

### Who

Hi, 👋 I'm Chris and I made this.

You can find me online here:

* [@mccrmx](https://twitter.com/mccrmx)
* [mccormick.cx](https://mccormick.cx/)

