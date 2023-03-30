from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.email = user_d.get("email")
        user.password  = user_d.get("password")
        user.username = user_d.get("username")
        user.surname = user_d.get("surname")
        user.favorite_genre_id = user_d.get("favorite_genre_id")
        user.favorite_movie_id = user_d.get("favorite_movie_id")

        self.session.add(user)
        self.session.commit()


    def add_to_favorites(self, data):
         user = self.get_one(data.get('id'))
         user.favorite_movie.append(data.get("movie"))
         self.session.commit()

    def remove_from_favorites(self, data):
        user = self.get_one(data.get('id'))
        user.favorite_movie.remove(data.get("movie"))
        self.session.commit()