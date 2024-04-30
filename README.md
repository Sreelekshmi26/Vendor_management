# Vendor Management System with Performance Metrics

This repository contains a Django-based Vendor Management System that handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Features

1. **Vendor Profile Management**:
    - **Model Design**: Store vendor information including name, contact details, address, and a unique vendor code.
    - **API Endpoints**:
        - `POST /api/vendors/`: Create a new vendor.
        - `GET /api/vendors/`: List all vendors.
        - `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
        - `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
        - `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

2. **Purchase Order Tracking**:
    - **Model Design**: Track purchase orders with fields like PO number, vendor reference, order date, items, quantity, and status.
    - **API Endpoints**:
        - `POST /api/purchase_orders/`: Create a purchase order.
        - `GET /api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
        - `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
        - `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
        - `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

3. **Vendor Performance Evaluation**:
    - **Metrics**:
        - **On-Time Delivery Rate**: Percentage of orders delivered by the promised date.
        - **Quality Rating**: Average of quality ratings given to a vendor’s purchase orders.
        - **Response Time**: Average time taken by a vendor to acknowledge or respond to purchase orders.
        - **Fulfilment Rate**: Percentage of purchase orders fulfilled without issues.
    - **API Endpoints**:
        - `GET /api/vendors/{vendor_id}/performance`: Retrieve a vendor's performance metrics.

## Technologies

- Python 3
- Django
- Django REST Framework
- JSONField
- PostgreSQL (or any other compatible database)
- Docker

## Setup Instructions

To set up this project locally using Docker, follow these steps:

1. **Clone the repository**:
    ```shell
    git clone [repository-url]
    cd vendor-management-system
    ```

2. **Build the Docker images**:
    ```shell
    docker-compose build
    ```

3. **Set up the environment variables**:
    - Copy the `.env.example` file to a new `.env` file and configure the environment variables as needed.

4. **Run the project**:
    ```shell
    docker-compose up
    ```

5. **API Documentation**:
    - You can use tools like Postman or CURL to test the API endpoints.


## Additional Information

- This project uses Django signals to trigger the creation of new historical performance records when a vendor's performance metrics are updated.
- Make sure to follow best practices in Django development, including adhering to PEP 8 style guidelines.


## Contact

- For any questions or feedback, please contact the repository maintainer at [sreelu266@gmail.com].

---

Thank you for checking out this project!
