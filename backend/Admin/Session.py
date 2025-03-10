import base64
import datetime
import os
from Admin.Database import Database


class Session:

    def __init__(self,sessionId):
        self.connection=Database().get_connection()
        cur=self.connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS sessions(id,username,sessionStart,lastAction)")
        self.loadSession(sessionId)

    def loadSession(self,sessionId):
        self.connection.execute("UPDATE sessions SET lastAction=? WHERE id=?",(datetime.datetime.now().timestamp(),sessionId))
        self.connection.commit()
        res = self.connection.execute("SELECT id,username,sessionStart,lastAction,lastAction-sessionStart AS sessionTime FROM sessions WHERE id=?",(sessionId,)).fetchone()
        if res:
            self.session=dict(zip(["id","user","sessionStart","lastAction","sessionTime"],res))
            self._isValid=True
        else:
            self._isValid=False

    def getSession(self):
        return self.session
    
    def isValid(self):
        return self._isValid
    
    def newSession(self,user):
        session={
            "id": base64.b64encode(os.urandom(64)).hex(),
            "user": user,
            "sessionStart": datetime.datetime.now().timestamp(), 
            "lastAction": datetime.datetime.now().timestamp(),
            "sessionTime": 0
        }
        self.connection.execute("INSERT INTO sessions(id,username,sessionStart,lastAction) VALUES (?,?,?,?)",(
            session["id"],
            session["user"],
            session["sessionStart"],
            session["lastAction"]))
        self.connection.commit()
        self.loadSession(session["id"])