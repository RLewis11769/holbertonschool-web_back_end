// Routes to match URL to correct controller
import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

// Router class creates modular, mountable route handlers
// Complete middleware and routing system
const router = express.Router();

// Routes to match URL to correct controller
router.get('/', AppController.getHomepage);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = router;
