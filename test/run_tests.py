import os, sys

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
            self.test_json.append({
                'json': open('%s.json' % fpath).read(),
                'output': open('%s.txt' % fpath).read(),
            })

    def tearDown(self):
        pass

    '''
        Exception handling tests
    '''
    def test_empty_json_exception(self, *args, **kwargs):
        _json = ''
        with self.assertRaises(Exception) as context:
            json2html.convert(json = _json)

        self.assertIn("Please use json2html", context.exception)

    def test_invalid_json_exception(self, *args, **kwargs):
        _json = {'name'}
        with self.assertRaises(TypeError) as context:
            json2html.convert(json = _json)

        self.assertIn('is not JSON serializable', str(context.exception))

    def test_dict_instead_of_list_exception(self, *args, **kwargs):
        _json = [{}]
        with self.assertRaises(Exception) as context:
            json2html.convert(json = _json)

        self.assertIn('Not a valid JSON list', str(context.exception))

    def test_all(self):
        for i in range(0, len(self.test_json)):
            _json = self.test_json[i]['json']
            output = json2html.convert(json = _json)

            self.assertEqual(str(output), self.test_json[i]['output'])

if __name__ == '__main__':
    unittest.main()
