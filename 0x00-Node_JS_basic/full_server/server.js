// Actually set up server used in other files
import express from 'express';

// Requires routes as basically import
const routes = require('./routes/index');

// Set up express app
const app = express();

// Configure middleware used by routes
// All are executed every time request is made no matter what URL is hit
app.use(routes);

app.listen(1245);

export default app;
