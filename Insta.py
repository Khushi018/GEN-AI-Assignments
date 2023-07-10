from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize posts as an empty list
posts = []
post_id_counter = 1


# Endpoint to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter
    
    data = request.get_json()
    username = data.get('username')
    caption = data.get('caption')
    
    post = {
        'id': post_id_counter,
        'username': username,
        'caption': caption,
        'likes': 0,
        'comments': []
    }
    
    posts.append(post)
    post_id_counter += 1
    
    return jsonify(post), 201


# Endpoint to view all posts
@app.route('/posts', methods=['GET'])
def view_posts():
    return jsonify(posts)


# Endpoint to delete a post by ID
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            return jsonify({'message': 'Post deleted'})
    
    return jsonify({'message': 'Post not found'}), 404


# Endpoint to increase the likes of a post by 1
@app.route('/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            post['likes'] += 1
            return jsonify({'message': 'Post liked'})
    
    return jsonify({'message': 'Post not found'}), 404


# Endpoint to add a comment to a post
@app.route('/posts/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    data = request.get_json()
    comment = data.get('comment')
    
    for post in posts:
        if post['id'] == post_id:
            post['comments'].append(comment)
            return jsonify({'message': 'Comment added'})
    
    return jsonify({'message': 'Post not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)






































Certainly! Below is an example implementation of a simple Flask application that meets the requirements you've mentioned. It includes the basic operations of post creation, post viewing, post deletion, likes, and comments using Python data structures (dictionaries and lists). Please note that this is a simplified implementation for demonstration purposes and may not include error handling or security measures.

python
Copy code
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize posts as an empty list
posts = []
post_id_counter = 1


# Endpoint to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter
    
    data = request.get_json()
    username = data.get('username')
    caption = data.get('caption')
    
    post = {
        'id': post_id_counter,
        'username': username,
        'caption': caption,
        'likes': 0,
        'comments': []
    }
    
    posts.append(post)
    post_id_counter += 1
    
    return jsonify(post), 201


# Endpoint to view all posts
@app.route('/posts', methods=['GET'])
def view_posts():
    return jsonify(posts)


# Endpoint to delete a post by ID
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            return jsonify({'message': 'Post deleted'})
    
    return jsonify({'message': 'Post not found'}), 404


# Endpoint to increase the likes of a post by 1
@app.route('/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            post['likes'] += 1
            return jsonify({'message': 'Post liked'})
    
    return jsonify({'message': 'Post not found'}), 404


# Endpoint to add a comment to a post
@app.route('/posts/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    data = request.get_json()
    comment = data.get('comment')
    
    for post in posts:
        if post['id'] == post_id:
            post['comments'].append(comment)
            return jsonify({'message': 'Comment added'})
    
    return jsonify({'message': 'Post not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
To test the application, you can use tools like cURL or Postman to make HTTP requests to the provided endpoints. For example:

To create a new post:

Method: POST
Endpoint: http://localhost:5000/posts
Body: {"username": "john", "caption": "My first post"}
To view all posts:

Method: GET
Endpoint: http://localhost:5000/posts
To delete a post with ID 1:

Method: DELETE
Endpoint: http://localhost:5000/posts/1
To like a post with ID 1:

Method: POST
Endpoint: http://localhost:5000/posts/1/like
To add a comment to a post with ID 1:

Method: POST
Endpoint: http://localhost:5000/posts/1/comment
Body: {"comment": "Great post!"}
