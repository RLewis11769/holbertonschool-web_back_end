// App to be tested by api.test.js
const express = require('express');

const app = express();

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});
app
  .get('/', (req, res) => {
    res.send('Welcome to the payment system');
  })
  // Regex verification that id is a number of indeterminate length
  .get('/cart/:id([0-9]*)', (req, res) => {
    res.send(`Payment methods for cart ${req.params.id}\n`);
  });

module.exports = app;
