#!/usr/bin/env python
# coding: utf-8

# In[1]:


# type in input file path and output file path as arguments in the command line
# so that I can directly run the below command in terminal: 
# python billing_calculation_answer_zhongyi_zhang <"input_file_path"> <"output_file_path">
# Then go to the output file path and I will get the output cost_report.txt file.
from argparse import ArgumentParser

parser = ArgumentParser(description="Generate total policy amount txt file.")
parser.add_argument('input_path_file', metavar = 'input_path_file', type=str, help='input txt file path')
parser.add_argument('output_path_file', metavar = 'output_path_file', type=str, help='output txt file path')

args = parser.parse_args()
input_path_file = args.input_path_file
output_path_file = args.output_path_file

# input and output path and file ready in string format; create a function for the calculation algorithms:
def calculation(input_path_file: str, output_path_file: str):
    # open the input txt file, read in lines, and convert into a list with removing leading and trailing white spaces.
    with open(input_path_file) as w:
        policy = [item.lstrip().rstrip() for item in w.readlines()]
    
    # create a list to record the declared order for members and healthcare providers. Always members first, then providers.
    members_list = []
    providers_list = []
    for i in policy:
        if str(i[0:6]).upper() == 'MEMBER' and i[7:] not in members_list:
            members_list.append("* " + i[7:])
        elif str(i[0:8]).upper() == 'PROVIDER' and i[9:] not in providers_list:
            providers_list.append("* " + i[9:])

    order = members_list + providers_list

    # filter for all the bills record from the input billing log txt file and convert into a list array.
    all_bills = [i for i in policy if str(i[0:4]).upper() == 'BILL']
    
    # break the above all_bills list into nested list to separate members'/providers' name, date, and amount
    # here I use the deque open-source data type since I can directly manipulate data from both ends of the list
    # I also applied stack techniques to always append the pop item from the stack (last-in-first-out)
    from collections import deque
    bills = []
    for i, j in enumerate(all_bills):
        bills.append(deque())
        stack = j.split(' ')[1:] # no need to have the word "Bill" as the first element.
        for k in j.split(' ')[-1:-4:-1]: # only members' name, date, and amount
            bills[i].appendleft(stack.pop()) 
        bills[i].appendleft(' '.join(stack)) # the rest in the stack is the healthcare providers' name. convert to string back. 
    bills = [list(i) for i in bills] # convert back to list from deque
    
    # convert the amount into float datatype
    for i in bills: 
        i[-1] = float(i[-1])

    # create a function to convert date into month format "YYYY-mm-01",
    # appending a new letter-format element at the end of each bill
    def convert_month_year(l: list):
        for i in l:
            i[-2] = i[-2][0:8] + '01'
            if i[-2][5:7] == '01':
                i.append('January ' + i[-2][:4])
            elif i[-2][5:7] == '02':
                i.append('February ' + i[-2][:4])
            elif i[-2][5:7] == '03':
                i.append('March ' + i[-2][:4])
            elif i[-2][5:7] == '04':
                i.append('April ' + i[-2][:4])
            elif i[-2][5:7] == '05':
                i.append('May ' + i[-2][:4])
            elif i[-2][5:7] == '06':
                i.append('June ' + i[-2][:4])
            elif i[-2][5:7] == '07':
                i.append('July ' + i[-2][:4])
            elif i[-2][5:7] == '08':
                i.append('August ' + i[-2][:4])
            elif i[-2][5:7] == '09':
                i.append('September ' + i[-2][:4])
            elif i[-2][5:7] == '10':
                i.append('October ' + i[-2][:4])
            elif i[-2][5:7] == '11':
                i.append('November ' + i[-2][:4])
            elif i[-2][5:7] == '12':
                i.append('December ' + i[-2][:4])
        return l

    convert_month_year(bills) # apply the above function to the list
    
    # convert into datetime datatype and sort by month first for later data preparation
    from datetime import datetime
    bills.sort(key=lambda x: datetime.strptime(x[2], "%Y-%m-%d"))

    providers = []
    members = []
    for i, j in enumerate(bills):
        members.append([])
        providers.append([])
        members[i].append(j[-1] + ":")
        members[i].append("* " + j[1]) # adding a "* " in front of members name
        members[i].append(j[-2])
        providers[i].append(j[-1] + ":")
        providers[i].append("* " + j[0]) # adding a "* " in front of healthcare providers name
        providers[i].append(j[-2])
    members_providers = members + providers  # combine members and providers name into one list.
    # re-organize the above list and filter only the data I will need later.
    
    # create a dictionary to sum the amount group by yearmonth and member/provider name
    from collections import defaultdict
    d = {i[0]: dict() for i in members_providers} # create a dictionary with keys as members' and providers' name
    for i in members_providers:
        if i[0] not in d.keys():  # this condition shouldn't be used since I already created all the keys in the dictionary. just in case.
            d.update({i[0]: dict()})
        # if month and year in the dictionary but members/providers name not in the sub-dictionary, create with the amount
        if i[0] in d.keys() and i[1] not in d[i[0]].keys():
            d[i[0]].update({i[1]: i[2]})
        # if month and year in the dictionary and members/providers name also in the sub-dictionary, adding/accumulate the amount    
        elif i[0] in d.keys() and i[1] in d[i[0]].keys():  
            d[i[0]][i[1]] += i[2]
    
    # the above dictionary is in bills order, so I change to the "declared order" with the order list I created at beginning
    for i, j in d.items():
        d[i] = {m: n for m, n in sorted(j.items(), key=lambda pair: order.index(pair[0]))}
    
    # for each amount value, change to string datatype, adding $ dollar sign in the front, separated by comma, and round 2 decimal points
    for i, j in d.items():
        for k, v in j.items():
            j[k] = "$" + "{0:,.2f}".format(v)

    # The above nested dictionary is ready to write into a cost report txt file with the output path from the command.
    with open(output_path_file, 'w') as f:
        for month_year, name in d.items():
            f.write(month_year + '\n')
            f.write("\n".join(["{}: {}".format(value_key, digit) for value_key, digit in name.items()]))
            f.write('\n')

# testing the file in the command.
if __name__ == '__main__':
    try:
        calculation(input_path_file, output_path_file)
        print("Finished. Please check your output path, and the cost report.txt file will be there.")
    except FileNotFoundError:
        print("Please double check your file path. The path is not found.")

