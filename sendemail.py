import yagmail

user = 'throwaway195195@gmail.com'
app_password = 'ourlmcbmfapfugbo'
to = 'austingibb@gmail.com'

def sendemail(body="", subject="3060 Alert"):
    content = [body]

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')