# Restaurant Service Website

A Django-based web application for a restaurant service that includes features such as user authentication, a menu page, and an add-to-cart functionality. The user can create their personal account, and browse the menu items and can add to their cart.

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
   - Each card shows the name and image of the food item.
   - Clicking on a card shows a popup with detailed information.
   - Users can add items to their cart.
   
4. *Cart*:
   - Displays items added to the cart by the user.
   - Shows a small image, name, and price of each item.

## Technologies Used

- *Django*
- *Tailwind CSS*
- *HTML*
- *JavaScript*

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