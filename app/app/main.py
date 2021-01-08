import os
from app import app, db
from .core import app_setup
from .models import user

# sam = user.User('Sam','1234','12345','Floripa','Sam@gmail.com')
# Pedro = user.User('Pedro','1234','12345','Floripa','Pedro@gmail.com')

# db.session.add_all([sam,Pedro])
# db.session.commit()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=os.environ['PORT'])
