# MailingList
Mailing tool for EHS CS Council
Download the packages first. Type in ‘pip install jinja2 openpyxl’
Once done, on the code, the places where I’ve marked, #1, #2, etc, are places to edit.
#1 - This is the sender’s email which is in this case, ehscscouncil@gmail.com
#2 - the password of the account
#3 - the path to the excel spreadsheet in your computer
#4 - the path to the text file containing the script. This should be a text file.

Important info: 
> Make sure the word document is saved as a Plain text file and not a word document itself. 
> The content on the excel should be arranged as rows in the following format—> to, CC, Grade, Name, Author, Date, Attachments.
> The format of the text file should be:
Dear {{name}},

We are hoping to facilitate Hour of Code activities for your {{grade}} classroom on {{date}}.

Best,
{{author}}
> The script can be edited and more text text can be added without disturbing the text in the wrapped format.
> The smtp port number should always be 528(which is what is right now), unless we don’t use gmail for sending the email

