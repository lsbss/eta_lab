from collections import OrderedDict


class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}
        self.invalid_char = ['#', '@', '!', '$', '%']

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        for nome in self.invalid_char:
            if nome in name:
                return 'Nome invalido'

        if not number:
            return 'Numero invalido'

        if not name:
            return 'Nome invalido'

        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'

        return 'Numero já cadastrado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        for nome in self.invalid_char:
            if nome in name:
                return 'Nome invalido'

        if name not in self.entries:
            return 'Nome nao encontrado'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return sorted(self.entries.items())
    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return sorted(self.entries.items(), reverse=True)
    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if name not in self.entries:
            return 'Numero nao encontrado'

        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, name, number):
        """
        Change number value by name
        :param name: String with name
        :param number: String with number
        :return: return 'Numero editado'
        """
        if name in self.entries:
            self.entries[name] = number
            return 'Numero editado'

        return 'Nome nao encontrado'

    def get_name_by_number(self, number):
        """
        Return name value by number
        :param name: String with name
        :param number: String with number
        :return: return Name
        """
        if number not in self.entries.values():
            return 'Numero nao encontrado'

        return list(self.entries.keys())
