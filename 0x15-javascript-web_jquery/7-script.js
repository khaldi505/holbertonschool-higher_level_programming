fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
.then(res => res.json())
.then(json =>
$(document).ready(function(){
    $("DIV#character").text(json.name);
}));

