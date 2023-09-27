# Community Website for Barangay Santa. Lucia

### What

### Why



1. Before getting started, create an .env file containing the following:
   ```
   DATABASE_URL='mysql://<user>:<password>@localhost:<port>/'
   DATABASE_NAME='<name-of-db>'
   SECRET_KEY='<your-secret-key>'
   ```
2. Use the venv module to create a virtual environment for the project.
   ```
   python3 -m venv venv
   ```
3. Install the required packages.
   ```
   pip install -r requirements.txt
   ```
4. Run app.py
   ```
   python app.py
   ```