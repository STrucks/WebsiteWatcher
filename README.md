# WebsiteWatcher

This project is a simple watcher on a website to see if a certain 
product gets available.

## Requirements
+ A SMTP server must be running on your localhost to notify when the
website has changed.
+ Windows 10 as host system (tested on Windows 10.0)

## Environment Variables
To set the sender and receiver, use the following environment variables:

+ ``SENDER``: your email address of your Account on the SMTP.
+ ``RECEIVER``: the email that will receive the emails

## Run the program
### Run the executable program
Run the following commands 
```
SET RECEIVER="your@email.com"
SET SENDER="smtp@address.com"
dist/__main__.exe
```

### Run the code
Make sure to use python 3.8.6 or higher. 
Creating a virtual environment is strongly advised.
Run ``pip install -r requirements.txt``
Then, run 
```
SET RECEIVER="your@email.com"
SET SENDER="smtp@address.com"
python __main__.py
```





