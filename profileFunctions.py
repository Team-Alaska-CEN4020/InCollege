from userSearch import *
from UserCreateLogin import *
import globalVars
from UI import *
from database import *
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands



def createProfile():
    spacer()
    header('Create your InCollege profile')

    # Take inputs for profile data
    title = input(
        "Enter your title (e.g., '3rd year Computer Science student'): ")
    major = input("Enter your major: ")
    major = formatMajor(major)
    university = input("Enter your university: ")
    university = formatUniversity(university)
    paragraph = input("Enter a paragraph about yourself: ")

    # Initialize lists for experience and education
    experience = []
    education = []

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

    # Insert the profile data into the profiles table
    cursor.execute("""INSERT INTO profiles (userID, title, major, university, About) VALUES (?, ?, ?, ?, ?)""",
                   (globalVars.userID, title, major, university, paragraph))

    conn.commit()

    # Retrieve the auto-generated profileID
    profile_id = cursor.lastrowid

    # Insert experience and education data into their respective tables
    for exp_data in experience:
        cursor.execute("""INSERT INTO experience (userID, jobTitle, employer, dateStarted, dateEnded, location, description) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (globalVars.userID, exp_data['Job Title'], exp_data['Employer'], exp_data['Date Started'], exp_data['Date Ended'], exp_data['Location'], exp_data['Description']))
        conn.commit()

    for edu_data in education:
        cursor.execute("""INSERT INTO education (userID, schoolName, degree, yearsAttended) VALUES (?, ?, ?, ?)""",
                       (globalVars.userID, edu_data['School Name'], edu_data['Degree'], edu_data['Years Attended']))
        conn.commit()

    print("Your profile has been created successfully!")








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

    print(f"Title: {profile[2]}")
    print(f"Major: {profile[3]}")
    print(f"University: {profile[4]}")
    print(f"About: {profile[5]}\n")

    # Fetch experience and education from their respective tables based on the user's ID
    cursor.execute("SELECT * FROM experience WHERE userID = ?", (globalVars.userID,))
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

    cursor.execute("SELECT * FROM education WHERE userID = ?", (globalVars.userID,))
    education_data = cursor.fetchall()

    if education_data:
        print("\nEducation:")
        for edu in education_data:
            print("  - School Name:", edu[2])
            print("    Degree:", edu[3])
            print("    Years Attended:", edu[4])



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

    # Update the profile data in the profiles table
    cursor.execute("UPDATE profiles SET title = ?, major = ?, university = ?, About = ? WHERE userID = ?",
                   (title or existing_profile[2], major or existing_profile[3],
                    university or existing_profile[4], paragraph or existing_profile[5], globalVars.userID))
    conn.commit()

    print("Your profile has been updated successfully!")

    # Optionally, update experience and education
    update_experience = input("Do you want to update your experience (yes/no)? ")
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
    exp_id_to_update = input("Enter the experience ID you want to update (or press Enter to skip): ")
    if exp_id_to_update:
        # Take inputs for the updated experience
        job_title = input("Enter the updated job title: ")
        employer = input("Enter the updated employer: ")
        date_started = input("Enter the updated date started: ")
        date_ended = input("Enter the updated date ended: ")
        location = input("Enter the updated location: ")
        description = input("Enter the updated job description: ")

        # Update the experience entry in the table
        cursor.execute("UPDATE experience SET jobTitle = ?, employer = ?, dateStarted = ?, dateEnded = ?, location = ?, description = ? WHERE experienceID = ?",
                       (job_title, employer, date_started, date_ended, location, description, exp_id_to_update))
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
    edu_id_to_update = input("Enter the education ID you want to update (or press Enter to skip): ")
    if edu_id_to_update:
        # Take inputs for the updated education
        school_name = input("Enter the updated school name: ")
        degree = input("Enter the updated degree: ")
        years_attended = input("Enter the updated years attended: ")

        # Update the education entry in the table
        cursor.execute("UPDATE education SET schoolName = ?, degree = ?, yearsAttended = ? WHERE educationID = ?",
                       (school_name, degree, years_attended, edu_id_to_update))
        conn.commit()

    print("Education updated successfully!")
