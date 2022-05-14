


class User:

    def __init__(self, firstName,  lastName, email, id=None, title=None, gender=None, \
        dateOfBirth=None, registerDate=None, updatedDate=None, phone=None, picture=None, location=None, **kwargs):
        self._id = id
        self._title = title
        self._first_name = firstName
        self._last_name = lastName
        self._gender = gender
        self._email = email
        self._date_of_birth = dateOfBirth
        self._register_date = registerDate
        self._updated_date = updatedDate
        self._phone = phone
        self._picture = picture
        self._location = location
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def gender(self):
        return self._gender

    @property
    def email(self):
        return self._email

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def register_date(self):
        return self._register_date

    @property
    def updated_date(self):
        return self._updated_date

    @property
    def phone(self):
        return self._phone

    @property
    def picture(self):
        return self._picture

    @property
    def location(self):
        return self._location

    def __str__(self) -> str:
        output = f''' 
            id: {self.id} 
            title: {self.title}
            firstName: {self.first_name}
            lastName: {self.last_name}
            gender: {self.gender}
            email: {self.email}
            dateOfBirth: {self.date_of_birth}
            registerDate: {self.register_date}
            updatedDate: {self.updated_date}
            phone: {self.phone}
            picture: {self.picture}
            location: {self.location}
        '''
        
        return output