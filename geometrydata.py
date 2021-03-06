import pandas
import json
import csv
from PopulationFinder import population_scrapper


def itfile(filepath):
    '''Iterable File[ITFILE]'''
    file = open(filepath)
    fp = csv.reader(file)
    return fp


def geodata():
    """
            embeds the longitude and latitude of all the countries
            with the population of those countries thereby providing
            information regarding population region which can be used
            to map the data.
    """
    population_scrapper(
        "http://www.worldometers.info/world-population/population-by-country/")
    index = 0
    file = open('world.json', 'w+')
    i = []
    country = []
    geometry = json.load(open('countries.json'))
    population = itfile('populationdata.csv')
    index = 0

    for row in population:
        if (row[1] != 'Country'):
            country.append(row[1])
    for j in range(3):
        index = 0
        for i in geometry['features']:
            if (i['properties']['ADMIN'] in country):
                pass
            else:
                del geometry['features'][index]
            index += 1
    index = 0

    for i in geometry['features']:
        population = itfile('populationdata.csv')
        count = 0
        for column in population:
            if (i['properties']['ADMIN'] == column[1]):
                i['properties']['POP2018'] = column[2]
                count = 1
                int(i['properties']['POP2018'])
    if(count == 0):
        pass
        #del geometry['features'][index]

    json.dump(geometry, file)
    file.close()
