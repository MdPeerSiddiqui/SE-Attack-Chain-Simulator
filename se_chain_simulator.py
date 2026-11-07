#!/usr/bin/env python3
"""
PEER'S SE Attack Chain Simulator - End-to-End Social Engineering Cyber Kill Chain Suite
Sqrock IT Solutions - Cybersecurity Internship Phase 1 (Day 15 Final Capstone)
Author: Mohammed Peer Siddiqui
License: MIT
"""

import os
import sys
import json
import hashlib
import math
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# Standard Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIMS_DIR = os.path.join(BASE_DIR, "simulations")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
DEFAULT_REPORT_JSON = os.path.join(SIMS_DIR, "attack_chain_report.json")
DEFAULT_REPORT_TXT = os.path.join(SIMS_DIR, "attack_chain_summary.txt")

os.makedirs(SIMS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)


class SEAttackChainSimulator:
    """Master Capstone Simulator: End-to-End Cyber Kill Chain & SOAR Defense Orchestrator."""

    def __init__(self, target_org="Sqrock IT Solutions", target_domain="sqrock-solutions.com"):
        self.target_org = target_org
        self.target_domain = target_domain
        self.chain_state = {
            "simulation_id": f"SIM-KILLCHAIN-{int(datetime.now().timestamp())}",
            "started_at": datetime.now().isoformat(),
            "target_org": target_org,
            "target_domain": target_domain,
            "phases": {},
            "status": "INITIALIZED"
        }

    # =========================================================================
    # PHASE 1: RECONNAISSANCE & OSINT ENUMERATION (TA0043 / T1593)
    # =========================================================================
    def execute_phase1_recon(self):
        """Perform passive OSINT scanning, employee enumeration, and digital footprint profiling."""
        recon_data = {
            "phase_name": "Phase 1: Reconnaissance & Target Footprinting",
            "mitre_id": "TA0043 (Reconnaissance) / T1593 (Search Open Websites)",
            "status": "COMPLETED",
            "timestamp": datetime.now().isoformat(),
            "target_domain": self.target_domain,
            "discovered_mx_records": ["mail.sqrock-solutions.com", "mx2.sqrock-solutions.com"],
            "enumerated_employees": [
                {"name": "John Smith", "role": "Senior Financial Controller", "email": "j.smith@sqrock-solutions.com", "risk": "CRITICAL"},
                {"name": "Sarah Connor", "role": "Systems Administrator", "email": "s.connor@sqrock-solutions.com", "risk": "HIGH"},
                {"name": "Mohammed Peer Siddiqui", "role": "Lead Security Engineer", "email": "m.siddiqui@sqrock-solutions.com", "risk": "LOW"}
            ],
            "identified_subdomains": ["portal.sqrock-solutions.com", "vpn.sqrock-solutions.com", "payroll.sqrock-solutions.com"],
            "vulnerability_notes": "Financial controller j.smith identified with public executive profile and external portal login access."
        }
        self.chain_state["phases"]["phase_1_recon"] = recon_data
        return recon_data

    # =========================================================================
    # PHASE 2: WEAPONIZATION & SPEAR PHISHING CRAFTING (TA0042 / T1566)
    # =========================================================================
    def execute_phase2_weaponization(self, target_user="j.smith@sqrock-solutions.com"):
        """Craft psychological lure email payload with credential harvesting link and tracking tokens."""
        tracking_token = hashlib.md5(f"{target_user}_{datetime.now().timestamp()}".encode()).hexdigest()[:10]
        weaponization_data = {
            "phase_name": "Phase 2: Weaponization & Spear Phishing Lure Crafting",
            "mitre_id": "TA0042 (Resource Development) / T1566.002 (Spearphishing Link)",
            "status": "COMPLETED",
            "timestamp": datetime.now().isoformat(),
            "target_victim": target_user,
            "psychological_trigger": "Urgency & Financial Authority (NIST SP 800-50 Principle)",
            "spoofed_sender": "corporate-payroll@sqrock-portal.com",
            "subject": "URGENT: Mandatory Direct Deposit Audit & Tax Compliance Notice",
            "harvesting_url": f"https://sqrock-verify-portal.net/auth?token={tracking_token}",
            "tracking_token": tracking_token,
            "email_body_preview": (
                "Attention John: Failure to verify your employee banking credentials within 24 hours "
                "will result in suspension of current payroll disbursements. Click here to confirm identity."
            )
        }
        self.chain_state["phases"]["phase_2_weaponization"] = weaponization_data
        return weaponization_data

    # =========================================================================
    # PHASE 3: DELIVERY & EXPLOITATION (TA0001 / TA0002 / T1204)
    # =========================================================================
    def execute_phase3_exploitation(self):
        """Simulate victim lure engagement, credential harvesting submission, and token detonator."""
        exploitation_data = {
            "phase_name": "Phase 3: Delivery, Exploitation & Credential Harvesting",
            "mitre_id": "TA0001 (Initial Access) / T1204.001 (User Execution: Malicious Link)",
            "status": "COMPLETED",
            "timestamp": datetime.now().isoformat(),
            "victim_clicked": True,
            "harvested_credentials": {
                "username": "j.smith@sqrock-solutions.com",
                "password_hash": hashlib.sha256(b"Summer2026!").hexdigest()[:16] + "...",
                "source_client_ip": "10.0.4.15",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0"
            },
            "tripwire_detonation": "Canary token det_token_8849 activated at 19:48:02 UTC.",
            "posture": "COMPROMISED (Victim submitted credentials to spoofed portal)"
        }
        self.chain_state["phases"]["phase_3_exploitation"] = exploitation_data
        return exploitation_data

    # =========================================================================
    # PHASE 4: TELEMETRY CORRELATION & SIEM DETECTION (TA0006 / TA0003)
    # =========================================================================
    def execute_phase4_siem_detection(self):
        """Simulate SIEM multi-source ingestion and behavioral correlation of the intrusion."""
        siem_data = {
            "phase_name": "Phase 4: Telemetry Correlation & SIEM Threat Detection",
            "mitre_id": "TA0006 (Credential Access) / T1110 (Brute Force) / T1114.003 (Mail Forwarding)",
            "status": "COMPLETED",
            "timestamp": datetime.now().isoformat(),
            "correlated_alerts": [
                {
                    "alert_id": "ALRT-BF-198_51_100_42",
                    "severity": "HIGH",
                    "tactic": "Credential Access",
                    "description": "5 consecutive failed authentication attempts against j.smith from 198.51.100.42"
                },
                {
                    "alert_id": "ALRT-ATO-j.smith",
                    "severity": "CRITICAL",
                    "tactic": "Account Takeover",
                    "description": "Adversary successfully authenticated followed by creation of rule=forward_all"
                },
                {
                    "alert_id": "ALRT-EXCH-081824",
                    "severity": "CRITICAL",
                    "tactic": "Collection / Exfiltration",
                    "description": "Exchange InboxRule AutoArchive redirects all emails to attacker-drop@proton.me"
                }
            ],
            "total_alerts": 3,
            "escalation": "CRITICAL P1 ALERT DISPATCHED TO SOAR ORCHESTRATOR"
        }
        self.chain_state["phases"]["phase_4_siem"] = siem_data
        return siem_data

    # =========================================================================
    # PHASE 5: AUTOMATED INCIDENT RESPONSE & CONTAINMENT (TA0040 / NIST SP 800-61)
    # =========================================================================
    def execute_phase5_containment(self):
        """Execute automated NIST SP 800-61 Rev.2 containment actions across identity, mailbox & perimeter."""
        containment_data = {
            "phase_name": "Phase 5: Automated Containment & SOAR Playbook Execution",
            "mitre_id": "TA0040 (Impact Mitigation) / NIST SP 800-61 Rev.2 Section 3.3",
            "status": "COMPLETED",
            "timestamp": datetime.now().isoformat(),
            "actions_executed": [
                {
                    "action": "IDENTITY_CONTAINMENT",
                    "target": "j.smith@sqrock-solutions.com",
                    "result": "Disabled AD account, revoked Kerberos TGTs and OAuth refresh tokens."
                },
                {
                    "action": "MAILBOX_CONTAINMENT",
                    "target": "AutoArchive Forwarding Rule",
                    "result": "Purged rule=forward_all to attacker-drop@proton.me and isolated phishing lure."
                },
                {
                    "action": "NETWORK_PERIMETER_BLOCK",
                    "target": "198.51.100.42",
                    "result": "Injected edge firewall drop rule: iptables -I INPUT -s 198.51.100.42 -j DROP."
                },
                {
                    "action": "EVIDENCE_SANDBOXING",
                    "target": "evidence_phish_lure.eml",
                    "result": "Preserved artifact into quarantine/ with SHA-256 digest."
                }
            ],
            "final_containment_latency_seconds": 1.42,
            "remediation_status": "FULL CONTAINMENT ACHIEVED - BLAST RADIUS NEUTRALIZED"
        }
        self.chain_state["phases"]["phase_5_containment"] = containment_data
        self.chain_state["status"] = "SIMULATION_SUCCESSFULLY_CONTAINED"
        return containment_data

    def run_entire_chain(self):
        """Execute all five phases sequentially and return full simulation dossier."""
        self.execute_phase1_recon()
        self.execute_phase2_weaponization()
        self.execute_phase3_exploitation()
        self.execute_phase4_siem_detection()
        self.execute_phase5_containment()
        return self.chain_state

    def export_reports(self, json_path=DEFAULT_REPORT_JSON, txt_path=DEFAULT_REPORT_TXT):
        """Export comprehensive Capstone simulation audit dossiers."""
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(self.chain_state, f, indent=2)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("=" * 80 + "\n")
            f.write("    SQROCK IT SOLUTIONS - END-TO-END SOCIAL ENGINEERING ATTACK CHAIN AUDIT\n")
            f.write("=" * 80 + "\n")
            f.write(f"Simulation ID       : {self.chain_state['simulation_id']}\n")
            f.write(f"Target Organization : {self.chain_state['target_org']}\n")
            f.write(f"Target Domain       : {self.chain_state['target_domain']}\n")
            f.write(f"Execution Started   : {self.chain_state['started_at']}\n")
            f.write(f"Final Posture Status: {self.chain_state['status']}\n")
            f.write("-" * 80 + "\n\n")

            for p_key, p_data in self.chain_state["phases"].items():
                f.write(f"[{p_data['status']}] {p_data['phase_name']}\n")
                f.write(f"  MITRE ATT&CK : {p_data['mitre_id']}\n")
                f.write(f"  Timestamp    : {p_data['timestamp']}\n")
                f.write(f"  Details      : {json.dumps(p_data, indent=4)}\n")
                f.write("-" * 80 + "\n\n")

            f.write("EXECUTIVE VERDICT: Full end-to-end simulation successfully conducted.\n")
            f.write("Attacker kill chain was successfully identified by SIEM and contained by SOAR in 1.42s.\n")

        return self.chain_state


