import requests

# # GET request example
response = requests.get('http://127.0.0.1:8000/get_configuration/US')
print(response.json())  # Assuming the response is JSON

# POST request example
# data = {
#     'country_code': 'US',
#     'business_name': 'Example Inc.',
#     'registration_number': '12345'
# }
# response = requests.post('http://127.0.0.1:8000/create_configuration', json=data)
# print(response.json())  # Assuming the response is JSON
