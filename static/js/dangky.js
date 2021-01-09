// //kiem tra s la email hay khong
function isEmail(s) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(s).toLowerCase());
}

$(document).ready(function() {
    $(".btnRegister ").click(function(e) {
        var user_name = $("#id_username").val();
        var use_phone = $("#id_phone_number").val();
        var user_email = $("#id_email").val();
        var user_pass = $("#id_password1").val();
        var user_re_pass = $("#id_password2").val();
        var checkEmail = isEmail(user_email);
        var sttError = 1;
        if (user_name == null || user_name == '') {
            $("#id_username").focus();
            $(".item_message .message").html('Vui lòng nhập họ và tên.');
        } else if (use_phone == null || use_phone == '') {
            $("#id_phone_number").focus();
            $(".item_message .message").html('Vui lòng nhập số điện thoại liên lạc.');
        } else if (user_email == null || user_email == '') {
            $("#id_email").focus();
            $(".item_message .message").html('Vui lòng nhập email.');
        } else if (!checkEmail) {
            $("#id_email").focus();
            $(".item_message .message").html('Vui lòng nhập đúng email.');
        } else if (user_pass == null || user_pass == '') {
            $("#id_password1").focus();
            $(".item_message .message").html('Vui lòng nhập mật khẩu.');
        } else if (user_re_pass == null || user_re_pass == '') {
            $("#id_password1").focus();
            $(".item_message .message").html('Vui lòng nhập lại mật khẩu.');
        } else if (user_pass != user_re_pass) {
            $("#id_password2").focus();
            $(".item_message .message").html('Nhập lại mật khẩu không trùng khớp.');
        } else { sttError = 0; }
        if (sttError == 1) { e.preventDefault(); }
    });
});