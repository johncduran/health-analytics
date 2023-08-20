# health-analytics
This repository is a primer for HHA 504/507
## explanation 
In this code I created a function that would calculate the body fat percentage of an individual. Once the code is run it will ask you to put in your weight, height, age and gender as these are all variables used in the calculation. I decided this would be used as the function since BMI is a component used in both the male and female formulas. The if/else statement first starts by going through and performing the formulas based on if the person is male or female. The only differnce between them is the last number. Then in case there is some issue with how the user inputted the their gender I added the else statement to give them a bit of help to write it correctly since it would be case sensitive. 
### expected output
Once run the user will be prompted to enter their weight, height, gender and age. I used the following info as an exmaple and it seemed to have worked.

Enter weight in pounds: 130
Enter height in inches: 68
Enter gender (male/female): male
Enter age: 23
Male body fat percentage: 12.807128027681664

As you can see if will output the body fat as a float. 
The only issues that would come up that I noticed would be if a float gets intputted into one of the variables or if a capitalized character gets inputted in the male or female variable