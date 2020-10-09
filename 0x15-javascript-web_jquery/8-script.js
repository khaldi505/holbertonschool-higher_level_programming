$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(response) {
    const len = response.results.length;
    let counter = 0;
    for (counter; counter < len; counter++) {
        let title = response.results[counter]["title"];
        li_title = "<li>" + title + "</li>";
        $("UL#list_movies").append(li_title);
    }
}
)
