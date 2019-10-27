# TodoRest
ToDo application with Flask and RestAPI

# First
1. git clone ` https://github.com/DenisOstr/TodoRest `

# Run application
1. Run the following commands (in cmd):
   - ` python virtualenv flask `
   - ` python app.py `
2. Open in another cmd window:
   - ` curl -i http://localhost:5000/tasks `
   - ` curl -i http://localhost:5000/tasks/{id} ` where {id} is 1, 2 or 3

# Run application with Insomnia
1. Run Insomnia (if not installed then install Insomnia app)
2. Run application with following commands (in cmd):
   - ` python virtualenv flask `
   - ` python app.py `
3. Create requests in Insomnia:
   - GET ` http://localhost:5000/tasks `
   - GET ` http://localhost:5000/tasks/{id} `
   - POST ` http://localhost:5000/tasks/{id}?title={title}&description={description} `
   - PUT ` http://localhost:5000/tasks/{id}?title={title}&description={description}&done={done} `
   - DELETE ` http://localhost:5000/tasks/{id} `

# Author
Denis Ostrovsky

# License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/DenisOstr/TodoRest/blob/master/LICENSE)
> © Denis Ostrovsky