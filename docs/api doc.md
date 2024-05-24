# Sky Guard Aviation SaaS Platform API Documentation

## User Endpoints

### Register User
- **URL:** `/user/register`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "string",
        "email": "string",
        "password": "string",
        "role": "string"  // optional, defaults to "user"
    }
    ```

### Login User
- **URL:** `/user/login`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```

### Get User Profile
- **URL:** `/user/profile`
- **Method:** `GET`
- **Headers:**
    ```http
    Authorization: Bearer <token>
    ```

## Maintenance Endpoints

### Predict Maintenance
- **URL:** `/maintenance/predict_maintenance/<int:aircraft_id>`
- **Method:** `GET`
- **Headers:**
    ```http
    Authorization: Bearer <token>
    ```

## Dashboard Endpoints

### Maintenance Chart
- **URL:** `/dashboard/maintenance_chart`
- **Method:** `GET`
- **Headers:**
    ```http
    Authorization: Bearer <token>
    ```
