
class Customer:
    
    all_customers = []

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.add_customer_to_all(self)

    def given_name(self):
        return self.firstname
    
    def family_name(self):
        return self.lastname
    
    def full_name(self):
        return f'{self.firstname} {self.lastname}'
    
    @classmethod
    def add_customer_to_all(cls, customer):
        cls.all_customers.append(customer)
    
    @classmethod
    def all(cls):
        return cls.all_customers
    
# -------------------------------------------------------------------


class Restaurant:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    
# --------------------------------------------------------------------


class Review:

    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    @property
    def customer(self):
        return self.customer
    
    @property
    def restaurant(self):
        return self.restaurant