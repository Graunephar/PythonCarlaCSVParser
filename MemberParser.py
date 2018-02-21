import csv


class MemberParser:

    def __init__(self):
        pass

    def load_memebers(self, filename):
        with open(filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
