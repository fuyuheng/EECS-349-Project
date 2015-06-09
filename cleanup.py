__author__ = 'AlanFu'
import csv, numpy, sys, math
from sklearn import tree

# # ---------------------------------------
# # weather 01 -> 02: discards irrelevant variables
# fileName = "weather_01.csv"
# reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
# data = numpy.array(reader)
# data = numpy.delete(data, [0, 2, 3, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 1)
# writer = open("weather_02.csv", "w")
# csvWriter = csv.writer(writer)
# csvWriter.writerows(data)
# writer.close()


# # ---------------------------------------
# # weather 02 -> 03: calculate the average value for each day
# # M is not counted into the average
# # If the entire category has M value throughout the day, that day has M average for that category
# fileName = "weather_02.csv"
# reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
# data = numpy.array(reader)
# for row in range(1, len(data)):
#     data[row][0] = data[row][0][ :10]
#
# # # convert all value except for date to numeric
# # for i in range(1, len(data)):
# #     for j in range(1, len(data[1])):
# #         if data[i][j] != 'M':
# #             data[i][j] = float(data[i][j])
#
# updateData = numpy.array(data[0])
# date = '2001-01-01'
# dayArray = numpy.array(data[0])
#
# for row in range(1, len(data)):
#     # if instance is still in the same date
#     if data[row][0] == date and row != len(data)-1:
#         dayArray = numpy.vstack((dayArray, data[row]))
#     else:
#         if row == len(data)-1:
#             dayArray = numpy.vstack((dayArray, data[row]))
#         temp = data[row]
#         date = data[row][0]
#         dayAvg = []
#         dayAvg.append(dayArray[1][0])
#         for col in range(1, len(dayArray[0])):
#             avgList = []
#             for row in range(1, len(dayArray)):
#                 if dayArray[row][col] != 'M':
#                     avgList.append(float(dayArray[row][col]))
#             dayAvg.append(numpy.mean(avgList))
#
#         updateData = numpy.vstack((updateData, dayAvg))
#         dayArray = numpy.array(data[0])
#         dayArray = numpy.vstack((dayArray, temp))
#
# writer = open("weather_03.csv", "w")
# csvWriter = csv.writer(writer)
# csvWriter.writerows(updateData)
# writer.close()


# # ---------------------------------------
# # crime_raw -> 01: discards irrelevant variables, change data format
# fileName = "crime_data_raw.csv"
# reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
# data = numpy.array(reader)
# data = numpy.delete(data, [0, 1, 3, 4, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 1)
# for row in range(1, len(data)):
#     oldDate = data[row][0]
#     newDate = oldDate[6:10] + "-" + oldDate[0:2] + "-" + oldDate[3:5]
#     data[row][0] = newDate
# writer = open("crime_01.csv", "w")
# csvWriter = csv.writer(writer)
# csvWriter.writerows(data)
# writer.close()


# # ---------------------------------------
# # count types of crimes
# fileName = "crime_01.csv"
# reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
# data = numpy.array(reader)
# crimeType = []
# count = 0
# for row in range(1, len(data)):
#     if data[row][1] not in crimeType:
#         crimeType.append(data[row][1])
#         count += 1
# print crimeType


