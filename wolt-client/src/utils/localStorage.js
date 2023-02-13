
export const saveToStorage = (key, value) => {
    localStorage.setItem(key, value);
}

export const getFromStorage = (key) => {
    const cacheData = localStorage.getItem(key);
    return cacheData;
}

export const removeFromStorage = (key) => {
    localStorage.removeItem(key);
}


