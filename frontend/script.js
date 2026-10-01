const API = "http://127.0.0.1:8000/api";


async function home() {
  try {
    const response = await fetch(`${API}/`)

    const data = await response.json();
    console.log(data.message);
    alert(data.message);
  } catch (error) {
    console.error("could not connect to the backend:", error);
  }
}

async function add_or_update_mark() {
  const studentId = document.getElementById("student-id").value;
  const subject = document.getElementById("subject").value;
  const marks = Number(document.getElementById("marks").value);

  if (!studentId || !subject || isNaN(marks)) {
    alert("Pleach fill in all the fields!!")
    return;
  }

  const payload = {
    subject: subject,
    score: marks
  };

  try {
    const response = await fetch(`${API}/students/${studentId}/marks`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)

    });

    if (!response.ok) {
      throw new Error(errorData.detail || `${response.status}`);
    }
    const data = await response.json();
    alert("Marks has been updated!")
    console.log("Updated dat:", data);

    document.getElementById("subject").value = "";
    document.getElementById("marks").value = "";
  } catch (error) {
    console.error("Failed to update marks:", error);
    alert("Could not update marks. Check console for details");
  }
}

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

async function to_remove_student() {
  const studentId = Number(document.getElementById("Student-Id").value);

  if (isNaN(studentId)) {
    alert("Please fill in the student ID!")
    return;
  }

  const payload = {
    ID: studentId,
  };

  try {
    const response = await fetch(`${API}/students/{student}/remove`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });
  }

}