# # ---------------------------------------
# # crime 01 -> 02: count instances of crimes per day, rate of arrest and count for each major type of crime
# fileName = "crime_01.csv"
# reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
# data = numpy.array(reader)
#
# updateData = numpy.array(["date", "total count", "arrest rate", "sex offense", "theft", "assault and battery", "burglary", "robbery", "substance", "homicide", "gambling", "prostitution", "arson", "domestic violence", "others"])
# date = '2001-01-01'
# dayArray = numpy.array(data[0])
#
# for row in range(1, len(data)):
#     if row % 2000 == 0:
#         print str(float(row)/(len(data)+1)*100) + "% completed!"
#
#     # if instance is still in the same date
#     if data[row][0] == date and row != len(data)-1:
#         dayArray = numpy.vstack((dayArray, data[row]))
#     else:
#         if row == len(data)-1:
#             dayArray = numpy.vstack((dayArray, data[row]))
#         temp = data[row]
#         date = data[row][0]
#
#         crimeCount = len(dayArray)-1
#         arrestCount = 0
#         sexOffense = 0
#         theft = 0
#         assaultAndBattery = 0
#         burglary = 0
#         robbery = 0
#         substance = 0
#         homicide = 0
#         gambling = 0
#         prostitution = 0
#         arson = 0
#         domesticViolence = 0
#         others = 0
#
#         for row in range(1, len(dayArray)):
#             if dayArray[row][3] != "false":
#                 arrestCount += 1
#             if dayArray[row][1] in ["SEX OFFENSE", "CRIM SEXUAL ASSAULT"]:
#                 sexOffense += 1
#             if dayArray[row][1] == "THEFT":
#                 theft += 1
#             if dayArray[row][1] in ["ASSAULT", "BATTERY"]:
#                 assaultAndBattery += 1
#             if dayArray[row][1] in ["BURGLARY", "CRIMINAL TRESPASS"]:
#                 burglary += 1
#             if dayArray[row][1] == "ROBBERY":
#                 robbery += 1
#             if dayArray[row][1] in ["NARCOTICS", "LIQUOR LAW VIOLATION", "OTHER NARCOTIC VIOLATION"]:
#                 substance += 1
#             if dayArray[row][1] == "HOMICIDE":
#                 homicide += 1
#             if dayArray[row][1] == "GAMBLING":
#                 gambling += 1
#             if dayArray[row][1] == "PROSTITUTION":
#                 prostitution += 1
#             if dayArray[row][1] == "ARSON":
#                 arson += 1
#             if dayArray[row][1] == "DOMESTIC VIOLENCE":
#                 domesticViolence += 1
#         others = crimeCount - sexOffense - theft - assaultAndBattery - burglary - robbery - substance - homicide - gambling - prostitution - arson - domesticViolence
#
#         updateData = numpy.vstack((updateData, [dayArray[1][0], crimeCount, float(arrestCount)/crimeCount, sexOffense, theft, assaultAndBattery, burglary, robbery, substance, homicide, gambling, prostitution, arson, domesticViolence, others]))
#
#         dayArray = numpy.array(data[0])
#         dayArray = numpy.vstack((dayArray, temp))
#
# writer = open("crime_02.csv", "w")
# csvWriter = csv.writer(writer)
# csvWriter.writerows(updateData)
# writer.close()


# # ---------------------------------------
# # combine weather and crime data
# fileName = "weather_03.csv"
# reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
# weatherData = numpy.array(reader)
#
# fileName = "crime_02.csv"
# reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
# crimeData = numpy.array(reader)
#
# combinedData = numpy.concatenate((weatherData[0], crimeData[0]))
# crimeRow = 1
#
# for row in range(1, len(weatherData)):
#     if row % 500 == 0:
#         print str(float(row)/(len(weatherData)+1)*100) + "% completed!"
#     weatherInstance = weatherData[row]
#     for i in range(crimeRow, len(crimeData)):
#         if crimeData[i][0] == weatherInstance[0]:
#             combinedInstance = numpy.concatenate((weatherInstance, crimeData[i]))
#             crimeRow = i + 1
#     combinedData = numpy.vstack((combinedData, combinedInstance))
#
# combinedData = numpy.delete(combinedData, [8], 1)
#
# writer = open("weather_and_crime_base.csv", "w")
# csvWriter = csv.writer(writer)
# csvWriter.writerows(combinedData)
# writer.close()


# ---------------------------------------
# categorize crime counts based on its relative position in the 180d-before to 180d-after period into 1, 2, 3, 4
# 1: lowest (in terms of absolute count) 25%; 2: mid-lower 25%; 3: mid-higher 25%; 4: highest 25%
# or into k categories
# replace nan in precipitation with 0
fileName = "weather_and_crime_base.csv"
reader = list(csv.reader(open(fileName, "rb"), delimiter=','))
data = numpy.array(reader)

for row in range(1, len(data)):
    if data[row][6] == "nan":
        data[row][6] = 0

for col in range(8, len(data[0])):
    countRow = data[:, col]
    updateRow = [countRow[0]]

    k = 2

    # categorize the first 180 count, special because they have less than 180 precedents
    postIndex = 361
    sortedCounts = sorted(countRow[1:postIndex+1])
    for i in range(1, 181):
        rank = sortedCounts.index(countRow[i])
        updateRow.append(int(math.ceil((rank+0.01)/361*k)))

    # categorize after the first 180 count and before the last 180 count
    for i in range(181, len(countRow) - 180):
        prevIndex = i-180
        postIndex = i+180
        sortedCounts = sorted(countRow[prevIndex:postIndex])
        rank = sortedCounts.index(countRow[i])
        updateRow.append(int(math.ceil((rank+0.01)/362*k)))

    # categorize the last 180 count, special because they have less than 180 counts afterward
    prevIndex = len(countRow) - 361
    sortedCounts = sorted(countRow[prevIndex:len(countRow)])
    for i in range(prevIndex, len(countRow)):
        rank = sortedCounts.index(countRow[i])
        updateRow.append(int(math.ceil((rank+0.01)/361*k)))

    for i in range(1, len(data)):
        data[i][col] = updateRow[i]


writer = open("weather_and_crime_categorized.csv", "w")
csvWriter = csv.writer(writer)
csvWriter.writerows(data)
writer.close()