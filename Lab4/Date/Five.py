from datetime import *

date_now = datetime.now()
new_date = date_now - timedelta(days=5)

print(new_date)