window.UI = (function () {
  const $list = () => document.getElementById("list");
  const $messages = () => document.getElementById("messages");

  function setMessage(text, type = "") {
    $messages().innerHTML = text ? `<div class="${type}">${text}</div>` : "";
  }

  function renderTasks(tasks) {
    if (!tasks || tasks.length === 0) {
      $list().innerHTML = '<div class="card">No tasks yet.</div>';
      return;
    }
    $list().innerHTML = tasks
      .map((t) => `<div class="card"><strong>${t.title}</strong><div>${t.status}</div></div>`)
      .join("");
  }

  return { setMessage, renderTasks };
})();


