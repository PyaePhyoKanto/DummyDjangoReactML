// src/ItemsList.js
import React, { useState, useEffect } from 'react';

const ItemsList = () => {
    const [items, setItems] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const apiUrl = `${process.env.REACT_APP_API_BASE_URL}api/items`;
        console.log(apiUrl);
        fetch(apiUrl)
            .then(response => {
                console.log(response);
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => setItems(data))
            .catch(error => {
                console.error('Error fetching data:', error);
                setError(error);
            });
    }, []);

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div>
            <h2>Items</h2>
            <ul>
                {items.map(item => (
                    <li key={item.id}>{item.name}</li>  // Adjust according to your data structure
                ))}
            </ul>
        </div>
    );
};

export default ItemsList;
