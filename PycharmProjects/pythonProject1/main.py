# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# import pandas as pd
# import tensorflow as tf
# import keras
# def decodeString(s: str):
#     def build(encoded):
#             digit =''
#             idx = 0
#             decoded = ''
#             while idx < len(encoded) and encoded[idx] !=']':
#                 # Start Recursion on open bracket
#                 if encoded[idx] == '[':
#                     res,i = build(encoded[idx+1:])
#                     # print(res,i)
#                     decoded += int(digit) * res
#                     #jump index based on encoded inner string len
#                     idx += i + 1
#                     #reset digit
#                     digit= ''
#                 elif encoded[idx].isalpha():
#                     decoded += encoded[idx]
#                 else:
#                     digit +=encoded[idx]
#                 idx+=1
#             return decoded,idx
#
#     return build(s)[0]

import argparse, os
# from argparse import ArgumentParser
#
# parser = ArgumentParser(description="Generate total policy amount txt file.")
# parser.add_argument('input_path', metavar = 'input_path', type=str, help='input txt file path')
# parser.add_argument('output_path', metavar = 'output_path', type=str, help='output txt file path')
#
# args = parser.parse_args()
# input_path = args.input_path
# output_path = args.output_path
#
# def calculation(input_path: str, output_path: str):
#     with open(input_path) as w:
#         policy = [item.lstrip().rstrip() for item in w.readlines()]
#
#     members_list = []
#     providers_list = []
#     for i in policy:
#         if str(i[0:6]).upper() == 'MEMBER' and i[7:] not in members_list:
#             members_list.append("* " + i[7:])
#         elif str(i[0:8]).upper() == 'PROVIDER' and i[9:] not in providers_list:
#             providers_list.append("* " + i[9:])
#
#     order = members_list + providers_list
#
#     all_bills = [i for i in policy if str(i[0:4]).upper() == 'BILL']
#
#     from collections import deque
#     bills = []
#     for i, j in enumerate(all_bills):
#         bills.append(deque())
#         stack = j.split(' ')[1:]
#         for k in j.split(' ')[-1:-4:-1]:
#             bills[i].appendleft(stack.pop())
#         bills[i].appendleft(' '.join(stack))
#     bills = [list(i) for i in bills]
#     for i in bills:
#         i[-1] = float(i[-1])
#
#     def convert_month_year(l: list):
#         for i in l:
#             i[-2] = i[-2][0:8] + '01'
#             if i[-2][5:7] == '01':
#                 i.append('January ' + i[-2][:4])
#             elif i[-2][5:7] == '02':
#                 i.append('February ' + i[-2][:4])
#             elif i[-2][5:7] == '03':
#                 i.append('March ' + i[-2][:4])
#             elif i[-2][5:7] == '04':
#                 i.append('April ' + i[-2][:4])
#             elif i[-2][5:7] == '05':
#                 i.append('May ' + i[-2][:4])
#             elif i[-2][5:7] == '06':
#                 i.append('June ' + i[-2][:4])
#             elif i[-2][5:7] == '07':
#                 i.append('July ' + i[-2][:4])
#             elif i[-2][5:7] == '08':
#                 i.append('August ' + i[-2][:4])
#             elif i[-2][5:7] == '09':
#                 i.append('September ' + i[-2][:4])
#             elif i[-2][5:7] == '10':
#                 i.append('October ' + i[-2][:4])
#             elif i[-2][5:7] == '11':
#                 i.append('November ' + i[-2][:4])
#             elif i[-2][5:7] == '12':
#                 i.append('December ' + i[-2][:4])
#         return l
#
#     convert_month_year(bills)
#
#     from datetime import datetime
#     bills.sort(key=lambda x: datetime.strptime(x[2], "%Y-%m-%d"))  # sort by month first for later data preparation
#
#     providers = []
#     members = []
#     for i, j in enumerate(bills):
#         members.append([])
#         providers.append([])
#         members[i].append(j[-1] + ":")
#         members[i].append("* " + j[1])
#         members[i].append(j[-2])
#         providers[i].append(j[-1] + ":")
#         providers[i].append("* " + j[0])
#         providers[i].append(j[-2])
#     members_providers = members + providers  # combine members and providers name into one list.
#     # re-organize the above list and filter only the data I will need later.
#
#     from collections import defaultdict
#     d = {i[0]: dict() for i in members_providers}
#     for i in members_providers:
#         if i[0] not in d.keys():  # this condition shouldn't be used since I already created all the keys in the dictionary
#             d.update({i[0]: dict()})
#         if i[0] in d.keys() and i[1] not in d[i[0]].keys():  # if month and year in the dictionary but members/providers name not in the sub-dictionary
#             d[i[0]].update({i[1]: i[2]})
#         elif i[0] in d.keys() and i[1] in d[i[0]].keys():  # if month and year in the dictionary and members/providers name also in the sub-dictionary, then adding and accumulate the value
#             d[i[0]][i[1]] += i[2]
#
#     for i, j in d.items():
#         d[i] = {m: n for m, n in sorted(j.items(), key=lambda pair: order.index(pair[0]))}
#
#     for i, j in d.items():
#         for k, v in j.items():
#             j[k] = "$" + "{0:,.2f}".format(v)
#
#     with open(output_path, 'w') as f:
#         for month_year, name in d.items():
#             f.write(month_year + '\n')
#             f.write("\n".join(["{}: {}".format(value_key, digit) for value_key, digit in name.items()]))
#             f.write('\n')
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     try:
#         calculation(input_path, output_path)
#         print("Finished. Please check your output path.")
#     except FileNotFoundError:
#         print("Please double check your file path. The path is not found.")

    # print_hi('PyCharm')
    # print(decodeString("3[a]2[bc]"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    try:
        import nume
    except ModuleNotFoundError:
        print("Please check the file path and import the file you want to run.")