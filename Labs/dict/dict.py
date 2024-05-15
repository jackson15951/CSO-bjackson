"""
    CS110 Lab
    Dictionary Lab

    Updated By: FIXME1

    CSCI 110
    Date: FIXME2

    Working with Python dictionary (dict) data structure.
"""
import os

# create a mapping of state names to their codes using a dictionary
states = {
     # FIXME3 – add codes for the rest of the states #fixed#
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'CA': 'Sacramento',
    'MI': 'Lansing',
    'FL': 'Tallahassee'
}

# add some more entires to capitalCity dictionary
capitalCity['NY'] = 'Albany'
capitalCity['OR'] = 'Salem'


# FIXME4: Add rest of the states’ capital cities to capitalCity dictionary #fixed#

capitalCity['AL'] = 'Montgomery'
capitalCity['AK'] = 'Juneau'
capitalCity['AZ'] = 'Phoenix'
capitalCity['AR'] = 'Little Rock'
capitalCity['CO'] = 'Denver'
capitalCity['CT'] = 'Hartford'
capitalCity['DE'] = 'Dover'
capitalCity['GA'] = 'Atlanta'
capitalCity['HI'] = 'Honolulu'
capitalCity['ID'] = 'Boise'
capitalCity['IL'] = 'Springfield'
capitalCity['IN'] = 'Indianapolis'
capitalCity['IA'] = 'Des Moines'
capitalCity['KS'] = 'Topeka'
capitalCity['KY'] = 'Frankfort'
capitalCity['LA'] = 'Baton Rouge'
capitalCity['ME'] = 'Augusta'
capitalCity['MD'] = 'Annapolis'
capitalCity['MA'] = 'Boston'
capitalCity['MN'] = 'Saint Paul'
capitalCity['MS'] = 'Jackson'
capitalCity['MO'] = 'Jefferson City'
capitalCity['MT'] = 'Helena'
capitalCity['NE'] = 'Lincoln'
capitalCity['NV'] = 'Carson City'
capitalCity['NH'] = 'Concord'
capitalCity['NJ'] = 'Trenton'
capitalCity['NM'] = 'Santa Fe'
capitalCity['NC'] = 'Raleigh'
capitalCity['ND'] = 'Bismarck'
capitalCity['OH'] = 'Columbus'
capitalCity['OK'] = 'Oklahoma City'
capitalCity['PA'] = 'Harrisburg'
capitalCity['RI'] = 'Providence'
capitalCity['SC'] = 'Columbia'
capitalCity['SD'] = 'Pierre'
capitalCity['TN'] = 'Nashville'
capitalCity['TX'] = 'Austin'
capitalCity['UT'] = 'Salt Lake City'
capitalCity['VT'] = 'Montpelier'
capitalCity['VA'] = 'Richmond'
capitalCity['WA'] = 'Olympia'
capitalCity['WV'] = 'Charleston'
capitalCity['WI'] = 'Madison'
capitalCity['WY'] = 'Cheyenne'



def menu():
    print("""
            Enter one of the menu options:
            [1] Find US state's code given its name
            [2] Find US state's capital given its code
            [3] Find US state's capital given its name
            [4] Exit the program
        """)


def main():
    while True:
        # clear screen
        os.system('clear')
        # print menu
        menu()
        # get menu option
        option = input()
        if option == '4':
            print('SEE YOU AGAIN... GOOD BYE!')
            break

        if option == '1':
            state = input('Enter a US state name: ')
            if state in states:  # check if state is in states dict
                print('Code for {} is {}.'.format(state, states[state]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))
        elif option == '2':
            # FIXME5 - complete menu option 2 #fixed#
            
            capital = input("Enter a US state's capital code: ")
            if capital in capitalCity:  
                print('name for {} is {}.'.format(capital, capitalCity[capital]))
            else:
                print("Sorry! The US state's capital code '{}' NOT found!".format(capital))


        # FIXME6 - complete menu option 3 #fixed#
        elif option == '3': 
            state = input("Enter a US state name: ")
            if state in states:  
                print('Capital for {} is {}.'.format(state, capitalCity[states[state]]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))

        # FIXME7 - handle the case where user enters invalid menu option #fixed#
        else: print('Sorry, that is not an option')
        
        print('Enter to continue...')
        input()


if __name__ == "__main__":
    main()