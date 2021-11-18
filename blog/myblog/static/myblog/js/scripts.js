if (document.querySelector(".notallowededit")) {
  document.querySelector(".notallowededit").onclick = () => {
    alert("Редактировать пост имеет право лишь его автор или администратор!");
  };
}

if (document.querySelector(".unregister_like")) {
  document.querySelector(".unregister_like").onclick = () => {
    alert("Для оценивания поста необходимо зарегистрироваться!");
  };
}

function showList(theme) {
  theme.classList.toggle("detail");
  theme.classList.toggle("show");
  if (theme.classList.contains("detail")) {
    document.querySelector("ul").style.display = "block";
  } else {
    document.querySelector("ul").style.display = "none";
  }
}

window.onload = () => {
  if (document.querySelector(".adaptive_categories")) {
    let theme = document
      .querySelector(".adaptive_categories")
      .querySelector(".active_category");
    theme.onclick = () => {
      showList(theme);
    };
  } else {
  }
};

if (document.querySelector("#site-name")) {
  alert("хач")
}
