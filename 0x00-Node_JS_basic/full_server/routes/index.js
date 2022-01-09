// Routes to match URL to correct controller
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const express = require('express');

// Router class creates modular, mountable route handlers
// Complete middleware and routing system
const router = express.Router();

// Routes to match URL to correct controller
router.get('/students/:major', StudentsController.getAllStudentsByMajor);
router.get('/students', StudentsController.getAllStudents);
router.get('/', AppController.getHomepage);

module.exports = router;
