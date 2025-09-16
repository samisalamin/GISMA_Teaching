import re

# Original examples for reference
def example_basic_matching():
    print("Example 1: Basic Pattern Matching")
    text = "The quick brown fox jumps over the lazy dog."
    pattern = r"\b\w{4}\b"  # Match all 4-letter words
    matches = re.findall(pattern, text)
    print("4-letter words found:", matches)
    print()

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

# STUDENT TASK SOLUTIONS
print("="*60)
print("STUDENT TASK SOLUTIONS")
print("="*60)

# Task 1: Modify example_basic_matching to find words with more than 5 letters
def task1_long_words():
    print("Task 1: Words with more than 5 letters")
    text = "The quick brown fox jumps over the lazy dog."
    pattern = r"\b\w{6,}\b"  # Match words with 6 or more letters
    matches = re.findall(pattern, text)
    print("Words with more than 5 letters:", matches)
    print()

# Task 2: Extract the name from the contact string
def task2_extract_name():
    print("Task 2: Extract name, phone, and email")
    contact_info = "Name: Alice, Phone: (123) 456-7890, Email: alice@example.com"
    
    # Extract name
    name_pattern = r"Name:\s*([A-Za-z\s]+?),"
    name = re.search(name_pattern, contact_info)
    
    # Extract phone and email (from original)
    phone_pattern = r"\(\d{3}\) \d{3}-\d{4}"
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    phone = re.search(phone_pattern, contact_info)
    email = re.search(email_pattern, contact_info)
    
    print("Name found:", name.group(1).strip() if name else "None")
    print("Phone number found:", phone.group() if phone else "None")
    print("Email address found:", email.group() if email else "None")
    print()

# Task 3: Count message types in log file
def task3_count_messages():
    print("Task 3: Count message types in log file")
    # Create the sample file
    sample_text = """Error: File not found
Warning: Disk space low
Info: Update completed
Error: Access denied
Info: System rebooted
Warning: Memory usage high
Error: Network timeout"""
    
    with open("log.txt", "w") as f:
        f.write(sample_text)
    
    # Read and count message types
    with open("log.txt", "r") as f:
        content = f.read()
        
        error_count = len(re.findall(r"Error:", content))
        warning_count = len(re.findall(r"Warning:", content))
        info_count = len(re.findall(r"Info:", content))
        
        print(f"Error messages: {error_count}")
        print(f"Warning messages: {warning_count}")
        print(f"Info messages: {info_count}")
        print()

# Task 4: Replace email addresses with "[email hidden]"
def task4_hide_emails():
    print("Task 4: Replace emails with '[email hidden]'")
    text = "Contact John at john@company.com or Sarah at sarah.smith@example.org for more info."
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    hidden_text = re.sub(email_pattern, "[email hidden]", text)
    print("Original text:", text)
    print("Modified text:", hidden_text)
    print()

# Task 5: Validate IP address
def task5_validate_ip():
    print("Task 5: Validate IP addresses")
    def is_valid_ip(ip):
        # Pattern for valid IP address (0-255 for each octet)
        pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        return bool(re.match(pattern, ip))
    
    test_ips = ["192.168.1.1", "256.1.1.1", "192.168.1", "10.0.0.1", "999.999.999.999", "127.0.0.1"]
    
    for ip in test_ips:
        result = "Valid" if is_valid_ip(ip) else "Invalid"
        print(f"{ip:<15} -> {result}")
    print()

# Task 6: Validate email address
def task6_validate_email():
    print("Task 6: Validate email addresses")
    def is_valid_email(email):
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.match(pattern, email))
    
    test_emails = [
        "example123@test.com",
        "user.name@domain.co.uk", 
        "invalid.email",
        "@invalid.com",
        "test@.com",
        "valid_email@example.org"
    ]
    
    for email in test_emails:
        result = "Valid" if is_valid_email(email) else "Invalid"
        print(f"{email:<25} -> {result}")
    print()

# Task 7: Extract dates in DD/MM/YYYY format
def task7_extract_dates():
    print("Task 7: Extract dates in DD/MM/YYYY format")
    text = "Today is 12/05/2023 and tomorrow is 13/05/2023. The meeting was on 01/12/2022 and the deadline is 25/12/2023."
    
    # Pattern for DD/MM/YYYY (with basic validation)
    date_pattern = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b"
    dates = re.findall(date_pattern, text)
    
    print("Original text:", text)
    print("Dates found:")
    for date in dates:
        full_date = f"{date[0]}/{date[1]}/{date[2]}"
        print(f"  {full_date}")
    
    # Alternative: find complete date strings
    complete_dates = re.findall(r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b", text)
    print("Complete date strings:", complete_dates)
    print()

# Run all tasks
print("Running original examples first:")
example_basic_matching()
example_extracting_data()
example_file_reading()

print("Now running student task solutions:")
task1_long_words()
task2_extract_name()
task3_count_messages()
task4_hide_emails()
task5_validate_ip()
task6_validate_email()
task7_extract_dates()

print("All tasks completed!")