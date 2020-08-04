$(document).ready(function () {

    $("td.val:contains('-')").addClass('r');
    $("td.val:contains('+')").addClass('g');
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
});


$(document).ready(function () {
    $('.modal').modal();
});


document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.autocomplete');
    var instances = M.Autocomplete.init(elems, options);
});


$(window).on("load", function () {
    $(".loader-wrapper").fadeOut("slow");
});
