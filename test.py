import unittest

import ntpl

t = ntpl.slurp("index.html")

class TestNoTemplate(unittest.TestCase):
    def test_attr(self):
        self.assertEqual(ntpl.attr(t, "h1", "someattr"), "yes")
        self.assertEqual(ntpl.attr(t, "h1", "hi"), None)
        t1 = ntpl.attr(t, "h1", "hi", "cool")
        self.assertEqual(ntpl.attr(t1, "h1", "hi"), "cool")

    def test_attrs(self):
        self.assertEqual(ntpl.attrs(t, "div", "id"), ["first", "second"])

    def test_remove(self):
        self.assertTrue("<li>" in t)
        self.assertFalse("<li>" in ntpl.remove(t, "li"))

    def test_replace(self):
        self.assertTrue("<p>Fooe.</p>" in t)
        self.assertFalse("<p>Barre.</p>" in t)
        t1 = ntpl.replace(t, "p", "Barre.")
        self.assertFalse("<p>Fooe.</p>" in t1)
        self.assertTrue("<p>Barre.</p>" in t1)

    def test_replaceWith(self):
        self.assertTrue("<p>Fooe.</p>" in t)
        self.assertFalse("<h2>Barre.</h2>" in t)
        t1 = ntpl.replaceWith(t, "p", "<h2>Barre.</h2>")
        self.assertFalse("<p>Fooe.</p>" in t1)
        self.assertTrue("<h2>Barre.</h2>" in t1)

    def test_render(self):
        self.assertEqual(ntpl.render(
            [["p", {"class": "one"}, "First paragraph."],
             ["p", "Second paragraph."]]),
            """<p class="one">First paragraph.</p><p>Second paragraph.</p>""")

    def test_render_replace(self):
        self.assertTrue("<p>Fooe.</p>" in t)
        self.assertFalse("<h2>Yay.</h2>" in t)
        insert = ntpl.render(["h2", "Yay."])
        t1 = ntpl.replaceWith(t, "p", insert)
        self.assertFalse("<p>Fooe.</p>" in t1)
        self.assertTrue("<h2>Yay.</h2>" in t1)

if __name__ == '__main__':
    unittest.main()
