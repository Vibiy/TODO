function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


$(document).ready(function(){
                var $myForm = $('.my-ajax-form')
                $myForm.submit(function(event){
                    event.preventDefault()
                    var $formData = $(this).serialize()
                    var $thisURL = $myForm.attr('data-url') || window.location.href
                    $.ajax({
                        method: "POST",
                        url: $thisURL,
                        data: $formData,
                        success: handleFormSuccess,
                        error: handleFormError,
                    })

                    function handleFormSuccess(data, textStatus, jqXHR){
                        console.log(data)
                        console.log(textStatus)
                        console.log(jqXHR)
                        $myForm[0].reset(); // reset form data
                    }

                    function handleFormError(jqXHR, textStatus, errorThrown){
                        console.log(jqXHR)
                        console.log(textStatus)
                        console.log(errorThrown)
                    }
                })
})
