import getopt
import sys

from validator import generate_emails, validate


def main(argv):
    firstname = ""
    lastname = ""
    domain = ""
    year = -1
    r = 5
    separators = []

    usage_info = 'Usage: python email_guesser.py -f <firstname> -l <lastname> -y <year> -d <domain> -s <separators> -r <range>'

    try:
        opts, args = getopt.getopt(argv, "hf:l:y:d:s:r:",
                                   ["firstname=", "lastname=", "year=", "domain=", "separators=", "range="])
    except getopt.GetoptError:
        print 'Invalid parameters'
        print usage_info
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print usage_info
            sys.exit()
        elif opt in ("-f", "--firstname"):
            firstname = arg
        elif opt in ("-l", "--lastname"):
            lastname = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-d", "--domain"):
            domain = arg
        elif opt in ("-s", "--separators"):
            separators = list(arg)
        elif opt in ("-r", "--range"):
            r = int(arg)

    emails = generate_emails(firstname, lastname, domain, year, separators, r)
    print "Generated list of", len(emails), "emails"
    print "Validating emails..."
    valid_emails = validate(emails)
    print "\nFound valid emails: "
    if len(valid_emails) == 0:
        print "None"
    else:
        for email in valid_emails:
            print email


if __name__ == "__main__":
    main(sys.argv[1:])
