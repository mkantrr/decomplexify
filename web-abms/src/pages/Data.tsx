import React, { useState } from 'react';
import { useTheme } from '@mui/material/styles';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import axios from 'axios';
import * as XLSX from 'xlsx'; // SheetJS for Excel export

interface RowData {
    [key: string]: any; // Flexible structure for each row
}

const Data: React.FC = () => {
    const theme = useTheme();

    const [data, setData] = useState<RowData[]>([]); // Array of objects for rows
    const [columns, setColumns] = useState<string[]>([]); // Array of column names

    // Fetch data from the API
    const fetchModelData = async () => {
        try {
            const response = await axios.get('/api/data/model'); // Replace with your API endpoint
            const { columns, data } = response.data; // Assume API returns { columns: [], data: [] }
            setColumns(columns);
            setData(data);
        } catch (error) {
            console.error('Error fetching model data:', error);
        }
    };

    // Fetch data from the API
    const fetchAgentData = async () => {
        try {
            const response = await axios.get('/api/data/agent'); // Replace with your API endpoint
            const { columns, data } = response.data; // Assume API returns { columns: [], data: [] }
            setColumns(columns);
            setData(data);
        } catch (error) {
            console.error('Error fetching agent data:', error);
        }
    };


    // Export to CSV
    const exportToCSV = () => {
        const csvContent =
            [columns.join(','), ...data.map(row => columns.map(col => row[col]).join(','))].join('\n');
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'dataset.csv');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    // Export to Excel
    const exportToExcel = () => {
        const worksheet = XLSX.utils.json_to_sheet(data);
        const workbook = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(workbook, worksheet, 'Dataset');
        XLSX.writeFile(workbook, 'dataset.xlsx');
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
            <Box sx={styles.tableContainer}>
                {data.length > 0 ? (
                    <table style={styles.table}>
                        <thead>
                            <tr>
                                {columns.map((col, index) => (
                                    <th key={index} style={styles.th}>
                                        {col}
                                    </th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {data.map((row, rowIndex) => (
                                <tr key={rowIndex}>
                                    {columns.map((col, colIndex) => (
                                        <td key={colIndex} style={styles.td}>
                                            {row[col]}
                                        </td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                ) : (
                    <Typography>No data fetched yet.</Typography>
                )}
            </Box>
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