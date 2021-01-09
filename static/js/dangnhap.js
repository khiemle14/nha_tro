function isEmail(s) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(s).toLowerCase());
}

$(document).ready(function() {
    $(".btnLogin ").click(function(e) {

        var user_email = $("#id_username").val();
        var user_pass = $("#id_password").val();
        var checkEmail = isEmail(user_email);
        var sttError = 1;
        if (user_email == null || user_email == '') {
            $("#user_email").focus();
            $(".item_message .message").html('Vui lòng nhập tên tài khoản.');
        // } else if (!checkEmail) {
        //     $("#user_email").focus();
        //     $(".item_message .message").html('Vui lòng nhập đúng email.');
        } else if (user_pass == null || user_pass == '') {
            $("#user_pass").focus();
            $(".item_message .message").html('Vui lòng nhập mật khẩu.');
        } else { sttError = 0; }
        if (sttError == 1) { e.preventDefault(); }
    });
});