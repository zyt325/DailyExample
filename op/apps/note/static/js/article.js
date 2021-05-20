function article_edit(obj) {
    article_id = obj.getAttribute("article_id");
    class_id = obj.getAttribute("class_id");
    url = "/note/edit-note/?id=" + article_id;
    window.location.href = url;
  }

function goTop() {
  document.body.scrollTop = document.documentElement.scrollTop = 0;
}

function add_goTop() {
  var container = document.getElementById("container");
  var top_ico = document.createElement("button");
  top_ico.id = "goTop";
  top_ico.textContent = "TOP";
  top_ico.onclick = goTop;
  top_ico.setAttribute(
    "style",
    "position:fixed;bottom:40px;right:0;border-width:0;width:40px;height:40px;font-size:16px;background-color:#D4E6EB"
  );
  container.appendChild(top_ico);
}
window.onload = function () {
  //login_auth();
  add_goTop();
};
