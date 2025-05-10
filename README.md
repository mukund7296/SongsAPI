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

#### Option 2: **Install MongoDB Locally**

If you prefer running MongoDB locally:

* On **macOS** (with Homebrew):

  ```bash
  brew services start mongodb@5.0
  ```

* On **Linux**:

  ```bash
  sudo systemctl start mongod
  ```

### 5. Import Data into MongoDB

Before running the Flask app, you need to import the songs data into MongoDB. Use the `mongoimport` tool to do this.

```bash
mongoimport --db songs_db --collection songs --file songs.json --jsonArray
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

### 7. Access the API

You can interact with the API by sending HTTP requests to the following endpoints:

* **Get all songs (with pagination)**:

  ```http
  GET http://127.0.0.1:5002/songs?page=1&per_page=10
  ```

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
  GET http://127.0.0.1:5002/songs/<id>
  ```

### 8. Stopping the Flask App and MongoDB

* To stop the Flask app, press `CTRL+C` in the terminal where the app is running.

* To stop MongoDB in Docker:

```bash
docker stop songs_db
docker rm songs_db
```

Or, if running MongoDB locally, stop the MongoDB service:

* On **macOS** with Homebrew:

  ```bash
  brew services stop mongodb@5.0
  ```

* On **Linux**:

  ```bash
  sudo systemctl stop mongod
  ```

## API Documentation

* The API supports pagination, search by artist and title, and retrieving songs by ID.
* You can use tools like Postman or cURL to test the endpoints.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Steps to Customize:

1. **Repository URL**: Replace `<repository-url>` with the actual URL of your repository if you're hosting it on a platform like GitHub.
2. **MongoDB Setup**: If you use a different MongoDB version or setup, make sure to adjust the instructions accordingly.

This `README.md` covers setup, usage, and provides example API calls for your project! Let me know if you'd like to add more details or make any changes.
```
