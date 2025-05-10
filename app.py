from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/songs_db"  # Adjust MongoDB URI if needed
mongo = PyMongo(app)

# Helper function to format MongoDB ObjectId for response
def format_song(song, id_counter):
    # Convert _id to sequential integer
    song['id'] = id_counter
    song['_id'] = str(song['_id'])  # Keep original _id as string for internal use
    return {
        'id': song['id'],
        'artist': song['artist'],
        'title': song['title'],
        'difficulty': song['difficulty'],
        'level': song['level'],
        'released': song['released']
    }

# Route A: List Songs with Pagination
@app.route('/songs', methods=['GET'])
def get_songs():
    page = int(request.args.get('page', 1))  # Default to 1 if no page specified
    per_page = int(request.args.get('per_page', 10))  # Default to 10 items per page
    skip = (page - 1) * per_page

    songs = mongo.db.songs.find().skip(skip).limit(per_page)
    song_list = []
    id_counter = (page - 1) * per_page + 1  # Counter starts from 1 on each page
    for song in songs:
        song_list.append(format_song(song, id_counter))
        id_counter += 1

    # Count the total number of songs for pagination info
    total_count = mongo.db.songs.count_documents({})
    return jsonify({
        'songs': song_list,
        'total_count': total_count,
        'total_pages': (total_count // per_page) + (1 if total_count % per_page > 0 else 0),
        'current_page': page,
        'per_page': per_page
    })

# Route B: Average Difficulty (Optional level filter)
@app.route('/average_difficulty', methods=['GET'])
def average_difficulty():
    level = request.args.get('level', None)
    query = {}
    if level:
        query['level'] = int(level)

    avg_difficulty = mongo.db.songs.aggregate([
        {'$match': query},
        {'$group': {'_id': None, 'avg_difficulty': {'$avg': '$difficulty'}}}
    ])

    result = list(avg_difficulty)
    return jsonify({'average_difficulty': result[0]['avg_difficulty'] if result else 0})

# Route C: Search for Songs (By Title or Artist)
@app.route('/search', methods=['GET'])
def search_songs():
    message = request.args.get('message')
    if not message:
        return jsonify({'error': 'Search string is required'}), 400

    songs = mongo.db.songs.find({
        '$or': [
            {'title': {'$regex': message, '$options': 'i'}},  # Case-insensitive
            {'artist': {'$regex': message, '$options': 'i'}}
        ]
    })

    song_list = []
    id_counter = 1  # Reset ID counter for search results
    for song in songs:
        song_list.append(format_song(song, id_counter))
        id_counter += 1
    
    return jsonify(song_list)

# Route D: Add a Rating to a Song
@app.route('/rate', methods=['POST'])
def add_rating():
    song_id = request.json.get('song_id')
    rating = request.json.get('rating')

    if not song_id or not rating or not (1 <= rating <= 5):
        return jsonify({'error': 'Invalid song_id or rating'}), 400

    try:
        song_id = ObjectId(song_id)  # Ensure song_id is in ObjectId format
    except Exception as e:
        return jsonify({'error': 'Invalid song_id format'}), 400

    song = mongo.db.songs.find_one({'_id': song_id})
    if not song:
        return jsonify({'error': 'Song not found'}), 404

    mongo.db.ratings.insert_one({
        'song_id': song_id,
        'rating': rating
    })

    return jsonify({'message': 'Rating added successfully'})

# Route E: Get Ratings for a Song
@app.route('/ratings/<song_id>', methods=['GET'])
def get_ratings(song_id):
    try:
        song_id = ObjectId(song_id)  # Convert song_id to ObjectId
    except Exception as e:
        return jsonify({'error': 'Invalid song_id format'}), 400

    ratings = mongo.db.ratings.find({'song_id': song_id})

    if not ratings:
        return jsonify({'error': 'No ratings found for this song'}), 404

    rating_list = [rating['rating'] for rating in ratings]
    avg_rating = sum(rating_list) / len(rating_list)
    min_rating = min(rating_list)
    max_rating = max(rating_list)

    return jsonify({
        'average': avg_rating,
        'min': min_rating,
        'max': max_rating
    })

# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
