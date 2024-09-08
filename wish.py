import os

from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the API route
@app.route('/wish',methods=['POST'])
def wish_birthday():
    # Get the name from the request body (JSON format)
    data = request.json
    name = data.get('name')  # Extract 'name' from the received JSON

    # Generate the birthday message
    birthday_message = f"Happy Birthday, {name}!"

    # Return the message as JSON response
    return jsonify({"message": birthday_message})

if __name__ == '__main__':
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
