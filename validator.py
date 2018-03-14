from validate_email import validate_email


def generate_emails(firstname, lastname, domain, year=-1, separators=[""], r=5):
    firstname = firstname.lower()
    lastname = lastname.lower()
    emails = []
    sufixes = [""] + [str(i) for i in range(1, r + 1)]
    separators.append("")
    if year != -1:
        sufixes.append(str(year % 100))
    names = [firstname, firstname[0]]

    for separator in separators:
        for sufix in sufixes:
            for name in names:
                # first name + last name
                emails.append(name + separator + lastname + sufix + "@" + domain)
                # last name + first nae
                emails.append(lastname + separator + name + sufix + "@" + domain)

    return emails


def validate(emails):
    def is_valid(email):
        return bool(validate_email(email, verify=True))

    return filter(is_valid, emails)
