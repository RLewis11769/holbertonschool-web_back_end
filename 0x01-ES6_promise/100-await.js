import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  // Async function that calls function and returns obj when settled

  return Promise.allSettled([uploadPhoto(), createUser()])
    .then((data) => {
      // Note: Similar to 6 but actually returns data!
      const obj = {};
      // Only works if both promises resolve
      if (data[0].status === 'fulfilled' && data[1].status === 'fulfilled') {
        // Adds values from resolve/then at keys photo and user
        obj.photo = data[0].value;
        obj.user = data[1].value;
      } else {
        obj.photo = null;
        obj.user = null;
      }
      return obj;
    });
}
