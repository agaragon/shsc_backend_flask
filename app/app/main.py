import os
from .app import app
from .core import app_setup

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
