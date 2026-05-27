# Practical Tasks Using Online Simulators - Week 3

## Introduction

This guide provides hands-on cryptography exercises designed for CS students, focusing on applications of encryption, digital signatures, and security protocols.

---

## Task 1: Symmetric Encryption - Protecting Communications

Your company needs to send confidential pricing information to a partner. You'll use symmetric encryption where both parties share the same secret key.

### Online Simulator

**CyberChef** - https://gchq.github.io/CyberChef/

### Step-by-Step Instructions

1. **Access the Simulator**

   - Go to https://gchq.github.io/CyberChef/
   - You'll see a left sidebar with "Operations" and a main workspace
2. **Encrypt a Business Message**

   - In the "Operations" panel (left), search for "AES Encrypt"
   - Drag "AES Encrypt" to the "Recipe" area (middle)
   - In the "Input" box (top right), type your message:

     ```
     CONFIDENTIAL: Q4 pricing - Product A: $299, Product B: $449
     ```
3. **Configure Encryption Settings**

   - In the AES Encrypt operation settings:
     - **Key**: Enter a passphrase like `MySecretKey2024!`
     - **IV**: Leave as default or use `0000000000000000`0000000000000000
     - **Mode**: Select `CBC`
     - **Input format**: UTF8
     - **Output format**: Hex
4. **View Encrypted Result**

   - The "Output" panel shows your encrypted data in hexadecimal format
   - This gibberish is what would be transmitted securely
5. **Decrypt the Message**

   - Clear the recipe, search for "AES Decrypt"
   - Copy the encrypted output to the input box
   - Use the same key and settings as encryption
   - You should see your original message

### Task 2: Asymmetric Encryption & Digital Signatures - PKI Basics

### Understanding public-key infrastructure (PKI) is crucial for secure e-commerce, digital contracts, and authentication systems.

### Online Simulator

**travistidwell's RSA Encryption Demo** - https://travistidwell.com/jsencrypt/demo/

### Step-by-Step Instructions

1. **Generate Key Pair**

   - Visit https://travistidwell.com/jsencrypt/demo/
   - Click "Generate New Keys" button
   - Two keys appear: **Private Key** (keep secret) and **Public Key** (share freely)
2. **Understanding the Keys**

   - **Public Key**: Can be shared with anyone - like your business address
   - **Private Key**: Must be kept secret - like your vault combination
   - Notice they're mathematically related but you can't derive one from the other
3. **Encrypt a Message**

   - In the "Message to Encrypt" box, type:

     ```
     Contract approved. Wire $500,000 to account #12345
     ```
   - Click "Encrypt with Public Key"
   - Only the holder of the private key can decrypt this message
4. **Decrypt the Message**

   - The encrypted message appears in "Encrypted Message" box
   - Click "Decrypt with Private Key"
   - Original message reappears
5. **Simulate Public Key Distribution**

   - Copy your public key
   - Share it with a classmate (or save in a separate note)
   - Have them encrypt a message for you
   - Try to decrypt their message with YOUR private key (it should work)

### Task 3: Hash Functions - Data Integrity and Blockchain

### Hash functions ensure data hasn't been tampered with - crucial for contracts, audit logs, and blockchain technology.

### Online Simulator

**CyberChef** - https://gchq.github.io/CyberChef/

### Step-by-Step Instructions

1. **Create a Hash**

   - Go to https://gchq.github.io/CyberChef/
   - Search for "SHA256" in operations and drag it to the recipe
   - In the input box, type:

     ```
     Invoice #1001: $10,000 - Due: March 31, 2025
     ```
   - You'll see a 64-character hexadecimal hash in the output
2. **Test the "Avalanche Effect"**

   - Copy the hash value (it's like a fingerprint)
   - Now change just ONE character in your input:

     ```
     Invoice #1001: $10,001 - Due: March 31, 2025
     ```

     (Changed $10,000 to $10,001)
   - Notice the hash is completely different
   - This is the "avalanche effect" - tiny changes create totally different outputs
3. **Verify Data Integrity**

   - Imagine you send a contract file to someone
   - You also send the SHA256 hash separately (via SMS or email)
   - They receive the file and compute its hash
   - If the hashes match, the file wasn't tampered with
4. **Collision Resistance**

   - Try to create two different messages with the same hash
   - (You won't succeed - this would take billions of years)
   - This is why hashes are useful for verification

### Task 4: Password Security - Cracking and Best Practices

### t

Weak passwords are the #1 cause of business data breaches. Understanding password strength helps create better corporate policies.

### Online Simulator

**How Secure Is My Password** - https://www.security.org/how-secure-is-my-password/

### Step-by-Step Instructions

1. **Test Common Passwords**

   - Visit https://www.security.org/how-secure-is-my-password/
   - Test these passwords (DON'T use your real passwords):
     - `password123`
     - `Company2024`
     - `MyNameIsJohn`
     - `J0hn$on2024!`
     - `T7$mk9#Qz2@pLw8X`
2. **Analyze the Results**

   - Note the "time to crack" estimates
   - Understand what makes passwords strong:
     - Length (12+ characters)
     - Complexity (uppercase, lowercase, numbers, symbols)
     - Unpredictability (not dictionary words)
3. **Understand Attack Methods**

   - **Brute Force**: Trying all possible combinations
   - **Dictionary Attack**: Trying common words and patterns
   - **Rainbow Tables**: Pre-computed hashes of common passwords
   - **Credential Stuffing**: Using leaked passwords from other sites

### CyberChef Password Hashing Exercise

1. Go to https://gchq.github.io/CyberChef/
2. Add "SHA256" to the recipe
3. Input: `password123`
4. Copy the hash
5. Add another operation: "From Hex"
6. Search online "SHA256 password123" - you'll find the hash in public databases
7. This shows why unique passwords matter
