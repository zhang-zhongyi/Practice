
Author: Zhongyi Zhang
Title: Blue Cross Blue Shield Data Science Engineer Coding Prompt README



Instructions:

My answer "zhongyi_zhang_bcbs_submission.zip" file includes:

1. This zhongyi_zhang_bcbs_README.txt file.

2. The zhongyi_zhang_bcbs_answer.py file is my main code that is available to run in the terminal with input command arguments and will generate cost report txt file written in modular object-oriented programming (OOP) style. I didn't name this file as monthly_cost_report.py like the example in the pdf coding prompt. I included my name in the program file name, but please feel free to rename this program file to what you prefer.

3. The zhongyi_zhang_bcbs_tester.py file is also available to run in the terminal with passing files path as command arguments and can compare the sample cost report file provided by bcbs with the cost report file generated from my code line by line.

4. (Optional) another zhongyi_design.ipynb file that is not written in object-oriented programming (OOP) format and can directly run in even the most basic python IDE/software like Jupyter Notebook with manually typing in the input and output file path in the code and will also work to output the cost report txt file. (Optional, but this file has very detailed explanation to almost every line of my code, so I would like to include here).

5. (Optional) A screenshot_running_successfully_zhongyi_zhang.png screenshot to prove that I am running successfully in my local. This also shows how to pass argument and run my program for both my main program and the tester in the terminal. For convenience purpose, I downloaded and unzipped the "bcbs-coding-exercise.zip" file, and I directly put all my programs in the "examples" folder since all the sample billing_log.txt files and cost_report.txt files are here, so I don't need to type in a long path in my terminal command. If you want to save my programs in somewhere else, please feel free to type in the full path_to_file.txt in the terminal command as arguments. I also tested if I saved under a different path, and it works.

Steps to run my code:

1. download my zhongyi_zhang_bcbs_submission.zip file into the location you prefer.

2. unzip my submission file and move zhongyi_zhang_bcbs_answer.py file and zhongyi_zhang_bcbs_tester.py file to the computer location you prefer.

3. open terminal.

Direction to run my main code (zhongyi_zhang_bcbs_answer.py):

4. cd to the path where you have your zhongyi_zhang_bcbs_answer.py file.

5. if the billing_log you want to use as input also locate under this path, run below command: 

	python zhongyi_zhang_bcbs_answer.py billing_log_(small/medium/large/xlarge).txt zhongyi_zhang_cost_report.txt

   if the billing_log you want to use as input doesn't locate under this path, run below command: 

	python zhongyi_zhang_bcbs_answer.py <"path to the billing_log.txt"> <"path to the zhongyi_zhang_cost_report.txt if you want to generate at somewhere else">

*****
result of running above command in the terminal:

If my code successfully generates the cost report txt file, terminal will output: "Finished. Please check your output path, and the cost report.txt file will be there."

If the path you input is incorrect and computer cannot find the path you input or there is no such file under the path you input, the terminal will output: "Please double check your file path. The path is not found."
*****

Direction to run my tester (zhongyi_zhang_bcbs_tester.py):

6. (please feel free to check the output zhongyi_zhang_cost_report.txt file generated from my code in your path from the previous step) 
   Then run the tester program from the terminal:

   cd to the path where you have your zhongyi_zhang_bcbs_tester.py file
   if both the sample cost_report.txt file you want to use for comparison and the output zhongyi_zhang_cost_report.txt file locate under this current path, run below command: 

	python zhongyi_zhang_bcbs_tester.py cost_report_(small/medium/large/xlarge).txt zhongyi_zhang_cost_report.txt

   if the sample cost_report.txt file you want to use for comparison and/or the output zhongyi_zhang_cost_report.txt file doesn't locate under this path, run below command: 

	python zhongyi_zhang_bcbs_tester.py <"path to your sample cost_report.txt"> <"path to the output zhongyi_zhang_cost_report.txt">

*****
result of running above command in the terminal:

My tester py file will compare both txt files line by line and will output any line that unmatched both in file 1 and in file 2 directly in the terminal.

If every line matches, the terminal will output: "Great! Every line matches between the two files."

If the path to any of the txt files is incorrect or the file doesn't locate under the path you input, the terminal will output: "Please double check your file path. The path is not found."
*****

