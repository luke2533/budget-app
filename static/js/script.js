// Paycheck page

function setPaycheck() {
    var paycheck = $("#set-paycheck").val();
    console.log(paycheck)
    $("#spare").val(paycheck);
}

function calcPay() {
    var rent = parseFloat($("#rent").val());
    var budget = parseFloat($("#budget").val());
    var subscriptions = parseFloat($("#subscriptions").val());
    var debt = parseFloat($("#debt").val());
    var savings = parseFloat($("#savings").val());
    var spare = parseFloat($("#spare").val());

    $("#total").html(rent + budget + subscriptions + debt + savings + spare);
}
// https://itqna.net/questions/343/sum-2-inputs-and-appear-real-time-javascript