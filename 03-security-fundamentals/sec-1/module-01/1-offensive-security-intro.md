# 1.1 Offensive Security Intro

---

## Task 1: What is Offensive Security?

> *"To outsmart a hacker, you need to think like one."*

Offensive security means breaking into systems, exploiting bugs, and finding loopholes to test defenses before real attackers do.

```text
[ Offensive Security ] ───► Simulates attacks ───► Finds security flaws early
```

* **Goal:** Hack systems legally to fix weak points.
* **Key Process:** Ethical hacking and vulnerability scanning.

---

## Task 2: Hacking Your First Machine (FakeBank Lab)

### Target Info

* **Target URL:** `http://fakebank.thm/`
* **Account Name:** Mrs G. Benjamin
* **Account Number:** `8881`
* **Current Balance:** -$1,232.32

---

### Attack Steps

```text
[ Find Hidden Pages ] ───► [ Access Admin Portal ] ───► [ Transfer Funds ]
 (Gobuster Brute-Force)        (/bank-transfer)          (Account 2276 -> 8881)
```

1. **Scan for Hidden Pages:** Use **Gobuster** to search for secret web paths:
   ```bash
   gobuster -u [http://fakebank.thm](http://fakebank.thm) -w wordlist.txt dir
   ```
2. **Analyze Output:** Found `/bank-transfer` (Status: `200` OK).
3. **Exploit Portal:** Open `http://fakebank.thm/bank-transfer` and transfer **$2,000** from account `2276` to account `8881`.
4. **Get Flag:** New balance updated and displayed the flag: **`BANK-HACKED`**.

---

## Task 3: Offensive Security Careers

| Job Role | Main Focus |
|---|---|
| **Penetration Tester** | Finds and exploits security bugs in software or networks. |
| **Red Teamer** | Simulates full-scale adversary attacks against organizations. |
| **Security Engineer** | Builds, monitors, and defends system networks (Blue Team). |