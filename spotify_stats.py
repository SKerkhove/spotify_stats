import json
from collections import Counter, defaultdict

DEFAULT_FILE_NAME = "StreamingHistory0.json"


def countAmount(obj, key):
    c = Counter(player[key] for player in obj)
    return dict(c)


def countMSeconds(obj, key):
    d = defaultdict(int)
    for player in json_obj:
        d[player[key]] += player['msPlayed']
    return d


if __name__ == '__main__':
    choice = input("Select stats:"
                   "\n\t(1) Top songs by no of plays"
                   "\n\t(2) Top songs by minutes listened"
                   "\n\t(3) Top artists by no of plays"
                   "\n\t(4) Top artists by minutes listened"
                   "\n\nType the number of your choice\n")
    if choice not in ["1", "2", "3", "4"]:
        print("No valid choice made, will use default choice (1)")
        choice = 1
    else:
        choice = int(choice)

    fileName = input("Input file name:\n(Type 0 for default file " + DEFAULT_FILE_NAME + ")\n")
    if fileName == "0":
        fileName = DEFAULT_FILE_NAME

    with open(fileName,
              encoding='utf8') as f:

        json_obj = json.load(f)

        if choice == 1:
            thing_to_count = "trackName"
            d = countAmount(json_obj, thing_to_count)
        elif choice == 2:
            thing_to_count = "trackName"
            d = countMSeconds(json_obj, thing_to_count)
        elif choice == 3:
            thing_to_count = "artistName"
            d = countAmount(json_obj, thing_to_count)
        elif choice == 4:
            thing_to_count = "artistName"
            d = countMSeconds(json_obj, thing_to_count)

        # Probably not the best way but it works and fairly fast too
        sorted_list = sorted(d.items(),
                             key=lambda x: x[1],
                             reverse=True)
        sorted_dict = dict(sorted_list)

    list_length = input("Please type the length of the list you want:\n"
                        "(i.e. If you want a Top x, type x)\n"
                        "Type 0 to see the entire list\n")
    try:
        list_length = int(list_length)
        if list_length < 0:
            print("That is not an acceptable number, using default of 10 instead")
            list_length = 10
    except:
        print("That is not an acceptable number, using default of 10 instead")
        list_length = 10

    i = 1
    for key in sorted_dict.keys():
        if list_length != 0 and i > list_length:
            break

        if choice in [1, 3]:
            print(
                str(i) + ") " + key + " (with " + str(
                    sorted_dict[key]) + " streams)")
        else:
            minutes_listened = round(sorted_dict[key] / 60000)  # round doesn't do perfect rounding but good enough
            print(
                str(i) + ") " + key + " (with " + str(
                    minutes_listened) + " minutes listened)")
        i += 1

    if choice in [1, 2]:
        print("Total number of songs is ", len(sorted_dict))
    else:
        print("Total number of artists is ", len(sorted_dict))
