import requests
import sys

def main():

    madlib_lengths = userQueryLength()

    while True:
        if not madlib_lengths['min'].isnumeric() or not madlib_lengths['max'].isnumeric():
            print("Invalid entries, please try again. Entry must be a positive integer.")
            madlib_lengths = userQueryLength()
        elif int(madlib_lengths['min']) <= 0 or int(madlib_lengths['max']) <= 0:
            print("Invalid entries, please try again. Entry must be a positive integer.")
            madlib_lengths = userQueryLength()
        else:
            break

    if int(madlib_lengths['min']) > int(madlib_lengths['max']):
        madlib_lengths['min'], madlib_lengths['max'] = madlib_lengths['max'], madlib_lengths['min']

    base_url = "http://madlibz.herokuapp.com/api/random"
    madlib = requests.get(base_url, params={'maxlength':madlib_lengths['max'], 'minlength':madlib_lengths['min']})

    if madlib.status_code != 200:
        print(f"API Error. Status code: {madlib.status_code}")
        sys.exit(-1)

    madlib = madlib.json()

    title = madlib['title']

    print("\n")
    print("Madlib starting!")
    print("\n")
    print(title)
    print("\n")

    print(userQueryLib(madlib))



def userQueryLength():
    min_length = input("Please enter the minimum number of entries you would like to play with? ")
    max_length = input("Please enter the maximum number of entries you would like to play with? ")
    return {"min":min_length, "max":max_length}

def userQueryLib(madlib):
    blanks = madlib['blanks']
    values = madlib['value']

    madlib_result = ""

    for entry_type, entry_query in zip(blanks, values):
        curr_entry = input(f"Please enter a {entry_type}: ")
        madlib_result = madlib_result + entry_query + curr_entry

    return madlib_result

if __name__ == "__main__":
    main()
