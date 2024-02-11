Simple Todo CRUD API with RestFramework 
1. Technologies Used : Python , Django , VSCode , POstman , Mysql(You have to create database name db)
2. In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.
3. 4. First, we have to start up Django's development server : python manage.py runserver
   5. Create user for CRUD and Tokens with POST method : http://127.0.0.1:8000/api/v1/auth/register/
   6. To get a token first we need to request POST method : http://127.0.0.1:8000/api/v1/auth/token/
   7. requesting new access token with POST method : http://127.0.0.1:8000/api/v1/auth/token/refresh/ ()we have too put here refresh that we got in above link
   8. The API doesn't allow unauthenticated requests. but if ununthicated can get all the todo itmes only .
   9. And authicated requests can :
   10. http://127.0.0.1:8000/api/v1/todo/ "Authorization: Bearer {YOUR_TOKEN}" (get all the todo items) for athorization you have to put your token in bearer .
   11. GET http://127.0.0.1:8000/api/v1/todo/{todo_id}/ "Authorization: Bearer {YOUR_TOKEN}" (get todo item by id )
   12. http://127.0.0.1:8000/api/v1/todo/ "Authorization: Bearer {YOUR_TOKEN}" (create a new item )
   13. PUT http://127.0.0.1:8000/api/v1/todo/{todo_id}/ "Authorization: Bearer {YOUR_TOKEN}" (update an item by id )
   14. DELETE http://127.0.0.1:8000/api/v1/todo/{todo_id}/ "Authorization: Bearer {YOUR_TOKEN}" (Delete an item by id)
   15. Tested all that APIs in Postman 
