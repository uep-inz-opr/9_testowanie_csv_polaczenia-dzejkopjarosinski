# Add phoneCalls.csv to the commit



if __name__ == "__main__":
    pass

import csv

class MenadzerPolaczen:
    def ___init__(self,filename):
        self.filename = filename
        self.data_dict = self.read_data()


    def read_data(self):
        calls_dictionary = dict()
        with open(self.filename, 'r') as fin:
            reader = csv.reader(fin, delimiter= ",")
            headers = next(reader)

        for row in header:
            from_subsr = int(row[0])
             if from_subsr not in calls_dictionary:
                calls_dictionary[from_subsr] = 0
            calls_dictionary[from_subsr] += 1
        return calls_dictionary
    
    
    def pobierz_najczesciej_dzwoniacego(self):
        return max(self.data_dict.items(), key= lambda x: x[1])

if __name__ == "__main__":
  print(MenadzerPolaczen(input()).pobierz_najczesciej_dzwoniacego())
    