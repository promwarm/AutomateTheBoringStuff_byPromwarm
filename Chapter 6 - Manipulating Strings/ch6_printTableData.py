tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David!'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    max_length = 0
    count_lists = len(table) # 3
    # table must consist of one or more lists
    table_len = []
    for lijst in table:
        for item in lijst:
            if len(item)>int(max_length): max_length=len(item)
        table_len.append(max_length+1)
        max_length = 0

    for x in range(4):
        iteration = 0
        for y in range(3):
            #print (y,x, iteration)
            print(tableData[y][x].rjust(table_len[y]), end='')
            if y == 2: print('')
            iteration += 1

printTable(tableData)