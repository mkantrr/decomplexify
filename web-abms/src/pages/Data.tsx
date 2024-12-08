import React, { useState } from 'react';
import { useTheme } from '@mui/material/styles';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import axios from 'axios';
import Papa from 'papaparse'; // For CSV parsing
import { saveAs } from 'file-saver'; // For saving the CSV file
import * as XLSX from 'xlsx'; // SheetJS for Excel export

import DynamicTable from '../components/DynamicTable';

const Data: React.FC = () => {
    const theme = useTheme();

    const [data, setData] = useState<(string | number | null)[][]>([[]]); // Array of objects for rows
    const [columns, setColumns] = useState<string[]>([]); // Array of column names

    const [modelMessage, setModelMessage] = useState<string | null>(null);
    const [modelError, setModelError] = useState<boolean>(false);
    const [agentMessage, setAgentMessage] = useState<string | null>(null);
    const [agentError, setAgentError] = useState<boolean>(false);

    // Fetch data from the API
    const fetchModelData = async () => {
        try {
            const response = await axios.get('http://localhost:3001/api/model-data'); // Replace with your API endpoint
            // Check for errors in the response
            if (response.data.error) {
            throw new Error(response.data.error);
            }
            
            const { columns, data } = response.data; // Assume API returns { columns: [], data: [] }
            setColumns(columns);
            setData(data);

            // Update message state
            setModelError(false);
            setModelMessage(response.data.message || 'Model data fetched successfully!');
        } catch (error: any) {
            // Handle errors
            setModelError(true);
            setModelMessage(
                error.response?.data?.error || error.message || 'Failed to fetch model data.'
            );
        }
    };

    // Fetch data from the API
    const fetchAgentData = async () => {
        try {
            const response = await axios.get('http://localhost:3001/api/agent-data');
    
            // Check for errors in the response
            if (response.data.error) {
                throw new Error(response.data.error);
            }
            
            const { columns, data } = response.data; // Assume API returns { columns: [], data: [] }
            setColumns(columns);
            setData(data);

            // Update message state
            setAgentError(false);
            setAgentMessage(response.data.message || 'Agent data fetched successfully!');
        } catch (error: any) {
            // Handle errors
            setAgentError(true);
            setAgentMessage(
                error.response?.data?.error || error.message || 'Failed to fetch agent data.'
            );
        }
    };


    // Function to export the data to CSV
    const exportToCSV = () => {
      // Convert data into a format compatible with PapaParse
      const csvData = data.map(row => {
        return row.map(cell => (cell !== null ? cell : "")); // Handle null values in the data
      });

      const csv = Papa.unparse({
        fields: columns, // Use column names as headers
        data: csvData,   // Use the table data as rows
      });

      // Trigger the file download
      const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
      saveAs(blob, "dataset.csv");
    };

    // Function to export data to Excel (XLSX)
    const exportToExcel = () => {
      // Create a new workbook
      const wb = XLSX.utils.book_new();

      // Create a worksheet from the data
      const ws = XLSX.utils.aoa_to_sheet([columns, ...data]);  // Columns as first row, followed by the data

      // Append the worksheet to the workbook
      XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

      // Write the workbook to a Blob and trigger a download
      const wbout = XLSX.write(wb, { bookType: "xlsx", type: "binary" });

      // Convert binary string to Blob
      const buf = new ArrayBuffer(wbout.length);
      const view = new Uint8Array(buf);
      for (let i = 0; i < wbout.length; i++) {
        view[i] = wbout.charCodeAt(i) & 0xff;
      }

      // Create Blob and trigger file download
      const blob = new Blob([buf], { type: "application/octet-stream" });
      saveAs(blob, "dataset.xlsx");
    };

    return (
        <Box sx={styles.page}>
            <Box sx={styles.title}>
                <h2>
                    Data Sheet and Export
                </h2>
            </Box>
            <Box sx={styles.restOfPage}>
            <Box sx={styles.fetchButtonContainer}>
                <Button variant="contained" color="secondary" onClick={fetchModelData} sx={{ marginRight: 2 }}>
                    Fetch Model Data
                </Button>
                <Button variant="contained" sx={{
                                    backgroundColor: 'orange', // Custom orange color
                                    color: theme.palette.mode === 'dark' ? 'black' : 'white', // Ensure text is readable
                                    '&:hover': {
                                        backgroundColor: 'darkorange', // Darker orange on hover
                                    },
                                }} onClick={fetchAgentData}>
                    Fetch Agent Data
                </Button>
            </Box>
            {modelMessage && (
                    <Typography
                        sx={{
                            color: modelError ? '#ff6347' // Red for error
                            : theme.palette.mode === 'dark' ? '#fff' // White for success in dark mode
                                                        : '#000', // Black for success in light mode
                            fontWeight: 'bold',
                            marginBottom: '10px',
                        }}
                    >
                        Model Fetch: {modelMessage}
                    </Typography>
                )}
                {agentMessage && (
                    <Typography
                        sx={{
                            color: agentError ? '#ff6347' // Red for error
                            : theme.palette.mode === 'dark' ? '#fff' // White for success in dark mode
                                                        : '#000', // Black for success in light mode
                            fontWeight: 'bold',
                            marginBottom: '10px',
                        }}
                    >
                        Agent Fetch: {agentMessage}
                    </Typography>
                )}
            <DynamicTable columns={columns} data={data}/>
            <Box sx={styles.buttonsContainer}>
                <Button
                    variant="contained"
                    color="primary"
                    onClick={exportToCSV}
                    sx={{ marginRight: 2 }}
                >
                    Export to CSV
                </Button>
                <Button
                    variant="contained"
                    sx={{
                        backgroundColor: 'green',
                        color: theme.palette.mode === 'dark' ? 'black' : 'white', // Ensure text is readable
                        '&:hover': {
                            backgroundColor: 'darkgreen',
                        },
                    }}
                    onClick={exportToExcel}
                >
                    Export to Excel
                </Button>
            </Box>
            </Box>
        </Box>
    );
};

const styles = {
    page: {},
    title: {
        marginBottom: '20px',
    },
    restOfPage: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '20px',
        height: '100vh',
    },
    fetchButtonContainer: {
        marginBottom: '20px',
        display: 'flex',
        justifyContent: 'center',
        width: '100%',
    },
    tableContainer: {
        flex: 1,
        overflow: 'auto',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        width: '100%',
    },
    table: {
        width: '80%',
        borderCollapse: 'collapse' as const,
    },
    th: {
        border: '1px solid #ddd',
        padding: '8px',
        backgroundColor: '#f4f4f4',
        textAlign: 'left' as const,
    },
    td: {
        border: '1px solid #ddd',
        padding: '8px',
        textAlign: 'left' as const,
    },
    buttonsContainer: {
        marginTop: '20px',
        display: 'flex',
        justifyContent: 'center',
        gap: '10px',
        width: '100%',
    },
};

export default Data;