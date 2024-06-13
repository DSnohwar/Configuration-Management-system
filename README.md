# Country Configuration Manager

This is a FastAPI application for managing country configurations.

## Project Structure

```
__pycache__/
.env
.gitignore
app/
    __pycache__/
    database.py
    main.py
    models.py
    schemas.py
    test.py
requirements.txt
```

## Setup

1. Clone the repository.
2. Install the dependencies using pip:

```sh
pip install -r requirements.txt
```

3. Set up your database and update the `SQLALCHEMY_DATABASE_URL` in the `.env` file.

## Running the Application

To run the application, use the following command:

```sh
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /create_configuration`: Create a new country configuration.
- `GET /get_configuration/{country_code}`: Get country configuration by country code.
- `POST /update_configuration`: Update country configuration.
- `DELETE /delete_configuration`: Delete country configuration.

## Instructions to Use API Endpoints
1. Creating a Country Configuration
Endpoint: POST /create_configuration
Description: Create a new country configuration.

Example Usage:

```
curl -X POST "http://localhost:8000/create_configuration" -H "Content-Type: application/json" -d
{
    "country_code": "IND",
    "business_name": "Example Company",
    "registration_number": "12345"
}
```

2. Retrieving a Country Configuration
Endpoint: GET /get_configuration/{country_code}

Description: Retrieve country configuration by country code.

Example Usage:


```
curl -X GET "http://localhost:8000/get_configuration/IND"
```

3. Updating a Country Configuration
Endpoint: POST /update_configuration

Description: Update country configuration.

Example Usage:


```
curl -X POST "http://localhost:8000/update_configuration" -H "Content-Type: application/json" -d '{
    "country_code": "IND",
    "business_name": "Updated Company",
    "registration_number": "54321"
}'
```


4. Deleting a Country Configuration
Endpoint: DELETE /delete_configuration

Description: Delete country configuration by country code.

Query Parameter:

country_code: Code of the country configuration to delete.
Example Usage:

```
curl -X DELETE "http://localhost:8000/delete_configuration?country_code=IND"
```
## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
