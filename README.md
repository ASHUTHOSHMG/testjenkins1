# testjenkins1
How to use it 
# Python Script
Including email of receiver and sender, email server configuration for gmail is smtp.
# Github
In my Github repository - https://github.com/ASHUTHOSHMG/testjenkins1.git
Find the file 'Jenkinstest.py' which contains python script to automate the mail sending to the recipent
# Integrating Github with Jenkins using Pipeline Job
In the jenkins, create a pipeline item
Tick the option 'Build Periodically' under Build triggers, this would build the pipeline every saturday (Jenkins uses cron script to write a small syntax for scheduling the day, time and other related info which can be found under the same option)
![image](https://user-images.githubusercontent.com/65459598/192903291-103b0568-cea3-47b5-9b3f-f34b35cb3a7b.png)
In the pipeline description, select pipeline script
Pipeline script is a jenkins script where we mention to fetch the content from github reporsitory to build and run our program.
We can try sample pipeline script and it gives out the sample script where we need to mention the different stages like checkout ( to check our github repository for the file) and build ( to build our file from the mentioned github repository).
In between in order to generate the pipeline script for the different stages like checkout and build where we are integrating our github with Jenkins, we need to click on the pipeline syntax option and select 'checkout: Checkout from Version Control' option from the sample step and give our github repository link and generate pipeline script, copy the code and paste it back in the code section.
Second time in the pipeline syntax option in order to build the script we need to select 'git:Git' and then generate the syntax.
And at the last we also need to mention the windows batch command, for that again select pipeline syntax and select 'bat: Windows Batch Script' as the sample step and run the pipeline script.
![image](https://user-images.githubusercontent.com/65459598/192905037-0255f846-098d-4fe5-86ed-df24bda993e9.png)

Finally we apply and save the changes and then build the pipeline.
