// ------------------------------
// CRUD (Create, Read, Update, Delete)
// ------------------------------

// Metodos:
// Get - Leer
// Post - Crear
// Put, Patch - Actualizar
// Delete - Eliminar

// Para manejar las solicitudes con json,
// incluir middleware antes del routing:
app.use(express.json());

// ------------------------------
// METODO GET
// ------------------------------

// Manejo de solicitud por metodo get:
app.get('/api/products', (req, res) => {
  res.json(productList.products);
});

// Solicitud: ingresar a la url indicada en la ruta.
// http://localhost:3000/api/products

// ------------------------------
// METODO POST
// ------------------------------

// Manejo de solicitud por metodo post:
app.post('/api/products', (req, res) => {
  let newProduct = req.body;
  productList.push(newProduct);
  res.json(productList.products);
});

// Solicitud:
// POST http://localhost:3000/api/products HTTP/1.1
// Content-Type: application/json
// {
//   "id": 50921,
//   "name": "Chevrolet Onix Joy",
//   "description": "Generación 2019, variedad de colores. Motor 1.0, ideal para ciudad.",
//   "cost": 13500,
//   "currency": "USD",
//   "soldCount": 14,
//   "image": "img/prod50921_1.jpg"
// }

// ------------------------------
// METODO PUT
// ------------------------------

// Manejo de solicitud por metodo put:
app.put('/api/products/:id', (req, res) => {
  let id = req.params.id;
  let updatedProduct = req.body;
  let index = productList.products.findIndex(product => product.id == id);

  if (index >= 0) {
    productList.products[index] = updatedProduct;
  }
  res.json(productList.products);
});

// Solicitud:
// PUT http://localhost:3000/api/products/50921 HTTP/1.1
// Content-Type: application/json
// {
//   "id": 50921,
//   "name": "Chevrolet Onix Joy",
//   "description": "Generación 2019, variedad de colores. Motor 1.0, ideal para ciudad.",
//   "cost": 13500,
//   "currency": "USD",
//   "soldCount": 14,
//   "image": "img/prod50921_1.jpg"
// }

// ------------------------------
// METODO PATCH
// ------------------------------

// Manejo de solicitud por metodo patch:
app.patch('/api/products/:id', (req, res) => {
  let id = req.params.id;
  let updatedProperty = req.body;
  let index = productList.products.findIndex(product => product.id == id);

  if (index >= 0) {
    let productToUpdate = productList.products[index];
    Object.assign(productToUpdate, updatedProperty);
  }
  res.json(productList.products);
});

// Solicitud:
// PATCH http://localhost:3000/api/products/50921 HTTP/1.1
// Content-Type: application/json
// {
//   "soldCount": 14,
// }

// ------------------------------
// METODO DELETE
// ------------------------------

// Manejo de solicitud por metodo delete:
app.delete('/api/products/:id', (req, res) => {
  let id = req.params.id;
  let index = productList.products.findIndex(product => product.id == id);

  if (index >= 0) {
    productList.products.splice(index, 1);
  }
  res.json(productList.products);
});

// Solicitud:
// DELETE http://localhost:3000/api/products/50921 HTTP/1.1
