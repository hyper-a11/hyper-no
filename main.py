from hyper_no.scanner import scan_number
from hyper_no.exporter import export_to_json, export_to_csv, export_to_txt
from hyper_no.logger import log_result

if __name__ == "__main__":
    print("\033[96m[🔍] Hyper No. OSINT Phone Scanner v1.0\033[0m\n")
    number = input("\033[92m[📲] Enter phone number (e.g. +911234567890): \033[0m")

    result = scan_number(number)

    if not result.get("valid"):
        print("\n\033[91m[✗] Invalid number or error:\033[0m", result.get("error", "Unknown"))
    else:
        print("\n\033[92m[✓] Number Valid\033[0m")
        print(f"[🌍] Region: {result['region']}")
        print(f"[📡] Carrier: {result['carrier']}")
        print(f"[🕒] Time Zones: {', '.join(result['timezones'])}")
        print(f"[📞] E.164 Format: {result['e164_format']}")
        print(f"[✉️] Gmail Guess: {result['gmail_guess']}")
        print(f"[🔐] Breach Info: {result['breach_found']}")
        print(f"[👤] Possible Name: {result['name_guess']}")
        print(f"[📱] WhatsApp: {result['whatsapp_link']}")
        print(f"[✈️] Telegram: {result['telegram_link']}")
        print(f"[📘] Facebook Search: {result['facebook_link']}")
        print(f"[🌐] Google Results:")
        for i, g in enumerate(result['google_results'], 1):
            print(f"    {i}. {g}")

        export_to_json(result)
        export_to_csv(result)
        export_to_txt(result)
        log_result(result)

        print("\n\033[94m[✓] Data exported to output.json, output.csv, output.txt\033[0m")
