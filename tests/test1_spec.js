var frisby = require('frisby')
var data = require('./test_data/test_1_output.json')

frisby.create('RT/Food Method')
          .get('http://127.0.0.1:8000/v2/Retail/Food/')
          .expectStatus(200)
          .expectHeaderContains('content-type', 'application/json')
          .expectJSON(data)
          .toss();
