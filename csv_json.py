import csv
import json
import datetime

'''
 json in the following format:
 {
  "series":[ [time,val], ... ],
  "other key": val,
 }
 only care about series time/value pairs for this converter
'''

jsonInFile = 'sample_data.json'
csvOutFile = "sample_data.csv"

# opens up json file and chugs through 
def convertToCSV():
  with open(jsonInFile,'r') as jsonFile:
    jsonObj = json.load(jsonFile)
    with open(csvOutFile,'w') as outFile:
      for row in jsonObj['series']:
        epochTime = row[0]/1000
        rowDate = datetime.datetime.fromtimestamp(epochTime).strftime('%Y-%m-%d %H:%M:%S.%f')
        writer = csv.writer(outFile)
        writer.writerow([rowDate,row[1]])

def main():
  convertToCSV();

if __name__ == "__main__":
  main()