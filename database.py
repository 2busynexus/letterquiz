"""from sqlalchemy import create_engine, text

database_string = "mysql+pymysql://kvhc9tqhx0g0b2ii9y2d:pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs@aws-eu-west-2.connect.psdb.cloud/quizgamedb?charset=utf8mb4"
engine = create_engine(
  database_string,
  connect_args = {
    "ssl" : {
      "ssl-_ca": "/etc/ssl/cert.pem"
    }
  }
)

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM userProfile"))
  print(result.all())

conn = engine.connect()"""