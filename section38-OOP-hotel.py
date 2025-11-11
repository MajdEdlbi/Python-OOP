import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    # watermark is example is a class variable because it is shared among all instance
    watermark = "The real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
    #        all above is instance method
    @classmethod
    def get_hotels_count(cls, data):
       return len(data)



class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


    @staticmethod
    def convert(amount):
        return amount * 1.2




hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")