import globalVars
import time
from database import *
from UI import *
from friendFunctions import *
from userSearch import *
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands


def userHome():
    from landing import startupLanding

    exitInput = 0
    while exitInput == 0:
        spacer()
        header("Welcome User!")
        print("Please select the number of the service you would like to use:")
        print("(1)  Your InCollege Profile")
        print("(2)  Search for a job / internship")
        print("(3)  Find someone you know")
        print("(4)  Learn a new skill")
        print("(5)  Show My Network")
        print("(6)  Send Friend Request")
        print("(7)  Pending Friend Requests")

        uInput = input("Input Selection (Q to quit and return): ")

        if uInput == '1':  # UI edited for Epic-5
            userProfile()
            # userSearch()
            # createProfile()
        if uInput == '2':
            searchForJob()
        elif uInput == '3':
            userSearch()
        elif uInput == '4':
            learnASkill()
        elif uInput == '5':
            getFriends()
        elif uInput == '6':
            userSearch()
        elif uInput == '7':
            viewFriendRequests()
        elif uInput == 'Q' or uInput == 'q':
            exitInput = 1
            spacer()
        else:
            print("Invalid Option. Try Again")
            spacer()


#################################################### Epic-5 ####################################################


# Function to create a User Profile as a new user or existing user

def userProfile():
    # Check if a profile exists for the logged-in user in the profiles table
    cursor.execute("SELECT * FROM profiles WHERE userID = ?",
                   (globalVars.userID,))
    existing_profile = cursor.fetchone()

    if not existing_profile:
        # If no profile exists, create one
        createProfile()
    else:
        while True:
            spacer()
            header(f'Welcome, {globalVars.userFirstName}!')

            print("1. Display Your Profile")
            print("2. Edit Your Profile")
            print("3. Go Back")

            option = input("Select an option (1/2/3): ")

            if option == '1':
                # Display the user's profile
                displayProfile(existing_profile)
            elif option == '2':
                # Edit the user's profile
                editProfile(existing_profile)
            elif option == '3':
                # Go back to the main menu
                break
            else:
                print("Invalid option. Please choose a valid option.")


# def createProfile():
#     spacer()
#     header('Create your InCollege profile')

#     # Take inputs for profile data
#     title = input(
#         "Enter your title (e.g., '3rd year Computer Science student'): ")
#     major = input("Enter your major: ")
#     major = formatMajor(major)
#     university = input("Enter your university: ")
#     paragraph = input("Enter a paragraph about yourself: ")

#     # Initialize the experience and education variables
#     experience = []
#     education = []

#     # Capture up to three work experience details
#     for i in range(3):
#         print(f"Work Experience {i + 1}:")
#         job_title = input("Enter the job title: ")
#         employer = input("Enter the employer: ")
#         date_started = input("Enter the date started: ")
#         date_ended = input("Enter the date ended: ")
#         location = input("Enter the location: ")
#         description = input("Enter the job description: ")

#         # Store the work experience details as a dictionary
#         experience.append({
#             'Job Title': job_title,
#             'Employer': employer,
#             'Date Started': date_started,
#             'Date Ended': date_ended,
#             'Location': location,
#             'Description': description
#         })

#         add_more = input("Do you want to add more work experience (yes/no)? ")
#         if add_more.lower() != 'yes':
#             break

#     # Capture up to three education details
#     for i in range(3):
#         print(f"Education {i + 1}:")
#         school_name = input("Enter the school name: ")
#         degree = input("Enter the degree: ")
#         years_attended = input("Enter the years attended: ")

#         # Store the education details as a dictionary
#         education.append({
#             'School Name': school_name,
#             'Degree': degree,
#             'Years Attended': years_attended
#         })

#         add_more = input("Do you want to add more education (yes/no)? ")
#         if add_more.lower() != 'yes':
#             break

