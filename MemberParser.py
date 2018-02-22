import csv

from Member import Member


class MemberParser:
    def __init__(self, delimiter=";"):
        self.delimiter = delimiter
        self.header = {"firstname": HeaderItem("Fornavn"), "lastname": HeaderItem("Efternavn"),
                       "middlename": HeaderItem("Mellemnavn"), "birthdate": HeaderItem("Fødselsdag")}
        self._members = []

    def load_memebers(self, filename):
        with open(filename, newline='') as csvfile:
            memberreader = csv.reader(csvfile, delimiter=';', quotechar='|')

            rownum = 0;
            for row in memberreader:
                if rownum == 0:
                    header = self.load_header(row)
                else:
                    self.parse_member(header, row)
                rownum += 1

    def load_header(self, row):
        """
        Finds stuff in header
        :param row: The row to be xeached
        :return: an array of all the incices found
        """
        res = []
        rowindex = 0
        for data in row:
            for key in self.header:
                if self.header[key].name_in_csv == data:
                    self.header[key].index = rowindex
                    res.append(rowindex)
            rowindex += 1
        return res

    def parse_member(self, included_cols, row):

        firstnameindex = self.header["firstname"].index
        middlenameindex = self.header["middlename"].index
        lastnameindex = self.header["lastname"].index
        birthdateindex = self.header["birthdate"].index

        firstname = row[firstnameindex]
        lastname = row[lastnameindex]
        middlename = row[middlenameindex]
        birthdate = row[birthdateindex]

        resmember = Member(firstname, middlename, lastname, birthdate)
        self._members.append(resmember)

    def printmembers(self):
        for member in self._members:
            memstring = "Firstname: " + member.firstname + " Middlname: " + member.middlename + " Lastname: " + member.lastname + " Birthdate: " + member.birthdate
            print(memstring)

class HeaderItem:
    def __init__(self, name_in_csv):
        self.name_in_csv = name_in_csv
        self._index = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
