$(document).ready(function () {
    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")

    var total = 0
    for(var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]
        addShopping.addEventListener("click", function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/0/", {"productid": pid}, function (data) {
                if(data.status == "success"){
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid + "price").innerHTML = data.price

                    total = parseFloat(data.price)
                    document.getElementById("totalprice").innerHTML = total
                    // total += data.totalprice
                }
            })
        })
    }
    console.log("****",total)
    for(var j = 0;j <subShoppings.length;j++){
        subShopping = subShoppings[j]
        subShopping.addEventListener("click", function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/1/",{"productid": pid}, function (data) {
                if(data.status == "success"){
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid + "price").innerHTML = data.price
                    total -= data.totalprice
                    console.log("****2 ",total)
                    document.getElementById("totalprice").innerHTML = total

                    if(data.data == 0){
                        var li = document.getElementById(pid+"li")
                        li.parentNode.removeChild(li)

                    }
                }
            })
        })
    }

    var ischoses = document.getElementsByClassName("ischose")
    for(var j = 0;j <ischoses.length;j++){
        ischose = ischoses[j]
        ischose.addEventListener("click", function () {
           pid = this.getAttribute("goodsid")
            $.post("/changecart/2/", {"productid": pid}, function (data) {
                if(data.status == "success"){
                    //
                    document.getElementById(pid +"a").innerHTML = data.data
                    if(data.data != ""){
                        // total = data.totalprice
                        console.log(total)
                        document.getElementById("totalprice").innerHTML = total
                    }
                }
            })
        },false)
    }

    var ok = document.getElementById("ok")
    ok.addEventListener("click", function () {
        var f = confirm("是否确认下单？")
        if(f){
            $.post("/saveorder/", function (data) {
                if(data.status == "success"){
                    window.location.href = "http://127.0.0.1:8000/cart/"
                    // var li = document.getElementById(pid + "li")
                    // li.parentNode.removeChild(li)
                }
            })
        }
    }, false)


})

