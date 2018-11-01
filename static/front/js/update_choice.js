$(function () {
    var updateBtn =  $('.updateBtn');
    updateBtn.click(function () {
        var self = $(this);
        var dialog = $("#myModal");
        var tr = self.parent().parent();
        var choiceIdInput = dialog.find("[name='choiceId']");
        var choiceContentInput = dialog.find("[name='content']");
        var choiceAInput = dialog.find("[name='choiceA']");
        var choiceBInput = dialog.find("[name='choiceB']");
        var choiceCInput = dialog.find("[name='choiceC']");
        var choiceDInput = dialog.find("[name='choiceD']");
        var choiceSelect = dialog.find("[name='choiceResult']");

        choiceIdInput.val(tr.attr("data-id"));
        choiceContentInput.val(tr.attr("data-content"));
        choiceAInput.val(tr.attr("data-choiceA"));
        choiceBInput.val(tr.attr("data-choiceB"));
        choiceCInput.val(tr.attr("data-choiceC"));
        choiceDInput.val(tr.attr("data-choiceD"));
        choiceSelect.val(tr.attr("data-result"));
    });

    // 点击保存按钮
    var saveBtn = $(".saveBtn");
    saveBtn.click(function () {
        var self = $(this);
        var dialog = $("#myModal");
        var choiceIdInput = dialog.find("[name='choiceId']");
        var choiceContentInput = dialog.find("[name='content']");
        var choiceAInput = dialog.find("[name='choiceA']");
        var choiceBInput = dialog.find("[name='choiceB']");
        var choiceCInput = dialog.find("[name='choiceC']");
        var choiceDInput = dialog.find("[name='choiceD']");
        var choiceSelect = dialog.find("[name='choiceResult']");

        // 获取控件的值
        var choiceId = choiceIdInput.val();
        var choiceContent = choiceContentInput.val();
        var choiceA = choiceAInput.val();
        var choiceB = choiceBInput.val();
        var choiceC = choiceCInput.val();
        var choiceD = choiceDInput.val();
        var choiceResult = choiceSelect.val();

        url = "/update_choice/";
        data = {
           "choiceId": choiceId,
           "choiceContent": choiceContent,
            "choiceA": choiceA,
            "choiceB": choiceB,
            "choiceC": choiceC,
            "choiceD": choiceD,
            "choiceResult": choiceResult
        };
        $.post(
            url,
            data,
            function (data) {
                if (data=='success') {
                    console.log('成功');
                    dialog.modal("hide");
                    xtalert.alertSuccessToast('恭喜您修改成功！');
                    window.location.href = '/manager_choice/1/';
                }else{
                    console.log(data);
                }
            }
        );
    });

    // // 删除
    // var delBtn = $(".delBtn");
    // delBtn.click(function () {
    //     var self = $(this);
    //     data = {
    //         "choiceId": self.parent().parent().attr("data-id"),
    //     };
    //     xtalert.alertConfirm({
    //         "title": '您确定要删除吗？',
    //         "confirmCallback": function () {
    //             $.post(
    //                 '/del_choice/',
    //                 data,
    //                 function(data){
    //                     if (data == 'success'){
    //                         xtalert.alertToast(data);
    //                         window.location.href = '/manager_choice/1/';
    //                     }else{
    //                         xtalert.alertErrorToast(data);
    //                         window.location.href = '/manager_choice/1/';
    //                     }
    //                 }
    //             )
    //         }
    //     })

    // });
});