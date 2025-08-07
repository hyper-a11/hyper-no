import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def scan_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return {"valid": False, "error": "Invalid phone number format."}

        region = geocoder.description_for_number(parsed_number, "en")
        provider = carrier.name_for_number(parsed_number, "en")
        timezones = timezone.time_zones_for_number(parsed_number)
        e164_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        result = {
            "valid": True,
            "region": region,
            "carrier": provider,
            "timezones": list(timezones),
            "e164_format": e164_format,
            "gmail_guess": f"{parsed_number.national_number}@gmail.com",
            "whatsapp_link": f"https://wa.me/{parsed_number.national_number}",
            "telegram_link": f"https://t.me/+{parsed_number.national_number}",
            "facebook_link": f"https://facebook.com/search/top/?q={parsed_number.national_number}",
            "name_guess": "Ravi Kumar",  # static guess for now
            "google_results": [
                "Truecaller profile of Ravi Kumar",
                "Leaked database reference on Pastebin",
                "Facebook result for this number"
            ],
            "breach_found": breach_check(str(parsed_number.national_number))
        }
        return result

    except Exception as e:
        return {"valid": False, "error": str(e)}

def breach_check(number):
    try:
        with open("leaks/breaches.txt", "r") as f:
            leaks = f.read().splitlines()
        for line in leaks:
            if number in line:
                return "Found in Indian voter leak"
        return "No breach found"
    except FileNotFoundError:
        return "Leak database missing"
