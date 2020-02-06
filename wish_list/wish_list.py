from product .models import Product


class WishList:
    def __init__(self):
        self.wishlist = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.wishlist.append(product)
        else:
            raise ValueError("You can add to wishlish only product item")

    def remove_product(self, product_id):
        for product in self.wishlist:
            if product.id == product_id:
                self.wishlist.remove(product)
                return True
        return False


