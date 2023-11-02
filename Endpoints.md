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
| GET        | /user/<str:username>/                                             | View details for single user               |
| GET        | /user/profile/<str:user__username>/                               | View User's Profile                        |
| GET        | /series/<int:pk>/                                                 | View User's Profile                        |

