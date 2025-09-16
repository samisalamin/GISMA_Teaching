import re

# Example 1: Basic pattern matching
def example_basic_matching():
    print("Example 1: Basic Pattern Matching")
    text = "The quick brown fox jumps over the lazy dog."
    pattern = r"\b\w{4}\b"  # Match all 4-letter words
    matches = re.findall(pattern, text)
    print("4-letter words found:", matches)
    print()

# Example 2: Extracting data from strings
def example_extracting_data():
    print("Example 2: Extracting Data from Strings")
    contact_info = "Name: Alice, Phone: (123) 456-7890, Email: alice@example.com"
    phone_pattern = r"\(\d{3}\) \d{3}-\d{4}"
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    phone = re.search(phone_pattern, contact_info)
    email = re.search(email_pattern, contact_info)
    print("Phone number found:", phone.group() if phone else "None")
    print("Email address found:", email.group() if email else "None")
    print()

# Example 3: Reading from a file and finding patterns
def example_file_reading():
    print("Example 3: Reading from a File and Finding Patterns")
    # Create a sample file
    sample_text = """Error: File not found
Warning: Disk space low
Info: Update completed
Error: Access denied
Info: System rebooted"""
    with open("log.txt", "w") as f:
        f.write(sample_text)

    # Read the file and find all error messages
    with open("log.txt", "r") as f:
        content = f.read()
        error_pattern = r"Error:.*"
        errors = re.findall(error_pattern, content)
        print("Error messages found in file:")
        for error in errors:
            print(error)
    print()

# Run all examples
example_basic_matching()
example_extracting_data()
example_file_reading()

#Example 4: 
# Basic Regular Expressions
import re

text = "My email is example123@test.com and phone is 123-456-7890"

# Find email
email = re.findall(r"[\w.-]+@[\w.-]+", text)
print("Email:", email)

# Find phone number
phone = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print("Phone:", phone)

########################################################
# exercises for students
########################################################
# Student Tasks:
# 1. Modify example_basic_matching to find words with more than 5 letters.
# 2. Extend example_extracting_data to also extract the name from the string.
# 3. In example_file_reading, add functionality to count how many times each type of message (Error, Warning, Info) appears.
# 4. Create a new example that replaces all email addresses in a text with "[email hidden]".
# 5. Write a function that validates if a given string is a valid IP address.
# 6. Validate if a string is a valid email address using regex
# Example: "example123@test.com" -> Valid
# 7. Use regex to extract all dates in format DD/MM/YYYY from a string
# Example: "Today is 12/05/2023 and tomorrow is 13/05/2023"
