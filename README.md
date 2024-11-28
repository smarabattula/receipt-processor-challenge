# Receipt Processor API

## Assumptions made:
1. In the points calculation, I've assumed the time constraint **`after 2:00 PM and before 4:00 PM`** as from 2:00 PM to 3:59 PM (inclusive of 2:00 PM and exclusive of 4:00 PM)

## Steps to Run the Application
1. Clone the github repo into your machine
2. Ensure **Docker Engine** (or **Docker Desktop**) is installed on your machine
3. Build the Docker image bundled with all dependencies:
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
![image](https://github.com/user-attachments/assets/8ea6bac3-3c70-475a-a3d4-4850609e7d35)
- GET request  : `http://localhost:2500/receipts/<id>/points`
![image](https://github.com/user-attachments/assets/274bafa9-1506-43fb-bb25-d3985800b2a9)
