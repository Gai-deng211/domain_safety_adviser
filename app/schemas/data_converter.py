from .registration import RegistrationData


def change_data_to_model(data: dict[str, str | list[str]]) -> RegistrationData | None:
    try:
        converted_data = RegistrationData(**data)
        print("Data converted to Pydantic model successfully! ✅✅")
        return converted_data
    except Exception as ex:
        print(f"❌❌ Failed to converted your data due to the error:\n{str(ex).splitlines()[0]}")
        return None
    
if __name__ == '__main__':
    EXPECTED_VERSION = {
        'domain': 'bcit.ca', 
        'registered_on': '2000-10-19', 
        'expires_on': '2027-04-19', 
        'updated_on': '2026-06-03', 
        'status': ['client transfer prohibited', 'client update prohibited'], 
        'registrar': 'Internic.ca Inc.'
    }
    
    modelData = change_data_to_model(EXPECTED_VERSION)
    print(modelData)