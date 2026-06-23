from app.services.scrappy import scrapped_data_cleaner

RAW_WHOIS_DATA = [
    'bcit.ca',
    'Updated 5 days ago',
    'Domain Information',
    'Domain:', 'bcit.ca',
    'Registered On:', '2000-10-19',
    'Expires On:', '2027-04-19',
    'Updated On:', '2026-06-03',
    'Status:', 'client transfer prohibited', 'client update prohibited',
    'Name Servers:', 'gold.foundationdns.com', 'gold.foundationdns.net', 'gold.foundationdns.org', 'ns1.bcit.ca', 'ns2.bcit.ca', 'ns3.bcit.ca',
    'Registrar Information',
    'Registrar:', 'Internic.ca Inc.',
    'IANA ID:', 'not applicable',
    'URL:', 'www.internic.ca',
    'Abuse Email:', 'abuse@internic.ca',
    'Abuse Phone:', '+1.8886988850',
    'Registrant Contact',
    'Name:', 'British Columbia Institute of Technology',
    'Street:', '532 Montreal Rd',
    'Suite 261',
    'City:', 'Ottawa',
    'State:', 'ON',
    'Postal Code:', 'K1K4R4',
    'Country:', 'CA',
    'Phone:', '+1.8666421232',
    'Fax:', '+1.6137061248',
    'Email:', '@privacyhero.company',
    'Administrative Contact',
    'Name:', 'Connor Malcolm',
    'Organization:', 'Privacy Hero Inc.',
    'Street:', '532 Montreal Rd',
    'Suite 261',
    'City:', 'Ottawa',
    'State:', 'ON',
    'Postal Code:', 'K1K4R4',
    'Country:', 'CA',
    'Phone:', '+1.8666421232',
    'Fax:', '+1.6137061248',
    'Email:', '@privacyhero.company',
    'Technical Contact',
    'Name:', 'Connor Malcolm',
    'Organization:', 'Privacy Hero Inc.',
    'Street:', '532 Montreal Rd',
    'Suite 261',
    'City:', 'Ottawa',
    'State:', 'ON',
    'Postal Code:', 'K1K4R4',
    'Country:', 'CA',
    'Phone:', '+1.8666421232',
    'Fax:', '+1.6137061248',
    'Email:', '@privacyhero.company',
    'Billing Contact'
]

EXPECTED_VERSION = {
        'domain': 'bcit.ca', 
        'registered_on': '2000-10-19', 
        'expires_on': '2027-04-19', 
        'updated_on': '2026-06-03', 
        'status': ['client transfer prohibited', 'client update prohibited'], 
        'registrar': 'Internic.ca Inc.'
    }

def test_scrapped_data_cleaner_returns_dict():
    
    cleaned = scrapped_data_cleaner(RAW_WHOIS_DATA)
    
    assert cleaned == EXPECTED_VERSION
    assert len(cleaned) == 6
    assert cleaned["domain"] == "bcit.ca"
    assert cleaned["expires_on"] == "2027-04-19"