7. Done. I have tested successfully in my local. It should directly be able to generate the zhongyi_zhang_cost_report.txt file. 
By testing with your sample cost_report_small.txt, cost_report_medium.txt, and cost_report_large.txt file, every line matches. 
Please feel free to send me an email "zhongyi.zhang1995@gmail.com" to let me know if you have any questions to run my codes in the terminal or to my instruction guidance, or if you find any line unmatched.




************************************************************************************************************************************************

Documentation of my design decisions of my code including my thought process:

By reading the coding prompt,
There are two key things all related to orders I really concerned with:

1. The output txt file should be in chronicle order of the month year format

2. The output txt file members and providers name under each month-year should be in the same declared order from the input billing_log file, and always members first, then healthcare providers.



Detail Steps on how I solved the problem:

1. In the code of my modular design, I first need to import the argparse package for creating command arguments to let me pass arguments in the terminal command.

2. After initialize parameters in the class "Billing" I created, I will need a method "reader()" to read/extract the input billing_log.txt file. Read line by line and append into a list.

3. Then the next method "extract_declared_orders()" I have is to extract and record the declared orders of the members and healthcare providers into a list: members first then providers.

4. Then I created a method "extract_bills()" to extract only Bills record into a list and cleaned the data into a nested list in below format:

   [healthcare providers name, members name, month in "YYYY-mm-01", amount, letter format of month year]

   convert YYYY-mm-01 into datetime datatype for sorting, and convert amount into float datatype for adding later.
   Sort the nested list by the third element in each sub-list element, which is by month into chronicle order.
   In this method I used duque data structure. This is a basic open-source data structure that allows me to manage a list from both ends including appendleft() and popleft() methods.
   I also used stack algorithms, which stand for last-in-first-out (LIFO).

5. The next method "data_cleaning()" is to clean the above data list. Since the elements in my list is already in the chronicle/time order, I don't need the third element: the number format of month in "YYYY-mm-01".
   The output of this method will be like
   [[letter format of month year, members name, amount], 
    [letter format of month year, members name, amount],
    [letter format of month year, members name, amount],
    ......
    [letter format of month year, providers name, amount],
    [letter format of month year, providers name, amount],
    [letter format of month year, providers name, amount],
    ......]

6. Then I created the "calculating_bills()" method to accumulate/adding the bill amount of each member/provider per month-year, and write into a nested dictionary, something like this:
	{
	 'January 2021': {'A': 50, 'B': 100, 'C': 70}
	 'February 2021': {'B': 80, 'D': 170}
	 'April 2021': {'A': 230, 'M': 180, 'L': 320}
	 ......	
	}

7. The next method is "formatting()" which is used to format the above nested dictionary including match the order of each sub-dictionary under each month-year into the declared order I created for recording at the beginning in step 3. Then adding dollar sign "$" in front of each bill amount, separated by comma, and always keep two decimal places.

8. The last method is to create a "writer()" method to write the above nested dictionary into the txt file in the format the prompt required.

The last thing is to have the " if __name__ == '__main__': " statement to allow me to run in the terminal for this program.
Write a "try" and "except" statement to print the result in the terminal,
    try: 
        <run above methods in order>
	print("Finished. Please check your output path, and the cost report.txt file will be there.")

    except FileNotFoundError:
        print("Please double check your file path. The path is not found.")

If the path is incorrect, the terminal will print "Please double check your file path. The path is not found." instead of just showing an error.

This will be the design of my code.

My zhongyi_zhang_bcbs_tester.py program is a pretty simple program with adding the arguments for both file1 and file2. Then read file1 and read file2 and compare line by line. The zhongyi_zhang_bcbs_tester.py will print all the lines unmatched in file1.txt and file2.txt in the terminal. If every line matches, the terminal will output: "Great! Every line matches between the two files."
If the path to any of the txt files is incorrect or the file doesn't locate under the path you input, the terminal will output: "Please double check your file path. The path is not found."

************************************************************************************************************************************************

Note:
(As the screenshot.png shows) I compared all three cost_report_small.txt, cost_report_medium.txt, and cost_report_large.txt files, and all the line matches with the txt file generated from my code from terminal. It is working in my local. I also tried the billing_log_xlarge.txt file, and the terminal finished successfully and generated the cost_report.txt file instantly like below 5 seconds on my MacBook Pro. (My MacBook Pro is 2020 or 2021 version)

Please feel free to let me know if you have any questions regarding my code design, or if you cannot run my code or find any line unmatched. 
I would like to explain more about my thoughts and my codes. Thank you!

email: zhongyi.zhang1995@gmail.com
phone: +1 517-775-6621

