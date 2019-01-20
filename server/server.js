const express = require('express');
const app = express();
const port = 3000;
const request = require('request');
const multer = require('multer');
var upload = multer({dest: './images/'});
var fs = require("fs");

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, cache-control,");
    next();
});

app.get('/', function (req, res){
    res.send("Hello World!");
});

app.get('/info', function (req, res){
    res.send(fs.readFileSync("data.json"))
});

app.post('/profile', upload.single('img.jpg'), function (req, res, next){
    res.send(req.body);
    console.log('recieved');
});

app.post('/upload', upload.single('img.jpg'), function (req, res, next) {
    lat = req.body["lat"];
    long = req.body["long"];
    res.send(req.body);
    var options = { method: 'POST',
        url: 'https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/a0744455-ef6b-42b7-a958-ecc59184fcf8/url',
        qs: { iterationId: 'e1304b21-a4fc-4f14-8b6a-1889a61bfc90' },
        headers:
            { 'postman-token': '62346e2d-be57-ae84-8477-e51c97287dfb',
                'cache-control': 'no-cache',
                'prediction-key': '3a11f7dabf1d429a9408833a8851fac8',
                'content-type': 'application/json' },
        body: { Url: 'http://a4c94c54.ngrok.io/' + req.file['path']},
        json: true
    };

    request(options, function (error, response, body) {
        if (error) throw new Error(error);

        // console.log(body);
        if (detect(body)){
            console.log("body detected!")
        }
    });
});

function detect(data) {
    if (data['predictions'] === undefined){
        return false;
    }
    for (i = 0; i < data['predictions'].length; i++){
        if (data['predictions'][i]["tagName"].toLowerCase().includes('white van')){
            return true;
        }
    }
}

app.use('/images', express.static('images'));

app.listen(port, () => console.log(`Example app listening on port ${port}!`));

// detect(JSON.parse(""));