# ClocReport
CLOC report for Checkmarx 
# CLOC Report 

This project was created for technical review by checkmarx interview team. The program is intended to receive Github URL input, run CLOC (Count Lines of Code) 
on a GitHub Repo and e-mail the report as a .CSV file to a given e-mail.
Project currently only support Gmail e-mail accounts

## Getting Started

To Run this program you'll need to run it manually in a Terminal or CMD window and call on the repo_cloc.py file. Once called the user will begin
being querried for user input.

### Prerequisites

The things you need before installing the software.

* A gmail account
* Git installed on machine
* Cloc installed

### Installation

```
$ - Run the program in a terminal or cmd window
$ - Follows prompts in terminal to log-into your email and confirm e-mail of recepient
$ - Enter GitHub Repo URl when prompted
$ - The program will automatically download and run CLOC on the Repo and send the report to the destination e-mail
```

## Usage

An example of the use of this project

```
$ If a user needs a report for how much of their project is written in which programming language. This project can quickly run CLOC on a
given GitHub Repo. The report breaks down the repo into how many LOC are written in Python, PHP, Java, JS, Etc...

```

## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).


* Bugfixing: Project still has some bugs that need to be sorted out to allow for all E-mail accounts to be used
- Also working to display more information to the user as processes are working in the backgorund (E.G - when pulling and running CLOC on Repo
printing info to the user to let them know it's working).
- Need to iron out a few wrinkles in the code that's not allowing Github Repo to be pulled correctly

## Additional Documentation and Acknowledgments

* For more information and programs using CLOC: Dan Lowe - https://github.com/dannyloweatx/checkmarx/blob/master/sendclocreport.py
