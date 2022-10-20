def ml():
    global type_letter
    ml = input("More Letters? (Yes or No)")
    if ml == "Yes" or ml == "yes":
        type_letter = input("Job Offer or Rejection?")
    elif ml == "No" or ml == "no":
        print("Bye")
        quit()
    if type_letter == "Job Offer" or type_letter == "job offer" or type_letter == "Job offer":
        job()
    elif type_letter == "Rejection" or type_letter == "rejection":
        rejection()

def f():
    global fname
    fname = input("f Name?")
    while len(fname) < 2 or len(fname) > 10 or fname.isalpha() == False or fname.istitle() == False:
        print("Input error")
        print("Your name can't contain less than 2 letters, more than 10 letters, anything besides letters from the alphabet and must be capitalized.")
        f()
    last()

def last():
    global lname 
    lname = input("Last Name?")
    while len(lname) < 2 or len(lname) > 10 or lname.isalpha() == False or lname.istitle() == False:
        print("Input error")
        print("Your name can't contain less than 2 letters, more than 10 letters, anything besides letters from the alphabet and must be capitalized.")
        last()
    title()

def title():
    global jobname
    jobname = input("Job Title?")
    while len(jobname) < 10 or jobname.isnumeric():
        print("Input error")
        print("Your job title must contain a minimum of 10 characters without numbers")
        title()
    if type_letter == "Job Offer" or type_letter == "job offer" or type_letter == "Job offer":
        salary()
    elif type_letter == "Rejection" or type_letter == "rejection":
        feedback = input("Feedback(Yes or No?)")
        if feedback == "No":
            print("Here is the final letter to send:")
            print("Dear", fname, lname, ",")
            print("After careful evaluation of your application for the position of", jobname, ",")
            print("at this moment we have decided to proceed with another candidate.")
            print(
                "We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.")
            print("Sincerely,")
            print("HR Department of XYZ")
        elif feedback == "Yes":
            print("Here is the final letter to send:")
            print("Dear", fname, lname, ",")
            print("After careful evaluation of your application for the position of", jobname, ",")
            print("at this moment we have decided to proceed with another candidate.")
            print("Here we would like to provide you our feedback about the interview.")
            print(
                "You have sufficient testing knowledge but we expected to see more experience in web application testing techniques.")
            print(
                "We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.")
            print("Sincerely,")
            print("HR Department of XYZ")
        quit()


def salary():
    global salar
    annual_salary = float(input("Annual salary?").replace(".", "").replace(",", "."))
    thousands_separator = "."
    fractional_separator = ","
    salary2 ="{:,.2f}".format(float(annual_salary))
    while annual_salary < 20000.00 or annual_salary > 80000.00:
        print("Input error")
        print("The annual salary should be inbetween 20000.00 and 80000.00.")
        salary()
    salar = salary2.replace(",","b").replace(".",",").replace("b",".")
    date()

def date():
    global sdate
    sdate = input("Start Date?(YYYY-MM-DD)")
    y = sdate[:4]
    y = int(y)
    m = sdate[5:7]
    m = int(m)
    d = sdate[8:10]
    d = int(d)
    while y <2021 or y > 2022 or m < 1 or m > 12 or d < 1 or d > 31:
        print("Input error")
        print("Only in YYYY-MM-DD format and only in 2021 and 2022.")
        date()
    print("Here is the final letter to send:")
    print("Dear", fname, lname,",")
    print("After careful evaluation of your application for the position of",jobname,",")
    print("we are glad to offer you the job. Your salary will be", salar,"euro annually.")
    print("Your start date will be on", sdate,". Please do not hesitate to contact us with any questions.")
    print("Sincerely,")
    print("HR Department of XYZ")
    quit()

def job():
    f()
    last()
    title()
    salary()
    date()

def rejection():
    f()
    last()
    title()

ml()
