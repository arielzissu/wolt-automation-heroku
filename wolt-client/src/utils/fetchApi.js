import axios from 'axios';
import { SERVICE_URL } from './constants';

const axiosInstance = axios.create({
    baseURL: SERVICE_URL,
    timeout: 5000,
});


export const fetch = async (params) => {
    const { data } = await axiosInstance(params);
    return data;
};