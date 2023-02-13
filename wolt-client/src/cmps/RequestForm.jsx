import React from 'react';
import { Box, CircularProgress } from '@mui/material';
import { StyledWoltButton, StyledTextField, Form, StyledCard } from '../styled';

const RequestForm = ({ email, setEmail, emailErrMsg, websiteUrl, setWebsiteUrl, urlErrMsg, saveUserRequest, isLoadingSave }) => {
    return (
        <StyledCard>
            <Form>
                <Box mb={2} display="flex" flexDirection="column">
                    <StyledTextField
                        label="Mail"
                        type="email"
                        variant="standard"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        error={!!emailErrMsg}
                        helperText={emailErrMsg}
                        required
                        fullWidth
                    />
                    <StyledTextField
                        label="Website URL"
                        variant="standard"
                        type="url"
                        value={websiteUrl}
                        onChange={(e) => setWebsiteUrl(e.target.value)}
                        error={!!urlErrMsg}
                        helperText={urlErrMsg}
                        required
                        fullWidth
                    />
                </Box>
                <StyledWoltButton type="submit" onClick={saveUserRequest} variant="contained" disabled={isLoadingSave}>
                    {isLoadingSave ? <CircularProgress size={20} color="inherit" /> : 'Save'}
                </StyledWoltButton>
            </Form>
        </StyledCard>
    )
}

export default RequestForm;
