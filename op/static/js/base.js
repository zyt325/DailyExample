$('#navbar a').click(function () {
    this.css("font-weight","bold");
})

var pathname=document.location.pathname;
console.log(pathname)
if(pathname=='/'){
    nav='dashboard'
}else{
    nav=pathname.split('/')[1]
}


$("#navbar li[name="+nav+"]").css('background-color','#ffffff')
$("#navbar li[name="+nav+"]").css('font-weight','bold')