import os
import csv
import datetime
from datetime import date

# YNAB states: date,payee, memo, outflow, inflow
#
# example from bank
#Datum;Naam / Omschrijving;Rekening;Tegenrekening;Code;Af Bij;Bedrag (EUR);MutatieSoort;Mededelingen
#20180206;ETOS 7812 AMSTERDAM NLD;NL33INGB0655063803;;BA;Af;-18.67;Betaalautomaat;Pasvolgnr:002 05-02-2018 15:20 Transactie:A721P4 Term:W725Q5

#this works - but not quite right
#"Date","Payee","Memo","Amount"
#"2018-02-06","ETOS 7812 AMSTERDAM NLD","Pasvolgnr:002 Transactie:A721P4 Term:W725Q5","-18.67"

# all , in [6] needs to be replaced with .   print(amount.repl ace(",", "."))   done
# date to be formatted  20180206 -> 02/06/18   (done)
# Row[5] determines the value of [6] - if it is 'Af" then [6] needs to be a negative amount (*-1) OR!
# better yet create a new column called outflow
# examples:
#07/23/16,Payee 1,Memo,100.00,
#07/24/16,Payee 2,Memo,,500.00


inputfile = r"C:\Users\martin\Downloads\ING_dump.csv"
outputfile = open(r"C:\Users\martin\Downloads\ING_import.csv", 'w')
debug = "true"

header = ['date', 'payee', 'memo', 'outflow', 'inflow']



def int2date(argdate: int):
    year = int(argdate / 10000)
    month = int((argdate % 10000) / 100)
    day = int(argdate % 100)
    return date(year, month, day)



with open(inputfile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV) #Ignoring header line in csv

    for row in readCSV:

        #formatting date field
        datestring = str(int2date(int(row[0])))

        payee = row[1]
        memo = row[8]

        #determine if its a negative amount
        if row[5] == 'Af':
            outflow = row[6].replace(",", ".")
            inflow = ''
        elif row[5] == 'Bij':
            inflow = row[6].replace(",", ".")
            outflow = ''

        #build string
        row_out = {datestring, payee, memo, outflow, inflow}

        #debug output
        if debug == 'true':
            print("date:", datestring)
            print("payee:", payee)
            print("memo:", memo)
            print("inflow:", inflow)
            print("outflow:", outflow)
            print row_out
            print("----")


with open(inputfile + today +  + ".csv", 'w', newline='') as e:
    dict_writer = csv.DictWriter(e, fieldnames=header)
    dict_writer.writeheader()
    dict_writer.writerow(row_out)

#date,payee, memo, outflow, inflow
