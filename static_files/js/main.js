setTimeout(function() {
    $('#message').fadeOut(0, 'slow');
}, 3000);

$(function (){
    $('#btn-change-avatar').click(() => {
        $('#btn-change-avatar').slideUp(1000);
        $('#upload-avatar').slideDown(1000);
    });

    $(window).on('load', () => {
        const url = window.location.pathname;
        if(url === "/accounts/login/")
         $('#login-button').click();
    })

    $(document).on('click', '.btn-wishlist', function(e) {
        e.preventDefault();
        const id = $(this).data('id');
        $.ajax({
            type: 'POST',
            url: `/products/${id}/wishlist/`,
            dataType: 'json',
            data: {},
            success: function (data) {
                document.location.href='https://127.0.0.1/products/'
            }
        })
    })
});











function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

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