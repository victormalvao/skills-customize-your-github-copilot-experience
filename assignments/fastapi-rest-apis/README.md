# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework. You'll create endpoints that handle HTTP requests, validate data with Pydantic models, and implement best practices for API development.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with basic HTTP endpoints (GET, POST, PUT, DELETE) for managing a collection of items. Implement proper route handling and response codes.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Implement GET endpoint to retrieve all items
- Implement POST endpoint to create a new item
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Return appropriate HTTP status codes (200, 201, 404, etc.)

### 🛠️ Implement Data Validation with Pydantic

#### Description
Add Pydantic models to validate incoming request data and ensure type safety. Create request/response schemas that enforce data structure and constraints.

#### Requirements
Completed program should:

- Define Pydantic models for request and response data
- Validate data types and required fields automatically
- Implement custom validators for business logic
- Return validation errors with clear error messages
- Use models consistently across all endpoints

### 🛠️ Add Advanced Features (Stretch Goal)

#### Description
Enhance your API with advanced features like filtering, pagination, error handling, and API documentation.

#### Requirements
Completed program should:

- Implement query parameters for filtering and pagination
- Add comprehensive error handling with meaningful error messages
- Provide automatic API documentation (Swagger UI)
- Include request/response examples in documentation
- Test all endpoints using the built-in Swagger UI
