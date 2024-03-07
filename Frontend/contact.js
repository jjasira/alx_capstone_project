document.addEventListener("DOMContentLoaded", () => {
  let submitForm = document.getElementById("contact-form");

  submitForm.addEventListener("submit", (event) => {
    event.preventDefault();
    handleFormSubmit();
  });
});

const handleFormSubmit = () => {
  let firstNameInput = document.getElementById("firstName");
  let lastNameInput = document.getElementById("lastName");
  let emailInput = document.getElementById("email");

  const firstName = firstNameInput.value.trim();
  const lastName = lastNameInput.value.trim();
  const email = emailInput.value.trim();

  if (validateEmail(email)) {
    const requestBody = {
      first_name: firstName,
      last_name: lastName,
      email: email,
    };
    register(requestBody);
    let submitForm = document.getElementById("contact-form");
    submitForm.style.display = "none";
    let message = document.createElement("p");
    message.innerHTML = `You have successfully subscribed to the Newsletter with ${email}`;
    document.getElementById("form-container").appendChild(message);
  } else {
    const alertParagraph = document.createElement("p");
    alertParagraph.innerHTML = "Please enter a valid email address";
    alertParagraph.style.color = "red";
    document.getElementById("contact-form").appendChild(alertParagraph);
  }
};

const register = async (requestBody) => {
  const url = "http://127.0.0.1:5000/create_contact";
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestBody),
  };
  console.log(options);

  const response = await fetch(url, options);
  if (response.status !== 201 && response.status !== 200) {
    const data = await response.json();
    alert(data.message);
  } else {
    alert("Your Contact has been saved successfully");
  }
};

function validateEmail(email) {
  let validateRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  return validateRegex.test(email);
}
