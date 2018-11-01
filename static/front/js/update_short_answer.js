$(function () {
    var updateBtn =  $('.updateBtn');
    updateBtn.click(function () {
        var self = $(this);
        var dialog = $("#myModal");
        var tr = self.parent().parent();
        var idInput = dialog.find("[name='id']");
        var contentInput = dialog.find("[name='content']");
        var result = dialog.find("[name='result']");

        idInput.val(tr.attr("data-id"));
        contentInput.val(tr.attr("data-content"));
        result.val(tr.attr("data-result"));
    });

    // 点击保存按钮
    var saveBtn = $(".saveBtn");
    saveBtn.click(function () {
        var self = $(this);
        var dialog = $("#myModal");
        var idInput = dialog.find("[name='id']");
        var contentInput = dialog.find("[name='content']");
        var resultInput = dialog.find("[name='result']");

        // 获取控件的值
        var id = idInput.val();
        var content = contentInput.val();
        var result = resultInput.val();

        url = "/update_short_answer/";
        data = {
           "id": id,
           "content": content,
            "result": result,
        };
        $.post(
            url,
            data,
            function (data) {
                if (data=='success') {
                    console.log('成功');
                    dialog.modal("hide");
                    xtalert.alertSuccessToast('恭喜您修改成功！');
                    window.location.href = '/manager_short_answer/1/';
                }else{
                    console.log(data);
                }
            }
        );
    });

});