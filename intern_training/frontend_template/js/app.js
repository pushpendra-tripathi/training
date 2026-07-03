window.App = (function () {
  async function init() {
    try {
      UI.setMessage("Loading tasks...");
      const tasks = await API.getTasks();
      UI.setMessage("");
      UI.renderTasks(tasks);
    } catch (e) {
      UI.setMessage("Failed to load tasks. Is the backend running at http://localhost:8000?", "error");
    }
  }

  return { init };
})();


