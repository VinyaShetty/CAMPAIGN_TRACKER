from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # To allow frontend access

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # your MySQL username
        password="root",    # your MySQL password
        database="campaign_db"
    )

# Add a new campaign
@app.route('/api/campaigns', methods=['POST'])
def add_campaign():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO campaigns (campaign_name, client_name, start_date, status) VALUES (%s, %s, %s, %s)",
        (data['campaign_name'], data['client_name'], data['start_date'], data['status'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Campaign added successfully"}), 201

# Get all campaigns
@app.route('/api/campaigns', methods=['GET'])
def get_campaigns():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM campaigns")
    campaigns = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(campaigns)

# Update campaign status
@app.route('/api/campaigns/<int:id>', methods=['PUT'])
def update_campaign_status(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE campaigns SET status=%s WHERE id=%s", (data['status'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Status updated successfully"})

# Delete a campaign
@app.route('/api/campaigns/<int:id>', methods=['DELETE'])
def delete_campaign(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM campaigns WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Campaign deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
