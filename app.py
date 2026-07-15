from flask import Flask, request, jsonify
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API Studio Kirana Berjalan"

@app.route("/api/contact", methods=["POST"])
def contact():

    data = request.get_json()

    nama = data.get("nama")
    email = data.get("email")
    telepon = data.get("telepon")
    kebutuhan = data.get("kebutuhan")
    proyek = data.get("proyek")

    # Validasi sederhana
    if not nama:
        return jsonify({
            "success": False,
            "message": "Nama wajib diisi"
        }), 400

    if not email:
        return jsonify({
            "success": False,
            "message": "Email wajib diisi"
        }), 400

    print("=" * 40)
    print("DATA MASUK")
    print("Nama      :", nama)
    print("Email     :", email)
    print("Telepon   :", telepon)
    print("Kebutuhan :", kebutuhan)
    print("Proyek    :", proyek)
    print("=" * 40)

    return jsonify({
        "success": True,
        "message": "Pesan berhasil diterima!",
        "data": {
            "nama": nama,
            "email": email,
            "telepon": telepon,
            "kebutuhan": kebutuhan,
            "proyek": proyek
        }
    })

# if __name__ == "__main__":
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
    
    # app.run(debug=True)