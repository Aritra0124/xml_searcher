def string_matching(pattern, text, m, n):
    loc = []
    for i in range(0, n - m + 1):
        for j in range(0, m):

            if text[i + j] != pattern[j]:
                break
            if j == m - 1:
                loc.append(i)
                break

    if loc is not None:
        return loc
    else:
        return loc.append(-1)


def item(text, start, end):
    print(text[start:end])


def tag_name_finder(text, start):
    i = 0
    text = text[start:]
    while text[i] != ">":
        i += 1
    tag = text[1:i]
    return tag


def hierarchy_finder(text, start, end):
    tag_name = []
    text = text[start:end]
    start_loc = string_matching("<", text, len("<"), len(text))
    if len(start_loc) != 0:
        print("Hierarchy found \n")
        end_loc = string_matching("</", text, len("</"), len(text))
        for i in range(0, len(end_loc)):
            start_loc.remove(end_loc[i])
        for i in range(0, len(start_loc)):
            tag_name.append(tag_name_finder(text, int(start_loc[i])))
        tags = tag_name

        for i in range(0, len(tags) - 2):
            if tag_name.count(tags[i]) != 1:
                tag_name.remove(tags[i])
        for i in range(0, len(tag_name)):
            d, start_location, end_location, start_tag = tag_finder(tag_name[i], text)
            for j in range(0, len(start_location)):
                item(text, int(start_location[j]) + len(start_tag), end_location[j])
        return 1
    else:
        print("Hierarchy not found \n")
        return 0


def tag_finder(tag, text):
    start_tag = "<" + tag + ">"
    end_tag = "</" + tag + ">"
    start_location = string_matching(start_tag, text, len(start_tag), len(text))
    # print(start_location)  # location checking
    if len(start_location) != 0:
        end_location = string_matching(end_tag, text, len(end_tag), len(text))
        if start_location is not None and end_location is not None:
            return 1, start_location, end_location, start_tag
    else:
        return 0, 0, 0, None


def checker(tag, text):
    f = 0
    flag, start_location, end_location, start_tag = tag_finder(tag, text)
    if flag == 1:
        print("\nTag is found")
        print("Checking if any hierarchy is present in between that tag")
        for i in range(0, len(start_location)):
            f = hierarchy_finder(text, int(start_location[i]) + len(start_tag), end_location[i])
            if f == 0:
                pass
            break
        if f == 0:
            for j in range(0, len(start_location)):
                item(text, int(start_location[j]) + len(start_tag), end_location[j])
    elif flag == 0:
        print("\nNot Found")
    # return start_location, end_location


def main():
    file = str(input("Enter the file name with full file path:\n"))
    obj = input("Enter the tag:\n")
    data = open(file, "r")
    checker(obj, data.read())


main()
