Instructions for installing SCEC software.  
----------------------------------------------- 

User of the system can install and use SCEC software using src/ folder. 
- User need to install python3 in their system to start using SCEC system. 
- Once python3 setup in their machine, user can directly run "make" command to install other dependencies and setup. 
- Once all the requirement downloaded using requirement.txt, user can run the "src/src/main.py". 
- If user want some other inputs, "src/test.in" can be updated. 
- To run test cases associated with the SCEC system, "pytest src/testing" can be used for manual run. Otherwise make also contains test for testing modules. 


Manual steps for Linux: 
1. clone repository 
2. make run - to create virtual environment, install dependencies and run main file. 
3. make test - to run the test cases 

Manual steps for Windows: 
1. Install Python >= 3.9.0 
2. Setup "make" in Windows: To easy install http://gnuwin32.sourceforge.net/packages/make.htm install setup file. 
3. Clone github repository 
4. make run - to create virtual environment, install dependencies and run main file. 
5. make test - to run the test cases 
