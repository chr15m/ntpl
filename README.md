Un-template is a minimal Python library to manipulate and render HTML without using a templating language. Instead it works on raw HTML and uses Python's native datastructures to represent new document fragments.

To manipulate an existing HTML document, you pass a string containing `html` into the functions `replace`, `remove`, `replaceWith`, and `attr` and then use a CSS-style `selector` to choose the HTML elements that you want to manpulate. You generate HTML from scratch by passing Python datastructures to the declarative `render` function. You can combine the manipulation and rendering functions to update an existing HTML document with new content.

If you're writing a back end web service you can use this library to modify pure HTML on the server side and then pass it directly back to the browser in the HTTP response.

Inspired by Clojure's [Enlive](https://github.com/cgrand/enlive) and [Hiccup](https://github.com/weavejester/hiccup), this library uses [pyhiccup](https://github.com/nbessi/pyhiccup) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) to do it's work.

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


