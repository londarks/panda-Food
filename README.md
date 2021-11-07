
<h1 align="center">
  <img src="project/static/assets/ippai_food.svg"  alt="php" width="120">
</h1>

### 🛠️Under construction 🛠️
1. Token expired
2. Page admin (functions)
3. Create function to add new products
4. Add and send orders to the order area ✔️
5. Reload token for update user info ✔️
6. Sing up user ✔️
7. Sing in User ✔️
8. All pages ✔️
9. Test ✔️

### :computer: Instalação
1. Clone the repository and install requeriments.txt
2. Set variables : `export FLASK_APP=project`, `export FLASK_ENV=development`
3. start Database: `flask db init`, `flask db upgrade` and `flask db migrate`
4. Run the aplication: `flask run`

### 📝Routes

```
Endpoint           Methods    Rule
-----------------  ---------  -----------------------
admin.auth         POST       /auth
admin.cart         GET        /cart/<item>
admin.logout       GET        /logout/
admin.register     POST       /register
admin.static       GET        /static/<path:filename>
admin.update_user  POST       /update_user
pages.admin        GET        /admin
pages.contact      GET        /contact
pages.dashboard    GET        /dashboard
pages.forgot       GET        /forgot
pages.get_product  GET        /product/<name>
pages.index        GET, POST  /
pages.login        GET        /login
pages.pedidos      GET        /pedidos
pages.singup       GET        /singup
pages.static       GET        /static/<path:filename>
static             GET        /static/<path:filename>
```


## Autor
- **👾 Londarks** - _Developer_ - [Twitter](https://twitter.com/londarks)