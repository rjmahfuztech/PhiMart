# Phimart - E-commerce RESTful API

Phimart is a fully functional e-commerce RESTful API built using Django Rest Framework (DRF). This API provides endpoints for managing products, product categories, product reviews, shopping carts, and orders. It also features authentication via JWT using Djoser and includes API documentation with Swagger (drf-yasg).

## Features

- **User Authentication**: JWT-based authentication using Djoser.
- **Product Management**: CRUD operations for products.
- **Category Management**: CRUD operations for product categories.
- **Product Reviews**: Users can add and view reviews.
- **Cart Management**: Add, remove, and update cart items.
- **Order Processing**: Place orders and manage order history.
- **API Documentation**: Integrated Swagger UI for easy API exploration.

## Technologies Used

- **Django** - High-level Python web framework.
- **Django Rest Framework (DRF)** - Framework for building RESTful APIs.
- **Djoser** - Authentication system using JWT.
- **drf-yasg** - Generates API documentation with Swagger.
- **PostgreSQL / SQLite** - Database for storing application data.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rjmahfuztech/PhiMart.git
   cd phimart
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication (Djoser JWT)

| Method | Endpoint             | Description                        |
| ------ | -------------------- | ---------------------------------- |
| POST   | `/auth/jwt/create/`  | Generate access and refresh tokens |
| POST   | `/auth/jwt/refresh/` | Refresh access token               |
| POST   | `/auth/jwt/verify/`  | Verify token validity              |

### Categories

| Method | Endpoint                | Description                     |
| ------ | ----------------------- | ------------------------------- |
| GET    | `/api/categories/`      | List all categories             |
| POST   | `/api/categories/`      | Add a new category (Admin only) |
| GET    | `/api/categories/{id}/` | Retrieve category details       |
| PUT    | `/api/categories/{id}/` | Update category (Admin only)    |
| DELETE | `/api/categories/{id}/` | Delete category (Admin only)    |

### Products

| Method | Endpoint              | Description                    |
| ------ | --------------------- | ------------------------------ |
| GET    | `/api/products/`      | List all products              |
| POST   | `/api/products/`      | Add a new product (Admin only) |
| GET    | `/api/products/{id}/` | Retrieve product details       |
| PUT    | `/api/products/{id}/` | Update product (Admin only)    |
| DELETE | `/api/products/{id}/` | Delete product (Admin only)    |

### Product Reviews

| Method | Endpoint                      | Description          |
| ------ | ----------------------------- | -------------------- |
| GET    | `/api/products/{id}/reviews/` | List product reviews |
| POST   | `/api/products/{id}/reviews/` | Add a review         |

### Cart

| Method | Endpoint          | Description               |
| ------ | ----------------- | ------------------------- |
| GET    | `/api/cart/`      | View cart items           |
| POST   | `/api/cart/`      | Add item to cart          |
| PUT    | `/api/cart/{id}/` | Update cart item quantity |
| DELETE | `/api/cart/{id}/` | Remove item from cart     |

### Orders

| Method | Endpoint            | Description                  |
| ------ | ------------------- | ---------------------------- |
| GET    | `/api/orders/`      | List all orders (Admin only) |
| POST   | `/api/orders/`      | Place an order               |
| GET    | `/api/orders/{id}/` | View order details           |

## API Documentation

Swagger UI is available at:

```
http://127.0.0.1:8000/swagger/
```

Redoc documentation is available at:

```
http://127.0.0.1:8000/redoc/
```

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, feel free to contact me at **rjmahfuz.islam@gmail.com** or visit my [GitHub profile](https://github.com/rjmahfuztech/).
