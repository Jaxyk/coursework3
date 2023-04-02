import calendar
import datetime

import jwt

from constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService


class AuthService():
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise Exception()

            data = {
                'email': user.email,
            }

            now = datetime.datetime.utcnow()
            min30 = now + datetime.timedelta(minutes=30)
            data['exp'] = calendar.timegm(min30.timetuple())
            access_token = jwt.encode(data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

            days130 = now + datetime.timedelta(days=130)
            data['exp'] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

            return {'access_token': access_token, 'refresh_token': refresh_token}
        else:
            user = self.user_service.get_by_email(email=email)

            if user is None:
                raise Exception()

            if not self.user_service.compare_passwords(user.password, password):
                raise Exception()

            data = {
                'email': user.email
            }

            now = datetime.datetime.utcnow()
            data['exp'] = calendar.timegm(now.timetuple())
            data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])

            return {'access_token': access_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM] )
        email = data.get("email")
        return self.generate_tokens(email, None, is_refresh=True)

