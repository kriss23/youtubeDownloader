var express = require('express')
var bodyParser = require('body-parser')
var exec = require('child_process').exec;

var app = express()
app.use(bodyParser.json())

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};

app.get('*', function(req, res, next){
    // if(req.headers.host == 'vion-stage.mixd.tv' || req.headers.host == 'localhost:3000')  //if it's a sub-domain
    if(req.headers.host == 'vion-stage.mixd.tv')  //if it's a sub-domain
        req.url = '/vion-stage' + req.url;  //append some text yourself
    next();
});

app.get('/', function(req, res) {
    res.send({
        'result': 'error',
        'msg': {
            'error': "API endpoint missing"
        }
    });
})

app.listen(9756, function(){
    console.log('Server listening on', 9757)
})
