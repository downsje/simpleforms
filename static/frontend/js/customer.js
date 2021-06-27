$(document).on('submit', '#post-form',function(e){
    e.preventDefault();
    $.ajax({
        url : "/project/customer_form/",
        type : "POST", 
        data : { customer_name: $('#id_customer_name').val(),
                 email_address: $('#id_email_address').val(),
                 subscription_type: $('#id_subscription_type').val(),
                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
 
        }, 
        success : function(json) {
            //reset the form
            if (json['error'] == ""){
                document.getElementById("post-form").reset();

                //alert the user that the submit was successful
                alert('Your customer information was submitted successfully');
                //update the customer grid with the new customer
                $("#jsGrid").jsGrid("loadData");
            }
            else{
                alert(json['error'])
            }

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            alert('Unable to add your customer information successfully');
            
        }
    });
})


$(document).ready(function () {

    loadGrid();
  

});

function loadGrid(){
//create a grid to retrieve all customers
    $("#jsGrid").jsGrid({
        width: "100%",
        shrinkToFit: false,
        forceFit: true,
        editing: false,
        sorting: true,
        autoload: true,
        paging: false,
        filtering: false,
       
        controller: {
            loadData: function (filter) {
                var d = $.Deferred();

                $.ajax({
                    type: "GET",
                    url: "customer_list/",
                    data: filter
                }).done(function (result) {
                    if (result.length > 0) {
                        d.resolve($.map(result, function (item) {
                            return $.extend(item.fields, { id: item.pk });
                        }));
                    }
                    else {
                        d.resolve({ data: [], itemsCount: 0 })
                    }
                }).fail(function (result) {
                    d.resolve({ data: [], itemsCount: 0 })
                })

                return d.promise();
            },
       

        },
        fields: [
            { name: "customer_name", type: "text", title: "Customer Name"},
            { name: "subscription_type", title: "Subscription Type" },
            { name: 'email_address', type:"text", title: "Email Address"},
          

        ]
    });

}