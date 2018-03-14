# Email guesser

A simple python-based tool for generating and validating email address based on given first/last name and birth year

Usage: ```python email_guesser.py -f <firstname> -l <lastname> -y <year> -d <domain>```

e.g. ```python email_guesser.py -f John -l Smith -y 1982 -d gmail.com```

should generate:
- smithjohn@gmail.com
- smithj@gmail.com
- smithjohn1@gmail.com
- jsmith1@gmail.com
- johnsmith2@gmail.com
- smithjohn2@gmail.com
- jsmith2@gmail.com
- johnsmith3@gmail.com
- smithjohn3@gmail.com
- jsmith3@gmail.com
- johnsmith4@gmail.com
- smithjohn4@gmail.com
- jsmith4@gmail.com
- smithj4@gmail.com
- jsmith5@gmail.com
- smithjohn82@gmail.com
- jsmith82@gmail.com
- smithj82@gmail.com