def print_banner():
    """Display terminal banner."""
    print(Fore.CYAN + Style.BRIGHT + r"""
   _____ ______            _______ _______       _____ _  __   _____ _____ __  __ _    _ _            _______ ____  _____  
  / ____|  ____|   /\     |__   __|__   __|/\   / ____| |/ /  / ____|_   _|  \/  | |  | | |        /\|__   __/ __ \|  __ \ 
 | (___ | |__     /  \       | |     | |  /  \ | |    | ' /  | (___   | | | \  / | |  | | |       /  \  | | | |  | | |__) |
  \___ \|  __|   / /\ \      | |     | | / /\ \| |    |  <    \___ \  | | | |\/| | |  | | |      / /\ \ | | | |  | |  _  / 
  ____) | |____ / ____ \     | |     | |/ ____ \ |____| . \   ____) |_| |_| |  | | |__| | |____ / ____ \| | | |__| | | \ \ 
 |_____/|______/_/    \_\    |_|     |_/_/    \_\_____|_|\_\ |_____/|_____|_|  |_|\____/|______/_/    \_\_|  \____/|_|  \_\
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + " [*] Capstone End-to-End Social Engineering Attack Chain & SOAR Simulator v2.0")
    print(Fore.GREEN + " [*] Developer: Mohammed Peer Siddiqui | Sqrock IT Solutions Cybersecurity Lab")
    print(Fore.WHITE + " [*] MITRE ATT&CK Matrix: TA0043 -> TA0042 -> TA0001 -> TA0002 -> TA0006 -> TA0040\n")


def run_interactive_menu():
    """CLI driver loop."""
    sim = SEAttackChainSimulator()

    while True:
        print_banner()
        print(Fore.LIGHTBLUE_EX + " [=== MASTER ATTACK CHAIN SIMULATION & DEFENSE MENU ===]")
        print(Fore.WHITE + " [1] Execute Phase 1: Passive Reconnaissance & Target Footprinting")
        print(Fore.WHITE + " [2] Execute Phase 2: Weaponization & Spear Phishing Lure Crafting")
        print(Fore.WHITE + " [3] Execute Phase 3: Delivery, Exploitation & Credential Harvesting")
        print(Fore.WHITE + " [4] Execute Phase 4: Telemetry Correlation & SIEM Threat Detection")
        print(Fore.WHITE + " [5] Execute Phase 5: Automated Containment & SOAR Playbook Execution")
        print(Fore.WHITE + " [6] Execute Complete End-to-End Simulation (All 5 Phases)")
        print(Fore.WHITE + " [7] Export Capstone Simulation Audit Reports (JSON & Text Dossier)")
        print(Fore.WHITE + " [8] Exit Suite\n")

        try:
            choice = input(Fore.CYAN + " attack-chain@sqrock-soc:~$ " + Style.RESET_ALL).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting Simulation Suite...")
            break

        if choice == "1":
            print(Fore.YELLOW + "\n[*] Executing Phase 1: Passive OSINT & Reconnaissance...")
            p1 = sim.execute_phase1_recon()
            print(Fore.GREEN + f"[+] Discovered MX Records    : {', '.join(p1['discovered_mx_records'])}")
            print(Fore.GREEN + f"[+] Enumerated Target Users  : {len(p1['enumerated_employees'])} employees identified.")
            for e in p1["enumerated_employees"]:
                print(Fore.WHITE + f"    - {e['name']} ({e['role']}) -> {e['email']} [{Fore.RED}{e['risk']}{Fore.WHITE}]")
            print()
            input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")

        elif choice == "2":
            print(Fore.YELLOW + "\n[*] Executing Phase 2: Weaponization & Lure Generation...")
            p2 = sim.execute_phase2_weaponization()
            print(Fore.GREEN + f"[+] Target Victim      : {p2['target_victim']}")
            print(Fore.GREEN + f"[+] Persuasion Trigger : {p2['psychological_trigger']}")
            print(Fore.GREEN + f"[+] Harvesting URL     : {Fore.CYAN}{p2['harvesting_url']}")
            print(Fore.WHITE + f"[+] Preview Body       : {p2['email_body_preview']}\n")
            input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")

        elif choice == "3":
            print(Fore.YELLOW + "\n[*] Executing Phase 3: Delivery, Exploitation & Credential Capture...")
            p3 = sim.execute_phase3_exploitation()
            print(Fore.RED + Style.BRIGHT + f"[!] CREDENTIALS HARVESTED FROM VICTIM PORTAL INTERACTION:")
            print(Fore.WHITE + f"    Username         : {p3['harvested_credentials']['username']}")
            print(Fore.WHITE + f"    Password Hash    : {p3['harvested_credentials']['password_hash']}")
            print(Fore.WHITE + f"    Client IP        : {p3['harvested_credentials']['source_client_ip']}")
            print(Fore.GREEN + f"[+] Canary Detonator : {p3['tripwire_detonation']}\n")
            input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")

        elif choice == "4":
            print(Fore.YELLOW + "\n[*] Executing Phase 4: SIEM Correlation & Threat Ingestion...")
            p4 = sim.execute_phase4_siem_detection()
            print(Fore.GREEN + f"[+] Ingested Telemetry -> {p4['total_alerts']} Critical Threat Alerts Correlated:")
            for a in p4["correlated_alerts"]:
                sev_col = Fore.RED if a["severity"] == "CRITICAL" else Fore.YELLOW
                print(f"    [{sev_col}{a['severity']}{Style.RESET_ALL}] {a['alert_id']} - {a['description']}")
            print(Fore.CYAN + f"\n[+] Status: {p4['escalation']}\n")
            input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")

        elif choice == "5":
            print(Fore.YELLOW + "\n[*] Executing Phase 5: Automated SOAR Containment Playbook...")
            p5 = sim.execute_phase5_containment()
            print(Fore.GREEN + f"[+] Playbook Latency: {p5['final_containment_latency_seconds']} seconds.")
            for act in p5["actions_executed"]:
                print(Fore.WHITE + f"    [COMPLETED] {act['action']} on {act['target']}")
                print(Fore.LIGHTBLACK_EX + f"      -> {act['result']}")
            print(Fore.GREEN + Style.BRIGHT + f"\n[+] {p5['remediation_status']}\n")
            input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")

        elif choice == "6":
            print(Fore.YELLOW + "\n[*] RUNNING FULL END-TO-END ATTACK CHAIN & CONTAINMENT SIMULATION...")
            sim.run_entire_chain()
            print(Fore.GREEN + "[+] Phase 1: Reconnaissance         -> COMPLETED")
            print(Fore.GREEN + "[+] Phase 2: Weaponization          -> COMPLETED")
            print(Fore.GREEN + "[+] Phase 3: Delivery & Exploitation-> COMPLETED")
            print(Fore.GREEN + "[+] Phase 4: SIEM Threat Correlation-> COMPLETED")
            print(Fore.GREEN + "[+] Phase 5: Automated SOAR Contain -> COMPLETED")
            print(Fore.CYAN + f"\n[+] Simulation Status: {sim.chain_state['status']}\n")
            input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")

        elif choice == "7":
            print(Fore.YELLOW + "\n[*] Exporting formal Capstone simulation audit dossiers...")
            sim.export_reports()
            print(Fore.GREEN + f"[+] JSON Report exported: {DEFAULT_REPORT_JSON}")
            print(Fore.GREEN + f"[+] Text Dossier exported: {DEFAULT_REPORT_TXT}\n")
            input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")

        elif choice == "8":
            print(Fore.CYAN + "\n[*] Shutting down Capstone Simulation Engine. Congratulations on completing Phase 1!\n")
            break
        else:
            print(Fore.RED + "\n[!] Invalid selection. Please choose 1-8.\n")


if __name__ == "__main__":
    if len(sys.argv) > 1 and "--batch" in sys.argv:
        simulator = SEAttackChainSimulator()
        simulator.run_entire_chain()
        simulator.export_reports()
        print("[+] Headless Capstone Attack Chain execution completed.")
    else:
        run_interactive_menu()
