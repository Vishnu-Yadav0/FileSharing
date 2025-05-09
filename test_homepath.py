import os
import getpass

username = getpass.getuser()
home_path = os.environ.get('USERPROFILE') or os.path.expanduser("~")

print("Username:", username)
print("Home Path:", home_path)
