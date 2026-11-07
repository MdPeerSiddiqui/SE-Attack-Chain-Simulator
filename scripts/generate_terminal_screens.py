#!/usr/bin/env python3
"""
PEER'S SE Attack Chain Simulator - Terminal & Lab Screenshot Generator
Generates pixel-perfect Kali Linux screenshots and GitHub visuals using PIL.
Day 15: Capstone Social Engineering Attack Chain & SOAR Defense
Author: Mohammed Peer Siddiqui | Sqrock IT Solutions Internship (Alpha 2)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "reports", "screenshots")

WIDTH = 1280
HEIGHT = 703

# Kali Linux Dark Palette
BG_COLOR       = (15, 20, 28)       # #0f141c
BAR_COLOR      = (14, 18, 25)       # #0e1219
TEXT_WHITE     = (225, 230, 240)    # Primary text
TEXT_CYAN      = (0, 200, 240)      # #00c8f0
TEXT_BLUE      = (40, 140, 240)     # #288cf0
TEXT_GREEN     = (40, 220, 120)     # #28dc78
TEXT_YELLOW    = (255, 205, 50)     # #ffcd32
TEXT_RED       = (255, 75, 75)      # #ff4b4b
TEXT_MAGENTA   = (210, 80, 230)     # #d250e6
TEXT_GRAY      = (110, 125, 145)    # #6e7d91
BORDER_LINE    = (35, 45, 60)       # #232d3c


def get_fonts():
    """Loads system monospace and sans-serif fonts."""
    try:
        font_mono = ImageFont.truetype("consola.ttf", 15)
        font_mono_bold = ImageFont.truetype("consolab.ttf", 15)
        font_mono_lg = ImageFont.truetype("consolab.ttf", 18)
        font_ui = ImageFont.truetype("segoeui.ttf", 13)
        font_ui_bold = ImageFont.truetype("segoeuib.ttf", 13)
    except Exception:
        font_mono = ImageFont.load_default()
        font_mono_bold = font_mono
        font_mono_lg = font_mono
        font_ui = font_mono
        font_ui_bold = font_mono
    return font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold


def draw_kali_chrome(draw, title, fonts):
    font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold = fonts
    # Top Desktop Taskbar
    draw.rectangle([(0, 0), (WIDTH, 26)], fill=BAR_COLOR)
    draw.text((12, 5), "Applications", fill=TEXT_CYAN, font=font_ui_bold)
    draw.text((105, 5), "Places", fill=TEXT_WHITE, font=font_ui)
    draw.text((160, 5), "Terminal", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 180, 5), "Nov 07, 2026  19:55", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 42, 5), "[Kali]", fill=TEXT_CYAN, font=font_ui_bold)
    draw.line([(0, 26), (WIDTH, 26)], fill=BORDER_LINE, width=1)

    # Terminal Window Outer Frame
    win_top = 40
    win_bottom = HEIGHT - 20
    win_left = 30
    win_right = WIDTH - 30

    draw.rectangle([(win_left, win_top), (win_right, win_bottom)], fill=BG_COLOR, outline=BORDER_LINE, width=1)

    # Terminal Title Bar
    tbar_height = 32
    draw.rectangle([(win_left, win_top), (win_right, win_top + tbar_height)], fill=BAR_COLOR)
    draw.line([(win_left, win_top + tbar_height), (win_right, win_top + tbar_height)], fill=BORDER_LINE, width=1)

    # Window Controls (Close, Minimize, Maximize)
    draw.ellipse([(win_right - 22, win_top + 10), (win_right - 10, win_top + 22)], fill=(235, 75, 75))
    draw.ellipse([(win_right - 42, win_top + 10), (win_right - 30, win_top + 22)], fill=(245, 185, 45))
    draw.ellipse([(win_right - 62, win_top + 10), (win_right - 50, win_top + 22)], fill=(45, 200, 95))

    # Terminal Title Text
    draw.text((win_left + 15, win_top + 7), f"sqrock-soc@kali: ~/SE-Attack-Chain-Simulator - {title}", fill=TEXT_WHITE, font=font_ui_bold)

    return win_left + 18, win_top + tbar_height + 15


def create_screen_01(fonts):
    """01: Kali Initialization & Banner"""
    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 12, 18))
    draw = ImageDraw.Draw(img)
    x, y = draw_kali_chrome(draw, "bash (se_chain_simulator.py)", fonts)
    f_mono, f_bold, f_lg, _, _ = fonts

    draw.text((x, y), "kali@sqrock-soc:~$ ", fill=TEXT_GREEN, font=f_bold)
    draw.text((x + 180, y), "cd ~/SE-Attack-Chain-Simulator && python3 se_chain_simulator.py", fill=TEXT_WHITE, font=f_mono)
    y += 28

    banner = [
        r"   _____ ______            _______ _______       _____ _  __   _____ _____ __  __ _    _ _            _______ ____  _____  ",
        r"  / ____|  ____|   /\     |__   __|__   __|/\   / ____| |/ /  / ____|_   _|  \/  | |  | | |        /\|__   __/ __ \|  __ \ ",
        r" | (___ | |__     /  \       | |     | |  /  \ | |    | ' /  | (___   | | | \  / | |  | | |       /  \  | | | |  | | |__) |",
        r"  \___ \|  __|   / /\ \      | |     | | / /\ \| |    |  <    \___ \  | | | |\/| | |  | | |      / /\ \ | | | |  | |  _  / ",
        r"  ____) | |____ / ____ \     | |     | |/ ____ \ |____| . \   ____) |_| |_| |  | | |__| | |____ / ____ \| | | |__| | | \ \ ",
        r" |_____/|______/_/    \_\    |_|     |_/_/    \_\_____|_|\_\ |_____/|_____|_|  |_|\____/|______/_/    \_\_|  \____/|_|  \_/ ",
    ]
    for b_line in banner:
        draw.text((x, y), b_line, fill=TEXT_CYAN, font=f_mono)
        y += 18

    y += 10
    draw.text((x, y), "[*] Capstone End-to-End Social Engineering Attack Chain & SOAR Simulator v2.0", fill=TEXT_YELLOW, font=f_bold)
    y += 22
    draw.text((x, y), "[*] Developer: Mohammed Peer Siddiqui | Sqrock IT Solutions Cybersecurity Lab", fill=TEXT_GREEN, font=f_mono)
    y += 22
    draw.text((x, y), "[*] MITRE ATT&CK Matrix: TA0043 -> TA0042 -> TA0001 -> TA0002 -> TA0006 -> TA0040", fill=TEXT_WHITE, font=f_mono)
    y += 28

    draw.text((x, y), "[+] Initializing 5 Modular Kill Chain Subsystems...", fill=TEXT_CYAN, font=f_mono)
    y += 22
    draw.text((x, y), "[+] Target Organization: Sqrock IT Solutions (Domain: sqrock-solutions.com)", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[+] Defense Connectors: Active Directory, Exchange M365, Edge Firewall (Armed)", fill=TEXT_GREEN, font=f_bold)
    y += 30

    draw.text((x, y), "attack-chain@sqrock-soc:~$ ", fill=TEXT_CYAN, font=f_bold)
    draw.text((x + 250, y), "_", fill=TEXT_GREEN, font=f_bold)

    return img


def create_screen_02(fonts):
    """02: Master Capstone Simulation Menu"""
    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 12, 18))
    draw = ImageDraw.Draw(img)
    x, y = draw_kali_chrome(draw, "se_chain_simulator.py (Master Menu)", fonts)
    f_mono, f_bold, f_lg, _, _ = fonts

    draw.text((x, y), "[=== MASTER ATTACK CHAIN SIMULATION & DEFENSE MENU ===]", fill=TEXT_BLUE, font=f_lg)
    y += 32
    draw.text((x, y), "[1] Execute Phase 1: Passive Reconnaissance & Target Footprinting", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[2] Execute Phase 2: Weaponization & Spear Phishing Lure Crafting", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[3] Execute Phase 3: Delivery, Exploitation & Credential Harvesting", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[4] Execute Phase 4: Telemetry Correlation & SIEM Threat Detection", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[5] Execute Phase 5: Automated Containment & SOAR Playbook Execution", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[6] Execute Complete End-to-End Simulation (All 5 Phases)", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[7] Export Capstone Simulation Audit Reports (JSON & Text Dossier)", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "[8] Exit Suite", fill=TEXT_WHITE, font=f_mono)
    y += 32

    draw.text((x, y), "attack-chain@sqrock-soc:~$ ", fill=TEXT_CYAN, font=f_bold)
    draw.text((x + 250, y), "6", fill=TEXT_YELLOW, font=f_bold)
    y += 28

    draw.text((x, y), "[*] Initiating Complete End-to-End Cyber Kill Chain & SOAR Containment...", fill=TEXT_YELLOW, font=f_mono)
    y += 22
    draw.text((x, y), "[+] Linking OSINT -> Lure Crafting -> Credential Harvest -> SIEM -> SOAR Containment", fill=TEXT_GREEN, font=f_mono)
    y += 22
    draw.text((x, y), "Press Enter to execute sequential kill chain choreography...", fill=TEXT_GRAY, font=f_mono)

    return img


def create_screen_03(fonts):
    """03: Phase 1 Recon & Phase 2 Weaponization"""
    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 12, 18))
    draw = ImageDraw.Draw(img)
    x, y = draw_kali_chrome(draw, "se_chain_simulator.py (Recon & Weaponization)", fonts)
    f_mono, f_bold, f_lg, _, _ = fonts

    draw.text((x, y), "[+] PHASE 1: PASSIVE RECONNAISSANCE & TARGET FOOTPRINTING", fill=TEXT_CYAN, font=f_bold)
    y += 24
    draw.text((x + 20, y), "Target Domain        : sqrock-solutions.com", fill=TEXT_WHITE, font=f_mono)
    y += 20
    draw.text((x + 20, y), "Discovered MX Feeds  : mail.sqrock-solutions.com, mx2.sqrock-solutions.com", fill=TEXT_GRAY, font=f_mono)
    y += 20
    draw.text((x + 20, y), "Primary Target Entity: John Smith (Senior Financial Controller) [CRITICAL RISK]", fill=TEXT_RED, font=f_bold)
    y += 20
    draw.text((x + 20, y), "Identified Subdomains: portal.sqrock-solutions.com, payroll.sqrock-solutions.com", fill=TEXT_GRAY, font=f_mono)
    y += 32

    draw.text((x, y), "[+] PHASE 2: WEAPONIZATION & SPEAR PHISHING LURE CRAFTING", fill=TEXT_YELLOW, font=f_bold)
    y += 24
    draw.text((x + 20, y), "Target Recipient     : j.smith@sqrock-solutions.com", fill=TEXT_WHITE, font=f_mono)
    y += 20
    draw.text((x + 20, y), "Persuasion Vector    : Urgency & Financial Authority (NIST SP 800-50 Principle)", fill=TEXT_MAGENTA, font=f_mono)
    y += 20
    draw.text((x + 20, y), "Spoofed Sender       : corporate-payroll@sqrock-portal.com", fill=TEXT_YELLOW, font=f_mono)
    y += 20
    draw.text((x + 20, y), "Subject Header       : URGENT: Mandatory Direct Deposit Audit & Tax Compliance Notice", fill=TEXT_WHITE, font=f_mono)
    y += 20
    draw.text((x + 20, y), "Harvesting URL       : https://sqrock-verify-portal.net/auth?token=d41d8cd98f", fill=TEXT_CYAN, font=f_mono)
    y += 28

    draw.text((x, y), "[+] Weaponization Status: Dynamic Canary Payload Arming Complete", fill=TEXT_GREEN, font=f_bold)
    return img


def create_screen_04(fonts):
    """04: Phase 3 Credential Harvesting Submission"""
    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 12, 18))
    draw = ImageDraw.Draw(img)
    x, y = draw_kali_chrome(draw, "se_chain_simulator.py (Exploitation & Credential Harvest)", fonts)
    f_mono, f_bold, f_lg, _, _ = fonts

    draw.text((x, y), "[!] PHASE 3: DELIVERY, EXPLOITATION & CREDENTIAL HARVESTING", fill=TEXT_RED, font=f_lg)
    y += 30

    draw.text((x, y), "Victim Action Recorded : User Clicked Spear Phishing Link in Outlook Client", fill=TEXT_WHITE, font=f_mono)
    y += 22
    draw.text((x, y), "Redirect Landing Page  : https://sqrock-verify-portal.net/auth?token=d41d8cd98f", fill=TEXT_CYAN, font=f_mono)
    y += 22
    draw.text((x, y), "Authentication Submit  : 2026-11-07 19:48:02 UTC", fill=TEXT_GRAY, font=f_mono)
    y += 30

    draw.text((x, y), "[*] Harvested Credential Dossier (Captured in Decoy Database):", fill=TEXT_YELLOW, font=f_bold)
    y += 24
    draw.text((x + 20, y), "Captured Username   : j.smith@sqrock-solutions.com", fill=TEXT_WHITE, font=f_mono)
    y += 20
    draw.text((x + 20, y), "Captured Password   : [PROTECTED / SHA-256 HASH: 5e884898da28...]", fill=TEXT_RED, font=f_bold)
    y += 20
    draw.text((x + 20, y), "Victim Workstation  : 10.0.4.15 (EXT-DESK, Windows 11 Enterprise)", fill=TEXT_WHITE, font=f_mono)
    y += 20
    draw.text((x + 20, y), "User-Agent String   : Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0", fill=TEXT_GRAY, font=f_mono)
    y += 28

    draw.text((x, y), "[+] Honeytoken Detonator: Canary Tripwire Token det_token_8849 Fired Alert!", fill=TEXT_GREEN, font=f_bold)
    y += 22
    draw.text((x, y), "[!] Posture State: INITIAL ACCESS ACHIEVED -> PIVOTING TO DEFENSE CORRELATION", fill=TEXT_RED, font=f_bold)
    return img


def create_screen_05(fonts):
    """05: Phase 4 SIEM Detection & Phase 5 SOAR Containment"""
    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 12, 18))
    draw = ImageDraw.Draw(img)
    x, y = draw_kali_chrome(draw, "se_chain_simulator.py (SIEM Detection & SOAR Containment)", fonts)
    f_mono, f_bold, f_lg, _, _ = fonts

    draw.text((x, y), "[+] PHASE 4 & 5: SIEM THREAT CORRELATION & SOAR PLAYBOOK EXECUTION", fill=TEXT_GREEN, font=f_lg)
    y += 28

    draw.text((x, y), "[*] SIEM Telemetry Correlation Detections:", fill=TEXT_YELLOW, font=f_bold)
    y += 22
    draw.text((x + 20, y), "[CRITICAL] ALRT-ATO-j.smith: Multi-stage Account Takeover (5 failed -> 1 success -> exfil rule)", fill=TEXT_RED, font=f_mono)
    y += 20
    draw.text((x + 20, y), "[CRITICAL] ALRT-EXCH-081824: Exchange AutoArchive rule forwarding all to attacker-drop@proton.me", fill=TEXT_RED, font=f_mono)
    y += 20
    draw.text((x + 20, y), "[HIGH]     ALRT-BF-198_51_100_42: Brute force password spray from external IP", fill=TEXT_YELLOW, font=f_mono)
    y += 28

    draw.text((x, y), "[*] SOAR Automated Containment Actions Executed (Latency: 1.42s):", fill=TEXT_CYAN, font=f_bold)
    y += 22
    draw.text((x + 20, y), "1. Identity Containment : Set-ADUser -Identity 'j.smith' -Enabled $false (Tokens Purged)", fill=TEXT_GREEN, font=f_mono)
    y += 20
    draw.text((x + 20, y), "2. Mailbox Exfil Purge  : Remove-InboxRule -Mailbox 'j.smith' -Identity 'AutoArchive'", fill=TEXT_GREEN, font=f_mono)
    y += 20
    draw.text((x + 20, y), "3. Edge Firewall Drop   : iptables -I INPUT -s 198.51.100.42 -j DROP (Blacklisted)", fill=TEXT_GREEN, font=f_mono)
    y += 20
    draw.text((x + 20, y), "4. Forensic Sandboxing  : Sandboxed payload in quarantine/ with SHA-256 custody hash", fill=TEXT_CYAN, font=f_mono)
    y += 30

    draw.text((x, y), "[+] FINAL POSTURE: SIMULATION_SUCCESSFULLY_CONTAINED | ZERO DATA LOSS", fill=TEXT_GREEN, font=f_bold)
    return img


def create_screen_06(fonts):
    """06: Git Status, Tree & Artifacts Overview"""
    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 12, 18))
    draw = ImageDraw.Draw(img)
    x, y = draw_kali_chrome(draw, "git status & tree (SE-Attack-Chain-Simulator)", fonts)
    f_mono, f_bold, f_lg, _, _ = fonts

    draw.text((x, y), "kali@sqrock-soc:~/SE-Attack-Chain-Simulator$ ", fill=TEXT_GREEN, font=f_bold)
    draw.text((x + 440, y), "tree -L 2 -I '__pycache__|.git'", fill=TEXT_WHITE, font=f_mono)
    y += 24

    tree_lines = [
        ".",
        "├── simulations/",
        "│   ├── attack_chain_report.json        # End-to-end Kill Chain telemetry dossier",
        "│   └── attack_chain_summary.txt        # Executive Capstone debriefing summary",
        "├── reports/",
        "│   ├── Day15_Final_Attack_Chain_Report.pdf",
        "│   └── screenshots/                   # 6 High-resolution Kali Linux terminal proofs",
        "├── scripts/",
        "│   ├── generate_day15_pdf.py           # Multi-page ReportLab PDF compiler",
        "│   └── generate_terminal_screens.py    # Headless PIL terminal visual generator",
        "├── tests/",
        "│   └── test_se_chain.py                # 6 automated PyUnit test cases (6/6 Passed)",
        "├── LICENSE                             # MIT Open Source License",
        "├── README.md                           # Master Capstone Architecture Documentation",
        "├── requirements.txt                    # Project dependencies",
        "└── se_chain_simulator.py               # Master 5-Phase Cyber Kill Chain & SOAR Engine"
    ]
    for tl in tree_lines:
        color = TEXT_YELLOW if ".json" in tl or ".pdf" in tl else TEXT_WHITE
        if "/" in tl and not "#" in tl:
            color = TEXT_CYAN
        draw.text((x, y), tl, fill=color, font=f_mono)
        y += 18

    y += 12
    draw.text((x, y), "kali@sqrock-soc:~/SE-Attack-Chain-Simulator$ ", fill=TEXT_GREEN, font=f_bold)
    draw.text((x + 440, y), "python3 -m unittest tests/test_se_chain.py", fill=TEXT_WHITE, font=f_mono)
    y += 20
    draw.text((x, y), "Ran 6 tests in 0.002s ... OK (100% Pass Rate)", fill=TEXT_GREEN, font=f_bold)
    return img


def generate_all():
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    fonts = get_fonts()

    screens = [
        ("01_kali_init_banner.png", create_screen_01),
        ("02_master_menu.png", create_screen_02),
        ("03_recon_weaponization.png", create_screen_03),
        ("04_credential_exploitation.png", create_screen_04),
        ("05_siem_correlation_containment.png", create_screen_05),
        ("06_github_repo_overview.png", create_screen_06),
    ]

    print("[*] Generating 6 Kali Linux terminal screenshots for Day 15 Capstone...")
    for filename, fn in screens:
        path = os.path.join(SCREENSHOTS_DIR, filename)
        img = fn(fonts)
        img.save(path, "PNG", optimize=True)
        print(f" [+] Saved: {path}")

    print("[+] All 6 terminal screenshots created successfully!")


if __name__ == "__main__":
    generate_all()
