from dao.model.favorite import Favorite


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Favorite).get(bid)

    def get_all(self):
        return self.session.query(Favorite).all()

    def create(self, favorite_d):
        ent = Favorite(**favorite_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        favorite_d = self.get_one(rid)
        self.session.delete(favorite_d)
        self.session.commit()

    def update(self, favorite_d):
        director = self.get_one(favorite_d.get("id"))
        director.name = favorite_d.get("name")

        self.session.add(favorite_d)
        self.session.commit()


