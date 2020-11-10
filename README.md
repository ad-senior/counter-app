# App Name: Counter
This app has been developed with Angular 10 (for the frontend development)
and Django 3 (for the backend development).

## 1. Frontend
### Deployment
- Go to the `counter-client` directory.
- Run the frontend locally using the bello command:
    ```bash
    npm install && npm start
    ```

## 2. Backend
### Deployment
- Go to the `counter-server` directory.
- Install packages in the requirements.txt like so:
    ```bash
    pip install -r requirements.txt
    ```
- Please make sure the db connection configuration is correct in the ./counter/settings.py.
- Migrate models using the bellow command:
    ```bash
    python manage.py migrate
    ```
- Please make sure you entered the correct username in ./api/management/commands/cron_set.py
- Set up a cron job to reset the count in database to 2 every monday:
    ```bash
    python manage.py cron_set
    ``` 
  (Note: Please run this command only one time)
- Run the backend locally using the bellow command:
    ```bash
    python manage.py runserver
    ```

### API Information
| Type | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/counter/` | Return the count number |
| POST | `/api/counter/` | Reduce the count number by one |
| POST | `/api/counter/reset/` | Reset the count number to 2 |

### Unit tests
- Please run the bellow command to run tests:
    ```bash
    python manage.py test
    ```
