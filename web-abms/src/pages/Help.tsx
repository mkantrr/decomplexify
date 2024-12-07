import React from 'react';
import {
    Accordion,
    AccordionSummary,
    AccordionDetails,
    Typography,
    Box,
    Link,
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { Link as RouterLink } from 'react-router-dom';

const Help: React.FC = () => {
    return (
        <Box sx={styles.page}>
            <Typography variant="h4" sx={styles.title}>
                Need some help?
            </Typography>
            <Box sx={styles.container}>
                <Accordion>
                    <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="section1-content"
                        id="section1-header"
                    >
                        <Typography variant="h6">What is Decomplexify?</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            Decomplexify is an app designed to help students understand complex
                            systems through agent-based modeling. It allows users to define models
                            using an intuitive Gherkin-like instruction set without needing to code.
                            See examples{' '}
                            <Link component={RouterLink} to="/documentation" underline="hover">
                                here
                            </Link>.
                        </Typography>
                    </AccordionDetails>
                </Accordion>

                <Accordion>
                    <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="section2-content"
                        id="section2-header"
                    >
                        <Typography variant="h6">How do I define a model?</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            You can define your model using the input fields on the Create page. The
                            fields allow you to specify the model, agents, and their routines. Once defined, the model can be created and stepped through
                            dynamically.
                        </Typography>
                    </AccordionDetails>
                </Accordion>

                <Accordion>
                    <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="section3-content"
                        id="section3-header"
                    >
                        <Typography variant="h6">How does the grid work?</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            The grid represents the environment where agents interact. It updates
                            dynamically based on the model's rules and time steps. You can interact
                            with the grid by creating a model and stepping through the simulation.
                        </Typography>
                    </AccordionDetails>
                </Accordion>

                <Accordion>
                    <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="section4-content"
                        id="section4-header"
                    >
                        <Typography variant="h6">Where can I learn more?</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            Visit the{' '}
                            <Link component={RouterLink} to="/documentation" underline="hover">
                                Documentation page
                            </Link>{' '}
                            for detailed instructions and examples of how to use Decomplexify. You
                            can also reach out to support for further assistance.
                        </Typography>
                    </AccordionDetails>
                </Accordion>
            </Box>
        </Box>
    );
};

const styles = {
    page: {
        padding: '20px',
    },
    title: {
        textAlign: 'center',
        marginBottom: '20px',
        fontWeight: 'bold',
    },
    container: {
        display: 'flex',
        flexDirection: 'column',
        gap: '10px',
    },
};

export default Help;
