$(document).ready(function(){
    

$('#stateId').change(function(){
$stateid=$(this).val()
$.ajax({
    url: '/dist',
    type: 'post',
    data:{
        "state":$stateid
    },
    success: function(data){
        console.log(data.values[0].id)
        // $('#districtId').append(
        //         $('<option></option>').val(data.values[0].id).html(data.values[0].district)
        //     )
            for(i=0;i<(data.values).length;++i){
                $('#districtId').append(
                    $('<option></option>').val(data.values[i].id).html(data.values[i].district)
                )
            }
}


// districtId

})


})








})