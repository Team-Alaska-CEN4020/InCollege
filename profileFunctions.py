import globalVars
from UI import *
from database import *
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

def createProfile():
    from loginLanding import userHome
    while True:
        spacer()
        header('Create your InCollege profile')
        cursor.execute("SELECT userID FROM profiles WHERE userID=?", (globalVars.userID,))
        profile_exists = cursor.fetchone()
        cursor.execute("SELECT * FROM profiles WHERE userID=?", (globalVars.userID,))
        profile_data = cursor.fetchone()
        if (not profile_exists) or (profile_data[2]==None) or (profile_data[3]==None) or (profile_data[4]==None) or (profile_data[5]==None) :
            # Insert an initial row with NULL values for the user's profile
            cursor.execute("""INSERT INTO profiles (userID, title, major, university, About) VALUES (?, NULL, NULL, NULL, NULL)""",
                       (globalVars.userID,))
            conn.commit()
            profileDetails()
            uInput = input("Would you like to continue (Y/N): ")
            if uInput.upper()!='Y':
                userHome()
        
        cursor.execute("SELECT userID FROM experience WHERE userID=?", (globalVars.userID,))
        experience_exists = cursor.fetchone()
        if not experience_exists:
            experienceDetails()
            uInput1 = input("Would you like to continue (Y/N): ")
            if uInput1.upper()!='Y':
                userHome()

        cursor.execute("SELECT userID FROM education WHERE userID=?", (globalVars.userID,))
        education_exists = cursor.fetchone()
        if not education_exists:
            educationDetails()
            print("Your profile has been created successfully!")
            userHome()

    


def profileDetails():
    from loginLanding import userHome
    print("Profile Details:")
    # Take inputs for profile data
    cursor.execute("SELECT * FROM profiles WHERE userID=?", (globalVars.userID,))
    profile_details = cursor.fetchone()

    while True:
        if profile_details[2] == None: 
            title = input("Incomplete profile details. Please enter your title (e.g., '3rd year Computer Science student'): ")
            cursor.execute("UPDATE profiles SET title = ? WHERE userID = ?", (title, globalVars.userID))
            conn.commit()
            uInput = input("Would you like to continue? (Y/N): ")
            if uInput.upper() != 'Y':
                userHome()

        if profile_details[3] == None: 
            major = input("Incomplete profile details. Please enter your major: ")
            major = formatMajor(major)
            cursor.execute("UPDATE profiles SET major = ? WHERE userID = ?", (major, globalVars.userID))
            conn.commit()
            uInput = input("Would you like to continue? (Y/N): ")
            if uInput.upper() != 'Y':
                userHome()
        
        if profile_details[4] == None: 
            university = input("Incomplete profile details. Please enter your university: ")
            university = formatUniversity(university)
            cursor.execute("UPDATE profiles SET university = ? WHERE userID = ?", (university, globalVars.userID))
            conn.commit()
            uInput = input("Would you like to continue? (Y/N): ")
            if uInput.upper() != 'Y':
                userHome()

        if profile_details[5] == None: 
            paragraph = input("Incomplete profile details. Please enter a paragraph about yourself: ")
            cursor.execute("UPDATE profiles SET About = ? WHERE userID = ?", (paragraph, globalVars.userID))
            conn.commit()
            return
    


