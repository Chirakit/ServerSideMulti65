function addStaff(emp, url, token) {
    const data = {emp_id: emp.value};

    // กำหนด path ให้ถูกต้อง
    fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Item updated successfully')
            window.location.reload()
        })
        .catch(error => console.error('Error:', error));
}

async function removeStaff(emp_Id, url, token) {
    const data = {emp_id: emp_Id};
    // กำหนด path ให้ถูกต้อง
    fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Item updated successfully')
            window.location.reload()
        })
        .catch(error => console.error('Error:', error));
}
