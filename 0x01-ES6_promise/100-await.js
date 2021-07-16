import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  return Promise.allSettled([uploadPhoto(), createUser()])
    .then((data) => {
      const arr = [];
      if (data[0].status === 'fulfilled' || data[1].status === 'fulfilled') {
        arr.push({ photo: data[0].value, user: data[1].value });
      } else {
        arr.push({ photo: null, user: null });
      }
      return arr;
    });
}
