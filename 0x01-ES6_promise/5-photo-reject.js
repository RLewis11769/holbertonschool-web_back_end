export default function uploadPhoto(filename) {
  // Return rejected promise

  return Promise.reject(Error(`${filename} cannot be processed`));
}
