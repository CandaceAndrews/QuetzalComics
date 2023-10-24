### 🐌 API ENDPOINTS

| HTTP Verbs | Endpoints                                                         | Action                                     |         
| ---------- | ----------------------------------------------------------------- | ------------------------------------------ |
| GET        | /auth/users                                                       | Return info for logged in user             |
| POST       | /auth/users                                                       | Create new user                            |
| POST       | /auth/token/login                                                 | User login                                 |
| POST       | /auth/token/logout                                                | User logout                                |
| GET        | /auth/users/me                                                    | Retrieve authenticated user                |
| PATCH      | /auth/users/me                                                    | Update authenticated user                  |
| DELETE     | /auth/users/me                                                    | Delete authenticated user                  |
|            |                                                                   |                                            |
| GET        | users/<str:username>/                                             | View details for single user               |

