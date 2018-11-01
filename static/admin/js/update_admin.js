// 在模态框中点击保存的事件
$(function () {
    // 单选框点击事件
    var checkBox = $("#checkbox");
    checkBox.click(function () {
        console.log('点击事件');
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
        var uidInput = $("input[name='uid']");
        var nameInput = $("input[name='name']");
        var emailInput = $("input[name='email']");
        var phoneInput = $("input[name='phone']");


        var uid = uidInput.val();
        var name = nameInput.val();
        var email = emailInput.val();
        var phone = phoneInput.val();

        var checkBox = $("#checkbox");
        var is_super = checkBox.val();

        if(!name || !email || !phone ){
            xtalert.alertInfoToast('请输入完整的信息！');
            return;
        }

        url = '/update_user/';

        $.post(
            url,{
                'uid': uid,
                'name': name,
                'email': email,
                'phone': phone,
                'is_super':is_super,
            },
            function (data, status) {
                if (data == 'success') {
                    xtalert.alertSuccessToast('信息修改成功');
                    window.location.href='/admin_manager_user/1/';
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
        var uid = tr.attr("data-uid");
        var name = tr.attr("data-name");
        var email = tr.attr("data-email");
        var phone = tr.attr("data-phone");
        var is_super = tr.attr("data-is-super");

        var uidInput = dialog.find("input[name='uid']");
        var nameInput = dialog.find("input[name='name']");
        var emailInput = dialog.find("input[name='email']");
        var phoneInput = dialog.find("input[name='phone']");
        var is_supercheck = dialog.find("checkbox[name='super_admin']");
        var saveBtn = dialog.find("#save-info-btn");

        uidInput.val(uid);
        nameInput.val(name);
        emailInput.val(email);
        phoneInput.val(phone);
        is_supercheck.checked = false;
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
                url = '/delete_user/';
                var tr = self.parent().parent();
                var uid = tr.attr("data-uid");
                $.post(
                    url,{
                        'uid': uid,
                    },
                    function (data, status) {
                        if (data == 'success') {
                            xtalert.alertSuccessToast('信息已删除!');
                            window.location.href='/admin_manager_user/1/';
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
