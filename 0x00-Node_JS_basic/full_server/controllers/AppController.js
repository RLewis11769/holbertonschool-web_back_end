// Controller for user interface for / route

class AppController {
  // App controller

  static getHomepage(req, res) {
    // Return homepage rendering
    return res.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
