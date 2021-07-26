export default function handleResponseFromAPI(promise) {
  // Handle response from promise (then - resolved/settled, catch - rejected)

  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
