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


async function delete_student() {
  const inputVal = document.getElementById("delete_student-id").value;
  const studentId = parseInt(inputVal, 10);

  if (isNaN(studentId)) {
    alert("Please enter a valid numeric Student ID!");
    return;
  }

  try {
    const response = await fetch(`${API}/students/${studentId}`, {
      method: "DELETE"
    });

    if (!response.ok) {
      const errorData = await response.json();

      // Extract detail string if array (FastAPI 422 error response structure)
      let errorMessage = "Failed to delete student";
      if (Array.isArray(errorData.detail)) {
        errorMessage = errorData.detail.map(err => `${err.loc.join('.')}: ${err.msg}`).join(", ");
      } else if (typeof errorData.detail === "string") {
        errorMessage = errorData.detail;
      }

      throw new Error(errorMessage);
    }

    const data = await response.json();
    alert(data.message);

    document.getElementById("delete_student-id").value = "";
    load_students();
  } catch (error) {
    console.error("Failed to delete student:", error);
    alert(`Could not delete student: ${error.message}`);
  }
}
