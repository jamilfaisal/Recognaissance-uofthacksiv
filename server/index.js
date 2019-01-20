// content of index.js
const http = require('http');
const port = 3000;
const request = require('request');
const fs = require('fs');
const express = require('express');

var app = express();

app.use('/images', express.static())

app.post('/upload', function(req, res){
    console.log('ok');
});

const requestHandler = (req, response) => {

    if (req.method === 'POST'){
        var options = { method: 'POST',
        url: 'https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/a0744455-ef6b-42b7-a958-ecc59184fcf8/url',
        qs: { iterationId: 'e1304b21-a4fc-4f14-8b6a-1889a61bfc90' },
        headers:
            { 'postman-token': '62346e2d-be57-ae84-8477-e51c97287dfb',
                'cache-control': 'no-cache',
                'prediction-key': '3a11f7dabf1d429a9408833a8851fac8',
                'content-type': 'application/json' },
        body: { Url: 'https://i.gyazo.com/366ceacc532ce34b29e580d0115664a4.jpg' },
        json: true };

        request(options, function (error, response, body) {
            if (error) throw new Error(error);

            console.log(body);
        });
    }
};

const server = http.createServer(requestHandler);

server.listen(port, (err) => {
    if (err) {
        return console.log('something bad happened', err);
    }

    console.log(`server is listening on ${port}`);
});