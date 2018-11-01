
$(function () {
    $('.postTestPager').click(function () {
        $('#postTestPagerDialog').modal('show');
        var self = $(this);
        var tr = self.parent().parent();
        var id = tr.attr('data-id');

        $("#save-info-btn").click(function(){
            var dialog = $("#postTestPagerDialog");
            var testTimeInput = dialog.find("input[id='inputTestTime']");
            var testTime = testTimeInput.val();
            var testClass = $('#testClass').val();
            $.post("/post_test_pager/",
                {
                    'id': id,
                    'test_time': testTime,
                    'test_class': testClass
                },function(result){
                if (result == 'success'){
                    xtalert.alertSuccess('恭喜您，试卷发布成功');
                    dialog.modal("hide");
                    setTimeout(function () {
                        window.location.href = '/manager_test_pager/1/'
                    }, 3000);
                } else {
                    xtalert.alertError(result);
                }
            });
        });
    });
});