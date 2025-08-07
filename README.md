# 📱 Hyper No. — Phone Number OSINT Scanner

**Hyper No.** is a lightweight, no-API OSINT module that gathers intelligence from phone numbers using only open-source methods. Designed for ethical researchers, cybersecurity analysts, and red teamers, it's fully offline, API-free, and Termux-compatible.

---

## 🔍 Features

- ✅ Validates phone numbers (E.164 format)
- 🌍 Detects region, carrier, and timezone
- 📧 Generates common Gmail permutations
- ⚠️ Checks against local breach database
- 👤 Simulates possible owner name (mocked)
- 📱 Creates direct links to:
  - WhatsApp
  - Telegram
  - Facebook search
- 🌐 Simulates Google OSINT results (dork-style)
- 💾 Exports results to:
  - `output.json`
  - `output.csv`
  - `output.txt`
- 🧾 Logs all scans to `scanner.log`
- 🌗 CLI dark mode output with color highlights
- ✅ 100% API-free, works offline

---

## ⚙️ Installation

### 1. Clone the repo

```bash
pkg update && pkg upgrade
pkg install python git
pip install phonenumbers
git clone https://github.com/hyper-a11/hyper-no1.git
cd hyper-no1
pip install -r requirements.txt
python3 main.py

--- 

### EXAMPLE 📩
[✓] Number Valid: True
[+] Region: India
[+] Carrier: Airtel
[+] Time Zones: ['Asia/Kolkata']
[+] Format (E.164): +911234567890
[+] Gmail Guess: 911234567890@gmail.com
[⚠️] Breach Found: Found in Indian voter leak
[👤] Possible Name: Ravi Kumar
[📱] WhatsApp: https://wa.me/911234567890
[+] Telegram: https://t.me/+911234567890
[+] Facebook: https://facebook.com/search/top/?q=911234567890
[🌐] Public Google Results:
  1. Truecaller profile of Ravi Kumar
  2. Leaked database reference on Pastebin
  3. Facebook result for this number

_ _ _ 



RUN CODE

' python3 main.py '

