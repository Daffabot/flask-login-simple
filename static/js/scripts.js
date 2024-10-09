$(document).ready(function(){
    $("#signup").submit(function(e) {
        console.log("Submitted")
        e.preventDefault(); // avoid to execute the actual submit of the form.    
        let $form = $(this);
        let $error = $form.find(".error");
        let $data = $form.serialize();

        $.ajax({
            url: "/user/prosignup",
            type: "POST",
            data: $data,
            dataType: "json",
            success: function(resp) {
                console.log(resp);
            },
            error: function(resp) {
                console.log(resp);
            }
        })
    });
})
console.log("berjalan");