import math

__all__ = ['PointsService']


class PointsService:

    @staticmethod
    def calculate_points(receipt):
        points = 0

        # Alphanumeric characters in the retailer's name
        retailer = receipt["retailer"]
        points += sum(char.isalnum() for char in retailer)

        # Total is a round, whole amount
        total = float(receipt["total"])
        if total.is_integer():
            points += 50

        # Total is a multiple of 0.25
        if total % 0.25 == 0:
            points += 25

        # 5 points for every pair of items
        points += (len(receipt["items"]) // 2) * 5

        # Items with a description length multiple of 3
        for item in receipt["items"]:
            description = item["shortDescription"].strip()
            if len(description) % 3 == 0:
                price = float(item["price"])
                points += math.ceil(price * 0.2)

        # The day in the purchase date is odd
        purchase_date = receipt["purchaseDate"]
        day = int(purchase_date.split("-")[2])
        if day % 2 != 0:
            points += 6

        # The time of purchase is between 2:00pm and 4:00pm
        purchase_time = receipt["purchaseTime"]
        hour = int(purchase_time[:2])
        if 14 <= hour < 16:  # 2:00 PM to 4:00 PM
            points += 10

        return points
