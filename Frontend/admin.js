const getContacts = async () => {
  const contacts1 = await fetch("http://127.0.0.1:5000/contacts");
  const contactsData = await contacts1.json();
  contactsData.contacts.forEach((contact) => {
    const contactDetails = document.createElement("div");
    const contactDetail = document.createElement("p");
    contactDetail.innerHTML = `${contact.firstName} ${contact.lastName} ${contact.email}`;
    contactDetails.appendChild(contactDetail);
    const contactContainer = document.getElementById("contacts-container");
    contactContainer.appendChild(contactDetails);
    console.log(contact);
  });
};

getContacts();
