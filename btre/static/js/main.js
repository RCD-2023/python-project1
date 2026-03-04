const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
  const el = document.getElementById('message');
  if (el) {
    el.remove();
  }
}, 2000);