#     # Insert the data into the profiles table
#     cursor.execute("""INSERT INTO profiles (profileID, userID, title, major, university, paragraph, experience, education)VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (globalVars.userID, globalVars.userID, title, major, university, paragraph, experience, education))

#     conn.commit()

#     print("Your profile has been created successfully!")
def createProfile():
    spacer()
    header('Create your InCollege profile')

    # Take inputs for profile data
    title = input("Enter your title (e.g., '3rd year Computer Science student'): ")
    major = input("Enter your major: ")
    major = formatMajor(major)
    university = input("Enter your university: ")
    university = formatUniversity(university)
    paragraph = input("Enter a paragraph about yourself: ")

    # Initialize lists for experience and education
    experience = []
    education = []

    # Capture up to three work experiences
    for i in range(3):
        print(f"Work Experience {i + 1}:")
        job_title = input("Enter the job title: ")
        employer = input("Enter the employer: ")
        date_started = input("Enter the date started: ")
        date_ended = input("Enter the date ended: ")
        location = input("Enter the location: ")
        description = input("Enter the job description: ")

        # Append the work experience to the list
        experience.append({
            'Job Title': job_title,
            'Employer': employer,
            'Date Started': date_started,
            'Date Ended': date_ended,
            'Location': location,
            'Description': description
        })

        add_more = input("Do you want to add more work experience (yes/no)? ")
        if add_more.lower() != 'yes':
            break

    # Capture up to three education details
    for i in range(3):
        print(f"Education {i + 1}:")
        school_name = input("Enter the school name: ")
        degree = input("Enter the degree: ")
        years_attended = input("Enter the years attended: ")

        # Append the education to the list
        education.append({
            'School Name': school_name,
            'Degree': degree,
            'Years Attended': years_attended
        })

        add_more = input("Do you want to add more education (yes/no)? ")
        if add_more.lower() != 'yes':
            break

    # Convert experience and education to strings
    experience_str = "\n".join([", ".join(f"{key}: {value}" for key, value in exp.items()) for exp in experience])
    education_str = "\n".join([", ".join(f"{key}: {value}" for key, value in edu.items()) for edu in education])

    # Insert the data into the profiles table
    cursor.execute("""INSERT INTO profiles (userID, title, major, university, paragraph, experience, education) VALUES (?, ?, ?, ?, ?, ?, ?)""", (globalVars.userID, title, major, university, paragraph, experience_str, education_str))

    conn.commit()

    print("Your profile has been created successfully!")


def formatMajor(major):
    formatted_major = ' '.join(word.capitalize() for word in major.split())
    return formatted_major


def formatUniversity(university):
    formatted_university = ' '.join(word.capitalize() for word in university.split())
    return formatted_university

def displayProfile(profile):
    spacer()
    header(f'Your Profile, {globalVars.userFirstName} {globalVars.userLastName}')

    print(f"Title: {profile[2]}")
    print(f"Major: {profile[3]}")
    print(f"University: {profile[4]}")
    print(f"About: {profile[5]}")

    experience_str = profile[6]
    if experience_str:
        print("\nExperience:")
        experience_list = experience_str.split("\n")
        for exp in experience_list:
            exp_dict = {item.split(":")[0]: item.split(":")[1] for item in exp.split(", ")}
            print("  - Job Title:", exp_dict['Job Title'])
            print("    Employer:", exp_dict['Employer'])
            print("    Date Started:", exp_dict['Date Started'])
            print("    Date Ended:", exp_dict['Date Ended'])
            print("    Location:", exp_dict['Location'])
            print("    Description:", exp_dict['Description'])

    education_str = profile[7]
    if education_str:
        print("\nEducation:")
        education_list = education_str.split("\n")
        for edu in education_list:
            edu_dict = {item.split(":")[0]: item.split(":")[1] for item in edu.split(", ")}
            print("  - School Name:", edu_dict['School Name'])
            print("    Degree:", edu_dict['Degree'])
            print("    Years Attended:", edu_dict['Years Attended'])



