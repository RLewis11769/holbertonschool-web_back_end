import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  // Async function that calls function and returns obj when settled

  return Promise.allSettled([uploadPhoto(), createUser()])
    .then((data) => {
      // Note: Similar to 6 but actually returns data!
      const arr = {};
      // Only works if both promises resolve
      if (data[0].status === 'fulfilled' && data[1].status === 'fulfilled') {
        // Adds values from resolve/then at keys photo and user
        arr.photo = data[0].value;
        arr.user = data[1].value;
      } else {
        arr.photo = null;
        arr.user = null;
      }
      return arr;
    });
}
