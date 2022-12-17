# API DOCUMENTATION
 
 - Relational Database  (SQL) for user credential and product catalog
 - Key-value Database (REDIS) for storing data in cart
 - Document Database  (MONGO) for storing data in checkout page and order histoy
 - Graph Database     (NEO4J) for product recomendation
 
 | HTTP METHOD                        | POST                         | GET                             | DELETE                             |
|------------------------------------|------------------------------|---------------------------------|------------------------------------|
| **SQL**                            |                              |                                 |                                    |
| /hp                                | -                            | List of Products                | -                                  |
| /hp/add                            | Add Product Catalog          | -                               | -                                  |
| /hp/stock                          | Update Product Stock         | -                               | -                                  |
| /hp/<int:id_hp>                    | -                            | Get Product by Id               | -                                  |
| /hp/<int:id_hp>/delete             | -                            | -                               | Delete Product by Id               |
| /user                              | -                            | List All User Data              | -                                  |
| /user/add                          | Add User                     | -                               | -                                  |
| /user/<int:id_user>                | -                            | Get User by Id                  | -                                  |
| **REDIS**                          |                              |                                 |                                    |
| /cart                              | -                            | Get Product in Cart             | -                                  |
| /cart/add                          | Add Product to Cart          | -                               | -                                  |
| /cart/<int:id_cart>/checkout       | -                            | Get Product in Cart by Id       | -                                  |
| /cart/<int:id_cart>/delete         | -                            | -                               | Delete Product in Cart by Id       |
| **MONGODB**                        |                              |                                 |                                    |
| /checkout                          | -                            | Get Product in Checkout Page    | -                                  |
| /checkout/<int:id_checkout>        | -                            | Get Product in Checkout by ID   | -                                  |
| /checkout/add                      | Add Product to Checkout Page | -                               | -                                  |
| /checkout/<int:id_checkout>/delete | -                            | -                               | Delete Product in Checkout by Id   |
| /order                             | -                            | Get Data in Order History       | -                                  |
| /order/<int:id_order>              | -                            | Get Data in Order History by Id | -                                  |
| /order/add                         | Add Data to Order History    | -                               | -                                  |
| /order/<int:id_order>/delete       | -                            | -                               | Delete Data in Order History by Id |
| /checkout/clear                    | -                            | -                               | Delete All Data in Order History   |
| **NEO4J**                          |                              |                                 |                                    |
| /product/rank                      | -                            | Get Product Recomendation       | -                                  |
