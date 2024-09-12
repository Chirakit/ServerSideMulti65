function deleteProject(pro_id, url, token) {
    const data = {project_id: pro_id};
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
            console.log('Item deleted successfully')
            window.location.reload()
        })
        .catch(error => console.error('Error:', error));
}