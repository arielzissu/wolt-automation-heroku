import styled from 'styled-components';
import { WOLT_COLOR } from './utils/constants';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';

export const StyledWoltButton = styled(Button)`
  color: white;
  background-color: ${WOLT_COLOR};
  border-radius: 5rem;
  min-width: max-content;
  width: 100px;
  margin: 0 auto;
  height: 32px;
`;

export const StyledTextField = styled(TextField)`
  min-width: 300px !important;
`;

export const AlertContainer = styled(Box)`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
`;

export const Form = styled.form`
  display: flex;
  flex-direction: column;
`;

export const StyledCard = styled(Card)`
  padding: 10px;
  border-radius: 10px;
  min-height: 100px;
  background-color: rgba(255, 255, 255, 0.9) !important;
`;

export const ContainMainPage = styled(Box)`
  background-color: ${WOLT_COLOR};
  padding: 24px 12px 0 24px;
  height: 100%;
`;