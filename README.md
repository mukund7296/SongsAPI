# SongsAPI
Here’s a `README.md` file for your Flask and MongoDB project:

````markdown
# Song API with Flask and MongoDB

This project is a simple RESTful API built using Flask and MongoDB to manage songs data. It provides endpoints to fetch songs from a MongoDB database and supports features like pagination and search by artist or title.

## Requirements

- Python 3.x
- Flask
- MongoDB (can be run locally or in Docker)

## Setup Instructions

### 1. Clone the Repository

If you don't have the repository yet, clone it:

```bash
git clone https://github.com/mukund7296/SongsAPI.git
cd SongsAPI
````

### 2. Create a Virtual Environment

If you don't have a virtual environment set up, create and activate one:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

Once your virtual environment is active, install the required dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the following dependencies:

* Flask
* pymongo

### 4. Set Up MongoDB

You can run MongoDB using Docker or install it locally.

#### Option 1: **Run MongoDB with Docker (Recommended)**

1. **Pull the MongoDB image:**

```bash
docker pull mongo:4.4
```

2. **Run MongoDB as a container:**

```bash
docker run -d --name songs_db -p 27017:27017 mongo:4.4
```

3. **Verify the container is running:**

```bash
docker ps
```

<img width="1256" alt="image" src="https://github.com/user-attachments/assets/8fc9e55b-e7bc-4529-ad8e-3bb609a16712" />

### 5. Import Data into MongoDB

Before running the Flask app, you need to import the songs data into MongoDB. Use the `mongoimport` tool to do this.

```bash
mongoimport --db songs_db --collection songs --file songs.json --jsonArray
```
Note : Find the correct path: Since you're currently in the directory that contains the songs.json file, you can simply use a relative path. You can confirm the location of songs.json by running:

```bash
ls
```
This will list the contents of the current directory. Since your songs.json is listed, you can now copy it directly into the Docker container.

Copy the file into the container: Run the docker cp command from the same directory where songs.json is located:

```bash
docker cp songs.json songs_db:/songs.json
```

This will copy the songs.json file into the MongoDB container.

Import the data into MongoDB: Now, run the import command to load the data into MongoDB:

```bash
docker exec -it songs_db mongoimport --db songs_db --collection songs --file /songs.json --jsonArray
```

This will import the songs data from the `songs.json` file into the `songs_db` database.

### 6. Run the Flask App

Once MongoDB is running and the data is imported, you can start the Flask server.

```bash
python app.py
```

You should see output like:

```bash
* Running on http://127.0.0.1:5002
```

This means the Flask app is running on port 5002.
<img width="566" alt="image" src="https://github.com/user-attachments/assets/411964b4-6221-437b-b54d-ae92637c1d42" />


### 7. Access the API

You can interact with the API by sending HTTP requests to the following endpoints:


* **Get all songs (with pagination)**:

     ```http
  GET http://127.0.0.1:5002/songs?page=1&per_page=4
  ```
  
   <img width="966" alt="image" src="https://github.com/user-attachments/assets/a57d983d-9069-4691-9951-165cad916f4c" />

  ```http
  GET http://127.0.0.1:5002/songs
  ```

<img width="1437" alt="image" src="https://github.com/user-attachments/assets/d80166bd-84de-4c38-b3f6-a8320e5140fb" />

* **Search songs by artist**:

  ```http
  GET http://127.0.0.1:5002/songs?artist=The%20Yousicians
  ```

* **Search songs by title**:

  ```http
  GET http://127.0.0.1:5002/songs?title=Lycanthropic%20Metamorphosis
  ```

* **Get a specific song by its ID**:

  ```http
  GET [http://127.0.0.1:5002/songs/681f8dde7a2277b2b2625fd4](http://127.0.0.1:5002/songs?id=681f8dde7a2277b2b2625fd4)
  ```
  <img width="996" alt="image" src="https://github.com/user-attachments/assets/c019da40-a8b3-4a85-998b-dbd8aa7a5c08" />


### 8. Stopping the Flask App and MongoDB

* To stop the Flask app, press `CTRL+C` in the terminal where the app is running.

* To stop MongoDB in Docker:

```bash
docker stop songs_db
docker rm songs_db
```
