# Jiilna Backend Tasks

This project contains two simple tasks for backend practice using Python and Flask.

---

## Task 1: Product Calculation

In this task, I created a Python program that asks the user to enter:
- product name
- quantity
- price

Then the program calculates:
- total price
- tax (15%)
- final total

---

## Task 2: Simple API (Flask)

In this task, I built a simple API using Flask.

The API allows:
- viewing all products
- adding a new product

---

## Endpoints

### GET /products
Returns all products as a list.

---

### POST /products
Adds a new product.

Example request:
```json
{
  "name": "Laptop",
  "quantity": 2,
  "price": 3000
}