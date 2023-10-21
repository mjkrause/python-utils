#!/usr/bin/env python3
import unittest
from src.multidimensional_array_encoder import MultiDimensionalArrayEncoder
from src.multidimensional_array_encoder import hinted_tuple_hook
import json


class TestMultiDimensionalArrayEncoder(unittest.TestCase):

    def setUp(self):
        self.enc = MultiDimensionalArrayEncoder()
        self.test_input_1 = (2,)
        self.test_input_2 = {(2,): 'a'}
        self.test_input_3 = {'a': {(2,): {1: 'a'}}}
        self.test_input_4 = {'a': 'b'}

    def test_tuple_encode(self):
        expected = '{"__tuple__s_i_g_n_i_f_i_e_r__": "[2]"}'
        observed = self.enc.encode(self.test_input_1)
        self.assertEqual(expected, observed)
        # print('test_input_1 encoded:', self.enc.encode(self.test_input_1), self.test_input_1)

    def test_tuple_decode(self):
        expected = (2,)
        observed = json.loads(self.enc.encode(self.test_input_1),
                              object_hook=hinted_tuple_hook, )
        self.assertEqual(expected, observed)

        # print('test_input_1 decoded:',
        #       json.loads(self.enc.encode(self.test_input_1),
        #                  object_hook=hinted_tuple_hook, )
        #       )

    def test_dict_tuple_as_key_encoded(self):
        expected = '{"{\\"__tuple__s_i_g_n_i_f_i_e_r__\\": \\"[2]\\"}": "a"}'
        observed = f'{self.enc.encode(self.test_input_2)}'
        self.assertEqual(expected, observed)

        # print('test_input_2 encoded:', self.enc.encode(self.test_input_2))

    def test_dict_tuple_as_key_decoded(self):
        expected = {(2,): 'a'}
        observed = json.loads(self.enc.encode(self.test_input_2), object_hook=hinted_tuple_hook, )
        self.assertEqual(expected, observed)

        # print('test_input_2 decoded:',
        #       json.loads(self.enc.encode(self.test_input_2),
        #                  object_hook=hinted_tuple_hook, )
        #       )

    def test_dict_of_tuples_encode(self):
        expected = '{"a": {"{\\"__tuple__s_i_g_n_i_f_i_e_r__\\": \\"[2]\\"}": {"1": "a"}}}'
        observed = f'{self.enc.encode(self.test_input_3)}'
        self.assertEqual(expected, observed)
        # print('test_input_3 encoded:', self.enc.encode(self.test_input_3))

    def test_dict_of_tuples_decode(self):
        expected = {'a': {(2,): {'1': 'a'}}}
        observed = json.loads(self.enc.encode(self.test_input_3), object_hook=hinted_tuple_hook, )
        self.assertEqual(expected, observed)
        # print('test_input_3 decoded:',
        #       json.loads(self.enc.encode(self.test_input_3),
        #                  object_hook=hinted_tuple_hook, )
        #       )

    def test_dict_encode(self):
        expected = '{"a": "b"}'
        observed = f'{self.enc.encode(self.test_input_4)}'
        self.assertEqual(expected, observed)
        # print('test_input_4  encoded:', self.enc.encode(self.test_input_4))

    def test_dict_decode(self):
        expected = {'a': 'b'}
        observed = json.loads(self.enc.encode(self.test_input_4), object_hook=hinted_tuple_hook, )
        self.assertEqual(expected, observed)
        # print('test_input_4 decoded:',
        #       json.loads(self.enc.encode(self.test_input_4),
        #                  object_hook=hinted_tuple_hook, )
        #       )


if __name__ == '__main__':
    unittest.main()
