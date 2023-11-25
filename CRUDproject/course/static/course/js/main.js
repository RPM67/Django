function Add() {
  var form = document.getElementById("courseForm");

  if (form.checkValidity()) {
    alert("Course added into the database successfully!");
  } 
  else {
  }
}


function confirmDelete() {
  return confirm("Are you sure you want to delete this course?");
}


function Update() {
  var form = document.getElementById("courseForm");

  if (form.checkValidity()) {
    alert("course updated into database database successfully!");
  } 
  else {
  }
}
