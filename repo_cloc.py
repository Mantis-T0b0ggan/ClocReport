import smtplib, ssl, getpass, subprocess, pip, sys, os, shutil, re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Global Variables for script
clocExe = "cloc-1.92.exe"
server = 'smtp.gmail.com'
fromEmail = ''
password = ''
toEmail = ''
binDirectory = './bin/'
curDirectory = './'
branch = ''
reg_ex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
gitUrl = ''




# Defining the function to automatically send the Cloc report via e-mail
def sendEmail():
	subject = f('CLOC report of repository {repoName}')
	
	message = MIMEMultipart()
	message['Subject'] = subject
	message['From'] = fromEmail
	message['To'] = toEmail
	
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(clocReport, "rb").read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="'+ clocReport)
	message.attach(part)
	context = ssl.create_default_context()

	print ('Github repo cloc report to ' + toEmail)

	with smtplib.SMTP(smtpServer) as server:
		server.starttls(context = context)
		server.login(fromEmail, password)
		server.sendmail(fromEmail, toEmail, message.as_string())

# Defining function to pull the given Github Repository
def pullRepo():
	repo = repoName()
	if not os.path.exists(curDirectory+repo):
		git.Git(curDirectory).clone(gitUrl)
	print('Pulling git repo now...')

	gitrepo = git.Repo(repo)
	gcmd = git.cmd.Git(repo)
	gcmd.pull()
	gitrepo.git.checkout("-f", branch)
	proc = subprocess.Popen([binDirectory+clocExe,curDirectory+repo, "--csv","--out", clocReport , "--quiet"], stdout=subprocess.PIPE)
	proc.stdout.read()

# Getting the Repository name automatically from the Repo URL
def repoName():
	return(gitUrl[gitUrl.rfind('/') + 1:gitUrl.rfind('.')])

# Confirming input matches a correct e-mail address
def confirm_input():
	if(re.fullmatch(reg_ex, toEmail)):
		print("Valid Email")

	else:
		print("Invalid Email")


#Running the program
confirm_input()	
clocReport = repoName() + branch + ".csv"	
pullRepo()
sendEmail()
