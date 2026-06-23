from playwright.sync_api import sync_playwright

# 1. TODO | get the raw data from the whois.com (scrapper)
def whois_web_scrapper(domain_url: str | None = None) -> list[str] | None:
    if not domain_url:
        print("❌❌ Failed! No doman url provided => whois_web_scrapper(None)")
        return None
    try:
        with sync_playwright() as ply:
            broswer = ply.chromium.launch() # launch google chrome and show it real time
            page = broswer.new_page()
            page.goto("https://whois.com/") # go to whois.com homepage
            page.get_by_placeholder("Enter Domain or IP").type(domain_url)
            page.keyboard.press("Enter")
            
            contents = page.locator(".whois-data").inner_text().split('\n')
            # print(contents)
            print("Your request was successful ✅✅")
            broswer.close()
            return contents
    except Exception as error:
        print(f"❌❌ Failed to perform the request due to the error:\n{str(error).splitlines()[0]}")
        return None

# 2. TODO | clean the data to only have the needed fields
def scrapped_data_cleaner(data: list[str] | None) -> dict[str, str | list[str]] | None:
    if not data:
        print('❌❌ No data provided')
        return None

    FIELDS_TO_PERSERVE = [
        "domain",
        "registered_on",
        "expires_on",
        "updated_on",
        "registrar",
        "registrant_organization",
        "registrant_country",
        "status"
    ]

    filtered_data = {}
    current_key = None

    for line in data:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            current_key = line[:-1].lower().replace(" ", "_")
            filtered_data[current_key] = []
        else:
            if current_key:
                filtered_data[current_key].append(line)

    # Only keep specified fields and format output
    final_data = {}
    for key, val in filtered_data.items():
        if key in FIELDS_TO_PERSERVE:
            # flatten single-line fields to str
            if len(val) == 1:
                final_data[key] = val[0]
            else:
                final_data[key] = val

    return final_data

# TODO | all the functions together
def end_state_data(url: str | None = None) -> dict[str, str | list[str]] | None:
    try:
        whois_data = whois_web_scrapper(url)
        final_data = scrapped_data_cleaner(whois_data)
        return final_data
    except:
        return None
    

if __name__ == '__main__':
    data = whois_web_scrapper("bcit.ca")
    print("\n\n")
    print(data)
    print("\n\n")
    # result = scrapped_data_cleaner(data)
    # print("\n\n")
    # print(result)