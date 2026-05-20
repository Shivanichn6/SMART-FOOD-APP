from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session
)

import sqlite3

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)



# ============================================
# FLASK APP
# ============================================

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

app.secret_key = "smart_food_secret_key"

DATABASE = "smart_food.db"

# ============================================
# DATABASE CONNECTION
# ============================================

def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn

# ============================================
# CREATE TABLE
# ============================================

def init_db():

    with get_db_connection() as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT NOT NULL,

                email TEXT UNIQUE NOT NULL,

                password_hash TEXT NOT NULL
            )
        """)

# ============================================
# FOOD ITEMS
# ============================================

MENU_ITEMS = [

    {
        "id": 1,
        "name": "Classic Veg Burger",
        "category": "Fast Food",
        "price": 99,
        "image": "https://th.bing.com/th/id/OIP.9oCUME-nS4ZS8eWpbJh8iwHaFw?w=228&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },

    {
        "id": 2,
        "name": "Cheese Burst Pizza",
        "category": "Italian",
        "price": 249,
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
    },

    {
        "id": 3,
        "name": "Masala Dosa",
        "category": "South Indian",
        "price": 149,
        "image": "https://th.bing.com/th/id/OIP.9oCUME-nS4ZS8eWpbJh8iwHaFw?w=228&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },

    {
        "id": 4,
        "name": "Paneer Wrap",
        "category": "Healthy Food",
        "price": 179,
        "image": "https://tse2.mm.bing.net/th/id/OIP.X_WvLFi8LM97PQfTh6hlcwHaEJ?rs=1&pid=ImgDetMain&o=7&rm=3"
    },

    {
        "id": 5,
        "name": "White Sauce Pasta",
        "category": "Italian",
        "price": 229,
        "image": "https://images.unsplash.com/photo-1555949258-eb67b1ef0ceb"
    },

    {
        "id": 6,
        "name": "French Fries",
        "category": "Snacks",
        "price": 89,
        "image": "https://images.unsplash.com/photo-1576107232684-1279f390859f"
    },

    {
        "id": 7,
        "name": "Veg Momos",
        "category": "Street Food",
        "price": 119,
        "image": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb"
    },

    {
        "id": 8,
        "name": "Paneer Butter Masala",
        "category": "Indian",
        "price": 269,
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398"
    },

    {
        "id": 9,
        "name": "Spring Rolls",
        "category": "Chinese",
        "price": 169,
        "image": "https://www.connoisseurusveg.com/wp-content/uploads/2022/04/baked-spring-rolls-sq.jpg"
    },

    {
        "id": 10,
        "name": "Hakka Noodles",
        "category": "Chinese",
        "price": 199,
        "image": "https://tse4.mm.bing.net/th/id/OIP.bJ8yjE300e06YzG69WgR-QHaJQ?rs=1&pid=ImgDetMain&o=7&rm=3"
    },

    {
        "id": 11,
        "name": "Samosa",
        "category": "Snacks",
        "price": 49,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950"
    },

    {
        "id": 12,
        "name": "Rasgulla",
        "category": "Sweet Dish",
        "price": 99,
        "image": "https://th.bing.com/th/id/OIP.ZftYXE0uJ0gcB7gIssXD6wHaE8?w=300&h=200&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },

    {
        "id": 13,
        "name": "Chole Bhature",
        "category": "North Indian",
        "price": 189,
        "image": "https://th.bing.com/th/id/OIP.vGFD_2WwLkhNkIvEauOw1AHaE7?w=290&h=193&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },

    {
        "id": 14,
        "name": "Tandoori Roti",
        "category": "Indian",
        "price": 29,
        "image": "https://th.bing.com/th/id/OIP.S3ZxlbmUfgLCgD46gG1JKQHaHa?w=190&h=190&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },

    {
        "id": 15,
        "name": "Pav Bhaji",
        "category": "Street Food",
        "price": 159,
        "image": "https://images.unsplash.com/photo-1606491956689-2ea866880c84"
    },

    {
        "id": 16,
        "name": "Cold Coffee",
        "category": "Beverage",
        "price": 129,
        "image": "https://images.unsplash.com/photo-1517701604599-bb29b565090c"
    },

    {
        "id": 17,
        "name": "Milkshake",
        "category": "Dessert",
        "price": 149,
        "image": "https://images.unsplash.com/photo-1577805947697-89e18249d767"
    },

    {
        "id": 18,
        "name": "Veg Maggie",
        "category": "Fast Food",
        "price": 79,
        "image": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841"
    },

    {
        "id": 19,
        "name": "Paneer Maggi",
        "category": "Fast Food",
        "price": 109,
        "image": "https://th.bing.com/th/id/OIP.lSjh0vzUwSO8QxpZWG1gugHaE8?w=245&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },

    {
        "id": 20,
        "name": "Chocolate Cake",
        "category": "Dessert",
        "price": 299,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },

    {
        "id": 21,
        "name": "Brownie",
        "category": "Dessert",
        "price": 139,
        "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c"
    },

    {
        "id": 22,
        "name": "Ice Cream",
        "category": "Dessert",
        "price": 89,
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
    },

    {
        "id": 23,
        "name": "Cheese Burger",
        "category": "Fast Food",
        "price": 189,
        "image": "https://images.unsplash.com/photo-1550547660-d9450f859349"
    },

    {
        "id": 24,
        "name": "Cheese Pizza",
        "category": "Italian",
        "price": 349,
        "image": "https://th.bing.com/th/id/OIP.dV5iSXdvqXsz7LR7jBH1QwHaEO?w=233&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },

    {
        "id": 25,
        "name": "Balushai",
        "category": "Sweet",
        "price": 199,
        "image": "https://tse2.mm.bing.net/th/id/OIP.7_AngZkQ-2ewNdk8MgV73gHaHa?rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 25,
        "name": "Black Forest Cake",
        "category": "Chinese",
        "price": 199,
        "image": "https://th.bing.com/th/id/OIP.17EKhCgLc5gI1GpyivOvaQHaE8?w=208&h=139&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },
{
        "id": 25,
        "name": "Black Rasgulee",
        "category": "Sweet",
        "price": 199,
        "image": "https://i.ytimg.com/vi/bjIHvJi3UKk/maxresdefault.jpg"
    },

]
# ============================================
# HOME PAGE
# ============================================

@app.route('/')
def home():

    cart = session.get('cart', [])

    return render_template(
        'index.html',
        featured_items=MENU_ITEMS,
        cart_count=len(cart)
    )

# ============================================
# ABOUT PAGE
# ============================================

@app.route('/about')
def about():
    return render_template('about.html')

# ============================================
# POLICY PAGE
# ============================================

@app.route('/policy')
def policy():
    return render_template('policy.html')

# ============================================
# MENU PAGE
# ============================================

@app.route('/menu')
def menu():

    cart = session.get('cart', [])

    search = request.args.get('search', '')

    if search:

        filtered_items = [

            item for item in MENU_ITEMS

            if search.lower() in item['name'].lower()

            or search.lower() in item['category'].lower()

        ]

    else:

        filtered_items = MENU_ITEMS

    return render_template(

        'menu.html',

        menu_items=filtered_items,

        cart_count=len(cart),

        search=search

    )


@app.route('/add-to-cart/<int:item_id>')
def add_to_cart(item_id):

    cart = session.get('cart', [])

    for item in MENU_ITEMS:

        if item['id'] == item_id:

            found = False

            for cart_item in cart:

                if cart_item['id'] == item_id:

                    cart_item['quantity'] = cart_item.get('quantity', 1) + 1

                    found = True

                    break

            if not found:

                item_copy = item.copy()

                item_copy['quantity'] = 1

                cart.append(item_copy)

            break

    session['cart'] = cart

    flash("Item Added To Cart Successfully")

    return redirect(url_for('menu'))



@app.route('/cart')
def cart():

    cart = session.get('cart', [])

    total = sum(
        item['price'] * item.get('quantity', 1)
        for item in cart
    )

    return render_template(
        'cart.html',
        cart=cart,
        total=total
    )

@app.route('/remove-from-cart/<int:item_id>')
def remove_from_cart(item_id):

    cart = session.get('cart', [])

    updated_cart = []

    for item in cart:

        if item['id'] != item_id:
            updated_cart.append(item)

    session['cart'] = updated_cart

    return redirect(url_for('cart'))
# ============================================
# CHECKOUT PAGE
# ============================================

@app.route('/checkout')
def checkout():

    cart = session.get('cart', [])

    total = sum(
        item['price'] * item.get('quantity', 1)
        for item in cart
    )

    return render_template(
        'checkout.html',
        cart=cart,
        total=total
    )

# ============================================
# PAYMENT PAGE
# ============================================

@app.route('/payment', methods=['GET', 'POST'])
def payment():

    cart = session.get('cart', [])

    total = sum(item['price'] for item in cart)

    if request.method == 'POST':

        address = request.form['address']

        payment_method = request.form.get('payment_method')

        session['address'] = address

        session['payment_method'] = payment_method

        return redirect(url_for('success'))

    return render_template(
        'payment.html',
        total=total
    )

# ============================================
# PLACE ORDER
# ============================================

@app.route('/place-order', methods=['POST'])
def place_order():

    session['cart'] = []

    flash("Order Placed Successfully")

    return redirect(url_for('success'))

# ============================================
# SUCCESS PAGE
# ============================================

@app.route('/order-success')
def success():

    address = session.get('address')

    payment_method = session.get('payment_method')

    return render_template(
        'success.html',
        address=address,
        payment_method=payment_method
    )

# ============================================
# SIGNUP PAGE
# ============================================

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']

        password = request.form['password']

        hashed_password = generate_password_hash(password)

        try:

            with get_db_connection() as conn:

                conn.execute("""
                    INSERT INTO users(
                        name,
                        email,
                        password_hash
                    )

                    VALUES(?, ?, ?)
                """, (name, email, hashed_password))

            flash("Account Created Successfully")

            return redirect(url_for('signin'))

        except:

            flash("Email Already Exists")

            return redirect(url_for('signup'))

    return render_template('signup.html')

# ============================================
# SIGNIN PAGE
# ============================================

@app.route('/signin', methods=['GET', 'POST'])
def signin():

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        with get_db_connection() as conn:

            user = conn.execute(
                "SELECT * FROM users WHERE email = ?",
                (email,)
            ).fetchone()

        if user and check_password_hash(
            user['password_hash'],
            password
        ):

            session['user_id'] = user['id']

            session['user_name'] = user['name']

            flash("Login Successful")

            return redirect(url_for('home'))

        else:

            flash("Invalid Email Or Password")

            return redirect(url_for('signin'))

    return render_template('signin.html')

# ============================================
# LOGOUT
# ============================================

@app.route('/logout')
def logout():

    session.clear()

    flash("Logged Out Successfully")

    return redirect(url_for('home'))

# ============================================
# ADMIN LOGIN
# ============================================

@app.route('/admin-login')
def admin_login():
    return render_template('admin/login.html')

# ============================================
# ADMIN DASHBOARD
# ============================================

@app.route('/admin')
def admin_dashboard():
    return render_template('admin/index.html')

# ============================================
# START APP
# ============================================

if __name__ == '__main__':

    init_db()

   app.run(host="0.0.0.0", port=5000, debug=True)