# def displayProfile(profile):
#     spacer()
#     header(f'Your Profile, {globalVars.userFirstName} {globalVars.userLastName}')

#     print(f"Title: {profile[1]}\n")
#     print(f"Major: {profile[2]}\n")
#     print(f"University: {profile[3]}\n")
#     print(f"About: {profile[4]}\n")
    
#     experience = profile[5].split("\n")
#     if len(experience) > 1:
#         print("Experience:")
#         for exp in experience:
#             print(f"  - {exp}\n")
#     else:
#         print(f"Experience: {profile[5]}\n")
    
#     education = profile[6].split("\n")
#     if len(education) > 1:
#         print("Education:")
#         for edu in education:
#             print(f"  - {edu}\n")
#     else:
#         print(f"Education: {profile[6]}\n")



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
    experience = input(
        "Enter your updated experience (or press Enter to keep it the same): ")
    education = input(
        "Enter your updated education (or press Enter to keep it the same): ")

    # Update the profile data in the profiles table
    cursor.execute("UPDATE profiles SET title = ?, major = ?, university = ?, paragraph = ?, experience = ?, education = ? WHERE userID = ?",
                   (title or existing_profile[1], major or existing_profile[2], university or existing_profile[3],
                    paragraph or existing_profile[4], experience or existing_profile[5], education or existing_profile[6], globalVars.userID))
    conn.commit()

    print("Your profile has been updated successfully!")

# # Calling userProfile() to initiate the profile management
# userProfile()


#################################################### Epic-5^#####################################################


# Option functions to fill out once we understand what we need to do for them
def searchForJob():
    # print("Searching for a job is under construction")
    spacer()
    header('Welcome to Job Search')
    print("(1)  Post a Job")
    uInput = input("Input Selection (Q to quit): ")

    exitInput = 0
    while exitInput == 0:
        if uInput == '1':
            print("\nEnter the following information about the job: ")
            title = input("Enter the job title: ")
            description = input("Enter the job description: ")
            employer = input("Enter the employer: ")
            location = input("Enter the location: ")
            salary = input("Enter the job's salary: ")
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")

            storeJob(title, description, employer,
                     location, salary, firstname, lastname)

        elif uInput == 'Q' or uInput == 'q':
            exitInput = 1
            spacer()

        else:
            print("Invalid Option Try again")


def learnASkill():
    loopBreaker1 = True
    while loopBreaker1:
        print("\nPlease select any of following skills:")
        print("1. Web Development ")
        print("2. Leadership ")
        print("3. Time management ")
        print("4. Data Literacy ")
        print("5. Interview Prep ")
        print("6. Return to Welcome Screen ")
        UserOption = int(input("Please select your option: "))
        if UserOption == 1:
            print("Web Development is under construction")
        elif UserOption == 2:
            print("Leadership is under construction")
        elif UserOption == 3:
            print("Time management is under construction")
        elif UserOption == 4:
            print("Data literacy is under construction")
        elif UserOption == 5:
            print("Interview prep is under construction")
        elif UserOption == 6:
            userHome()
        else:
            print("Invalid input.")

        cont = input("Would you like to continue (yes/no): ")
        if cont.lower() == "yes":
            continue
        elif cont.lower() != "yes":
            loopBreaker1 = False
            exit(0)


def storeJob(title, description, employer, location, salary, firstName, lastName):
    cursor.execute("SELECT COUNT(*) FROM jobs")
    job_count = cursor.fetchone()[0]

    if job_count >= globalVars.maxJobPostings:
        print("All permitted jobs have been created. Please come back later.")
        userHome()

    cursor.execute("INSERT INTO jobs (title, description, employer, location, salary, firstname, lastname) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (title, description, employer, location, salary, firstName, lastName))

    conn.commit()
    print("Job stored in database")
    userHome()
