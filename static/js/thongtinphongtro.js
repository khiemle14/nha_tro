function load_ajax_pagination($value) {
    $.get($value, {}, function(html) {
        $('#_info_comment').html(html);
        $('html, body').animate({
            scrollTop: $('#_info_comment').position().top
        }, 'slow');
    });
}


function display_hidden_comment_form() {
    $('.button_reply').click(function() {
        $(this).parent().next().removeClass('hide');
        // $(this).addClass('hide');
    });
    $('._close_comment').click(function() {
        $(this).parent().parent().parent().addClass('hide');
        // $(this).parent().parent().parent().prev().removeClass('hide');
    });
}


function load_btn_rep(element) {

    var id_cmt = $('.btn-comment-mb-rep').parents().attr('id');


    id_cmt = id_cmt.replace('comment_reply_form', 'cmt_content')

    console.log(id_cmt);

    // if(!notEmpty(id_cmt,"Bạn phải nhập nội dung"))
    // return false;

    // if(!notEmpty("cmt_content","Bạn phải nhập nội dung"))
    // return false;

    $('.btn-comment-mb-rep').parent().find('.full-screen-mobile').addClass('display-open');
    $('.btn-comment-mb-rep').parent().find('.wrap_r').addClass('display-open');
}

function off_popup(element) {
    $('.btn-comment-mb-rep').parent().find('.full-screen-mobile').removeClass('display-open');
    $('.btn-comment-mb-rep').parent().find('.wrap_r').removeClass('display-open');
}

//Hiện *
function calcRate(r) {
    const f = ~~r, //Tương tự Math.floor(r)
        id = 'star' + f + (r % f ? 'half' : '')
    id && (document.getElementById(id).checked = !0)
}

//popup report
function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}