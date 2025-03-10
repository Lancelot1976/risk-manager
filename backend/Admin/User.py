import hashlib
from Admin.Database import Database

class User:

    _isValid = False 

    def __init__(self):
        self.connection=Database().get_connection()
        cur=self.connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users(username UNIQUE,password,email)")

    def hashPasswort(self,password):
        pw=hashlib.sha256()
        pw.update(bytes(password,"UTF8"))
        return pw.hexdigest()
    
    def createUser(self,username,password,email=""):
        self.connection.execute("REPLACE INTO users (username,password,email) VALUES (?,?,?)",(username,self.hashPasswort(password),email))
        self.connection.commit()

    def loadUser(self,username):    
        res=self.connection.execute("SELECT username,email FROM users WHERE username=? AND password=?",(username,)).fetchone()
        if (res and res[0]==username):
            self.userdata=dict(zip(["username","email"],res))
            self._isValid=True
        else:
            self.userdata=None
            self._isValie=False

    def loginUser(self,username,password):
        res=self.connection.execute("SELECT username,email FROM users WHERE username=? AND password=?",(username,self.hashPasswort(password))).fetchone()
        if (res and res[0]==username):
            self.userdata=dict(zip(["username","email"],res))
            self._isValid=True
        else:
            self.userdata=None
            self._isValie=False

    def isValid(self):
        return self._isValid