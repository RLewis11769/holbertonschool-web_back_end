export default function getFullResponseFromAPI(success) {
  const promise = new Promise((resolve) => {
    if (success) {
      resolve({ status: 200, body: success });
    }
  });

  promise.then(() => {
    console.log('Got a response from the API');
  });

  return promise;
}
