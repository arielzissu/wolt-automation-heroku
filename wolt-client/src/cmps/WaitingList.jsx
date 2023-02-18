import React from 'react';
import { Box, Typography } from '@mui/material';
import { StyledCard } from '../styled';

const WaitingList = ({ usersRequests }) => {
    return (
        <StyledCard>
            <Box display="flex" flexDirection="column" minWidth="300px">
                <Typography variant="body1">Waiting List</Typography>
                <ul style={{ display: 'flex', flexDirection: 'column' }}>
                    {
                        usersRequests?.map((userRequest, idx) => (
                            <li key={idx}><Typography variant="subtitle2">{userRequest}</Typography></li>
                        ))
                    }
                </ul>
            </Box>
        </StyledCard>
    )
}

export default WaitingList;
