import Functions
import build_data
used_data = build_data.get_data()

def command_creation(line):
    line = line.translate(str.maketrans({':':'@', '.':'@'}))
    linelist = line.split('@')
    linelist = [item.strip() for item in linelist]
    return linelist
#command_creation("percent:Ethnicities.Two or More Races")

def check_float(val):
    try:
        val = float(val)
        return val
    except ValueError:
        return False

def check_function_func(lists):
    global used_data
    if lists[2] == 'Percent 65 and Older':
        return True
    elif lists[2] == 'Percent Under 18 Years':
        return True
    elif lists[2] == 'Percent Under 5 Years':
        return True
    elif lists[2] == "Bachelor's Degree or Higher":
        return True
    elif lists[2] == 'High School or Higher':
        return True
    elif lists[2] == 'American Indian and Alaska Native Alone':
        return True
    elif lists[2] == 'Asian Alone':
        return True
    elif lists[2] == 'Black Alone':
        return True
    elif lists[2] == 'Hispanic or Latino':
        return True
    elif lists[2] == 'Native Hawaiian and Other Pacific Islander Alone':
        return True
    elif lists[2] == 'Two or More Races':
        return True
    elif lists[2] == 'White Alone':
        return True
    elif lists[2] == 'White Alone, not Hispanic or Latino':
        return True
    elif lists[2] == 'Per Capita Income':
        return True
    elif lists[2] == 'Persons Below Poverty Level':
        return True
    elif lists[2] == 'Median Household Income':
        return True
    elif lists[2] == '2010 Population':
        return True
    elif lists[2] == '2014 Population':
        return True
    elif lists[2] == 'Population Percent Change':
        return True
    elif lists[2] == 'Population per Square Mile':
        return True
    else:
        used_data = data_swap()
        return False

def data_swap():
    used_data = build_data.get_data()
    return used_data


def comparison_func(linelists):
    global used_data
    if linelists[0] == 'filter-gt':
        if linelists[1] == 'Education':
            if not check_float(linelists[3]):
                print("Not a valid float value in line",i)
                used_data = data_swap()
            elif check_function_func(linelists):
                if len(linelists) >= 5:
                    print("Not a valid argument in line", i)
                    used_data = data_swap()
                else:
                    return Functions.education_greater_than(used_data, linelists[2], float(linelists[3]))
            else:
                print("Not a valid argument in line",i)
                used_data = data_swap()
        elif linelists[1] == 'Ethnicities':
            if not check_float(linelists[3]):
                print("Not a valid float value in line",i)
                used_data = data_swap()
            elif check_function_func(linelists):
                if len(linelists) >= 5:
                    print("Not a valid argument in line", i)
                    used_data = data_swap()
                else:
                    return Functions.ethnicity_greater_than(used_data, linelists[2], float(linelists[3]))
            else:
                print("Not a valid argument in line", i)
                used_data = data_swap()
        elif linelists[1] == 'Income':
            return Functions.below_poverty_level_greater_than(used_data, linelists[3])
        else:
            print("System Error, comparison not in database (filter-gt)")
            used_data = data_swap()
    elif linelists[0] == 'filter-lt':
        if linelists[1] == 'Education':
            if not check_float(linelists[3]):
                print("Not a valid float value in line",i)
                used_data = data_swap()
            elif check_function_func(linelists):
                if len(linelists) >= 5:
                    print("Not a valid argument in line", i)
                    used_data = data_swap()
                else:
                    return Functions.education_less_than(used_data, linelists[2], float(linelists[3]))
            else:
                print("Not a valid argument in line", i)
                used_data = data_swap()
        elif linelists[1] == 'Ethnicities':
            if not check_float(linelists[3]):
                print("Not a valid float value in line",i)
                used_data = data_swap()
            elif check_function_func(linelists):
                if len(linelists) >= 5:
                    print("Not a valid argument in line", i)
                    used_data = data_swap()
                else:
                    return Functions.ethnicity_less_than(used_data, linelists[2], float(linelists[3]))
            else:
                print("Not a valid argument in line",i)
                used_data = data_swap()
        elif linelists[1] == 'Income':
            return Functions.below_poverty_level_less_than(used_data, linelists[3])
        else:
            print("System Error, comparison not in database (filter-lt)")
    elif linelists[0] == 'population':
        if linelists[1] == 'Education':
            if check_function_func(linelists):
                return Functions.population_by_education(used_data, linelists[2])
            else:
                print("Not a valid argument in line", i)
        elif linelists[1] == 'Ethnicities':
            if check_function_func(linelists):
                return Functions.population_by_ethnicity(used_data, linelists[2])
            else:
                print("Not a valid argument in line", i)
        elif linelists[1] == 'Income':
            if check_function_func(linelists):
                return Functions.population_below_poverty_level(used_data)
            else:
                print("Not a valid argument in line", i)
        else:
            print("System Error, comparison not in database (population)")
    elif linelists[0] == 'percent':
        if linelists[1] == 'Education':
            return Functions.percent_by_education(used_data, linelists[2])
        elif linelists[1] == 'Ethnicities':
            return Functions.percent_by_ethnicity(used_data, linelists[2])
        elif linelists[1] == 'Income':
            return Functions.percent_below_poverty_line(used_data)
        else:
            print("System Error, comparison not in database (percent)")


