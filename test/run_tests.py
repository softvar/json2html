# -*- coding: utf-8 -*-
import os, sys, re

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import unittest
from json2html import *

class TestJson2Html(unittest.TestCase):

    def setUp(self):
        self.test_json = []
        self.path = os.path.dirname(os.path.abspath('.'))

        self.jsonFiles = []
        self.jsonFiles += [each.split('.')[0] for each in os.listdir('.') if each.endswith('.json')]

        for _file in self.jsonFiles:
            fpath = os.path.join(self.path + '/test', _file)
            input_json = None
            expected_output = None
            with open('%s.json' % fpath, 'r') as f:
                input_json = f.read()
            with open('%s.txt' % fpath, 'r') as f:
                expected_output = f.read()
            self.test_json.append({
                'filename': _file,
                'json': input_json,
                'output': re.sub(
                    r"[\r\n\t]*",
                    "",
                    expected_output
                )
            })

    def tearDown(self):
        pass

    def test_empty_json(self, *args, **kwargs):
        self.assertEqual(
            json2html.convert(json = ""),
            ""
        )
        self.assertEqual(
            json2html.convert(json = []),
            ""
        )
        self.assertEqual(
            json2html.convert(json = {}),
            ""
        )

    def test_invalid_json_exception(self, *args, **kwargs):
        _json = "{'name'}"
        with self.assertRaises(ValueError) as context:
            json2html.convert(json = _json)
        self.assertIn('Expecting property name', str(context.exception))

    def test_funky_objects(self):
        class objecty_class1(object):
            pass
        class objecty_class2(object):
            def __repr__(self):
                return u"blübidö"
        class objecty_class3:
            pass
        class objecty_class4:
            def __repr__(self):
                return u"blübidöbidü"
        objecty_the_funky_object1 = objecty_class1()
        objecty_the_funky_object2 = objecty_class2()
        objecty_the_funky_object3 = objecty_class3()
        objecty_the_funky_object4 = objecty_class4()
        funky_non_json_object = (
            {"blib":(u"blüb", u"ـث‎"), u"ـث‎":1E-3},
            "blub",
            {
                1: objecty_the_funky_object1,
                2: objecty_the_funky_object2,
                3: objecty_the_funky_object3,
                4: objecty_the_funky_object4,
            },
            tuple([
                objecty_the_funky_object1,
                objecty_the_funky_object2,
                objecty_the_funky_object3,
                objecty_the_funky_object4
            ])
        )
        converted = json2html.convert(funky_non_json_object)
        self.assertTrue(u"ـث‎" in converted)
        self.assertTrue(u"blüb" in converted)
        self.assertTrue(u"blübidö" in converted)
        self.assertTrue(u"blübidöbidü" in converted)
        self.assertTrue(u"blübidöbidü" in converted)
        self.assertTrue(u"objecty_class1" in converted)
        self.assertTrue(u"objecty_class3" in converted)

    def test_dictlike_objects(self):
        class binary_dict(object):
            def __init__(self, one, two):
                self.one = one
                self.two = two

            def __getitem__(self, key):
                if key not in self.keys():
                    raise KeyError()
                if key == "one":
                    return self.one
                return self.two

            def __iter__(self):
                yield self.one
                yield self.two
                raise StopIteration()

            def __contains__(self, key):
                return key in self.keys()

            def keys(self):
                return ("one", "two")

            def items(self):
                return [(k, self[k]) for k in self.keys()]

        #single object
        self.assertEqual(
            json2html.convert(binary_dict([1, 2], u"blübi")),
            u'<table border="1"><tr><th>one</th><td><ul><li>1</li><li>2</li></ul></td></tr><tr><th>two</th><td>blübi</td></tr></table>'
        )
        #clubbed with single element
        self.assertEqual(
            json2html.convert([binary_dict([1, 2], u"blübi")]),
            u'<table border="1"><thead><tr><th>one</th><th>two</th></tr></thead><tbody><tr><td><ul><li>1</li><li>2</li></ul></td><td>blübi</td></tr></tbody></table>'
        )
        #clubbed with two elements
        self.assertEqual(
            json2html.convert([
                binary_dict([1, 2], u"blübi"),
                binary_dict("foo", "bar")
            ]),
            u'<table border="1"><thead><tr><th>one</th><th>two</th></tr></thead><tbody><tr><td><ul><li>1</li><li>2</li></ul></td><td>blübi</td></tr><tr><td>foo</td><td>bar</td></tr></tbody></table>'
        )
        #not clubbed, second element has different keys
        self.assertEqual(
            json2html.convert([
                binary_dict([1, 2], u"blübi"),
                {"three":3}
            ]),
            u'<ul><li><table border="1"><tr><th>one</th><td><ul><li>1</li><li>2</li></ul></td></tr><tr><th>two</th><td>blübi</td></tr></table></li><li><table border="1"><tr><th>three</th><td>3</td></tr></table></li></ul>'
        )

    def test_listlike_objects(self):
        class binary_tuple(object):
            def __init__(self, one, two):
                self.one = one
                self.two = two

            def __getitem__(self, key):
                if key == 0:
                    return self.one
                if key == 1:
                    return self.two
                raise KeyError()

            def __iter__(self):
                yield self.one
                yield self.two
                return

        #single object
        self.assertEqual(
            json2html.convert(binary_tuple([1, 2], u"blübi")),
            u'<ul><li><ul><li>1</li><li>2</li></ul></li><li>blübi</li></ul>'
        )

    def test_bool(self):
        self.assertEqual(
            json2html.convert(True),
            u'True'
        )

    def test_none(self):
        self.assertEqual(
            json2html.convert(None),
            u''
        )

    def test_xss(self):
        self.assertEqual(
            json2html.convert("<script></script>"),
            u"&lt;script&gt;&lt;/script&gt;"
        )
        self.assertEqual(
            json2html.convert("<script></script>", escape=False),
            u"<script></script>"
        )

    def test_all(self):
        for test_definition in self.test_json:
            _json = test_definition['json']
            _clubbing = "no_clubbing" not in test_definition['filename']
            print("testing %s" %(test_definition['filename']))
            self.assertEqual(
                json2html.convert(json=_json, clubbing=_clubbing, encode=True),
                test_definition['output'].encode('ascii', 'xmlcharrefreplace')
            )
            #testing whether we can call convert with a positional args instead of keyword arg
            self.assertEqual(
                json2html.convert(_json, clubbing=_clubbing, encode=True),
                test_definition['output'].encode('ascii', 'xmlcharrefreplace')
            )


if __name__ == '__main__':
    unittest.main()
