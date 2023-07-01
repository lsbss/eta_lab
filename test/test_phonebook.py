from unittest import TestCase

import pytest

from src.phonebook import Phonebook


class TestPhonebook(TestCase):

    def test_add(self):
        name = 'BOMBEIRO'
        number = '193'
        result = 'Numero adicionado'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_existing(self):
        name = 'POLICIA'
        number = '190'
        result = 'Numero já cadastrado'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_incorret_value_at_sign(self):
        name = 'BOMBEIR@'
        number = '192'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_incorret_value_hash(self):
        name = 'BOMBEIR#'
        number = '192'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_incorret_value_exclamation(self):
        name = 'BOMBEIR!'
        number = '192'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_incorret_value_dolar_sign(self):
        name = 'BOMBEIR$'
        number = '192'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_incorret_value_percentage(self):
        name = 'BOMBEIR%'
        number = '192'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_no_number(self):
        name = 'POLICIA'
        number = ''
        result = 'Numero invalido'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_add_no_name(self):
        name = ''
        number = '193'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.add(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_lookup(self):
        name = 'POLICIA'
        result = '190'

        pb = Phonebook()

        found_result = pb.lookup(name=name)
        self.assertEqual(result, found_result)

    def test_lookup_not_found(self):
        name = 'NOTFOUND'
        result = 'Nome nao encontrado'

        pb = Phonebook()

        found_result = pb.lookup(name=name)
        self.assertEqual(result, found_result)

    def test_lookup_hash(self):
        name = 'BOMBEIR#'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.lookup(name=name)
        self.assertEqual(result, found_result)

    def test_lookup_at_sign(self):
        name = 'BOMBEIR@'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.lookup(name=name)
        self.assertEqual(result, found_result)

    def test_lookup_exclamation(self):
        name = 'BOMBEIR!'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.lookup(name=name)
        self.assertEqual(result, found_result)

    def test_lookup_dolar_sign(self):
        name = 'BOMBEIR$'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.lookup(name=name)
        self.assertEqual(result, found_result)

    def test_lookup_percentage(self):
        name = 'BOMBEIR%'
        result = 'Nome invalido'

        pb = Phonebook()

        found_result = pb.lookup(name=name)
        self.assertEqual(result, found_result)

    def test_get_names(self):
        name = 'BOMBEIRO'
        number = '193'
        result = ['POLICIA', 'BOMBEIRO']

        pb = Phonebook()
        pb.add(name=name, number=number)

        found_result = pb.get_names()
        self.assertEqual(result, found_result)

    def test_get_numbers(self):
        name = 'BOMBEIRO'
        number = '193'
        result = ['190', '193']

        pb = Phonebook()
        pb.add(name=name, number=number)

        found_result = pb.get_numbers()
        self.assertEqual(result, found_result)

    def test_clear(self):
        result = 'phonebook limpado'

        pb = Phonebook()

        found_result = pb.clear()
        self.assertEqual(result, found_result)

    def test_search(self):
        name = 'POL'
        result = [{'POLICIA', '190'}]

        pb = Phonebook()

        found_result = pb.search(name)
        self.assertEqual(result, found_result)

    def test_search_not_found(self):
        name = 'XXX'
        result = []

        pb = Phonebook()

        found_result = pb.search(name)
        self.assertEqual(result, found_result)

    def test_phonebook_sorted(self):
        name = 'BOMBEIRO'
        number = '193'
        name_ = 'MARINHA'
        number_ = '185'
        result = [('BOMBEIRO', '193'), ('MARINHA', '185'), ('POLICIA', '190')]

        pb = Phonebook()
        pb.add(name=name, number=number)
        pb.add(name=name_, number=number_)

        found_result = pb.get_phonebook_sorted()
        self.assertEqual(result, found_result)

    def test_phonebook_reverse(self):
        name = 'BOMBEIRO'
        number = '193'
        name_ = 'MARINHA'
        number_ = '185'
        result = [('POLICIA', '190'), ('MARINHA', '185'), ('BOMBEIRO', '193')]

        pb = Phonebook()
        pb.add(name=name, number=number)
        pb.add(name=name_, number=number_)

        found_result = pb.get_phonebook_reverse()
        self.assertEqual(result, found_result)

    def test_delete(self):
        name = 'POLICIA'
        result = 'Numero deletado'
        pb = Phonebook()

        found_result = pb.delete(name)
        self.assertEqual(result, found_result)

    def test_delete_not_found(self):
        name = 'XXXX'
        result = 'Numero nao encontrado'
        pb = Phonebook()

        found_result = pb.delete(name)
        self.assertEqual(result, found_result)

    def test_change_number(self):
        name = 'POLICIA'
        number = '191'
        result = 'Numero editado'

        pb = Phonebook()

        found_result = pb.change_number(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_change_number_persist_value(self):
        name = 'POLICIA'
        number = '191'
        result = ['191']

        pb = Phonebook()

        pb.change_number(name=name, number=number)
        found_result = pb.get_numbers()
        self.assertEqual(result, found_result)

    def test_change_number_not_found(self):
        name = 'XXX'
        number = '191'
        result = 'Nome nao encontrado'

        pb = Phonebook()

        found_result = pb.change_number(name=name, number=number)
        self.assertEqual(result, found_result)

    def test_get_name_by_number(self):
        number = '190'
        result = ['POLICIA']

        pb = Phonebook()

        found_result = pb.get_name_by_number(number=number)
        self.assertEqual(result, found_result)

    def test_get_name_by_number_not_found(self):
        number = '999'
        result = 'Numero nao encontrado'

        pb = Phonebook()

        found_result = pb.get_name_by_number(number=number)
        self.assertEqual(result, found_result)
