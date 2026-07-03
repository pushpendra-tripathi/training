window.API = (function () {
  const BASE = "http://localhost:8000";

  async function fetchJSON(path, options = {}) {
    const res = await fetch(BASE + path, {
      credentials: "include",
      headers: { "Content-Type": "application/json", ...(options.headers || {}) },
      ...options,
    });
    const text = await res.text();
    const data = text ? JSON.parse(text) : null;
    if (!res.ok) {
      const err = new Error(`HTTP ${res.status}`);
      err.data = data;
      throw err;
    }
    return data;
  }

  function getTasks(params = {}) {
    const query = new URLSearchParams(params).toString();
    return fetchJSON(`/api/tasks/${query ? `?${query}` : ""}`);
  }

  return { getTasks };
})();


