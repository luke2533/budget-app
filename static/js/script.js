// Paycheck page

function setPaycheck() {
    var paycheck = $("#set-paycheck").val();
    console.log(paycheck)
}

// function total(grandTotal) {
//     var rent = $("#rent").val();
//     var budget = $("#budget").val();
//     var subscriptions = $("#subscriptions").val();
//     var debt = $("#debt").val();
//     var savings = $("#savings").val();
//     var spare = $("#spare").val();
//     var paycheck = $("#set-paycheck").val();
    
//     var grandTotal = rent + budget + subscriptions + debt + savings + spare
//     var total = $("#total").val(grandTotal);
//     console.log(total)
// }

// function total() {
//     var findTotal = $("[name=paycheck]");
//     var total = 0
//     for (var i = 0; i < findTotal.length; i++) {
//         if (parseInt(findTotal[i].value))
//             total += parseInt(findTotal[i].value);
//     }
//     $("#total").val() = total;

// }

var rent = $("#rent").val();
var budget = $("#budget").val();
var subscriptions = $("#subscriptions").val();
var debt = $("#debt").val();
var savings = $("#savings").val();
var spare = $("#spare").val();

var sum_value = 0;
$(".paycheck-value").each(function() {
    sum_value += +$(this).val();
    $("#total").val(sum_value);
})