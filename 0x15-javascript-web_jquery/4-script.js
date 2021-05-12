let tog = $("DIV#toggle_header");
tog.on("click", function () {
    let header = $("header");
    if (header.hasClass("red")) {
        header.removeClass("red");
        header.addClass("green");
    } else {
        header.removeClass("green");
        header.addClass("red");
    }
});
