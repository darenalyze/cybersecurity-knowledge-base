# Module 1.1 Offensive Security Intro
---
## Content
- [Module 1.1 Offensive Security Intro](#module-11-offensive-security-intro)
  - [Content](#content)
  - [Notes](#notes)
    - [Task 1 - What is Offensive Security?](#task-1---what-is-offensive-security)
    - [Task 2 - Hacking your first machine](#task-2---hacking-your-first-machine)
      - [Lab Environment Setup](#lab-environment-setup)
      - [Given Information:](#given-information)
      - [Your First Hack](#your-first-hack)
      - [Gobuster Scan Result](#gobuster-scan-result)
      - [Mission](#mission)
      - [Result:](#result)
      - [Question](#question)
    - [Task 3 - Careers in cyber security](#task-3---careers-in-cyber-security)
      - [How can I start learning?](#how-can-i-start-learning)
      - [What careers are there?](#what-careers-are-there)

## Notes
  ### Task 1 - What is Offensive Security?
  - 
    > "To outsmart a hacker, you need to think like one."

    **Why learn offensive security:**
    - Understand hacker tactics and enhance system defenses
    - Find vulnerabilities before attackers do
    - Learn attack techniques

    "Offensive Security" covers breaking into computer systems, exploiting software bugs, and finding loopholes in applications to gain unauthorized access.
    
    #### Beginning Your Learning Journey

    > "In this TryHackMe lesson, you will be guided through hacking your first website in a legal and safe environment. The goal is to show you how an ethical hacker operates. But before we do that, let's review by answering the questions below."

    #### Questions:
    1. Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system?  
        - [x] Offensive Security  
        - [ ] Defensive Security  

      > My Answer: "Offensive Security"  
      > Result: Correct
---

### Task 2 - Hacking your first machine
  This is my first Lab Machine that I'm going to hack. TryHackMe provides a fake banking system called "FakeBank" that is safe to attack.

  #### Lab Environment Setup
  - **Interface:** Split-screen layout. The left side displays the information/guide, and the right side hosts the Ubuntu lab machine with Firefox open at `http://fakebank.thm/`.
  - **Available Resources:** Firefox browser, a system terminal, and a `wordlist.txt` file containing 7,999 potential directory names.

  #### Given Information:
  - **Target IP Address:** `10.49.137.40`
  - **Banking site:** `http://fakebank.thm/`
  - **Bank account name:** Mrs G. Benjamin
  - **Bank account number:** `8881`
  - **Account balance:** -$1,232.32

  #### Your First Hack
  We will use a command-line utility called **Gobuster** to brute-force FakeBank's website to find hidden directories and pages. Gobuster takes a list of potential page/directory names and tests them against the target URL; if a page exists, it returns the HTTP status code.

  Gobuster will take a list of potential page or directory names and try accessing a website with each of them; if the page exists, it tells you."
  > **Concept:** Most companies use an admin portal page to grant staff access to basic administrative controls. For a bank, an employee might use this to transfer money between client accounts.
    
  1. Open the terminal inside the Lab machine.
  2. Execute the Gobuster directory search command:  
  ```
   gobuster -u [http://fakebank.thm](http://fakebank.thm) -w wordlist.txt dir
  ```
  #### Gobuster Scan Result
  ```
  =====================================================
  Gobuster v2.0.1              OJ Reeves (@TheColonial)
  =====================================================
  [+] Mode         : dir
  [+] Url/Domain   : http://fakebank.thm/
  [+] Threads      : 10
  [+] Wordlist     : wordlist.txt
  [+] Status codes : 200,204,301,302,307,403
  [+] Timeout      : 10s
  =====================================================
  2026/06/11 19:38:46 Starting gobuster
  =====================================================
  /images (Status: 301)
  /bank-transfer (Status: 200)
  =====================================================
  2026/06/11 19:38:58 Finished
  =====================================================
  ```
  The scan reveals that /bank-transfer returns a Status: 200, meaning the page exists and is publicly accessible.

  Navigating to http://fakebank.thm/bank-transfer uncovers the Staff Account Admin Portal:
  ```
  Staff Account
  Transfer money between accounts

  Admin Portal
  Send from
  Send to
  Amount to send in USD 
  Send Money 
  ```
  #### Mission 
  **Objective:** Transfer $2,000 from account `2276` to account `8881`.

  **Action:** Inputted `$2000` into the Amount field, `2276` into Send from, and `8881` into Send to, then executed the transfer.
  #### Result:
  ```
  Success, transfer completed

  You have successfully completed the transfer, here are the details for reference:

  Transfer reference:
  123

  Amount:
  $2000 USD

  Date of transfer:
  2026-06-11 
  ```
  - I clicked Return to Your Account and this text popped up:
  ```
  Congratulations - you hacked the bank!
  The answer to the TryHackMe question is BANK-HACKED
  ```
  #### Question 
  1. Above your account balance, you should now see a message indicating the answer to this question. Can you find the answer you need?
  > My answer: BANK-HACKED  
  > Result: Correct

---

### Task 3 - Careers in cyber security
#### How can I start learning?
Some people wonders how others become hackers (security consultants) or defenders (security analysts fighting cybercrime). Just know where parts are you really interested in and practice regularly using hands-on exercises. Build a habit learning with TryHackMe and you'll acquire the knowledge to get your first job in the industry.
#### What careers are there?
The cyber careers lesson goes into more depth about the different careers in cyber. However, here is a short description of a few offensive security roles:
- Penetration Tester - Responsible for testing technology products for finding exploitable security vulnerabilities.
- Red Teamer - Plays the role of an adversary, attacking an organization and providing feedback from an enemy's perspective.
- Security Engineer - Design, monitor, and maintain security controls, networks, and systems to help prevent cyberattacks.

I am Currently leaning towards Security Engineer or blue team.
