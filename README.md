"# Zion" 
 ## Zion's E-commerce App

This is a simple e-commerce application built using Django. It allows users to browse products, add them to their cart, and checkout.

### Installation

To install the application, follow these steps:

1. Clone the repository:

```
git clone https://github.com/Mashaun18/Zion.git
```

2. Change directory into the project folder:

```
cd Ria
```

3. Create a virtual environment:

```
python3 -m venv venv
```

4. Activate the virtual environment:

```
source venv/bin/activate
```

5. Install the required Python packages:

```
pip install -r requirements.txt
```

6. Migrate the database:

```
python manage.py migrate
```

7. Run the development server:

```
python manage.py runserver
```

### Models

The application has the following models:

* **Product**: This model represents a product that can be purchased. It has the following fields:

    * **id**: A unique identifier for the product.
    * **name**: The name of the product.
    * **description**: A description of the product.
    * **category**: The category of the product.
    * **price**: The price of the product.
    * **image**: An image of the product.
    * **other_image**: An additional image of the product.
    * **status**: The status of the product (available or unavailable).

* **Cart**: This model represents a shopping cart. It has the following fields:

    * **id**: A unique identifier for the cart.
    * **date_created**: The date the cart was created.
    * **user**: The user who owns the cart.

* **CartItem**: This model represents an item in a shopping cart. It has the following fields:

    * **cart**: The cart that the item belongs to.
    * **product**: The product that the item represents.
    * **quantity**: The quantity of the product in the cart.

### Views

The application has the following views:

* **ProductListView**: This view displays a list of all products.
* **ProductDetailView**: This view displays the details of a single product.
* **CartView**: This view displays the contents of the cart.
