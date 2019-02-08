from flaskr import app
import os

if  not os.path.exists("./flaskr/flaskr.db"):
    from flaskr.models import init
    init()
app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))