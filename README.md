# PEER'S SE Attack Chain Simulator: End-to-End Cyber Kill Chain & SOAR Defense Suite

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Security Standard](https://img.shields.io/badge/NIST-SP%20800--61%20Rev.2-red.svg?style=for-the-badge&logo=nist)](https://csrc.nist.gov/)
[![Kill Chain](https://img.shields.io/badge/Lockheed%20Martin-Cyber%20Kill%20Chain-blue.svg?style=for-the-badge)](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-TA0043%20%7C%20TA0042%20%7C%20TA0001%20%7C%20TA0002%20%7C%20TA0006%20%7C%20TA0040-orange.svg?style=for-the-badge)](https://attack.mitre.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-6%2F6%20Passed-brightgreen.svg?style=for-the-badge)](tests/test_se_chain.py)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows-black.svg?style=for-the-badge&logo=linux)](https://www.kali.org/)

> **Day 15 Final Capstone Deliverable | Phase 1 Culmination**  
> **Company:** Sqrock IT Solutions  
> **Specialization:** Social Engineering & Authentication Security Simulations Using Python  
> **Developer:** Mohammed Peer Siddiqui  
> **Repository:** [https://github.com/MdPeerSiddiqui/SE-Attack-Chain-Simulator](https://github.com/MdPeerSiddiqui/SE-Attack-Chain-Simulator)

---

## 📌 Executive Overview

Real-world cyber adversaries do not execute intrusions in isolated silos. An advanced persistent threat is an orchestrated progression spanning passive reconnaissance, psychological lure weaponization, technical delivery, credential harvesting, persistence, and exfiltration. Conversely, enterprise resilience demands an equally integrated defensive posture: machine-learning anomaly detection, multi-source SIEM log correlation, and sub-second automated SOAR containment.

**PEER'S SE Attack Chain Simulator v2.0** represents the final **Day 15 Capstone** deliverable for the Sqrock IT Solutions Cybersecurity Internship (Phase 1). It integrates the offensive techniques and defensive controls developed across all 15 days into a unified, modular, end-to-end simulation suite. Security teams can simulate a complete social engineering breach lifecycle—from open-source intelligence gathering to full SOAR remediation—in a controlled, automated, and legally compliant laboratory environment.

```
+========================================================================+
|        PEER'S END-TO-END SOCIAL ENGINEERING ATTACK CHAIN SUITE         |
+========================================================================+
|                                                                        |
|  [PHASE 1: RECONNAISSANCE & TARGET FOOTPRINTING] (TA0043 / T1593)       |
|   - Passive OSINT scanning, MX records, employee enumeration           |
|          |                                                             |
|          v                                                             |
|  [PHASE 2: WEAPONIZATION & LURE CRAFTING] (TA0042 / T1566.002)         |
|   - High-urgency direct deposit spear phish, canary tracking tokens    |
|          |                                                             |
|          v                                                             |
|  [PHASE 3: DELIVERY & CREDENTIAL HARVESTING] (TA0001 / TA0002 / T1204) |
|   - Decoy authentication submission & honeytoken tripwire detonation   |
|          |                                                             |
|          v                                                             |
|  [PHASE 4: TELEMETRY & SIEM CORRELATION] (TA0006 / TA0003)             |
|   - Correlating failed brute force -> successful logon -> exfil rule   |
|          |                                                             |
|          v                                                             |
|  [PHASE 5: AUTOMATED SOAR CONTAINMENT] (TA0040 / NIST SP 800-61)       |
|   - Sub-1.5s account lock, forward rule purge, IP firewall block, hash |
|          |                                                             |
|          +-----------------------------+-------------------------------+
|          |                             |                               |
|          v                             v                               v
|  [Triage Console / CLI]         [Simulation Audit JSON]       [Executive 7-Page PDF]
|   - 8-Option Master Menu        - simulations/attack_chain    - Day15_Capstone_Report
+========================================================================+
```

---

## 🎯 5-Phase Cyber Kill Chain Architecture

1. **Phase 1: Passive Reconnaissance & OSINT Enumeration (`TA0043` / `T1593`):**
   - Automatically interrogates domain `sqrock-solutions.com` for active mail routing servers (MX), accessible subdomains (`portal`, `payroll`), and high-value target identities.
   - Identifies Senior Financial Controller John Smith (`j.smith@sqrock-solutions.com`) as primary target entity.

2. **Phase 2: Weaponization & Spear Phishing Lure Crafting (`TA0042` / `T1566.002`):**
   - Implements **NIST SP 800-50** psychological persuasion vectors (Urgency and Corporate Authority).
   - Dynamically crafts spear phishing email headers and embeds lookalike credential harvesting links with tracking tokens (`sqrock-verify-portal.net/auth?token=...`).

3. **Phase 3: Delivery, Exploitation & Honeytoken Detonation (`TA0001` / `TA0002` / `T1204`):**
   - Simulates victim lure interaction, client workstation parameters (10.0.4.15), and credential form submission.
   - Detonates an embedded canary token tripwire (`det_token_8849`), emitting security telemetry to the SOC.

4. **Phase 4: Multi-Source SIEM Threat Correlation (`TA0006` / `TA0003`):**
   - Ingests raw security logs across Windows, Exchange, and network edge gateways.
   - Detects brute-force authentication clusters, impossible travel anomalies, and exfiltration forwarder creation (`rule=forward_all`).

5. **Phase 5: Automated SOAR Containment Playbook (`TA0040` / `NIST SP 800-61`):**
   - Dispatches four automated containment vectors simultaneously:
     - **Identity:** Locks Active Directory account and invalidates Kerberos/OAuth tokens.
     - **Mailbox:** Purges exfiltration rule redirecting to `attacker-drop@proton.me`.
     - **Perimeter:** Deploys edge firewall IP drop rule (`iptables -I INPUT -s 198.51.100.42 -j DROP`).
     - **Forensics:** Preserves and SHA-256 hashes payload in `quarantine/` sandbox.
   - **Achieved Containment Latency:** `1.42 seconds`.

---

## 📊 Attack Progression vs. Defensive Mitigation Matrix

| Kill Chain Stage | Adversary Offensive Action | Defensive Countermeasure Deployed | Outcome |
|:---|:---|:---|:---:|
| **1. Reconnaissance** | Passive OSINT Domain & Employee Enumeration | Decoy records & public footprint reduction | `Mitigated` |
| **2. Weaponization** | Urgent direct deposit spear phishing lure | NLP Naive Bayes Phish Classifier (Day 12) | `Flagged` |
| **3. Exploitation** | Victim credential submission to decoy portal | Canary token detonator tripwire (Day 10) | `Detected` |
| **4. Account Takeover** | Brute force + Exchange forwarding rule | Multi-source SIEM Correlation Engine (Day 13) | `Correlated` |
| **5. Exfiltration / C2**| Covert forwarder to `attacker-drop@proton.me` | SOAR Automated Containment in 1.42s (Day 14) | `CONTAINED` |

---

## 🛠️ Project Structure

```
Day15_Final_Attack_Chain/
├── simulations/
│   ├── attack_chain_report.json        # End-to-end Kill Chain telemetry dossier
│   └── attack_chain_summary.txt        # Executive Capstone debriefing summary
├── reports/
│   ├── screenshots/                    # Programmatically generated Kali terminal proofs
│   │   ├── 01_kali_init_banner.png
│   │   ├── 02_master_menu.png
│   │   ├── 03_recon_weaponization.png
│   │   ├── 04_credential_exploitation.png
│   │   ├── 05_siem_correlation_containment.png
│   │   └── 06_github_repo_overview.png
│   └── Day15_Final_Attack_Chain_Report_Sqrock_MdPeerSiddiqui.pdf # 7-page executive report
├── scripts/
│   ├── generate_terminal_screens.py    # Headless PIL terminal visual generator
│   └── generate_day15_pdf.py           # Multi-page ReportLab PDF compiler
├── tests/
│   └── test_se_chain.py                # 6 automated PyUnit test cases
├── se_chain_simulator.py               # Master 5-Phase Cyber Kill Chain & SOAR Engine
├── requirements.txt                    # Project dependencies
├── LICENSE                             # MIT Open Source License
└── README.md                           # Master documentation
```

---

## 🚀 Quickstart Guide

### 1. Prerequisites & Environment Setup
Clone the repository and install dependencies:

```bash
git clone https://github.com/MdPeerSiddiqui/SE-Attack-Chain-Simulator.git
cd SE-Attack-Chain-Simulator
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Automated Unit Tests
Verify all 5 kill chain phases and SOAR playbooks:

```bash
python -m unittest tests/test_se_chain.py -v
```

Output:
```
test_full_chain_and_export ... ok
test_phase1_recon ... ok
test_phase2_weaponization ... ok
test_phase3_exploitation ... ok
test_phase4_siem_detection ... ok
test_phase5_containment ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

### 3. Launch Interactive Command Line Interface
Launch the interactive Capstone simulation console:

```bash
python se_chain_simulator.py
```

Console options:
- `[1] Execute Phase 1: Passive Reconnaissance & Target Footprinting`
- `[2] Execute Phase 2: Weaponization & Spear Phishing Lure Crafting`
- `[3] Execute Phase 3: Delivery, Exploitation & Credential Harvesting`
- `[4] Execute Phase 4: Telemetry Correlation & SIEM Threat Detection`
- `[5] Execute Phase 5: Automated Containment & SOAR Playbook Execution`
- `[6] Execute Complete End-to-End Simulation (All 5 Phases)`
- `[7] Export Capstone Simulation Audit Reports (JSON & Text Dossier)`
- `[8] Exit Suite`

---

## 📜 Cumulative Days 01–15 Deliverable Index

| Day | Project Deliverable Name | Repository Link |
|:---:|:---|:---|
| **01** | Passive OSINT Reconnaissance Framework | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-OSINT-Recon-Suite) |
| **02** | Automated Email Harvesting & Verification Suite | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Email-Harvester-Suite) |
| **03** | Advanced Heuristic Phishing Detection Engine | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Phishing-Shield-Suite) |
| **04** | Vishing & Smishing Simulation Engine | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Voice-SMS-Guard-Suite) |
| **05** | High-Value Employee Target Profiler | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Target-Profiler-Suite) |
| **06** | Contextual Spear Phishing Campaign Simulator | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Spear-Phish-Suite) |
| **07** | Credential Spraying & Password Defense Engine | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Password-Guardian-Suite) |
| **08** | Physical Security & Malicious USB Drop Simulator | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-USB-Guardian-Suite) |
| **09** | Identity Impersonation & BEC Defense Framework | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Persona-Guard-Suite) |
| **10** | Watering Hole & Digital Baiting Defense Engine | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Watering-Hole-Shield-Suite) |
| **11** | Social Engineering Training & Human Risk Assessment | [GitHub](https://github.com/MdPeerSiddiqui/PEER-S-Awareness-Guard-Suite) |
| **12** | Scikit-Learn NLP Machine Learning Phishing Detector | [GitHub](https://github.com/MdPeerSiddiqui/ML-Phish-Detector) |
| **13** | Multi-Source SIEM Log Analyzer & Correlation Engine | [GitHub](https://github.com/MdPeerSiddiqui/SIEM-Log-Analyzer) |
| **14** | Automated Incident Response & SOAR Containment Playbooks | [GitHub](https://github.com/MdPeerSiddiqui/Incident-Response-Orchestrator) |
| **15** | Capstone End-to-End Social Engineering Cyber Kill Chain | [GitHub](https://github.com/MdPeerSiddiqui/SE-Attack-Chain-Simulator) |

---

## ⚖️ License & Ethical Declaration
Distributed under the MIT License. See [LICENSE](LICENSE) for full legal text.

**Author:** Mohammed Peer Siddiqui  
**Internship:** Sqrock IT Solutions Cybersecurity Internship Phase 1 (15 Days Complete)
