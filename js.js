var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};

fetch("http://127.0.0.1:5000/order_book", requestOptions)
//    .then(response => response.text())
//    .then(result => console.log(result))
    .then(function(response) {
        console.log(myJson);
    return response.json();
// })
//     .then(function(myJson) {
//     for(let i of myJson){
//         if(i.symbol == 'ETHBTC'){
//                 value_price_buy.value =`${i.price}`
//                 value_price_sell.value =`${i.price}`
//             }
//         drop_menu.innerHTML += `<button class="dropdown-item" type="button" id="${i.symbol}" onclick="traer(this.id)">${i.symbol}</button>`;
//     }
    console.log(myJson);
});