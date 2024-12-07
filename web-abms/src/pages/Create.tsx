import React, { useState, useEffect } from 'react';
import { useTheme } from '@mui/material/styles';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Tooltip from '@mui/material/Tooltip';
import axios from 'axios';

const LOCAL_STORAGE_KEY = 'createPageForm';
const CELL_SIZE = 50; // Grid cell size in pixels

interface GridCell {
    value: number; // Positive integer
}

interface GridData {
    key: string; // Key for the entire grid
    cells: GridCell[][]; // 2D array of cells
}

type FormValues = {
    model: string;
    modelRoutines: string;
    agent: string;
    agentRoutines: string;
};

const Create: React.FC = () => {
    const theme = useTheme();

    // Load initial state from localStorage
    const getInitialValues = (): FormValues => {
        const savedValues = localStorage.getItem(LOCAL_STORAGE_KEY);
        return savedValues
            ? JSON.parse(savedValues)
            : {
                  model: '',
                  modelRoutines: '',
                  agent: '',
                  agentRoutines: '',
              };
    };
    const [formValues, setFormValues] = useState(getInitialValues);

    const [gridData, setGridData] = useState<GridData>({
        key: "DefaultGrid", // Placeholder grid key
        cells: [],
    });
    const [gridDimensions, setGridDimensions] = useState({ rows: 20, cols: 10 }); // Example larger grid
    const [stepCount, setStepCount] = useState(1); // Variable for "Step [x] Times"


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


    // Simulate fetching grid data from an API
    useEffect(() => {
        const mockCells: GridCell[][] = Array.from({ length: gridDimensions.rows }, () =>
            Array.from({ length: gridDimensions.cols }, () => ({
                value: Math.ceil(Math.random() * 10), // Random positive integer
            }))
        );
        setGridData({
            key: "DefaultGrid", // Simulated API grid key
            cells: mockCells,
        });
    }, [gridDimensions]);

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
        console.log("Create triggered");
        try {
            const response = await axios.post('/api/create', formValues); // Replace with your API endpoint
            console.log('API Response:', response.data);
            alert('Data successfully submitted!');
        } catch (error) {
            console.error('Error submitting data:', error);
            alert('Failed to submit data.');
        }
    };

    // Handler for "Step Once"
    const handleStepOnce = () => {
        console.log("Step Once triggered");
        // Add your "Step Once" logic here
    };

    // Handler for "Step [x] Times"
    const handleStepXTimes = () => {
        console.log(`Step ${stepCount} times triggered`);
        // Add your "Step [x] Times" logic here
    };

    return (
        <Box sx={styles.page}>
            <Box sx={styles.container}>
                {/* Dynamic Grid */}
                <Box sx={styles.leftColumn}>
                    <DynamicGrid data={gridData.cells} />
                </Box>

                {/* Text Fields and Buttons */}
                <Box sx={styles.rightColumn}>
                    <TextField
                        label="Define the model"
                        multiline
                        rows={6}
                        defaultValue={formValues.model}
                        onBlur={handleFormChange('model')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />
                    <TextField
                        label="Define the model's routines"
                        multiline
                        rows={6}
                        defaultValue={formValues.modelRoutines}
                        onBlur={handleFormChange('modelRoutines')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />
                    <TextField
                        label="Define the agent"
                        multiline
                        rows={6}
                        defaultValue={formValues.agent}
                        onBlur={handleFormChange('agent')}
                        variant="outlined"
                        fullWidth
                        margin="normal"
                    />
                    <TextField
                        label="Define the agent's routines"
                        multiline
                        rows={6}
                        defaultValue={formValues.agentRoutines}
                        onBlur={handleFormChange('agentRoutines')}
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

const DynamicGrid: React.FC<{ data: GridCell[][] }> = ({ data }) => {
    const rows = data.length;
    const cols = data[0]?.length || 0;

    const colorMap: { [key: number]: string } = {
        0: '#ccc', // Grey for empty cells
        1: '#9c27b0', // Purple
        2: '#ff9800', // Orange
        3: '#2196f3', // Blue
        4: '#4caf50', // Green
        5: '#f44336', // Red
        6: '#e91e63', // Pink
        7: '#ffeb3b', // Yellow
        8: '#00bcd4', // Cyan
        9: '#795548', // Brown
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
                        title={`Row: ${rowIndex + 1}, Col: ${colIndex + 1}, Value: ${cell.value}`}
                        arrow
                    >
                        <Box
                            sx={gridStyles.cell}
                            style={{
                                backgroundColor: colorMap[cell.value] || '#ccc', // Dynamic shading based on value
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
      border: '1px solid #ccc',
      aspectRatio: '1', // Ensure square cells
      cursor: 'pointer',
  },
};

export default Create;