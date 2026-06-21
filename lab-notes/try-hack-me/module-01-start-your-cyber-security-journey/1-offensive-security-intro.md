# Module 1.1 Offensive Security Intro
---
## Content
- Task 1 - What is Offensive Security?
- Task 2 - Hacking your first machine
- Task 3 - Careers in cyber security

## Notes
- **Task 1 - What is Offensive Security?**
  - 
    "To outsmart a hacker, you need to think like one."

    Why learn offensive security:
    - Understand hacker tactics and enhance system defenses
    - Find vulnerabilities before attackers do
    - Learn attack techniques

    "Offensive Security" covers breaking into computer systems, exploiting software bugs, and finding loopholes in applications to gain unauthorized access.
    
        ### Beginning Your Learning Journey

        > "In this TryHackMe lesson, you will be guided through hacking your first website in a legal and safe environment. The goal is to show you how an ethical hacker operates.
        > But before we do that, let's review by answering the questions below."

    ## Questions:
    1. Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system?  
        - Offensive Security  
        - Defensive Security  
    
        > My Answer: "Offensive Security"  
        > Result: Correct
---
---
- **Task 2 - Hacking your first machine**
  -   
  - This is my first Lab Machine that I'm going to hack. 
  - They provide a fake banking system called "FakeBank" that is safe to hack.
  - My web screen is split into two, one is for information and a guide (left side), the other is the lab machine showing the web browser Firefox at http://fakebank.thm/ (right side)  
  - There are three useful file applications I can see: Firefox, a terminal, and wordlist.txt which has 7,999 lines of words. I can also see that the lab machine is running Ubuntu OS.

      ## Given Information:
      - Target IP Address: 10.49.137.40
      - Banking site: http://fakebank.thm/
      - Bank account name: Mrs G. Benjamin
      - Bank account number: 8881
      - Account balance: -$1,232.32

      ## Your First Hack
      > "We will use a command-line application called "Gobuster(opens in new tab)" to brute-force FakeBank's website to find hidden directories and pages.   
      > Gobuster will take a list of potential page or directory names and try accessing a website with each of them; if the page exists, it tells you."
      - I open terminal inside the Lab machine

      > "Most companies have an admin portal page, giving their staff access to basic admin controls for day-to-day operations. For a bank, an employee might need to transfer money to and from client accounts."
      - gobuster -u http://fakebank.thm -w wordlist.txt dir  
      #### **Result:**
      ---
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

      - I learned that this command has the ability to loop through the given text and try each entry on the given website. It finds hidden directories and pages.
      - We can see in the result that `/bank-transfer (Status: 200)` has a status of 200, which means it exists and loaded successfully.
      - I quickly navigated to /bank-transfer because **Gobuster** says it exists. So I went there to see the page and I saw:
      --- 
          Staff Account
          Transfer money between accounts

          Admin Portal
          Send from
          Send to
          Amount to send in USD 
          Send Money 

      ## Mission 
      > "Your mission is to transfer $2000 from bank account 2276 to your account (account number 8881). If your transfer was successful, you should now be able to see your new balance reflected on your account page."
      -  I put $2000 in the Amount to send in USDfield, 2276 inSend from, and 8881 in Send to, then clicked Send Money after double-checking the entered details.
      #### Result:
      ---
          Success, transfer completed

          You have successfully completed the transfer, here are the details for reference:

          Transfer reference:
          123

          Amount:
          $2000 USD

          Date of transfer:
          2026-06-11 
          
      - I clicked Return to Your Account and this text popped up:
      --- 
          Congratulations - you hacked the bank!
          The answer to the TryHackMe question is BANK-HACKED

  ### Question 
  1. Above your account balance, you should now see a message indicating the answer to this question. Can you find the answer you need?
  > My answer: BANK-HACKED  
  > Result: Correct
---
---
- **Task 3 - Careers in cyber security**
  - 
  - How can I start learning?
    - 
      Some people wonders how others become hackers (security consultants) or defenders (security analysts fighting cybercrime). Just know where parts are you really interested in and practice regularly using hands-on exercises. Build a habit learning with TryHackMe and you'll acquire the knowledge to get your first job in the industry.

  - What careers are there?
    - 
      The cyber careers lesson goes into more depth about the different careers in cyber. However, here is a short description of a few offensive security roles:
      - Penetration Tester - Responsible for testing technology products for finding exploitable security vulnerabilities.
      - Red Teamer - Plays the role of an adversary, attacking an organization and providing feedback from an enemy's perspective.
      - Security Engineer - Design, monitor, and maintain security controls, networks, and systems to help prevent cyberattacks.

