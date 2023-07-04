
"""
# Author: Zhongyi Zhang
# Title: BCBS Data Science Engineer Coding Prompt Tester

# This .py file is created for testing the output cost report txt file
# check if the output cost report file matches with the exmpale cost report txt file line by line

# open terminal, cd to where this .py tester file locate
# run below command:
python zhongyi_zhang_bcbs_tester.py <"path_to_file1.txt"> <"path_to_file2.txt">
"""

from argparse import ArgumentParser

parser = ArgumentParser(description="Test the output cost report txt file.")
parser.add_argument('input_path_file', metavar = 'input_path_file', type=str, help='input txt file path')
parser.add_argument('output_path_file', metavar = 'output_path_file', type=str, help='output txt file path')

args = parser.parse_args()
input_path_file = args.input_path_file
output_path_file = args.output_path_file

# testing the file in the command.
if __name__ == '__main__':
    try:
        file1 = open(input_path_file,'r')
        file2 = open(output_path_file,'r')
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
        unmatches_in_file1 = []
        unmatches_in_file2 = []
        for i in range(len(file1_lines)):
            if file1_lines[i] != file2_lines[i]:
                print("Line " + str(i+1) + " doesn't match.")
                print("--------------------")
                print("File1: " + file1_lines[i])
                print("File2: " + file2_lines[i])
                unmatches_in_file1.append(file1_lines[i])
                unmatches_in_file2.append(file2_lines[i])
        
        if not unmatches_in_file1 and not unmatches_in_file2:
            print("Great! Every line matches between the two files.")

        file1.close()
        file2.close()
    except FileNotFoundError:
        print("Please double check your file path. The path is not found.")
        

