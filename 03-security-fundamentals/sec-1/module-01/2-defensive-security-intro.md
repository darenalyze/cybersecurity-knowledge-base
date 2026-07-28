# Defensive Security Intro

---

## Task 1: Introduction to Defensive Security

Defensive security (**Blue Team**) focuses on protecting assets by preventing attacks and detecting intrusions early.

```text
               ┌──► Prevent Intrusions (Firewalls, Patches)
[ Blue Team ] ─┤
               └──► Detect & Respond (SIEM, Incident Response)
```

### Core Defensive Tasks

* **User Awareness:** Educating users to prevent phishing and social engineering.
* **System Patching:** Fixing software weaknesses before hackers exploit them.
* **Preventative Tools:**
  * **Firewall:** Controls incoming and outgoing network traffic.
  * **IPS (Intrusion Prevention System):** Blocks traffic matching attack signatures.
* **Logging & Monitoring:** Tracking network activity to spot unauthorized devices or logins.

---

## Task 2: Areas of Defensive Security

### 1. Security Operations Center (SOC) & Threat Intelligence

* **SOC:** Team that continuously monitors networks to catch security events.
  * **Focus:** Fixes vulnerabilities, enforces security policies, and blocks unauthorized logins.
* **Threat Intelligence:** Gathering data on adversaries to prepare defenses.

---

### 2. Digital Forensics & Incident Response (DFIR)

* **Digital Forensics:** Collecting attack evidence from digital sources.
  * **File System:** Finds hidden or deleted files.
  * **System Memory (RAM):** Inspects programs running in real time.
  * **System & Network Logs:** Tracks attacker actions and movement.
* **Incident Response:** A 4-phase plan to handle attacks and reduce damage:

```text
[ 1. Prepare ] ──► [ 2. Detect & Analyze ] ──► [ 3. Contain & Recover ] ──► [ 4. Post-Incident Review ]
```

---

### 3. Malware Analysis

Analyzing malicious software (Viruses, Trojans, Ransomware) to understand its behavior.

| Analysis Type | Method |
|---|---|
| **Static Analysis** | Inspects code without running it (requires assembly language). |
| **Dynamic Analysis** | Runs malware in a safe sandbox to observe active behavior. |

---

## Task 3: Practical SIEM Lab Walkthrough

### Scenario Overview
Investigating alerts in a **SIEM** (Security Information and Event Management) dashboard to find and block active threats.

```text
[ SIEM Alert ] ──► [ IP Reputation Check ] ──► [ Escalate ] ──► [ Block IP ]
```

### Attack Investigation Steps

1. **Spot Threat:** Found unauthorized SSH access from IP `143.110.250.149` on port `22`.
2. **Check Reputation:** Scanned IP on reputation lookup tool -> **100% Malicious** (China Mobile).
3. **Escalate:** Reported the breach to the **SOC Team Lead**.
4. **Block & Flag:** Added firewall rule to block `143.110.250.149`.
5. **Lab Flag:** **`THM{THREAT-BLOCKED}`**