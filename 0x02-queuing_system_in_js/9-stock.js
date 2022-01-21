// Put it all together to create a server and check stock

// Data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
]

// Data access
const getItemById = (id) => {
  // Return the item with the given itemId
  return listProducts.find(item => item.itemId === id);
}

// Server
const express = require('express');
const app = express();
app.listen(1245);

// Products
app.get('/list_products', (req, res) => {
  res.send(listProducts);
})

// In stock in Redis
const redis = require('redis');
const client = redis.createClient();
const { promisify } = require('util');

const promisifiedSet = promisify(client.set).bind(client);
const asyncGet = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => {
  // Set stock in Redis for given itemId
  promisifiedSet(`item.${itemId}`, stock);
}

const getStockById = async (itemId) => {
  // Return stock in Redis for given itemId
  await asyncGet(`item.${itemId}`);
}

// Product Detail
app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (item) {
    getStockById(itemId).then(stock => {
      item.initialAvailableQuantity = stock;
      res.send(item);
    })
  } else {
    res.status(404).send({ status:'Product not found' });
  }
});

// Reserve a product
app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  // Item doesn't exist in listProducts
  if (!item) res.status(404).send({ status: 'Product not found' });
  // Item exists in listProducts
  if (item.initialAvailableQuantity > 0) {
    // Reduce stock by 1 and confirm reservation
    item.initialAvailableQuantity--;
    reserveStockById(itemId, item.initialAvailableQuantity);
    res.send({ "status":"Reservation confirmed", "itemId": itemId });
  } else {
    // Item exists in listProducts but stock is 0
    res.status(404).send({ status: 'Product not available' });
  }
});
