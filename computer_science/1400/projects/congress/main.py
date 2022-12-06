def main():
    file = open("./book_data.txt")
    
    books = {}

    for line in file:
        line = line.split("|")
        code = line[2].strip()
        number = line[1]
        text = line[0]

        if code not in books:
            books[code] = []

        books[code].append(
            {
                'number': int(number),
                'len': len(text),
                'text': text,
            }
        )

    file = open("novel_summary.txt", "w")

    for key in books:
        books[key].sort(key = sort_by_number)
        books[key].sort(key = sort_by_length)

        shortest = books[key][len(books[key]) - 1]
        longest = books[key][0]
        average = 0

        file.write(key)
        for line in books[key]:
            file.write(line['text'] + "\n")
            average += line['len']

        average = average / len(books[key])
        
        print(key)
        print("Longest Line(" + str(longest['number']) + ")" + longest['text'])
        print("Shortest Line(" + str(shortest['number']) + ")" + shortest['text'])
        print("Average Line Length:" + str(round(average)))


def sort_by_length(line):
    return line['len']

def sort_by_number(line):
    return line['number']


if __name__ == "__main__":
    main()