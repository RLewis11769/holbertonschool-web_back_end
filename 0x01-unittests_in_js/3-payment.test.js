const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');
const sinon = require('sinon');

describe ('Test suite', () => {
  it('Test that sendPaymentRequestToApi is same as Utils.calculateNumber SUM', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    spy.calledWith('SUM', 100, 20);
    spy.restore();
  });
})
