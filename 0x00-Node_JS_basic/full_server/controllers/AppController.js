class AppController {
  // App controller

  static getHomepage(req, res) {
    // Return homepage
    return res.status(200).send('Hello Holberton School!');
  }
}
