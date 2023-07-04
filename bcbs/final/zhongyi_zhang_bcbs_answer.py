
"""
# Author: Zhongyi Zhang
# Title: BCBS Data Science Engineer Coding Prompt Answer Main Program (Available to run in terminal passing input and output path_to_file.txt)

# type in input file path and output file path pass as arguments in the command line
# so that I can directly run the below command in terminal
# first cd to the path where this py file locate, then run below command in terminal:
# $ python zhongyi_zhang_bcbs_answer.py <"path_to_billing_log.txt"> <"path_to_output_cost_report.txt">
# Then go to the output file path and I will get the output cost_report.txt file
"""

from argparse import ArgumentParser
from collections import deque
from datetime import datetime

class Billing:
    def __init__(self):
        """
        # initialize parameters, create input and output path as arguments in the command line
        """
        parser = ArgumentParser(description="Generate cost report txt file.")
        parser.add_argument('input_path_file', metavar = 'input_path_file', type=str, help='input txt file path')
        parser.add_argument('output_path_file', metavar = 'output_path_file', type=str, help='output txt file path')

        args = parser.parse_args()
        self.input_path_file = args.input_path_file
        self.output_path_file = args.output_path_file
        
        self.all_data = all_data = []
        self.order = order = []
        self.bills = bills = []
        self.members_providers = members_providers = []
        self.d = d = {}
    
    """ 
    # input and output path and file ready in string format; algorithms start from here:
    """ 
    def reader(self):
        """ 
        # open the input txt file, read in lines, and convert into a list with removing leading and trailing white spaces
        """ 
        with open(self.input_path_file) as w:
            self.all_data = [item.lstrip().rstrip() for item in w.readlines()]
        return self.all_data
    
    def extract_declared_orders(self, all_data):
        """ 
        # create a list to record the declared order for members and healthcare providers. Members first, then providers
        """
        members_list = []
        providers_list = []
        for i in self.all_data:
            if str(i[0:6]).upper() == 'MEMBER' and i[7:] not in members_list:
                members_list.append("* " + i[7:])
            elif str(i[0:8]).upper() == 'PROVIDER' and i[9:] not in providers_list:
                providers_list.append("* " + i[9:])

        self.order = members_list + providers_list
        return self.order
    
    def extract_bills(self, all_data):
        """
        # filter for all the bills record from the input billing log txt file and convert into a list array
        # break the all_bills list into nested list to separate members/providers name, date, and amount
        # here I use the deque open-source data structure since I can directly manipulate data from both ends of the list
        # I also applied stack algorithm techniques to always append the popped item from the stack (last-in-first-out)
        
        # no need to have the word "Bill" as the first element
        # only members name, date, and amount 
        # the rest in the stack is the healthcare providers name. convert back to string
        """
        all_bills = [i for i in self.all_data if str(i[0:4]).upper() == 'BILL']

        for i, j in enumerate(all_bills):
            self.bills.append(deque())
            stack = j.split(' ')[1:]    # no need to have the word "Bill"
            for k in j.split(' ')[-1:-4:-1]:    # only members name, date, and amount 
                self.bills[i].appendleft(stack.pop()) 
            self.bills[i].appendleft(' '.join(stack))    # the rest in the stack is the healthcare providers name. convert back to string
        self.bills = [list(i) for i in self.bills]    # convert back to list from deque

        """
        # convert the amount into float datatype 
        """
        for i in self.bills: 
            i[-1] = float(i[-1])
            
        """
        # create a function to convert date into month format "YYYY-mm-01"
        # appending a new letter-format month year element at the end of each bill
        """
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

        convert_month_year(self.bills) # apply the above function to the list
        
        """
        # convert into datetime datatype and sort by month first for later data preparation
        """
        self.bills.sort(key=lambda x: datetime.strptime(x[2], "%Y-%m-%d"))
        return self.bills
    
    def data_cleaning(self, bills):
        """
        # combine members and providers name into one list. re-organize the list and filter only the data I will need later
        # I will only need the letter-format of month year, members/providers name, and amount
        # adding a "* " in front of members and providers name
        """
        providers = []
        members = []
        for i, j in enumerate(self.bills):
            members.append([])
            providers.append([])
            members[i].append(j[-1] + ":")
            members[i].append("* " + j[1]) # adding a "* " in front of members name
            members[i].append(j[-2])
            providers[i].append(j[-1] + ":")
            providers[i].append("* " + j[0]) # adding a "* " in front of healthcare providers name
            providers[i].append(j[-2])
        self.members_providers = members + providers  
        
        return self.members_providers
    
    def calculating_bills(self, members_providers):
        """
        # This method is to create a dictionary to sum the amount group by month-year and member/provider name
        # first create a nested dictionary with keys as month-year
        # members and providers name will be the keys of sub-dictionary, values will be the accumulated amount per member/provider per month-year
        # if month-year in the dictionary but members/providers name not in the sub-dictionary, create the key value pair with the amount
        # if month-year in the dictionary and members/providers name also in the sub-dictionary, adding/accumulate the amount    
        """
        self.d = {i[0]: dict() for i in self.members_providers} 
        for i in self.members_providers:
            if i[0] not in self.d.keys():  # this condition shouldn't be used since I already created all the month-year as keys in the dictionary. just in case
                self.d.update({i[0]: dict()})
            if i[0] in self.d.keys() and i[1] not in self.d[i[0]].keys():
                self.d[i[0]].update({i[1]: i[2]})
            elif i[0] in self.d.keys() and i[1] in self.d[i[0]].keys():  
                self.d[i[0]][i[1]] += i[2]
        return self.d
    
    def formatting(self, d, order):
        """
        # the above dictionary is in the Bills order for members/providers name,
        # so I need to change to the "declared order" to match with the declared order list I created at beginning
        """
        for i, j in self.d.items():
            self.d[i] = {m: n for m, n in sorted(j.items(), key=lambda pair: self.order.index(pair[0]))}
        
        """
        # for each amount value, adding "$" dollar sign in the front, separated by comma, and round to 2 decimal places
        """
        for i, j in self.d.items():
            for k, v in j.items():
                j[k] = "$" + "{0:,.2f}".format(v)
        
        return self.d
    
    def writer(self, d):
        """
        # To write the above nested dictionary into a cost report txt file with the output path from the terminal command argument
        """
        with open(self.output_path_file, 'w') as f:
            for month_year, name in self.d.items():
                f.write(month_year + '\n')
                f.write("\n".join(["{}: {}".format(value_key, digit) for value_key, digit in name.items()]))
                f.write('\n')

"""
# testing the file in the command
# run above methods from the class in order
"""
if __name__ == '__main__':
    try:
        billing_logs = Billing()
        data = billing_logs.reader()
        declared_order = billing_logs.extract_declared_orders(data)
        bill = billing_logs.extract_bills(data)
        cleaned_data = billing_logs.data_cleaning(bill)
        amount_hashtable = billing_logs.calculating_bills(cleaned_data)
        final_data = billing_logs.formatting(amount_hashtable, declared_order)
        billing_logs.writer(final_data)
        print("Finished. Please check your output path, and the cost report.txt file will be there.")
    except FileNotFoundError:
        print("Please double check your file path. The path is not found.")

