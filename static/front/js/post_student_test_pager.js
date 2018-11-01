$(function () {
    var jiaojunBtn = $("#jiaojuanBtn");
    jiaojunBtn.click(function () {
        xtalert.alertConfirm({
            'msg': '确认交卷吗？',
            'confirmCallback': function () {
                var ChoiceUlArr = $(".ChoiceUL");
                ChoiceUlArr.each(function () {
                    var self = $(this);
                    var radioInput = $("input[type='radio']:checked");
                    var radioval = radioInput.val();
                    if(radioval == undefined){
                        setTimeout(function () {
                            xtalert.alertInfo('选择题未答完')
                        }, 500);
                    }else{
                        $("form").submit();
                    }
                });
            },
        })
    });
});