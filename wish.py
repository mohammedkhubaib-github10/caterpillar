import os

from flask import Flask, request, jsonify

app = Flask(__name__)


# Define the API route
@app.route('/wish', methods=['GET'])
def wish_birthday():
    # Generate the birthday message
    message = ["Happy Birthday", "Happy Friendship day", "Happy Fathers day"]
    messagedic = {}
    mes=[]
    for i in range(0, len(message)):
        messagedic={'message':message[i]}
        mes.append(messagedic)

    # Return the message as JSON response
    return jsonify(mes)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

