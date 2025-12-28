Hãy thực hiện tính năng Authentication (Đăng nhập) cho dự án AuraAIBackEnd dựa trên cấu trúc hiện có. Tuân thủ các yêu cầu sau:

1. **Database Model**: 
   - Tạo file `app/models/user.py`. Sử dụng `Base` từ `app/db/base.py`.
   - Model `User` gồm: id (UUID/Int), email (unique), hashed_password, full_name, is_admin (boolean, default=True).

2. **Schemas**: 
   - Tạo `app/schemas/token.py` (Token, TokenData) và `app/schemas/user.py` (UserLogin, UserOut) sử dụng Pydantic.

3. **Security Service**: 
   - Tạo `app/core/security.py` để xử lý: băm mật khẩu (bcrypt), kiểm tra mật khẩu, và tạo JWT Token (Sử dụng python-jose).
   - Lấy SECRET_KEY và ALGORITHM từ `app/core/config.py`.

4. **Business Logic**: 
   - Tạo `app/services/auth_service.py` chứa hàm `authenticate_user` và các logic liên quan đến xác thực.

5. **API Endpoints**: 
   - Tạo `app/api/v1/endpoints/auth.py` với route `/login` (POST). 
   - Route này nhận email/password, kiểm tra và trả về Bearer Token. 
   - Lưu ý: KHÔNG tạo route đăng ký (signup).

6. **Authentication Dependency**:
   - Tạo một dependency trong `app/api/deps.py` (hoặc vị trí phù hợp) tên là `get_current_user`. 
   - Dependency này sẽ giải mã JWT, kiểm tra user trong DB. Nếu token không hợp lệ hoặc không có token, trả về lỗi 401 Unauthorized.

7. **Global Protection**: 
   - Cấu hình trong `app/main.py` hoặc sử dụng Dependency ở cấp độ APIRouter để đảm bảo TẤT CẢ các endpoint (trừ /login) đều yêu cầu Bearer Token hợp lệ mới cho phép truy cập.

8. **Admin Initial Script**: 
   - Tạo một script độc lập `scripts/create_admin.py` để khởi tạo tài khoản admin đầu tiên.
   - Tài khoản: admin@auraai.com, mật khẩu: 123456 (phải được băm trước khi lưu vào DB).

Hãy sử dụng SQLAlchemy Async đã cấu hình trong `app/db/session.py`. Đảm bảo code sạch, có type hint và đúng chuẩn FastAPI. đọc 2 file `config.py` và `security.py` để xem có tái sử dụng lại được hay không