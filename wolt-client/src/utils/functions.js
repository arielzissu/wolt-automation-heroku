import { getFromStorage, saveToStorage } from "./localStorage";
import { CACHE_USER_EMAIL, EMAIL_REGEX, WOLT_URL_REGEX } from "./constants";

export const getCacheEmail = () => {
    const cacheEmail = getFromStorage(CACHE_USER_EMAIL);
    if (!cacheEmail) return '';
    return cacheEmail;
}

export const setCacheEmail = (newEmail) => {
    saveToStorage(CACHE_USER_EMAIL, newEmail);
}

export const checkIsValidEmail = (email) => EMAIL_REGEX.test(email);

export const checkIsValidUrl = (url) => {
    try {
        new URL(url);
        WOLT_URL_REGEX.test(url);
        return true;
    } catch (err) {
        return false;
    }
}