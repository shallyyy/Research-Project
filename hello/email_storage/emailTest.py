
import argparse

import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'jamesshally_@hotmail.com'
PASSWORD = 'Hillcrest9'


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email_storage addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    ids = []
    uuids = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
            ids.append(a_contact.split()[2])
            uuids.append(a_contact.split()[3])

    return names, emails, ids, uuids


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def reg_email():
    names, emails, ids, uuids = get_contacts('email_storage/contacts.txt')  # read contacts
    message_template = read_template('email_storage/message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email_storage:
    for name, email , ids, uuid in zip(names, emails, ids, uuids):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), PERSON_UUID=uuid.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Welcome to CS4415!"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="ul id",
                        type=int)
    parser.add_argument("-r", "--register", help="Checks users config",
                        action="store_true")
    args = parser.parse_args()

    if args.register:
        reg_email()



if __name__ == '__main__':
    main()