// Submit post on submit
$("#mycalc").on("submit", function(event){
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    calculate()
});

var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



// AJAX for posting
function calculate() {
    console.log("calculate is working!") // sanity check
    var валута_от = $("#id_валута_от").val();
    var валута_в = $("#id_валута_в").val();
    var сума = $("#id_сума").val();
    $.ajax({
        url: $("#mycalc").attr('action'), // the endpoint
        type : "POST", // http method
        data: {
            валута_от: валута_от,
            валута_в: валута_в,
            сума: сума
        },

        // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check

            if (json.success == true) {
                $("#result").replaceWith('<div id="result" style="margin:15px">Сума след превалутиране: '+json.result+'</div>');
            }
            else if (json.success == false) {
                console.log(value.errors);
            }
        }

    })
};
