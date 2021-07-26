/* eslint-disable no-param-reassign */

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  // Handle promises when all settled - either resolved or rejected (both will use .then)
  // Will be pending when run unless use async function

  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((data) => {
      // resolved returns array with keys status === 'fulfilled' and value - this is what we want
      // rejected returns array with keys status === 'rejected' and reason
      // Want error message in value key so the below is all just data manipulation
      // Note: From utils.js, so know data[0] resolves and data[1] rejects - check 100 for if
      // Note: eslint does not want .then data manipulated - should have created new obj
      data[1].value = `Error: ${data[1].reason.message}`;
      delete data[1].reason;
      return data;
    });
}
