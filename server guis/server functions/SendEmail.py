from DatabaseFunctions import UserExist
from Key import generate_license_key
from log_management import writing_in_log


def sendMail(user):
    import smtplib
    from email.mime.text import MIMEText
    if UserExist(user.email):
        myEmail = "adirtesler6@gmail.com"
        code = generate_license_key()
        smtp_server = 'smtp.gmail.com'  # Yes, exactly! The line smtp_server = 'smtp.gmail.com' is necessary to connect to Google's email servers (specifically Gmail's SMTP server).
        smtp_port = 587  # This is the port number used to connect to Gmail’s SMTP server using TLS
        msg = MIMEText("error")
        msg = MIMEText(code)
        msg['Subject'] = 'verfication code'
        msg['From'] = myEmail
        msg['To'] = user.email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(myEmail, "xsxs qsnr plfh rtvr")
        server.send_message(msg)
        server.quit()
        update_json_file(user, code)
        writing_in_log(f"User {user.email} got code : {code}")

        return True
    else:
        return False




import os
import json

json_file_path = os.path.dirname(__file__) + r"\CurrentCode.json"


def update_json_file(user, auth):
    new_data = {user.email: auth}

    # אם הקובץ לא קיים, ניצור אותו עם מילון ריק
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump({}, file)

    # נבדוק אם הקובץ ריק או אם יש נתונים תקינים
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:  # במקרה של קובץ לא תקין או ריק
        print("Error: The JSON file is empty or corrupted. Initializing as an empty dictionary.")
        data = {}

    # נוסיף או נשנה את הערכים בקובץ
    data.update(new_data)

    # נכתוב את הנתונים המעודכנים חזרה לקובץ
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)



def getCodeByEmail(user):
    # Check if the JSON file exists
    if not os.path.exists(json_file_path):
        print("JSON file does not exist.")
        return None

    # Open and read the JSON file
    with open(json_file_path, 'r') as file:
        try:
            data = json.load(file)
            # Check if the email exists in the data
            if user.email in data:
                return data[user.email]
            else:
                print("Email not found in the JSON file.")
                return None
        except json.JSONDecodeError:
            print("Error decoding JSON file.")
            return None
