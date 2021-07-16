import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  return Promise.allSettled([uploadPhoto(), createUser()])
    .then((data) => {
      const arr = {};
      if (data[0].status === 'fulfilled' && data[1].status === 'fulfilled') {
        arr.photo = data[0].value;
        arr.user = data[1].value;
      } else {
        arr.photo = null;
        arr.user = null;
      }
      return arr;
    });
}
