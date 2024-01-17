# Navigating the Data Science Landscape: An In-Depth Analysis of Salary Trends and Market Dynamics

## Deliverables
I will produce a report with the following deliverables:
1. A clear statement of the business task you have selected to investigate
2. A description of all data sources used
3. Documentation of any cleaning or manipulation of data
4. A summary of your analysis
5. Supporting visualizations and key findings
6. Based on what you discover, a list of additional deliverables you think would be helpful to include for further exploration
7. Your top high-level insights based on your analysis


## Overview
1. What type of company does your client represent, and what are they asking you to accomplish?
The client is myself and they are asking me to find out what is a fair wage for entry to mid level data scientist with two years of experience and a masters degree in mathematics in the United States.

2. What are the key factors involved in the business task you are investigating?
The key factors involved are: positions, location, experience, education, and market conditions.

3. What type of data will be appropriate for your analysis?
global and local numerical and categorical data.

4. Where will you obtain that data?
I'll try to find a dataset on Kaggle.

5. Who is your audience, and what materials will help you present to them effectively?

My audience is my interviewer(s), who is/are likely a data scientist or a group of data scientists. I think to present to them effectively, I should use tools commonly used in proffesion such as tableu, Python or R, SQL, and a storyboard to explain my method of analysis.


## Ask
What topic are you exploring?
I am exploring current market wages for people working the data sector.

● What is the problem you are trying to solve?
The problem I am trying to solve is curing my ignorance of the wage norms of people working in the data sector.

● What metrics will you use to measure your data to achieve your objective?
I can use average salary estimates, salary distributions, cost of living adjustments, and trend analysis.

● Who are the stakeholders?
I am the stakeholder since I need this information to make informed negotiations with my audience. Additionally, future employers/companies and interviewers, in the data sector since they could be influenced by my analysis.

● Who is your audience?
My audience is my interviewer(s), who is/are likely a data scientist or a group of data scientists. I think to present to them effectively, I should use tools commonly used in proffesion such as tableu, Python or R, SQL, and a storyboard to explain my method of analysis.

I should have two presentations, one for the technical interviewers and one for the HR person.The technical presentation will focus on methodology, data analysis, and technical insights. For the HR presentation it can focus on the practical implications like salary structure.

● How can your insights help your client make decisions?
 My insights can help me when I am interviewing with companies so I can negotiate from an informed perspective to get the best outcome for both me and the employer. 

## Prepare
I have found some data from Kaggle called 'Jobs and Salaries in Data Science, Salary trends in Data-Related Careers' by Hummaam Qaasim.
https://www.kaggle.com/datasets/hummaamqaasim/jobs-in-data

Where is your data located?
My data is located locally and on Github: https://github.com/Jassalazar1995/Analysis-of-Salary-Trends
● How is the data organized?
The data has 12 columns and a little over 9000 enteries with no missing values. The data includes both categorical, such as, title and experience level and numerical, such as, salary in USD.
● Are there issues with bias or credibility in this data? Does your data ROCCC?
This data does seem to be reliable since it is complete and it is unclear if it is accucate but brief google searches seem to indicate that it is inline with other averages. It is unclear if this data is bias.
The data is original.
The data is comprehensive.
The data is going up to 2023, so the data is current. Therefor the data ROCCCs.
The data is cited, coming from: https://ai-jobs.net/salaries/2023/
● How are you addressing licensing, privacy, security, and accessibility?
The data is an open, The licensor has granted me a worldwide royalty-free, non exclusive, perpetual, irrevocable copyright license to do what I will be doing with the data, refer to https://www.kaggle.com/datasets/hummaamqaasim/jobs-in-data and https://opendatacommons.org/licenses/dbcl/dbcl-10.txt
● How did you verify the data’s integrity?
I checked the website the data comes from, https://ai-jobs.net/salaries/2023/ and determined that they are a reputable company respected by the data science community.
● How does it help you answer your question?
It provides the major factors I need to understand salary trends such as Salary, job category, job title, employee residence, and experience level 
● Are there any problems with the data?
The only problem with the data is that it is very clean. This is an issue because it doesn't allow me to effectively display the cleaning process.

 Download data and store it appropriately.
● Identify how it’s organized.
The data has 12 columns and a little over 9000 enteries with no missing values. The data includes both categorical, such as, title and experience level and numerical, such as, salary in USD. Reference Analysis.py, function: data_organization(data). 
● Sort and filter the data.
I sorted and filtered the data and saved it into a dictionary where each key is a job title and the value is a dataframe containing the data for that job title sorted by salary in descending order.
● Determine the credibility of the data.
The data is complete and very clean as there are no missing values and the data in the columns are the same type, reference Analysis.py, functions: missing_values(data), check_datatype(data) data_organization(data). 