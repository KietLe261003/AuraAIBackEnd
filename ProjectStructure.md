AuraAIBackEnd/
├── app/
│   ├── main.py          # Điểm khởi đầu của ứng dụng
│   ├── core/            # Cấu hình hệ thống (config, security)
│   ├── api/             # Các endpoint (routes)
│   │   └── v1/          # Version 1 của API
│   ├── models/          # Database models (SQLAlchemy)
│   ├── schemas/         # Data models (Pydantic)
│   ├── services/        # Business logic (xử lý nghiệp vụ)
│   └── db/              # Kết nối database (session, base)
├── .env                 # Biến môi trường (Secret key, DB URL)
├── requirements.txt
└── alembic.ini