def display_func(data_list):
    for item in data_list:
        print('----------',item.county,",",item.state,'----------')
        print("Population:",item.population['2014 Population'])
        print("Age:")
        print("\t > 5 years:",item.age['Percent Under 5 Years'],"%")
        print("\t > 18 years:",item.age['Percent Under 18 Years'],"%")
        print("\t <= 65 years:",item.age['Percent 65 and Older'],"%")
        print("Education:")
        print("\t Bachelor's Degree or Higher:",item.education["Bachelor's Degree or Higher"],"%")
        print("\t High School or Higher:",item.education["High School or Higher"],"%")
        print("Ethnicities:")
        print("\t American Indian and Alaska Native Alone:",item.ethnicities['American Indian and Alaska Native Alone'],"%")
        print("\t Asian Alone:",item.ethnicities['Asian Alone'],"%")
        print("\t Black Alone:",item.ethnicities['Black Alone'],"%")
        print("\t Hispanic or Latino:",item.ethnicities['Hispanic or Latino'],"%")
        print("\t Native Hawaiian and Other Pacific Islander Alone:",item.ethnicities['Native Hawaiian and Other Pacific Islander Alone'],"%")
        print("\t Two or More Races:",item.ethnicities['Two or More Races'],"%")
        print("\t White Alone:",item.ethnicities['White Alone'],"%")
        print("\t White Alone, not Hispanic or Latino:",item.ethnicities['White Alone, not Hispanic or Latino'],"%")
        print("Income:")
        print("\t Per Capita Income: $",item.income['Per Capita Income'])
        print("\t Persons Below Poverty Level:",item.income['Persons Below Poverty Level'],"%")
        print("\t Median Household Income: $",item.income['Median Household Income'])



def command_argument(command_line):
    global i
    global used_data
    i = 1
    try:
        with open(command_line) as file:
            print("% python3 hw4.py", command_line)
            print(len(used_data),"records loaded")
            for line in file:
                linelist = command_creation(line)
                line = line.strip()
                if not line.strip():
                    continue
                if line == 'population-total':
                    print("2014 Population:", Functions.population_total(used_data))
                elif linelist[0] == 'filter-state':
                    linelist[1].upper()
                    filtered_data = Functions.filter_by_state(used_data, linelist[1])
                    used_data = filtered_data
                    print("Filter: state ==",linelist[1],"(",len(used_data),"entries)")
                    if len(used_data) == 0:
                        print("there are zero entries in this filter")
                        break
                elif linelist[0] == 'display':
                    display_func(used_data)
                elif linelist[0] == 'filter-gt':
                    used_data = comparison_func(linelist)
                elif linelist[0] == 'filter-lt':
                    used_data = comparison_func(linelist)
                elif linelist[0] == 'population':
                    print("2014",linelist[1],linelist[2],":",comparison_func(linelist))
                elif linelist[0] == 'percent':
                    print("2014",linelist[1],linelist[2],":",comparison_func(linelist),"%")
                elif line == 'population-total':
                    print("2014 Population:",Functions.population_total(used_data))
                else:
                    print("line:",i,"in",command_line,"has no valid argument to run, please take a look.")
                    used_data = data_swap()
                    continue
                i += 1
    except FileNotFoundError:
        print("Error, File not found. File may have been typed in incorrectly")


#main()
command_argument("task2_d.ops")

