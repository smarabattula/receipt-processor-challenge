# Receipt Processor API

## Steps to Run the Application
1. Clone the github repo into your machine
2. Ensure **Docker Engine** (or **Docker Desktop**) is installed on your machine
3. Build the Docker image:
   ```bash
   docker build -t receipt_processor .
4. Run the Docker container (Application runs on port 1777 in the container):
    ```bash
    docker run -p <port_no>:1777 receipt_processor
5. Test the API (Ex: Postman) from your port `<port_no>` via the following URL:
    ```bash
    http://localhost:<port_no>

### Example:
- Port Number: **2500**
- Docker build cmd: `docker build -t receipt_processor .`
- Docker run cmd: `docker run -p 2500:1777 receipt_processor`
- Example URL: `http://localhost:2500/`
- POST request : `http://localhost:2500/receipts/process`
- GET request  : `http://localhost:2500/<id>/points`

