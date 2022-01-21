// Function to create a job from a list of jobs
const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  for (const job of jobs) {
    const newJob = queue.create('push_notification_code_3', job).save();
    try {
      newJob
        .on('enqueue', () => {
          console.log(`Notification job created: ${newJob.id}`);
        })
        .on('complete', () => {
          console.log(`Notification job ${newJob.id} completed`);
        })
        .on('failed', (err) => {
          console.log(`Notification job ${newJob.id} failed: ${err}`);
        })
        .on('progress', (progress) => {
          console.log(`Notification job ${newJob.id} ${progress}% complete`);
        });
    // Add empty catch block to prevent error from breaking the loop
    } catch (err) {}
  };
};

module.exports = createPushNotificationsJobs;
