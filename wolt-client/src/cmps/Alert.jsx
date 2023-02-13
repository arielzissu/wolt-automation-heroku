import React from 'react';
import { Alert, AlertTitle } from '@mui/material';
import { AlertContainer } from '../styled';

const ApiAlert = ({ showAlert, apiResMsg }) => {
    if (!showAlert) return null;
    return (
        <AlertContainer>
            <Alert severity={apiResMsg.isSuccess ? "success" : "error"}>
                <AlertTitle>Error</AlertTitle>
                {apiResMsg.message}
            </Alert>
        </AlertContainer>
    )
}

export default ApiAlert;
