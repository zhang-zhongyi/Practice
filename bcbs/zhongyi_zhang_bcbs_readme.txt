Author: Zhongyi Zhang
Title: Blue Cross Blue Shield Data Science Engineer Coding Prompt Readme

Instructions:

My answer zip file includes 
1. this zhongyi_zhang_readme.txt file, 
2. the zhongyi_zhang_bcbs_answer.py file that is available to run in the terminal with input command arguments and will generate cost report txt file written in modular object-oriented programming (OOP) style
3. the zhongyi_zhang_bcbs_tester.py file that is also available to run in the terminal with input command arguments and can compare the sample cost report file provided by bcbs with the cost report file generated from my code line by line
4. another .py file that is not written in object-oriented programming (OOP) format and can directly run in even the most basic python software like Jupyter notebook with manually typing in the input and output file path in the code. (Optional, but I would like to include here)

Steps to run my code:
1. download my answer zip file into the location you prefer
2. unzip my answer file and move zhongyi_zhang_bcbs_answer.py file and zhongyi_zhang_bcbs_tester.py file to the computer location you prefer
3. open terminal
4. cd to the path where you put your zhongyi_zhang_bcbs_answer.py file

5. if the billing_log you want to use as input also locate under this path, run command: python zhongyi_zhang_bcbs_answer.py billing_log_(small/medium/large/xlarge).txt zhongyi_zhang_cost_report.txt
   if the billing_log you want to use as input doesn't locate under this path, run command: python zhongyi_zhang_bcbs_answer.py <"path to the billing_log.txt file"> <"path to the zhongyi_zhang_cost_report.txt file if you would like to generate at somewhere else">

if

6. (please feel free to check the output zhongyi_zhang_cost_report.txt file generated from my code) 
   Then run the tester program from the terminal:
   if the zhongyi_zhang_bcbs_tester.py locate under this current path, run command: python zhongyi_zhang_bcbs_tester.py cost_report_(small/medium/large/xlarge).txt zhongyi_zhang_cost_report.txt
   if the billing_log you want to test doesn't locate under this path, run command: python zhongyi_zhang_bcbs_answer.py <"path to your sample cost_report file"> <"path to the zhongyi_zhang_cost_report.txt file where you output">

7. If everything matches