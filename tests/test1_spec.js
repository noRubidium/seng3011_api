var frisby = require('frisby')
var data = require('./test_data/test_1_output.json')
var URL_VERSION = process.env.URL_VERSION

frisby.create('RT/Food Method')
          .get(URL_VERSION + 'Retail/Food/')
          .expectStatus(200)
          .expectHeaderContains('content-type', 'application/json')
          .expectJSON(data)
          .toss();
