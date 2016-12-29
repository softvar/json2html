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
        self.assertTrue(
            json2html.convert(json = ""),
            ""
        )
        self.assertTrue(
            json2html.convert(json = []),
            ""
        )
        self.assertTrue(
            json2html.convert(json = {}),
            ""
        )

    def test_invalid_json_exception(self, *args, **kwargs):
        if sys.version_info[:2] >= (2, 7): #Python below 2.7 doesn't have assertRaises, ommitting these tests
            _json = "{'name'}"
            with self.assertRaises(ValueError) as context:
                json2html.convert(json = _json)

            self.assertIn('Expecting property name', str(context.exception))

    def test_all(self):
        for test_definition in self.test_json:
            _json = test_definition['json']
            _clubbing = "no_clubbing" not in test_definition['filename']
            print("testing %s" %(test_definition['filename']))
            self.assertEqual(
                json2html.convert(json = _json, clubbing=_clubbing),
                test_definition['output']
            )
            #testing whether we can call convert with a positional args instead of keyword arg
            self.assertEqual(
                json2html.convert(_json, clubbing=_clubbing),
                test_definition['output']
            )


if __name__ == '__main__':
    unittest.main()
