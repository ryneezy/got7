## got7

A fun script to spam your friends funny giphy images using Twilio MMS.

#### Installation
```bash
$ virtualenv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
```
Edit `got7.py` and input your Twilio Account Sid, Auth Token, and a
Twilio phone number for

```
ACCOUNT_SID
AUTH_TOKEN
FROM_NUMBER
```

#### Usage

```bash
got7.py -q "funny giphy query" --body "message body" --to "E.164 Formatted Phone Numbers"

```

For Example:
```bash
got7.py -q "cats" --body "hello cats" --to "+11111111111" "+12222222222" "+13333333333"

```
