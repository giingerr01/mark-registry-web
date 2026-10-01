const API = "http://127.0.0.1:8000/api";

async function load_students() {
  const res = await fetch(`${API}/students/`);
  const students = await res.json();

  const list = document.getElementById("student-list");
  list.innerHTML = "";
  students.forEach(s => {
    const li = document.createElement("li");
    li.textContent = `${s.id} - ${s.name}`;
    list.appendChild(li);
  });
}

async function create_students() {
  const name = document.getElementById("name").value;
  const id = Number(document.getElementById("id").value);

  const res = await fetch(`${API}/students/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      id: id,
      name: name,
      marks: []
    })
  });
  if (!res.ok) {
    const err = await res.json();
    alert(err.detail);
    return;
  }
  load_students();
}
