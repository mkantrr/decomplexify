import React, { useState, useEffect } from 'react';
import { useTheme } from '@mui/material/styles';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Tooltip from '@mui/material/Tooltip';
import Link from '@mui/material/Link';
import axios from 'axios';

import { Link as RouterLink } from 'react-router-dom';

const LOCAL_STORAGE_KEY = 'createPageForm';
const CELL_SIZE = 50; // Grid cell size in pixels

interface GridData {
    key: string; // Key for the entire grid
    cells: [[]]; // 2D array of cells
}

type FormValues = {
    routines: string;
    model: string;
    model_routines: string;
    agent: string;
    agent_routines: string;
};

const Create: React.FC = () => {
    const theme = useTheme();

    // Load initial state from localStorage
    const getInitialValues = (): FormValues => {
        const savedValues = localStorage.getItem(LOCAL_STORAGE_KEY);
        return savedValues
            ? JSON.parse(savedValues)
            : {
                  routines: '',
                  model: '',
                  model_routines: '',
                  agent: '',
                  agent_routines: '',
              };
    };
    const [formValues, setFormValues] = useState(getInitialValues);

    const [gridData, setGridData] = useState<GridData>({
        key: "", // Placeholder grid key
        cells: [[]],
    });

    const [stepCount, setStepCount] = useState(1); // Variable for "Step [x] Times"

    const [responseMessage, setResponseMessage] = useState<string | null>(null);
    const [responseError, setResponseError] = useState<boolean>(false);


    // Save values to localStorage on page leave or refresh
    useEffect(() => {
        const saveData = () => {
            localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(formValues));
        };

        // Save on beforeunload (refresh or close)
        window.addEventListener('beforeunload', saveData);

        // Save on navigation
        return () => {
            saveData();
            window.removeEventListener('beforeunload', saveData);
        };
    }, [formValues]);


    // Handle input change and save to state
    const handleFormChange = (field: keyof typeof formValues) => (event: React.FocusEvent<HTMLInputElement>) => {
        const value = event.target.value;

        // Update state immediately for smooth typing
        setFormValues((prevValues) => ({
            ...prevValues,
            [field]: value,
        }));
    };

    // Handler for "Create"
    const handleCreate = async () => {
        try {
            const response = await axios.post('http://localhost:3001/api/create', formValues);

            if (response.data.error) {
                throw new Error(response.data.error);
            }

            // Clear error and set success message
            setResponseError(false);
            setResponseMessage(response.data.message || 'Model created successfully!');
            setGridData({key: response.data.key, cells: response.data.grid});
        } catch (error: any) {
            // Set error message
            setResponseError(true);
            setResponseMessage(
                error.response?.data?.error || error.message || 'An unexpected error occurred.'
            );
        }
    };

    // Handler for "Step Once"
    const handleStepOnce = async () => {
        try {
            const response = await axios.get('http://localhost:3001/api/step-once');
    
            const { key, data } = response.data;
    
            // Update state with new grid information
            setGridData({key: key, cells: data});
        } catch (error: any) {
            setResponseError(true);
            setResponseMessage(
                error.response?.data?.error || error.message || 'Failed to step the model once.'
            );
        }
    };

    // Handler for "Step [x] Times"
    const handleStepXTimes = async () => {
        try {
            let currentGridData = {key: gridData.key, cells: gridData.cells};
        
            for (let i = 0; i < stepCount; i++) {
                const response = await axios.get('http://localhost:3001/api/step-once');
        
                const { key, data } = response.data;
        
                // Update variables with the latest response
                currentGridData = {key: key, cells: data};
            }
        
            // Update state with new grid information
            setGridData(currentGridData);
        
            // Clear error and set success message
            setResponseError(false);
            setResponseMessage(
                `Model successfully stepped ${stepCount} times!`
            );
        } catch (error: any) {
            setResponseError(true);
            setResponseMessage(
                error.response?.data?.error ||
                    error.message ||
                    `Failed to step the model ${stepCount} times.`
            );
        }
    };

    return (
        <Box sx={styles.page}>
            <Typography sx={{
                    fontWeight: 'bold', 
                    marginBottom: '5px',
                    marginLeft: '10px'
                }}>
                    Visit the {' '}
                    <Link component={RouterLink} to="/docs" underline="hover">
                        Documentation page
                    </Link>{' '} to understand the Gherkin grammar you need to know!
                </Typography>
            <Box sx={styles.container}>
                {/* Dynamic Grid */}
                {!(gridData.key.length === 0) && (
                <Box sx={styles.leftColumn}>
                    <DynamicGrid data={gridData.cells} />
                </Box>
                )}

                {/* Text Fields and Buttons */}
                <Box sx={styles.rightColumn}>
                    {/* Display response message */}
                    {responseMessage && (
                    <Typography  sx={{
                        color: responseError ? '#ff6347' // Red for error
                                : theme.palette.mode === 'dark' ? '#fff' // White for success in dark mode
                                                            : '#000', // Black for success in light mode
                        fontWeight: 'bold',
                        marginBottom: '10px',
                    }}>
                        {responseMessage}
                    </Typography>
                )}
                    <TextField
                        label="Define any basic routines"
                        multiline
                        rows={5}
                        defaultValue={formValues.routines}
                        onBlur={handleFormChange('routines')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />
                    <TextField
                        label="Define the model"
                        multiline
                        rows={5}
                        defaultValue={formValues.model}
                        onBlur={handleFormChange('model')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />
                    <TextField
                        label="Define the model's routines"
                        multiline
                        rows={5}
                        defaultValue={formValues.model_routines}
                        onBlur={handleFormChange('model_routines')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />
                    <TextField
                        label="Define an agent"
                        multiline
                        rows={5}
                        defaultValue={formValues.agent}
                        onBlur={handleFormChange('agent')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />
                    <TextField
                        label="Define the agent's routines"
                        multiline
                        rows={5}
                        defaultValue={formValues.agent_routines}
                        onBlur={handleFormChange('agent_routines')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />

                    {/* Buttons Section */}
                    <Box sx={styles.buttonsContainer}>
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleCreate}
                            sx={{ marginRight: 2 }}
                        >
                            Create
                        </Button>
                        <Button
                            variant="contained"
                            color="secondary"
                            onClick={handleStepOnce}
                            sx={{ marginRight: 2 }}
                        >
                            Step Once
                        </Button>
                        <TextField
                            label="Times to Step"
                            type="number"
                            value={stepCount}
                            onChange={(e) => setStepCount(Number(e.target.value))}
                            sx={{ width: '100px', marginRight: 2 }}
                        />
                        <Button
                            variant="contained"
                            sx={{
                                backgroundColor: 'orange', // Custom orange color
                                color: theme.palette.mode === 'dark' ? 'black' : 'white', // Ensure text is readable
                                '&:hover': {
                                    backgroundColor: 'darkorange', // Darker orange on hover
                                },
                            }}
                            onClick={handleStepXTimes}
                        >
                            Step {stepCount} Times
                        </Button>
                    </Box>
                </Box>
            </Box>
        </Box>
    );
};

const DynamicGrid: React.FC<{ data: [[]] }> = ({ data }) => {
    const rows = data.length;
    const cols = data[0]?.length || 0;

    const colorMap: { [key: number]: string } = {
        0: '#9c27b0',  // Purple
        1: '#ff9800',  // Orange
        2: '#2196f3',  // Blue
        3: '#4caf50',  // Green
        4: '#f44336',  // Red
        5: '#e91e63',  // Pink
        6: '#ffeb3b',  // Yellow
        7: '#00bcd4',  // Cyan
        8: '#795548',  // Brown
        9: '#607d8b', // Gray
        10: '#673ab7', // Deep Purple
        11: '#3f51b5', // Indigo
        12: '#009688', // Teal
        13: '#ffc107', // Amber
        14: '#8bc34a', // Light Green
        15: '#cddc39', // Lime
        16: '#03a9f4', // Light Blue
        17: '#ff5722', // Deep Orange
        18: '#000000', // Black
    };

    return (
        <Box
            sx={{
                ...gridStyles.container,
                gridTemplateColumns: `repeat(${cols}, ${CELL_SIZE}px)`,
                gridTemplateRows: `repeat(${rows}, ${CELL_SIZE}px)`,
            }}
        >
            {data.map((row, rowIndex) =>
                row.map((cell, colIndex) => (
                    <Tooltip
                        key={`${rowIndex}-${colIndex}`}
                        title={
                            cell === null
                                ? `Row: ${rowIndex + 1}, Column: ${colIndex + 1} - Empty`
                                : `Row: ${rowIndex + 1}, Column: ${colIndex + 1} - Value: ${cell}`
                        }
                        arrow
                    >
                        <Box
                            sx={gridStyles.cell}
                            style={{
                                backgroundColor: colorMap[cell] || '#bbb', // Dynamic shading based on value
                            }}
                        />
                    </Tooltip>
                ))
            )}
        </Box>
    );
};

const styles = {
  page: {
      display: 'flex',
      flexDirection: 'column',
      height: '100vh', // Fix the page height to the viewport height
      overflow: 'hidden', // Prevent page scrolling
  },
  container: {
      display: 'flex',
      flex: 1,
      height: '100%',
  },
  leftColumn: {
      flex: .6,
      borderRight: '2px solid #ddd',
      height: '100%', // Constrain the height to the viewport
      padding: '10px',
      boxSizing: 'border-box', // Include padding and border in the height calculation
      overflow: 'auto',
      overflowY: 'auto',
  },
  rightColumn: {
      flex: .4,
      width: '100%',
      paddingLeft: '20px',
      paddingBottom: '20px',
      overflow: 'hidden', // Prevent scrolling in the right column
      overflowY: 'auto',
  },
  buttonsContainer: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: '20px',
    }
};

const gridStyles = {
  container: {
      display: 'grid',
      gap: '0', // Ensure no extra space between cells
      width: '100%',
  },
  cell: {
      border: '1px solid #ddd',
      aspectRatio: '1', // Ensure square cells
      cursor: 'pointer',
  },
};

export default Create;