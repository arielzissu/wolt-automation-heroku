import { fetch } from './utils/fetchApi';

export const getUsersRequests = (email) =>
    fetch({
        method: 'GET',
        url: `/getUsersRequests?email=${email}`
    });


export const createRequestUrl = (email, url) =>
    fetch({
        method: 'POST',
        url: `/createRequestUrl`,
        data: { email, url }
    });