# Restaurant Service Website

A Django-based web application for a restaurant service that includes features such as user authentication, a menu page, add-to-cart functionality, checkout, order summary ,order history, and user deatils. The user can create their personal account, and browse the menu items and can add their interest items to cart and can further checkout and view their order summary. Also in future they can see thier store details and order history.

## Features

1. *Homepage*: 
   - Provides information about the restaurant and its offerings.
   - Contains a navigation bar with links to login, signup, and menu pages.
   
2. *User Authentication*:
   - Login page for registered users.
   - Signup page for new users.
   - Logout functionality.
   - Only logged-in users can access the menu page.

3. *Menu Page*:
   - Displays menu items as cards.
   - A search option where users can search specific menu items
   - Each card shows the name and image of the food item.
   - Clicking on a card shows a popup with detailed information like price rating description.
   - Users can add items to their cart through aad to cart button in popup and also adjust the quantity.
   
4. *Cart*:
   - Displays items added by the user from menu.
   - Shows a small image, name, and price of each item.
   - Users can also update the required quantity of item through seek input or remove an item from cart, which also gets updated in database.
   - After reviewing cart changes, users can click checkout button.

5. *Checkout*:
   - User have to enter their basic details like full name, address, contact.
   - Can review their items in their order through order summary which also include the total price of the order as well as total quantity
   - After reviewing all details , user can click place order which asks a confirmation before placing an order, to be confirmed.
   - Once user confirm order, the alert shows order placed successfully
   - One thing to note that, as user places an order first time, he has to enter the user details, but when he orders again using same account, the details get autofilled from database in checkout details. But though user can edit the details in that particular order(optional).
   
6. *Order history and User details*:
   - whenever users logs in his account, he can visit the myorders page, where he can see his order history with a view option that opens user profile data and order items in that particular order fetched through order id from database.
   - The order history includes total price, quantity of particular items, ordered date , image as well as user details.   

## Technologies Used

- *Django*
- *HTML*
- *Tailwind CSS*
- *JavaScript and jquery*
- *Alertify.js*

## Installtion and usage
1.  **Clone the repo:**
    ```
    git clone https://github.com/sksmagr23/restaurant_service.git
    cd restaurant_service
    ```
2. **Set up virtual environment:**
    ```
    virtualenv venv
    source venv/bin/activate
    # this setup is for linux, for windows can refer docs, also ensure that pip, python and virtualenv are installed in system
    ```
3.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```
    python manage.py migrate
    ```
5.  **Collect static files:**
    ```
    python manage.py collectstatic
    ```  
4.  **Run the development server:**
    ```
    python manage.py runserver
    # open the url 'http://127.0.0.1:8000/'
    ```