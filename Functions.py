import data
def population_total(demographic_list : list[data.CountyDemographics]) -> int:
    total_pop = 0
    for counties in range(len(demographic_list)):
        total_pop += demographic_list[counties].population["2014 Population"]
    return total_pop

def filter_by_state(county_list : list[data.CountyDemographics], string : str) -> list[data.CountyDemographics]:
    special_list = []
    for counties in county_list:
        if counties.state == string:
            special_list.append(counties)
        else:
            continue
    return special_list

def population_by_education(county_list : list[data.CountyDemographics], string) -> float:
    num_of_educated = 0
    for county in range(len(county_list)):
        population = county_list[county].population["2014 Population"]
        for item in county_list[county].education:
            if item == string:
                num_of_educated += ((county_list[county].education[string]/100) * population)
            else:
                continue
    return num_of_educated

def population_by_ethnicity(county_list : list[data.CountyDemographics], string) -> float:
    num_of_races = 0
    for county in range(len(county_list)):
        population = county_list[county].population["2014 Population"]
        for item in county_list[county].ethnicities:

            if item == string:
                num_of_races += ((county_list[county].ethnicities[string]/100) * population)
            else:
                continue
    return num_of_races

def population_below_poverty_level(county_list : list[data.CountyDemographics]) -> float:
    num_below_poverty_level = 0
    for county in range(len(county_list)):
        population = county_list[county].population["2014 Population"]
        for item in county_list[county].income:
            if item == "Persons Below Poverty Level":
                num_below_poverty_level += ((county_list[county].income["Persons Below Poverty Level"]/100) * population)
            else:
                continue
    return num_below_poverty_level

def percent_by_education(county_list : list[data.CountyDemographics], string) -> float:
    total_pop = population_total(county_list)
    total_college_educated = round(population_by_education(county_list, string))
    percent_educated = (total_college_educated/total_pop)*100
    return percent_educated

def percent_by_ethnicity(county_list : list[data.CountyDemographics], string : str) -> float:
    total_pop = population_total(county_list)
    total_by_ethnicity = population_by_ethnicity(county_list, string)
    percent_by_ethnics = (total_by_ethnicity/total_pop)*100
    return percent_by_ethnics

def percent_below_poverty_line(county_list : list[data.CountyDemographics]) -> float:
    total_pop = population_total(county_list)
    total_below_poverty_line = round(population_below_poverty_level(county_list))
    percent_poverty_line = (total_below_poverty_line/total_pop)*100
    return percent_poverty_line


def education_greater_than(county_list : list[data.CountyDemographics], string : str, afloat : float) -> list[data.CountyDemographics]:
    counties_greater_than = []
    for county in range(len(county_list)):
        for item in county_list[county].education:
            if item == string:
                if county_list[county].education[string] > afloat:
                    counties_greater_than.append(county_list[county])
                else:
                    continue
            else:
                continue
    return counties_greater_than

def education_less_than(county_list : list[data.CountyDemographics], string : str, afloat : float) -> list[data.CountyDemographics]:
    counties_less_than = []
    for county in range(len(county_list)):
        for item in county_list[county].education:
            if item == string:
                if county_list[county].education[string] < afloat:
                    counties_less_than.append(county_list[county])
                else:
                    continue
            else:
                continue
    return counties_less_than


def ethnicity_greater_than(county_list : list[data.CountyDemographics], string : str, afloat : float) -> list[data.CountyDemographics]:
    counties_greater_than = []
    for county in range(len(county_list)):
        for item in county_list[county].ethnicities:
            if item == string:
                if county_list[county].ethnicities[string] > afloat:
                    counties_greater_than.append(county_list[county])
                else:
                    continue
            else:
                continue
    return counties_greater_than

def ethnicity_less_than(county_list : list[data.CountyDemographics], string : str, afloat : float) -> list[data.CountyDemographics]:
    counties_less_than = []
    for county in range(len(county_list)):
        for item in county_list[county].ethnicities:
            if item == string:
                if county_list[county].ethnicities[string] < afloat:
                    counties_less_than.append(county_list[county])
                else:
                    continue
            else:
                continue
    return counties_less_than



def below_poverty_level_greater_than(county_list : list[data.CountyDemographics], afloat : float) -> list[data.CountyDemographics]:
    counties_greater_than = []
    for county in range(len(county_list)):
        for item in county_list[county].income:
            if item == "Persons Below Poverty Level":
                if county_list[county].income["Persons Below Poverty Level"] > afloat:
                    counties_greater_than.append(county_list[county])
                else:
                    continue
            else:
                continue
    return counties_greater_than

def below_poverty_level_less_than(county_list : list[data.CountyDemographics], afloat : float) -> list[data.CountyDemographics]:
    counties_less_than = []
    for county in range(len(county_list)):
        for item in county_list[county].income:
            if item == "Persons Below Poverty Level":
                if county_list[county].income["Persons Below Poverty Level"] < afloat:
                    counties_less_than.append(county_list[county])
                else:
                    continue
            else:
                continue
    return counties_less_than