def experienceDetails():
    experience = []
    # Capture up to three work experience details
    for i in range(3):
        print(f"Work Experience {i + 1}:")
        job_title = input("Enter the job title: ")
        employer = input("Enter the employer: ")
        date_started = input("Enter the date started(MM/DD/YYYY): ")
        date_ended = input("Enter the date ended (MM/DD/YYYY): ")
        location = input("Enter the location: ")
        description = input("Enter the job description: ")

        # Store the work experience details as a dictionary
        exp_data = {
            'Job Title': job_title,
            'Employer': employer,
            'Date Started': date_started,
            'Date Ended': date_ended,
            'Location': location,
            'Description': description
        }
        experience.append(exp_data)

        add_more = input("Do you want to add more work experience (yes/no)? ")
        if add_more.lower() != 'yes':
            break

    # Insert experience data into its table
    for exp_data in experience:
        cursor.execute("""INSERT INTO experience (userID, jobTitle, employer, dateStarted, dateEnded, location, description) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (globalVars.userID, exp_data['Job Title'], exp_data['Employer'], exp_data['Date Started'], exp_data['Date Ended'], exp_data['Location'], exp_data['Description']))
        conn.commit()


def educationDetails():
    education = []
    # Capture up to three education details
    for i in range(3):
        print(f"Education {i + 1}:")
        school_name = input("Enter the school name: ")
        degree = input("Enter the degree: ")
        years_attended = input("Enter the years attended: ")

        # Store the education details as a dictionary
        edu_data = {
            'School Name': school_name,
            'Degree': degree,
            'Years Attended': years_attended
        }
        education.append(edu_data)

        add_more = input("Do you want to add more education (yes/no)? ")
        if add_more.lower() != 'yes':
            break
    # Insert education data into its table
    for edu_data in education:
        cursor.execute("""INSERT INTO education (userID, schoolName, degree, yearsAttended) VALUES (?, ?, ?, ?)""",
                       (globalVars.userID, edu_data['School Name'], edu_data['Degree'], edu_data['Years Attended']))
        conn.commit()


def formatMajor(major):
    formatted_major = ' '.join(word.capitalize() for word in major.split())
    return formatted_major


def formatUniversity(university):
    formatted_university = ' '.join(word.capitalize()
                                    for word in university.split())
    return formatted_university


def displayProfile(profile):
    spacer()
    header(
        f'Your Profile, {globalVars.userFirstName} {globalVars.userLastName}')
    if profile and None in profile[1:]:
            print(f"Title: {profile[2]}")
            print(f"Major: {profile[3]}")
            print(f"University: {profile[4]}")
            print(f"About: {profile[5]}\n")
    else:
        print("Profile Incomplete! Please complete to proceed.")
    spacer()


    cursor.execute("""
        SELECT e.experienceID, e.userID, e.jobTitle, e.employer, e.dateStarted, e.dateEnded, e.location, e.description
        FROM experience as e
        JOIN users as u ON e.userID = u.userID 
        WHERE e.userID = ?""", (globalVars.userID,))
    experience_data = cursor.fetchall()

    if experience_data:
        print("Experience:")
        for exp in experience_data:
            print("  - Job Title:", exp[2])
            print("    Employer:", exp[3])
            print("    Date Started:", exp[4])
            print("    Date Ended:", exp[5])
            print("    Location:", exp[6])
            print("    Description:", exp[7])

    cursor.execute("""
        SELECT edu.userID, edu.schoolName, edu.degree, edu.yearsAttended, u.userID
        FROM education as edu
        JOIN users as u ON edu.userID = u.userID 
        WHERE edu.userID = ?""", (globalVars.userID,))
    education_data = cursor.fetchall()

    if education_data:
        print("\nEducation:")
        for edu in education_data:
            print("  - School Name:", edu[1])
            print("    Degree:", edu[2])
            print("    Years Attended:", edu[3])


def editProfile(existing_profile):
    spacer()
    header(f'Edit Your Profile, {globalVars.userFirstName}!')

    # Display the user's current profile data
    displayProfile(existing_profile)

    # Take inputs for updated profile data
    title = input(
        "Enter your updated title (or press Enter to keep it the same): ")
    major = input(
        "Enter your updated major (or press Enter to keep it the same): ")
    university = input(
        "Enter your updated university (or press Enter to keep it the same): ")
    paragraph = input(
        "Enter an updated paragraph about yourself (or press Enter to keep it the same): ")

    # Update the profile data in the profiles table depending on which piece of data the user wanted to change
    if title != "":
        cursor.execute("UPDATE profiles SET title = ? WHERE userID = ?", (title, globalVars.userID))
        conn.commit()

    if major != "":
        cursor.execute("UPDATE profiles SET major = ? WHERE userID = ?", (major, globalVars.userID))
        conn.commit()

    if university != "":
        cursor.execute("UPDATE profiles SET university = ? WHERE userID = ?", (university, globalVars.userID))
        conn.commit()

    if paragraph != "":
        cursor.execute("UPDATE profiles SET About = ? WHERE userID = ?", (paragraph, globalVars.userID))
        conn.commit()

    print("Your profile has been updated successfully!")

    # Optionally, update experience and education
    update_experience = input(
        "Do you want to update your experience (yes/no)? ")
    if update_experience.lower() == "yes":
        updateExperience(globalVars.userID)

    update_education = input("Do you want to update your education (yes/no)? ")
    if update_education.lower() == "yes":
        updateEducation(globalVars.userID)


def updateExperience(user_id):
    # Display existing experience entries
    cursor.execute("SELECT experienceID, jobTitle, employer, dateStarted, dateEnded, location, description FROM experience WHERE userID = ?",
                   (user_id,))
    experience_entries = cursor.fetchall()

    spacer()
    header('Update Experience')
    print("Existing Experience Entries:")

    for exp in experience_entries:
        exp_id, job_title, employer, date_started, date_ended, location, description = exp
        print(f"Experience ID: {exp_id}")
        print(f"Job Title: {job_title}")
        print(f"Employer: {employer}")
        print(f"Date Started: {date_started}")
        print(f"Date Ended: {date_ended}")
        print(f"Location: {location}")
        print(f"Description: {description}")
        print("-" * 50)  # Separator

    # Choose an entry to update
    exp_id_to_update = input(
        "Enter the experience ID you want to update (or press Enter to skip): ")
    if exp_id_to_update != "":
        # Take inputs for the updated experience
        job_title = input("Enter the updated job title(or press Enter to keep it the same): ")
        employer = input("Enter the updated employer(or press Enter to keep it the same): ")
        date_started = input("Enter the updated date started(or press Enter to keep it the same): ")
        date_ended = input("Enter the updated date ended(or press Enter to keep it the same): ")
        location = input("Enter the updated location(or press Enter to keep it the same): ")
        description = input("Enter the updated job description(or press Enter to keep it the same): ")

        # Update the experience entry in the table depending on which piece of data the user wanted to change
        if job_title != "":
            cursor.execute("UPDATE experience SET jobTitle = ? WHERE experienceID = ?", (job_title, exp_id_to_update))
            conn.commit()

        if employer != "":
            cursor.execute("UPDATE experience SET employer = ? WHERE experienceID = ?", (employer, exp_id_to_update))
            conn.commit()

        if date_started != "":
            cursor.execute("UPDATE experience SET dateStarted = ? WHERE experienceID = ?", (date_started, exp_id_to_update))
            conn.commit()

        if date_ended != "":
            cursor.execute("UPDATE experience SET dateEnded = ? WHERE experienceID = ?", (date_ended, exp_id_to_update))
            conn.commit()

        if location != "":
            cursor.execute("UPDATE experience SET location = ? WHERE experienceID = ?", (location, exp_id_to_update))
            conn.commit()

        if description != "":
            cursor.execute("UPDATE experience SET description = ? WHERE experienceID = ?", (description, exp_id_to_update))
            conn.commit()


        print("Experience updated successfully!")


def updateEducation(user_id):
    # Display existing education entries
    cursor.execute("SELECT educationID, schoolName, degree, yearsAttended FROM education WHERE userID = ?",
                   (user_id,))
    education_entries = cursor.fetchall()

    spacer()
    header('Update Education')
    print("Existing Education Entries:")

    for edu in education_entries:
        edu_id, school_name, degree, years_attended = edu
        print(f"Education ID: {edu_id}")
        print(f"School Name: {school_name}")
        print(f"Degree: {degree}")
        print(f"Years Attended: {years_attended}")
        print("-" * 50)  # Separator

    # Choose an entry to update
    edu_id_to_update = input(
        "Enter the education ID you want to update (or press Enter to skip): ")
    if edu_id_to_update != "":
        # Take inputs for the updated education
        school_name = input("Enter the updated school name(or press Enter to keep it the same): ")
        degree = input("Enter the updated degree(or press Enter to keep it the same): ")
        years_attended = input("Enter the updated years attended(or press Enter to keep it the same): ")

        # Update the education entry in the table depending on which piece of data the user wanted to change
        if school_name != "":
            cursor.execute("UPDATE education SET schoolName = ? WHERE educationID = ?", (school_name, edu_id_to_update))
            conn.commit()

        if degree != "":
            cursor.execute("UPDATE education SET degree = ? WHERE educationID = ?", (degree, edu_id_to_update))
            conn.commit()

        if years_attended != "":
            cursor.execute("UPDATE education SET yearsAttended = ? WHERE educationID = ?", (years_attended, edu_id_to_update))
            conn.commit()
        
        
        print("Education updated successfully!")
