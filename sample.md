# Python Backend Learning Project - Task Manager API

## Goal

Build a production-style REST API using Flask that demonstrates:

* Authentication
* Authorization
* JWT
* Password hashing
* SQLAlchemy
* Repository pattern
* Service layer
* Pagination
* Filtering
* Search
* Testing
* API documentation

Domain model:

```text
User
 └── Tasks
```

No Projects in v1.

Projects can be added later as a migration exercise.

---

# Architecture

```text
project/
├── api/
├── services/
├── repositories/
├── models/
├── auth/
├── tests/
└── app.py
```

Example structure:

```text
api/
    auth_routes.py
    task_routes.py
    user_routes.py

services/
    auth_service.py
    task_service.py
    user_service.py

repositories/
    user_repository.py
    task_repository.py

models/
    user.py
    task.py

auth/
    jwt.py
    password.py
    decorators.py

tests/
```

---

# Database Models

## User

```text
id
email
password_hash
name
created_at
updated_at
```

## Task

```text
id
title
description
status
priority
due_date
created_at
updated_at
user_id
```

Status:

```text
todo
in_progress
completed
```

Priority:

```text
low
medium
high
```

---

# Authentication Endpoints

## POST /auth/register

Create a new account.

Requirements:

* Email required
* Password required
* Email uniqueness validation
* Hash password before storage
* Return user id

Concepts:

* Validation
* Password hashing
* Constraints
* Error handling

---

## POST /auth/login

Authenticate a user.

Requirements:

* Verify email/password
* Return JWT access token
* Reject invalid credentials

Concepts:

* Authentication
* JWT generation
* Security

---

## GET /auth/me

Return current authenticated user.

Requirements:

* JWT required

Concepts:

* Authentication middleware
* Authorization

---

# User Endpoints

## PATCH /users/me

Update profile.

Fields:

```text
name
```

Requirements:

* JWT required
* Only update current user

Concepts:

* Validation
* Service layer

---

## PATCH /users/me/password

Change password.

Requirements:

* JWT required
* Current password required
* New password required
* Rehash password

Concepts:

* Security workflows

---

# Task Endpoints

## POST /tasks

Create task.

Fields:

```text
title
description
priority
due_date
```

Requirements:

* JWT required
* Title required
* Status defaults to todo

Concepts:

* Ownership
* Validation

---

## GET /tasks

List current user's tasks.

Requirements:

* JWT required
* Return only tasks belonging to current user

Query Parameters:

```text
?page=1
?limit=20

?status=todo
?status=in_progress
?status=completed

?priority=low
?priority=medium
?priority=high

?sort=created_at
?sort=due_date

?order=asc
?order=desc
```

Concepts:

* Pagination
* Filtering
* Sorting
* Query building

---

## GET /tasks/{task_id}

Get single task.

Requirements:

* JWT required
* User must own task

Concepts:

* Resource authorization

---

## PATCH /tasks/{task_id}

Update task.

Fields:

```text
title
description
status
priority
due_date
```

Requirements:

* Partial updates
* User must own task

Concepts:

* PATCH semantics
* Validation

---

## DELETE /tasks/{task_id}

Delete task.

Requirements:

* User must own task

Concepts:

* Authorization
* Deletion workflows

Implementation decision:

```text
Hard delete
```

Keep v1 simple.

---

# Search

## GET /search/tasks

Query:

```text
?q=backend
```

Requirements:

* JWT required
* Search title
* Search description
* Only search user's tasks

Concepts:

* Dynamic queries
* Search functionality

---

# Authorization Rules

Authentication:

```text
JWT identifies the user.
```

Authorization:

```python
task.user_id == current_user.id
```

Rules:

* Users can only read their own tasks
* Users can only update their own tasks
* Users can only delete their own tasks

No roles.

No RBAC.

No permissions tables.

---

# Testing Requirements

Every endpoint must have tests covering:

## Success

```text
200
201
```

## Authentication Failure

```text
401
```

Missing token.

Invalid token.

Expired token.

## Authorization Failure

```text
403
```

User accesses another user's task.

## Validation Failure

```text
400
422
```

Missing fields.

Invalid values.

## Resource Not Found

```text
404
```

Missing task.

---

# API Documentation

Requirements:

* Swagger/OpenAPI documentation
* Every endpoint documented
* Request schemas documented
* Response schemas documented
* Authentication documented
* Error responses documented

Documentation should be available through a Swagger UI endpoint.

---

# Stretch Goals (After MVP)

Only start these after the entire MVP is complete:

* Refresh tokens
* Rate limiting
* Soft deletes
* Projects
* Task tags
* Task categories
* Docker
* CI/CD pipeline
* Role-based permissions

These are v2 features.
