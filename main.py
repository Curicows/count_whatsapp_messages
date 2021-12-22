
def run():
    file = open('messages.txt', encoding='utf-8')
    i = 0

    lines = file.readlines()
    for line in lines:
        datetime = None
        name = ""
        message = ""

        splited = line.split(' - ', 1)
        print(line.split(' - ',1))







    # coun = len(lines)
    # print(coun)



if __name__ == '__main__':
    run()
