from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):
        return self.session.query(User).all()

    def user_by_username(self, user_name):
        return self.session.query(User).filter(User.username == user_name).one()

    def create(self, data):
        ent = User(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update(self, data):
        user = self.get_one(data.get("id"))
        if data.get("name"):
            data.name = data.get("name")
        if data.get("role"):
            data.role = data.get("role")
        if data.get("password"):
            data.password = data.get("password")

        self.session.add(user)
        self.session.commit()
