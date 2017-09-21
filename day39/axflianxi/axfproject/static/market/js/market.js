// $(document).ready(function(){
//     var alltypebtn = document.getElementById("alltypebtn");
//     var showsortbtn = document.getElementById("showsortbtn");
//
//     var typediv = document.getElementById("typediv");
//     var sortdiv = document.getElementById("sortdiv");
//
//     typediv.style.display = "none";
//     sortdiv.style.display = "none";
//
//     alltypebtn.addEventListener("click", function(){
//         typediv.style.display = "block";
//         sortdiv.style.display = "none"
//
//     }, false);
//     showsortbtn.addEventListener("click", function(){
//         typediv.style.display = "none";
//         sortdiv.style.display = "block"
//     }, false);
//
//     typediv.addEventListener("click", function(){
//         typediv.style.display = "none"
//     }, false);
//     sortdiv.addEventListener("click", function(){
//         sortdiv.style.display = "none"
//     }, false);
//
//     var yellow = $(".yellow");
//     var yellowspan = $(".yellowSlide");
//     console.log("ceshi====");
//     yellow.eq(1).click(function(){
//         console.log("---------")
//         yellowspan.eq(1).trigger()
//     })
//      console.log("------11---")
// })

$(document).ready(function(){
    var alltypebtn = document.getElementById("alltypebtn")
    var showsortbtn = document.getElementById("showsortbtn")
    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    typediv.style.display = "none"
    sortdiv.style.display = "none"

    alltypebtn.onclick = function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    }
    typediv.onclick = function () {
        typediv.style.display = "none"
    }
    showsortbtn.onclick = function(){
        sortdiv.style.display = "block"
        typediv.style.display = "none"
    }
    sortdiv.onclick = function(){
        sortdiv.style.display = "none"
    }

    // $span = $("#yellowa li > span")
    // $yellowa = $("#yellowa li")
    //
    // $yellowa.on("click","a", function () {
    //     // $yellowa.css("border-left", "3px solid yellow")
    //     $span.toggle()
    //     // $(this).find(".y").toggle()
    // })

    // var span = document.getElementsByClassName("yellowSlide")
    // var yellow = document.getElementsByClassName("ye")
    // // for(var i = 0; i < yellow.length; i++){
    //     yellow[0].onmousedown = function(){
    //         span[0].style.display = "block"
    //         return
    //     }
    // }


})
















