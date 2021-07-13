import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      console.log(`${values[0].body}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
