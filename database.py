"""from sqlalchemy import create_engine, text


engine = create_engine("mysql+pymysql://kvhc9tqhx0g0b2ii9y2d:pscale_pw_Xb3ilMthaQ5E0D6Ccf2S1vYAGJrWAQObvaumYwnGTs@aws-eu-west-2.connect.psdb.cloud/quizgamedb?charset=utf8mb4")

connection_uri = (
    "mysql+pymysql://scott:tiger@192.168.0.134/test"
    "?ssl_ca=/home/gord/client-ssl/ca.pem"
    "&ssl_cert=/home/gord/client-ssl/client-cert.pem"
    "&ssl_key=/home/gord/client-ssl/client-key.pem"
    "&ssl_check_hostname=false"
)

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM userProfile"))
  print(result.all())
  """