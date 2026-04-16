# OrderCore

Backend-focused Django e-commerce project built to practice real-world shopping flow logic.

## About
OrderCore is the second e-commerce project in my backend-first Django learning roadmap.

The main goal of this project is to build and understand a complete order system with a database-based cart structure, snapshot logic, and user-based order management.

This project was developed step by step with a focus on understanding backend architecture instead of only building visual pages.

## Core Features
- Authentication system (login / register / logout)
- Dynamic navbar
- Dynamic homepage
- Category-based product filtering
- Product detail page
- Database-based cart system
- Add to cart / increase / decrease / remove cart items
- User-based cart logic
- Order model
- OrderItem model
- Snapshot logic for ordered products
- Checkout system (cart → order)
- Cart cleanup after checkout
- My Orders page
- Order detail page
- Order status management
- Dynamic order count in navbar

## Backend Highlights
- Database-based cart structure using `CartItem`
- Same product does not create a new row in cart, quantity increases instead
- `product_id` is used while adding to cart
- `cart_item_id` is used for increase / decrease / remove actions
- Navbar cart count is calculated from total quantity
- Order system stores product name and product price as snapshot fields
- Only authenticated users can access cart and order actions
- Users can only see their own orders

## Order Flow
1. User logs in
2. User adds products to cart
3. Cart items are stored in the database
4. User completes checkout
5. Order is created
6. OrderItems are created from cart items
7. Total price is calculated
8. Cart is cleaned after successful checkout

## Tech Stack
- Python
- Django
- Bootstrap
- SQLite

## Project Structure
- `products` app → product listing, category filter, detail pages
- `cart` app → database-based cart system
- `orders` app → order creation, order items, checkout, order history
- global templates + app-based templates
- slug-based detail structure

## What I Learned
- Building a database-based cart system
- Designing an order architecture
- Using snapshot logic in e-commerce
- Connecting cart flow to checkout flow
- Managing user-based data securely
- Using context processors for dynamic navbar data
- Thinking in backend-first project structure

## Status
✅ Backend core completed

OrderCore is completed as a backend-focused project.
The next project in the roadmap is **StockFlow**, which will focus on stock management.

## Roadmap Position
- Project 1 → StepCart
- Project 2 → OrderCore ✅
- Project 3 → StockFlow

## Author
Taner Şahin
GitHub: [taner-sahin](https://github.com/taner-sahin)