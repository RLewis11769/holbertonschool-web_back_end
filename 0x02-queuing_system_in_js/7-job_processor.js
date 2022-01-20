// Add blacklisted phone numbers, track progress and failure, and create queue
const kue = require('kue');
const q = kue.createQueue();

const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  // Log progress percentage of job completed
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    // If phone number is blacklisted, fail job
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  // Log progress percentage of job completed
  job.progress(50, 100);
  console.log(`Notification sent to ${phoneNumber}, with message: ${message}`);
  // Complet job
  done();
};

// Process jobs in push_notification_code_2 queue
// Only process 2 jobs at a time - optional limit on simultaneous connections
q.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
