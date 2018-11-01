
$(function () {
    $("#submit").click(
        function (event) {
            // event.preventDefault，是阻止按钮默认的提交表单的事件
            event.preventDefault();
            var oldpwdE = $("input[name=oldpwd]");
            var newpwdE = $("input[name=newpwd]");
            var newpwd2E = $("input[name=new2pwd]");

            var oldpwd = oldpwdE.val();
            var newpwd = newpwdE.val();
            var newpwd2 = newpwd2E.val();

            // 在末班的meta标签总渲染
        });
})