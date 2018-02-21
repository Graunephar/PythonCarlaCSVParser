class Member:

    def __init__(self, birthdate, firstname, middlename, lastname):
        self.birthdate = birthdate
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    @property
    def middlename(self):
        return self._middlename

    @middlename.setter
    def middlename(self, value):
        self.__middlename = value

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value):
        self._birthdate = value
