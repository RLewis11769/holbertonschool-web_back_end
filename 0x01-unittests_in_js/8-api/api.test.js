const api = require('./api');
const { expect } = require('chai');
const request = require('request');

describe ('Test suite', () => {
  // Should stub request in actual test
  it('Test that app returns correct status code and result', (done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    })
  });
})
