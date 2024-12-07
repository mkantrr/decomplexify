import React from 'react';
import { Box, Typography, Accordion, AccordionSummary, AccordionDetails, useTheme } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { styled } from '@mui/system';

const Documentation: React.FC = () => {
    const theme = useTheme(); // Access the current theme (light or dark)

    // Styled Components
    const PageContainer = styled(Box)({
        padding: '20px',
    });

    const Title = styled(Typography)({
        textAlign: 'center',
        marginBottom: '20px',
        fontWeight: 'bold',
    });

    const SectionContainer = styled(Box)({
        display: 'flex',
        flexDirection: 'column',
        gap: '10px',
    });

    const ExampleBox = styled(Box)(({ theme }) => ({
        backgroundColor: theme.palette.mode === 'dark' ? '#333' : '#f5f5f5',
        color: theme.palette.mode === 'dark' ? '#fff' : '#000',
        padding: '10px',
        borderRadius: '5px',
        fontFamily: 'monospace',
        overflow: 'auto',
    }));

    return (
        <PageContainer>
            {/* Title */}
            <Title variant="h4">Documentation</Title>
            <Typography variant="body1" sx={{ marginBottom: '20px' }}>
                Learn how to define your agent-based models using Gherkin grammar rules.
                Gherkin syntax allows you to write models intuitively and clearly. Below are the
                available rules and examples for using Decomplexify.
            </Typography>

            {/* Grammar Rules Sections */}
            <SectionContainer>
                {/* Define the Model */}
                <Accordion>
                    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                        <Typography variant="h6">Define the Model</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            Use the <strong>Given</strong> keyword to define the initial state of
                            the model.
                        </Typography>
                        <Typography>
                            <strong>Example:</strong>
                        </Typography>
                        <ExampleBox>
                            Given a grid of size 10x10
                        </ExampleBox>
                        <Typography>
                            This initializes a 10x10 grid for your model.
                        </Typography>
                    </AccordionDetails>
                </Accordion>

                {/* Define the Model Routines */}
                <Accordion>
                    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                        <Typography variant="h6">Define the Model Routines</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            Use the <strong>When</strong> keyword to define model behaviors or
                            routines.
                        </Typography>
                        <Typography>
                            <strong>Example:</strong>
                        </Typography>
                        <ExampleBox>
                            When agents move randomly across the grid
                        </ExampleBox>
                        <Typography>
                            This specifies that agents will randomly move on the grid during the
                            simulation.
                        </Typography>
                    </AccordionDetails>
                </Accordion>

                {/* Define an Agent */}
                <Accordion>
                    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                        <Typography variant="h6">Define an Agent</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            Use the <strong>And</strong> keyword to define specific attributes of
                            agents.
                        </Typography>
                        <Typography>
                            <strong>Example:</strong>
                        </Typography>
                        <ExampleBox>
                            And each agent has a type of "Predator" or "Prey"
                        </ExampleBox>
                        <Typography>
                            This defines two types of agents, "Predator" and "Prey."
                        </Typography>
                    </AccordionDetails>
                </Accordion>

                {/* Define the Agent Routines */}
                <Accordion>
                    <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                        <Typography variant="h6">Define the Agent Routines</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            Use the <strong>Then</strong> keyword to define the actions of agents.
                        </Typography>
                        <Typography>
                            <strong>Example:</strong>
                        </Typography>
                        <ExampleBox>
                            Then predators eat prey if they are in the same cell
                        </ExampleBox>
                        <Typography>
                            This specifies that predators will consume prey if they encounter them
                            in the same cell on the grid.
                        </Typography>
                    </AccordionDetails>
                </Accordion>

            </SectionContainer>
        </PageContainer>
    );
};

export default Documentation;
