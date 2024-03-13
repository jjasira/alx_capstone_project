const getContacts = async () => {
  const contacts1 = await fetch("http://127.0.0.1:5000/contacts");
  const contactsData = await contacts1.json();
  contactsData.contacts.forEach((contact) => {
    const nameRow = document.createElement("tr");
    nameRow.key = contact.id;
    const firstNameDetail = document.createElement("td");
    const lasttNameDetail = document.createElement("td");
    const emailDetail = document.createElement("td");
    firstNameDetail.textContent = contact.firstName;
    lasttNameDetail.textContent = contact.lastName;
    emailDetail.textContent = contact.email;
    nameRow.appendChild(firstNameDetail);
    nameRow.appendChild(lasttNameDetail);
    nameRow.appendChild(emailDetail);
    document.getElementById("table-body").appendChild(nameRow);
  });
};

getContacts();
