// Create queue and job - log on creation, completion, and failure
const kue = require('kue');

const q = kue.createQueue();
const job = q.create('push_notification_code', {
  phoneNumber: '918',
  message: 'This is the code to verify your account'
  }).save();

job
  .on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', (err) => {
    console.log('Notification job failed');
  });
