import React from 'react';
import { Box, Typography, Button } from '@mui/material';
import { styled } from '@mui/system';
import { useNavigate } from 'react-router-dom';

const Home: React.FC = () => {
    const navigate = useNavigate();

    // Styled Components
    const PageContainer = styled(Box)({
        padding: '20px',
        height: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        gap: '20px',
    });

    const WelcomeContainer = styled(Box)({
        marginBottom: '40px',
        textAlign: 'center',
    });

    const ButtonContainer = styled(Box)({
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        width: '100%',
        gap: '20px',
    });

    const CreateButton = styled(Button)({
        width: '100%',
        maxWidth: '800px',
        height: '200px',
        background: 'linear-gradient(to right, #9c27b0, #ff9800)', // Purple to Orange gradient
        color: 'white',
        fontWeight: 'bold',
        fontSize: '1.5rem',
        '&:hover': {
            background: 'linear-gradient(to right, #f57c00, #8e24aa)',
        },
    });

    const BottomButtonsContainer = styled(Box)({
        display: 'flex',
        width: '100%',
        maxWidth: '800px',
        justifyContent: 'center',
        gap: '20px',
    });

    const DataButton = styled(Button)({
        flex: 1,
        height: '200px',
        background: 'linear-gradient(to right, #2196f3, #ff9800)', // blue-orange gradient
        color: 'white',
        fontWeight: 'bold',
        fontSize: '1.2rem',
        '&:hover': {
            background: 'linear-gradient(to right, #f57c00, #1976d2)',
        },
    });

    const HelpButton = styled(Button)({
        flex: 1,
        height: '200px',
        background: 'linear-gradient(to right, #9c27b0, #2196f3)', // purple-blue gradient
        color: 'white',
        fontWeight: 'bold',
        fontSize: '1.2rem',
        '&:hover': {
            background: 'linear-gradient(to right, #1976d2, #8e24aa)',
        },
    });

    // Navigation Handlers
    const handleNavigate = (path: string) => {
        navigate(path);
    };

    return (
        <PageContainer>
            <WelcomeContainer>
                <Typography variant="h4" gutterBottom>
                    Welcome to <b>Decomplexify</b>!
                </Typography>
                <Typography variant="body1">
                    An intuitive way to understand and build complex systems through agent-based modeling without writing code.
                </Typography>
            </WelcomeContainer>

            <ButtonContainer>
                <CreateButton onClick={() => handleNavigate('/create')}>
                    Create
                </CreateButton>

                <BottomButtonsContainer>
                    <HelpButton onClick={() => handleNavigate('/help')}>
                        Data
                    </HelpButton>
                    <DataButton onClick={() => handleNavigate('/data')}>
                        Help
                    </DataButton>
                </BottomButtonsContainer>
            </ButtonContainer>
        </PageContainer>
    );
};

export default Home;
