# Receipt Processor API

## Steps to Run the Application

1. Ensure **Docker Engine** (or **Docker Desktop**) is installed on your machine.
2. Build the Docker image:
   ```bash
   docker build -t receipt_processor .
3. Run the Docker container:
    ```bash
    docker run -p <port_no>:1777 receipt_processor
4. Test the API (Ex: Postman) running on port `<port_no>`via the following URL:
    ```bash
    http://localhost:<port_no>

### Example:
- Port Number: 2500
- Example URL: `http://localhost:2500/`
- POST request : `http://localhost:2500/receipts/process`

- GET request  : `http://localhost:2500/<id>/points`

