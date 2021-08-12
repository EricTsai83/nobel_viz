# api/settings.py

# Optional MONGO variables
# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'



# Cross-Origin Resource Sharing(跨來源資源共享設定)
# 是否要讓其他資料伺服器http://localhost:5000"傳資料給其他伺服器http://localhost:8080
# 底下是白名單設置方式，不然因為安全性所以會被阻擋
X_DOMAINS = "http://localhost:8080"  # allow CORS requests from this domain
# X_DOMAINS = '*' # allow CORS requests from this domain

URL_PREFIX = "api"
MONGO_DBNAME = "nobel_prize"
DOMAIN = {
    "winners": {
        "schema": {
            "country": {"type": "string"},
            "category": {"type": "string"},
            "name": {"type": "string"},
            "year": {"type": "integer"},
            "gender": {"type": "string"},
        }
    }
}


X_DOMAINS = "*"  # allow CORS requests from all domains
# X_DOMAINS = 'http://localhost:8080' # allow CORS requests from this domain
HATEOAS = False
PAGINATION = False
