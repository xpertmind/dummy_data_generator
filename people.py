import csv
import os
import random
 
debug = 0

def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.
                for line in f:
                        content_array.append(line)
        return content_array

def fill_line(maxEntries, dataset):
        rec = ""
        no = random.randint(1, maxEntries)
        myset = {dataset[random.randint(0, len(dataset)-1)].rstrip()}
        if debug == 1:
            txt = " ({}) "
            rec += txt.format(no)

        while len(myset) < no:
            myset.add(dataset[random.randint(0, len(dataset)-1)].rstrip())

        for XY in myset:
            rec += "," + XY

        # fill the missing records with commas
        z = len(myset)
        while z < maxEntries:
            rec += ","
            z += 1

        return rec

first_names_filename = os.path.join(os.path.dirname(__file__), 'firstnames.csv')
last_names_filename = os.path.join(os.path.dirname(__file__), 'lastnames.csv')
companies_filename = os.path.join(os.path.dirname(__file__), 'companies.csv')
unis_filename = os.path.join(os.path.dirname(__file__), 'unis.csv')
li_filename = os.path.join(os.path.dirname(__file__), 'linkedin.csv')
hobbies_filename = os.path.join(os.path.dirname(__file__), 'hobbies.csv')
csv_file = os.path.join(os.path.dirname(__file__), 'people.csv')

firstnames = file_read(first_names_filename)
lastnames = file_read(last_names_filename)
companies = file_read(companies_filename)
unis = file_read(unis_filename)
linkedin = file_read(li_filename)
hobbies = file_read(hobbies_filename)

numFirstnames = len(firstnames)
numLastnames = len(lastnames)
numCompanies = len(companies)
numLiGroups = len(linkedin)
numHobbies = len(hobbies)

numUnis = len(unis)

headerLine="person,current_company,past_company1,past_company2,past_company3,education,linkedin_group1,linkedin_group2,linkedin_group3,hobby1,hobby2,hobby3";



records = int(input("Enter no of records: "))
f = open(csv_file, 'w')
f.write(headerLine+"\n")
for x in range(0, records):
    #name
    line = firstnames[random.randint(0, len(firstnames)-1)].rstrip() + " " + lastnames[random.randint(0, len(lastnames)-1)].rstrip()

    # companies
    line += fill_line(4, companies)

    #education
    line += "," + unis[random.randint(0, len(unis)-1)].rstrip()

    #linkedin
    # variable numbers of LI groups (min 1!)
    line += fill_line(3, linkedin)

    #hobbies
    # variable numbers of LI groups (min 1!)
    line += fill_line(3, hobbies)

    f.write(line + "\n")

f.close()
