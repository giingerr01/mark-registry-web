const API = "http://127.0.0.1:8000/api";

//Home :)
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

//shows a list of whole sutdents present in the database
async function load_students() {
  const response = await fetch(`${API}/students/`);
  const students = await response.json();

  students.sort((a, b) => a.id - b.id);

  const list = document.getElementById("student-list");
  list.innerHTML = "";

  // marks.forEach(marks => {
  //   const li = document.createElement("li");
  //   li.innerHTML = `${marks.subject}`;
  // })


  students.forEach(student => {
    const li = document.createElement("li");
    const markText = student.marks.length > 0 ? student.marks.map(mark => `${mark.subject}: ${mark.score}`).join(", ") : "No marks:";

    li.innerHTML = `
      <strong>Roll Number:</strong> ${student.id} <br>
      <strong>Student Name:</strong> ${student.name} <br>
      <strong>Marks:</strong> ${markText} <br>
      <strong>Student Email:</strong> ${student.email_id} <br>
    `;
    list.appendChild(li);
  });
}

// function defined for creating studnets
async function create_students() {
  const name = document.getElementById("name").value;
  const id = Number(document.getElementById("id").value);
  const email_id = document.getElementById("email_id").value;

  const res = await fetch(`${API}/students/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      id: id,
      name: name,
      email_id: email_id,
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
// add or update the data or detail of the students or their result
async function add_or_update_mark() {
  const studentId = document.getElementById("student-id").value;
  const subject = document.getElementById("subject").value;
  const score = Number(document.getElementById("marks").value);

  if (!studentId || !subject || isNaN(score)) {
    alert("Pleach fill in all the fields!!")
    return;
  }

  const payload = {
    subject: subject,
    score: score
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
      const errorData = await response.json();
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

//delete an student using their roll no.. for now only whole students gets deleted for now 
//later will add the functionalaty to delted the subjects too!!
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
