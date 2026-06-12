# Hacking your first machine
---

## My Understanding
- This is my first Lab Machines that i'm going to hack.  
- They prepare a fake banking system called "FakeBank" that safely to hack.  
- My web screen split into two, one is for information and guide (left side), the other one is the lab machine showing web browser fire fox that in http://fakebank.thm/ site (right side)   
- There is three usefull file aplication i see which is firefox, terminal and wordlis.txt that have 7999 lines of word text also i see that machine lab using ubuntu os

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

    - I learned that this terminal code is have a power to loop through the given texts and try it in given website. They finding a hidden directories and pages
    - We can see in result that `/bank-transfer (Status: 200)` have status of 200 which means it is exist and loaded succefully (did not tell in)
    - I quickly added the `/bank-transfer` because the **Gobuster** says it is exist. So i went there to see the page and i saw: 
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
    - I Put $2000 in `Amount to send in USD input`, 2276 to `Send from` and 8881 to `Send to` and finally I clicked `Send Money` after double checking of inputed details
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
        
    - I click `Return to Your Account` and This text pop up :
    --- 
        Congratulations - you hacked the bank!
        The answer to the TryHackMe question is BANK-HACKED

### Question 
1. Above your account balance, you should now see a message indicating the answer to this question. Can you find the answer you need?
> My answer: BANK-HACKED
> Result: Correct




