import React, { useState, useEffect } from 'react';
import { Box, Typography } from '@mui/material';
import { INVALID_EMAIL_ERR_MSG, INVALID_WEBSITE_URL_ERR_MSG } from './utils/constants';
import { getUsersRequests, createRequestUrl } from './service';
import { getCacheEmail, setCacheEmail, checkIsValidUrl, checkIsValidEmail } from './utils/functions';
import { ContainMainPage } from './styled';
// import WoltLogo from "./utils/images/Wolt-Logo.png";
import ApiAlert from "./cmps/Alert";
import RequestForm from "./cmps/RequestForm";
import WaitingList from "./cmps/WaitingList";


const App = () => {
  const [isLoadingSave, setIsLoadingSave] = useState(false);
  const [email, setEmail] = useState('');
  const [websiteUrl, setWebsiteUrl] = useState('');
  const [usersRequests, setUsersRequests] = useState(null);
  const [emailErrMsg, setEmailErrMsg] = useState(null);
  const [urlErrMsg, setUrlErrMsg] = useState(null);
  const [apiResMsg, setApiResMsg] = useState(null);
  const [showAlert, setShowAlert] = useState(false)


  const getUsersRequestsData = async (email) => {
    try {
      if (!email) return;
      const usersRequestsData = await getUsersRequests(email);
      setUsersRequests(usersRequestsData.pendingUrls);
    } catch (err) {
      setApiResMsg(err.response.data);
      setShowAlert(true);
    }
  }

  const init = async () => {
    const cacheEmail = getCacheEmail();
    setEmail(cacheEmail);
    if (cacheEmail !== '') {
      await getUsersRequestsData(cacheEmail);
    }
  }

  useEffect(() => {
    init();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const validateForm = (email, websiteUrl) => {
    const isValidEmail = checkIsValidEmail(email);
    if (!isValidEmail) {
      setEmailErrMsg(INVALID_EMAIL_ERR_MSG)
      return false;
    }
    const isValidUrl = checkIsValidUrl(websiteUrl);
    if (!isValidUrl) {
      setUrlErrMsg(INVALID_WEBSITE_URL_ERR_MSG)
      return false;
    }
    setEmailErrMsg(null);
    setUrlErrMsg(null);
    return true;
  }

  useEffect(() => {
    let timeId;
    if (showAlert) {
      timeId = setTimeout(() => {
        setShowAlert(false);
      }, 3000)
    }
    return () => {
      clearTimeout(timeId);
    }
  }, [showAlert])



  const saveUserRequest = async (e) => {
    e.preventDefault();
    try {
      setApiResMsg(null);
      setShowAlert(false);
      const isValidForm = validateForm(email, websiteUrl);
      if (!isValidForm) return;
      setIsLoadingSave(true);
      setCacheEmail(email);
      const res = await createRequestUrl(email, websiteUrl);
      setApiResMsg(res);
      setShowAlert(true);
      await init();
      setIsLoadingSave(false);
    } catch (err) {
      setIsLoadingSave(false);
      setApiResMsg(err.response.data);
      setShowAlert(true);
    }
  }

  return (
    <ContainMainPage>
      <ApiAlert showAlert={showAlert} apiResMsg={apiResMsg} />
      {/* <img src={WoltLogo} alt="Wolt" width="80px" height="100%" /> */}
      <Typography variant="h3" textAlign="center" color={'white'} mb={4}>Is it open?</Typography>
      <Box display="flex" flexDirection="column" justifyContent="space-between" px={2} maxWidth="60%" margin="0 auto">
        <Box display="flex" flexDirection="column" mb={4}>
          <RequestForm
            email={email}
            setEmail={setEmail}
            emailErrMsg={emailErrMsg}
            websiteUrl={websiteUrl}
            setWebsiteUrl={setWebsiteUrl}
            urlErrMsg={urlErrMsg}
            saveUserRequest={saveUserRequest}
            isLoadingSave={isLoadingSave}
          />
        </Box>
        <WaitingList usersRequests={usersRequests}/>
      </Box>
    </ContainMainPage>
  );
}

export default App;
