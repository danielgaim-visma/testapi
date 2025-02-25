import requests
import json

# API Configuration
base_url = "https://jira.visma.com"
username = "your-username"
api_token = "your-api-token"

session = requests.Session()
session.auth = (username, api_token)

# Define query URL outside functions
query_url = f"{base_url}/rest/assets/1.0/aql/objects"

try:
    # Make a simple test request first
    print("Making test request...")
    print(f"URL: {query_url}")

    response = session.get(query_url, params={
        "qlQuery": 'objectType = "GitHub Copilot"',
        "includeAttributes": True,
        "resultsPerPage": 1
    })

    # Print response details before trying to parse JSON
    print("\nResponse Status Code:", response.status_code)
    print("Response Headers:", dict(response.headers))
    print("\nRaw Response Text:")
    print(response.text)

    # Only try to parse JSON if we got a successful response
    if response.ok:
        data = response.json()
        print("\nParsed JSON Response:")
        print(json.dumps(data, indent=2))
    else:
        print("\nRequest failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print(f"\nRequest Error:")
    print(f"Error type: {type(e)}")
    print(f"Error message: {str(e)}")

    if hasattr(e, 'response'):
        print("\nResponse information:")
        print(f"Status code: {e.response.status_code if e.response else 'No response'}")
        print(f"Response text: {e.response.text if e.response else 'No response text'}")

except json.JSONDecodeError as e:
    print(f"\nJSON Parsing Error:")
    print(f"Error message: {str(e)}")
    print(f"Position: line {e.lineno}, column {e.colno}")

except Exception as e:
    print(f"\nUnexpected Error:")
    print(f"Error type: {type(e)}")
    print(f"Error message: {str(e)}")