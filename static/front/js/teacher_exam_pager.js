$(function () {
    var endBtn = $("input[name='endBtn']");
    endBtn.click(function () {
        xtalert.alertConfirm({
            'title': '您确定结束阅卷吗？',
            'confirmCallback': function () {
                $('form').submit();
            },
        })
    });
});