window.onload = function () {
    let url = "https://fourtonfish.com/hellosalut/?lang=" 
    const lang = $("INPUT#language_code").val();
    url = url + lang
    $.get(url, function(response) {
    $("INPUT#btn_translate").click(function(){
        $("DIV#hello").html(response.hello);
    });
});
};
