// 在模态框中点击保存的事件
$(function () {
    // 单选框点击事件
    var checkBox = $("#checkbox");
    checkBox.click(function () {
        var value = checkBox.val();
        if (value==1){
            checkBox.val(0);
        }else{
            checkBox.val(1);
        }
    });


    $(".save-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var idInput = $("input[name='id']");
        var nameInput = $("input[name='name']");
        var emailInput = $("input[name='email']");
        var phoneInput = $("input[name='phone']");
        var classInput = $("input[name='class_']");


        var id = idInput.val();
        var name = nameInput.val();
        var email = emailInput.val();
        var phone = phoneInput.val();
        var class_ = classInput.val();

        if(!name || !email || !phone || !class_){
            xtalert.alertInfoToast('请输入完整的信息！');
            return;
        }

        console.log(class_);
        url = '/update_student/';

        $.post(
            url,{
                'id': id,
                'name': name,
                'email': email,
                'phone': phone,
                'class_':class_,
            },
            function (data, status) {
                if (data == 'success') {
                    xtalert.alertSuccessToast('信息修改成功');
                    window.location.href='/admin_manager_student/1/';
                    $("#updatedialog").modal("hide");
                }
                else{
                    xtalert.alertErrorToast(data)
                }
            }
        )
    });
});



// 点击修改把信息绑定到模态框中
$(function () {
    $(".btn-update").click(function (event) {
        var self = $(this);
        var dialog = $("#updatedialog");
        // dialog.modal("show");

        var tr = self.parent().parent();
        var id = tr.attr("data-id");
        var name = tr.attr("data-name");
        var email = tr.attr("data-email");
        var phone = tr.attr("data-phone");
        var class_ = tr.attr("data-class");

        var idInput = dialog.find("input[name='id']");
        var nameInput = dialog.find("input[name='name']");
        var emailInput = dialog.find("input[name='email']");
        var phoneInput = dialog.find("input[name='phone']");
        var classInput = dialog.find("input[name='class_']");
        var saveBtn = dialog.find("#save-info-btn");

        idInput.val(id);
        nameInput.val(name);
        emailInput.val(email);
        phoneInput.val(phone);
        classInput.val(class_);
    });
});


// 点击删除用户的事件
$(function () {
    var btnDelete = $(".btn-delete");
    btnDelete.click(function () {
        var self = $(this);
        xtalert.alertConfirm({
            'confirmText': '确认',
            'cancelText': '取消',
            'msg': '确定删除此用户吗？',
            'confirmCallback': function () {
                url = '/delete_student/';
                var tr = self.parent().parent();
                var id = tr.attr("data-id");
                $.post(
                    url,{
                        'id': id,
                    },
                    function (data, status) {
                        if (data == 'success') {
                            xtalert.alertSuccessToast('信息已删除!');
                            window.location.href='/admin_manager_student/1/';
                        }
                        else{
                            xtalert.alertErrorToast(data)
                        }
                    }
                )
            }
        });
    });
});