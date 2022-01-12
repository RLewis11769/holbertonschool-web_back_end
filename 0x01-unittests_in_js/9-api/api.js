// App to be tested by api.test.js
const express = require('express');

const app = express();

app.listen(7865, console.log(`API available on localhost port 7865`))

app.get('/', (req, res) => res.end('Welcome to the payment system'))
// Regex verification that id is a number of indeterminate length
app.get('/cart/:id([0-9]*)', (req, res) => {
  const id = req.params.id;
  res.end(`Payment methods for cart ${id}`)
})

module.exports = app;
